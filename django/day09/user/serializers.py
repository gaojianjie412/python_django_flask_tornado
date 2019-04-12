
from rest_framework import serializers

from app.models import Student


class StuSerializer(serializers.ModelSerializer):
    s_name = serializers.CharField(max_length=10,
                                   min_length=2,
                                   error_messages={
                                       'required': '姓名必填',
                                       'max_length': '最大不能超过10字符',
                                       'min_length': '最小不能小于2字符'
                                   })

    class Meta:
        # 序列化的模型
        model = Student
        fields = ['s_name', 's_gender', 's_age', 'id']

    def to_representation(self, instance):
        data = super(StuSerializer, self).to_representation(instance)
        # data = {
        #     "s_name": "小明22",
        #     "s_gender": true,
        #     "s_age": 23
        # },
        data['s_gender'] = '男' if data['s_gender'] else '女'
        return data