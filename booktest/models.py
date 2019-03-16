from django.db import models


# Create your models here.
class AreaInfo(models.Model):
    atitle = models.CharField(verbose_name='地区名称', max_length=20)
    aParent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.atitle

    def title(self):
        return self.atitle

    # 增加排序
    title.admin_order_field = 'atitle'
    title.short_description = '地区名称'

    def parent(self):
        # 省级地区没有父级地区
        # 判断如果为None,则返回空
        if self.aParent is None:
            return ''
        return self.aParent.atitle

    parent.admin_order_field = 'atitle'
    parent.short_decription = '父级地区'

class PicTest(models.Model):
    goods_pic = models.ImageField(upload_to='booktest/')