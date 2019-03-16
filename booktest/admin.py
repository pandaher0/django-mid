from django.contrib import admin
from booktest.models import AreaInfo,PicTest


# Register your models here.
class AreaStackInline(admin.StackedInline):
    # model写多类的名字
    model = AreaInfo
    extra = 2

class AreaTabularInline(admin.TabularInline):
    model = AreaInfo
    extra = 2


class AreaInfoAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_display = ['id', 'atitle', 'title', 'parent']
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle']
    search_fields = ['atitle', 'id']

    # fields = ['aParent','atitle']
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aParent']})
    )
    # inlines = [AreaStackInline]
    inlines = [AreaTabularInline]

admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)
