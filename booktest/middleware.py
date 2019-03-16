# Author:hxj
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


# class BlockedIPSMiddleware(object):
#     # 禁止访问IP
#     EXCLUDE_IPS = ['127.0.0.1']
#
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         return self.get_response(request)
#
#     def process_view(self, request, view_func, *view_args, **view_kwargs):
#         """视图函数调用之前调用"""
#         user_ip = request.META['REMOTE_ADDR']
#         if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
#             return HttpResponse('<h1>forbidden</h1>')


class BlockedIPSMiddleware(MiddlewareMixin):
    '''中间件类'''
    EXCLUDE_IPS = ['127.0.0.1']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')


class TestMiddleware(MiddlewareMixin):
    # def __init__(self, get_response):
    #     print('------init')
    #     self.get_response = get_response

    def process_request(self, request):
        """产生request对象后，url匹配之前"""
        print('----process_request')
        # 干预过程，直接执行process_response
        # return HttpResponse('process_request')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        """url匹配后，视图函数调用之前"""
        print('-----process_view')
        # 干预过程，直接执行process_response
        # return HttpResponse('process_view')

    def process_response(self, request, response):
        """视图函数调用之后，内容返回之前"""
        print('------process_response')
        return response


class ExceptionTest1Middleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        """视图函数发生异常时调用"""
        print('process_exception1')


class ExceptionTest2Middleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        """视图函数发生异常时调用"""
        print('process_exception2')
