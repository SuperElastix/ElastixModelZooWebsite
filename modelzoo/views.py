from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.views import generic
from .models import Model
from django.conf import settings
from django.db.models import Q
from modelzoo.templatetags.filter_tags import CONTENT_CHOICES, DIMENSION_CHOICES, MODALITY_CHOICES
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import requests
from ipaddress import ip_address, ip_network
import hmac
from hashlib import sha1
from django.utils.encoding import force_bytes


# Create your views here.

class IndexView(generic.ListView):
    context_object_name = 'model_list'
    template_name = 'modelzoo/index2.html'

    def get_queryset(self):
        queryset = Model.objects.order_by('date')

        if 'modality' in self.request.GET:
            for mod,mod2 in MODALITY_CHOICES:
                if mod in self.request.GET.get('modality'):
                    queryset = queryset.filter(Q(con_mod_dims__icontains=mod))

        if 'dimensions' in self.request.GET:
            for dim,dim2 in DIMENSION_CHOICES:
                if dim in self.request.GET.get('dimensions'):
                    queryset = queryset.filter(Q(con_mod_dims__icontains=dim))

        if 'content' in self.request.GET:
            for con,con2 in CONTENT_CHOICES:
                if con in self.request.GET.get('content'):
                    queryset = queryset.filter(Q(con_mod_dims__icontains=con))

        if self.request.GET.get('q'):
            query = self.request.GET.get('q').lower()
            models = Model.objects.all()
            wanted_ids = []
            for m in models:
                for line in open(settings.MEDIA_ROOT + m.readme.name).readlines():
                    if query in line.lower():
                        wanted_ids.append(m.title)
                        break
            queryset = queryset.filter(
                Q(title__in=wanted_ids) |
                Q(title__icontains=query) | Q(modality__icontains=query) |
                Q(dimensions__icontains=query) | Q(content__icontains=query))
        return queryset

class DetailView(generic.DetailView):
    model = Model
    template_name = 'modelzoo/detail.html'

class DetailView_nb(generic.DetailView):
    model = Model
    template_name = 'modelzoo/detail_nb.html'

@require_POST
@csrf_exempt
def hello(request):
    
    # Verify if the request came from GitHub.
    forwarded_for = u'{}'.format(request.META.get('HTTP_X_FORWARDED_FOR'))
    client_ip_address = ip_address(forwarded_for)
    whitelist = requests.get('https://api.github.com/meta').json()['hooks']

    for valid_ip in whitelist:
        if client_ip_address in ip_network(valid_ip):
            break
        else:
            return HttpResponseForbidden('Permission denied.')

    # Verify the request signature.
    header_signature = request.META.get('HTTP_X_HUB_SIGNATURE')
    if header_signature is None:
        return HttpResponseForbidden('Permission denied.')

    sha_name, signature = header_signature.split('=')
    if sha_name != 'sha1':
        return HttpResponseServerError('Operation not supported.', status=501)

    mac = hmac.new(force_bytes(settings.GITHUB_WEBHOOK_KEY), msg=force_bytes(request.body), digestmod=sha1)
    if not hmac.compare_digest(force_bytes(mac.hexdigest()), force_bytes(signature)):
        return HttpResponseForbidden('Permission denied.')

    return HttpResponse('pong')
