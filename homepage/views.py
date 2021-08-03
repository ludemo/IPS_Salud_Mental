from homepage.forms import ComentarioHForm
from homepage.models import ComentariosHome
from django.http import HttpResponse
from django.shortcuts import render
from enfermedades.models import Enfermedad, PersonalM
from django.views.generic import TemplateView, CreateView
from django.http import JsonResponse


# Create your views here.
# View basada en función para renderizar el homepage
class HomeView(CreateView):
    template_name = "homepage.html"
    #context_object_name = 'enfermedades'
    model = ComentariosHome
    success_url = '.'
    form_class = ComentarioHForm
    
    #enfermedades = Enfermedad.objects.all() 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enfermedades'] = Enfermedad.objects.all()
        context['personalM'] = PersonalM.objects.all()
        context['comentariosH'] = ComentariosHome.objects.all()
        return context
    
    def render_to_response(self, context, **response_kwargs):
        """ """
        if self.request.is_ajax():
            print("ajax")
            data = list(context["comentariosH"].values())
            return JsonResponse({'postsH': data}) 
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )

