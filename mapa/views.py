from mapa.forms import ComentarioForm
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from mapa.models import Comentarios
from django.http import JsonResponse

# Create your views here.
class MapaView(CreateView):
    template_name = "mapa.html"
    model = Comentarios
    form_class = ComentarioForm
    success_url = '.'




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["comentarios"] = Comentarios.objects.all()
        #alright aqui traete los comentarios y metelo al context
        return context 

    def render_to_response(self, context, **response_kwargs):
        """ """
        if self.request.is_ajax():
            print("ajax")
            data = list(context["comentarios"].values())
            return JsonResponse({'posts': data}) 
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )

