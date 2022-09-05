from email.charset import Charset
from rest_framework.renderers import JSONRenderer
import json
from rest_framework.response import Response

class CustomJSONRender(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        status_code = renderer_context['response'].status_code
        ret = {
          "status": "success",
          "code": status_code,
          "data": data,
          "errors":None
        }

        if not str(status_code).startswith('2'):
            ret["status"] = "error"
            ret["data"] = None
            ret['errors'] = data
        return super(CustomJSONRender,self).render(ret, accepted_media_type, renderer_context)