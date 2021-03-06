from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=10, unique=True)
    s_age = models.IntegerField(default=20)
    s_gender = models.BooleanField(default=0)
    # auto_now_add: 创建时，默认字段赋值为最新的时间
    create_time = models.DateTimeField(auto_now_add=True)
    # auto_now: 修改数据时，自动赋值为更新字段时的时间
    update_time = models.DateTimeField(auto_now=True)
    math = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    wuli = models.DecimalField(max_digits=3, decimal_places=1, null=True)
    # 存图片的地址，数据库库中icon字段的类型为varchar
    icon = models.ImageField(upload_to='upload', null=True)
    is_delete = models.BooleanField(default=0)

    class Meta:
        db_table = 'student'
