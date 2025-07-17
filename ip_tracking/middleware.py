from .models import RequestLog, BlockedIP
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class LogIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        # Block if IP is blacklisted
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden('Your IP is blocked.')
        # Save log
        RequestLog.objects.create(ip_address=ip, path=path) 