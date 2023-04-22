from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
appname = 'timezones'
    
class BaseApiMixinView:
    schema = None
    # Need for skip django model permission
    _ignore_model_permissions = True   
    
class TimeZoneAPIView(BaseApiMixinView, APIView):
    
    def get(self, request, **kwargs):
        result = request.path        
        return Response(result) 
    

