from django import forms
from django.core.exceptions import ValidationError
import hashlib
from app01 import models


class RegForm(forms.ModelForm):
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '确认密码'}))

    class Meta:
        model = models.UserProfile
        fields = "__all__"
        exclude = ['is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 自定义的操作
        self.fields['username'].widget.attrs['placeholder'] = '用户名'
        self.fields['password'].widget = forms.PasswordInput(attrs={'placeholder': '密码'})
        self.fields['name'].widget.attrs['placeholder'] = '姓名'
        self.fields['mobile'].widget.attrs['placeholder'] = '手机号'
        self.fields['department'].choices = [('', '请选择部门')] + list(models.Department.objects.values_list('id', 'name'))

    def clean(self):
        self._validate_unique = True  # 在数据库校验唯一性
        password = self.cleaned_data.get('password', '')
        re_password = self.cleaned_data.get('re_password')
        if password == re_password:
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))

            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        self.add_error('password', '两次密码不一致')
        raise ValidationError('两次密码不一致')
