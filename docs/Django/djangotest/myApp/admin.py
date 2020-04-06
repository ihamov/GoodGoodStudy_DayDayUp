from django.contrib import admin

# Register your models here.

from .models import Grades,Students

# admin.TabularInline 或 admin.StackedInline 都可以，只是显示不同
class StudentsInfo(admin.TabularInline):
    model = Students
    extra = 2 # 每次创建2个


class GradesAdmin(admin.ModelAdmin):

    inlines = [StudentsInfo]

    # 列表属性
    # 显示字段
    list_display = ['pk', 'gname', 'gdate', 'ggirlnum', 'gboynum']
    # 过滤字段
    list_filter = ['gname']
    # 搜索字段
    search_fields = ['gname']
    # 分页
    list_per_page = 5

    # 添加修改也属性
    # 属性显示的先后顺序
    # fields = ['gdate', 'gname', 'gboynum', 'ggirlnum', 'isDelete']
    # 给属性分组
    # fields 与 fieldsets 不能同时使用
    fieldsets = [('num', {'fields': ['gboynum', 'ggirlnum']}), ('base', {'fields': ['gdate', 'gname', 'isDelete']})]

class StudentsAdmin(admin.ModelAdmin):

    # 解决布尔值男女显示问题
    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    # 设置页面列的名称
    gender.short_description = '性别'

    list_display = ['pk', 'sname', gender, 'sage', 'scontent', 'sgrade', 'isDelete']
    list_per_page = 2

    # 执行动作的位置
    actions_on_top = False
    actions_on_bottom = True

# 注册
admin.site.register(Grades, GradesAdmin)
admin.site.register(Students, StudentsAdmin)
