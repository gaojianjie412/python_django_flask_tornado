
from django import forms

from app.models import Student


class StuForm(forms.Form):

    username = forms.CharField(max_length=10,
                               min_length=2,
                               required=True,
                               error_messages={
                                   'required': '姓名字段必填',
                                   'min_length': '不能少于2字符',
                                   'max_length': '不能超过10字符'
                               })
    icon = forms.ImageField(required=True,
                            error_messages={
                                'required': '头像必填'
                            })
    gender = forms.CharField(required=True,
                             error_messages={
                                 'required': '性别必填'
                             })

    # def clean(self):
    #     # 转换性别为1或者是0
    #     gender = self.cleaned_data.get('gender')
    #     if gender == '男':
    #         self.cleaned_data['gender'] = 1
    #     else:
    #         self.cleaned_data['gender'] = 0
    #
    #     # 校验姓名是唯一的
    #     username = self.cleaned_data.get('username')
    #     stu = Student.objects.filter(s_name=username).first()
    #     if stu:
    #         raise forms.ValidationError({'username': '姓名重复'})
    #
    #     return self.cleaned_data

    def clean_username(self):
        # 只是校验姓名
        username = self.cleaned_data.get('username')
        stu = Student.objects.filter(s_name=username).first()
        if stu:
            raise forms.ValidationError('姓名重复')
        return self.cleaned_data['username']

    def clean_gender(self):
        # 只是校验性别
        # 转换性别为1或者是0
        gender = self.cleaned_data.get('gender')
        if gender == '男':
            self.cleaned_data['gender'] = 1
        else:
            self.cleaned_data['gender'] = 0
        return self.cleaned_data['gender']
