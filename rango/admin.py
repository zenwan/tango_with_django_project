#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""

"""
from django.contrib import admin

# Register your models here.
#添加这个类，定制管理界面
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','category','url')

#添加这个类，定制管理界面
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)} # 用name 字段来自动填充slug 字段

from rango.models import Category,Page

#注册定制界面的类
admin.site.register(Category,CategoryAdmin)
admin.site.register(Page,PageAdmin)



