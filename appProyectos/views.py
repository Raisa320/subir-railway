from django.http import HttpRequest
from django.shortcuts import  render
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import CreateView,DetailView, UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from appProyectos.forms import  ProyectoForm

from appProyectos.models import Proyecto
# Create your views here.
@login_required
def index(request):
    current_user=request.user
    context={
        "proyectos": current_user.proyecto_set.all(),
        "cantidad":current_user.proyecto_set.count(),
        "visitantes":current_user.visitanteportafolio_set.count(),
        "dashboard":"dashboard"
    }

    return render(request,"proyecto/index.html",context)


class ProyectoCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    form_class=ProyectoForm
    template_name = 'proyecto/form-proyecto.html'
    success_url = '/'
    success_message = "Se ha registrado tu proyecto correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Registrar"
        context['registrar']="registrar"
        return context
    
    def form_valid(self,form):
        form.instance.autor=self.request.user
        return super().form_valid(form)

class ProyectoUpdate(LoginRequiredMixin,SuccessMessageMixin,UserPassesTestMixin,UpdateView):
    form_class=ProyectoForm
    model=Proyecto
    template_name = 'proyecto/form-proyecto.html'
    success_message = "Se ha actualizado su proyecto correctamente"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "Actualizar"
        if context.get("proyecto").foto_img:
            context["url_img"]=context.get("proyecto").foto_img.url
        return context

    def form_valid(self,form):
        form.instance.autor=self.request.user
        if form.instance.foto_url:
            form.instance.foto_img=None
        return super().form_valid(form)

    def test_func(self):
        proyecto=self.get_object()
        if self.request.user==proyecto.autor:
            return True
        return False

class ProyectoDetailView(DetailView):
    model=Proyecto
    #template_name='proyecto/ver-proyecto.html'
    context_object_name="proyecto"

class ProyectoDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Proyecto
    template_name='proyecto/delete-proyecto.html'
    context_object_name="proyecto"
    success_url="/"
    
    def test_func(self):
        proyecto=self.get_object()
        if self.request.user==proyecto.autor:
            return True
        return False

