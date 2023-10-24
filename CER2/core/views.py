from django.shortcuts import render
from django.http import HttpResponse
from core.models import Entidad, Comunicado


# Create your views here.
def home(request):
    dataCom = Comunicado.objects.all()
    dataEnt = Entidad.objects.all()
    dataCom.order_by('fecha_publicacion')

    departamento_sel = request.GET.get('departamentos')
    
    context = {'dataEnt': dataEnt,
               'dataCom': dataCom,
               'departamento_sel': departamento_sel}
    
    
    return render(request, "core/index.html", context)