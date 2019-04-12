
from rest_framework.renderers import JSONRenderer


class MyJSONRenderer(JSONRenderer):
    """
    {
        'code': 200,
        'msg:'请求成功',
        'data': {data}
    }
    """
    def render(self, data, accepted_media_type=None, renderer_context=None):
        try:
            code = data['code']
            msg = data['msg']
            result = data['data']
        except:
            code = 200
            msg = '请求成功'
            result = data

        my_data = {
            'code': code,
            'msg': msg,
            'data': result
        }
        return super().render(my_data, accepted_media_type, renderer_context)

