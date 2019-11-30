'''
@Author: kiwi
@Date: 2019-11-30 15:31:26
@LastEditors: kiwi
@LastEditTime: 2019-11-30 17:11:38
@Description: 描述
'''

from django import forms
from app01 import models
from django.core.exceptions import ValidationError
import hashlib

class RegForm(forms.ModelForm):
    """Form definition for Reg."""
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'请再次输入密码'}))
    class Meta:
        """Meta definition for Regform."""

        model = models.UserProfile
        fields = '__all__'
        exclude = ['is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = '请输入用户名'
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder':'请输入密码'})
        self.fields['name'].widget.attrs['placeholder'] = '请输入姓名'
        self.fields['mobile'].widget.attrs['placeholder'] = '请输入手机号'
        self.fields['department'].choices = [('','请选择部门')] +list(models.Department.objects.values_list('id','name'))
            
    def clean(self):
        self._validate_unique = True
        password =  self.cleaned_data.get('password')    
        re_password =  self.cleaned_data.get('re_password')
        if password and re_password:
            if  password == re_password:
                md5 = hashlib.md5()
                md5.update(password.encode('utf-8'))
                self.cleaned_data['password'] = md5.hexdigest()
                return self.cleaned_data
            self.add_error('password','两次密码不一致')
            raise ValidationError('两次密码不一致')
        self.add_error('password','信息不能为空')
        self.add_error('re_password','信息不能为空')
        raise ValidationError('信息不一致')

