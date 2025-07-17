from .models import RequestLog, BlockedIP
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden
from django.core.cache import cache
from django_ip_geolocation.utils import get_ip_geolocation

CACHE_TIMEOUT = 60 * 60 * 24  # 24 hours

class LogIPMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR')
        path = request.path
        # Block if IP is blacklisted
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden('Your IP is blocked.')
        # Geolocation caching
        geo_cache_key = f'geo_{ip}'
        geo = cache.get(geo_cache_key)
        if not geo:
            geo = get_ip_geolocation(ip)
            cache.set(geo_cache_key, geo, CACHE_TIMEOUT)
        country = geo.get('country_name') if geo else None
        city = geo.get('city') if geo else None
        # Save log
        RequestLog.objects.create(ip_address=ip, path=path, country=country, city=city) 