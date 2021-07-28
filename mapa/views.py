from django.shortcuts import render
from django.views.generic import TemplateView
from mapa.models import Comentarios
from django.http import JsonResponse

# Create your views here.
class MapaView(TemplateView):
    template_name = "mapa.html" 
    def get_context_data(self, **kwargs):
        queryset = Comentarios.objects.all()
        context = super().get_context_data(**kwargs)
        context["Comentarios"] = queryset
        #alright aqui traete los comentarios y metelo al context
        return context 

    def render_to_response(self, context, **response_kwargs):
        if self.request.is_ajax():
            queryData = context["Comentarios"].values()
            data = list(queryData)

            return JsonResponse({'Comentarios': data}) 
        else:
            response_kwargs.setdefault('content_type', self.content_type)
            
            return self.response_class(
                request=self.request,
                template=self.get_template_names(),
                context=context,
                using=self.template_engine,
                **response_kwargs
            )

