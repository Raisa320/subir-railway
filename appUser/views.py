from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from appUser.forms import LoginForm,UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.views.generic import DetailView
from django.contrib.auth.models import User
from ipware import get_client_ip

from appUser.models import VisitantePortafolio
# Create your views here.
def registerPage(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'¡Tu cuenta ha sido creada! Puedes iniciar sesión')
            return redirect('login-page')
    else:
        form=UserRegisterForm()
    context={}
    context["form"]=form
    return render(request,"user/register-user.html",context)

def loginPage(request):
    context={}
    context["form"]=LoginForm()
    return render(request,"user/login.html",context)


class UserDetailsTemplate(DetailView):
    model=User
    template_name='user/portafolio.html'
    context_object_name="usuario"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get("usuario"):
            ip,is_routable=get_client_ip(self.request)
            usuario=context.get("usuario")
            if usuario.visitanteportafolio_set.filter(ipVisitante=ip).first() is None:
                ipBd=VisitantePortafolio(ipVisitante=ip,protafolioVisitado=usuario)
                ipBd.save()  
            context["proyectos"]=usuario.proyecto_set.all()
            context["servicios"]=usuario.profile.servicios.split(",")
        return context

def indexPortafolio(request):
    current_user=request.user
    context={
        "proyectos": current_user.proyecto_set.all(),
        "cantidad":current_user.proyecto_set.count(),
    }

    return render(request,"user/portafolio.html",context) 


@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST, instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'¡Tu cuenta ha sido actualizada!')
            return redirect('user-profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        "u_form":u_form,
        "p_form":p_form,
        "profile":"profile"
    }

    return render(request,'user/profile.html',context)