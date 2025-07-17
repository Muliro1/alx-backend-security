from .models import RequestLog
from django.utils.deprecation import MiddlewareMixin

class LogIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        # Save log
        RequestLog.objects.create(ip_address=ip, path=path) 