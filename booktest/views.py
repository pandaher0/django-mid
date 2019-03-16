from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.conf import settings
from booktest.models import PicTest, AreaInfo

# Create your views here.

EXCLUDE_IPS = ['127.0.0.1']


def blocked_ips(view_func):
    def wrapper(request, *args, **kwargs):
        # 获取浏览器端的ip地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>forbidden</h1>')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper


# @blocked_ips
def index(request):
    print('----index')
    return render(request, 'booktest/index.html')


# @blocked_ips
def static_test(request):
    print(settings.STATICFILES_FINDERS)
    # ['django.contrib.staticfiles.finders.FileSystemFinder',
    # 'django.contrib.staticfiles.finders.AppDirectoriesFinder']
    return render(request, 'booktest/static_test.html')


def show_upload(request):
    return render(request, 'booktest/upload_pic.html')


def upload_handle(request):
    # 1.获取上传文件的处理对象
    # <class 'django.core.files.uploadedfile.InMemoryUploadedFile'>
    # 文件不大于2.5m，放在内存中
    # 大于2.5m，放在临时文件中
    pic = request.FILES['pic']

    # print(pic.name)
    # pic.chunks()
    # print(type(pic))
    # 2.创建文件
    save_path = '%s/booktest/%s' % (settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取文件上传内容并写道创建的文件中
        for content in pic.chunks():
            f.write(content)

    # 4.在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s' % pic.name)
    # 5.返回
    return HttpResponse('ok')


def show_areas(request, pindex):
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 分页
    paginator = Paginator(areas, 10)

    # 总页数
    # print(paginator.num_pages)
    # 页码范围
    # print(paginator.page_range)

    if pindex == '':
        pindex = 1
    page = paginator.page(pindex)
    return render(request, 'booktest/show_areas.html', {'page': page})


def areas(request):
    return render(request, 'booktest/areas.html')


def prov(request):
    prov = AreaInfo.objects.filter(aParent__isnull=True)
    # 遍历对象，拼接json数据：id,atitle
    areas_list = []
    for area in prov:
        areas_list.append((area.id, area.atitle))

    return JsonResponse({'data': areas_list})


def city(request):
    prov_id = request.GET['prov_id']
    areas = AreaInfo.objects.filter(aParent=prov_id)
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))

    return JsonResponse({'data': area_list})


def dis(request, city_id):
    areas = AreaInfo.objects.filter(aParent=city_id)
    area_list = []
    for area in areas:
        area_list.append((area.id, area.atitle))

    return JsonResponse({'data': area_list})
