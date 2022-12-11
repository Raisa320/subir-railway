from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ProyectoCreate,ProyectoDetailView,ProyectoUpdate, ProyectoDeleteView

urlpatterns = [
    path('register/',ProyectoCreate.as_view() , name='proyecto-register'),
    path("ver/<int:pk>/", login_required(ProyectoDetailView.as_view(template_name="proyecto/ver-proyecto.html")), name="proyecto-ver"),
    path("<int:pk>/update/", ProyectoUpdate.as_view(), name="proyecto-update"),
    path("eliminar/<int:pk>/", ProyectoDeleteView.as_view(), name="proyecto-delete"),
    path("detail/<int:pk>/", ProyectoDetailView.as_view(template_name="proyecto/portafolio-detail.html"), name="proyecto-detail")
]
