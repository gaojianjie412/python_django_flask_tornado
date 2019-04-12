
import django_filters

from app.models import Student


class StuFilter(django_filters.rest_framework.FilterSet):

    # 指定模糊查询过滤的s_name字段
    name = django_filters.CharFilter('s_name', lookup_expr='contains')
    age0 = django_filters.CharFilter('s_age', lookup_expr='gt')
    age1 = django_filters.CharFilter('s_age', lookup_expr='lt')

    class Meta:
        model = Student
        fields = ['name', 'age0', 'age1']


