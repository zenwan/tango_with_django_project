#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@time: 2018/5/2 11:23
@author: wang.zheng@ctrip.com
@version: V0.01
@file: urls.py
"""

from django.conf.urls import url
from rango import views
"""
处理rango应用的url,url函数映射index视图
"""
urlpatterns = [
    url(r"^$",views.index,name='index'),
    url(r'category/(?P<category_name_slug>[\w\-]+)',views.show_category,name='show_category')
]