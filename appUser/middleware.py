from django.http import HttpResponse
from django.shortcuts import render
from ipware import get_client_ip

from appUser.models import VisitanteGeneral

def ip_register(get_response):
    def middleware(request):
        # Código que se ejecutará antes del llamado a la vista.
        ip,is_routable=get_client_ip(request)
        ipBd=VisitanteGeneral.objects.filter(ipVisitante=ip).first()
        if ipBd is None:
            ipBd=VisitanteGeneral(ipVisitante=ip)
            ipBd.save()
        response = get_response(request)
        return response
    return middleware