'''
@Author: kiwi
@Date: 2019-11-30 15:31:26
@LastEditors: kiwi
@LastEditTime: 2019-11-30 17:07:42
@Description: 描述
'''
from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.ClassList)
admin.site.register(models.Campuses)
admin.site.register(models.Department)
