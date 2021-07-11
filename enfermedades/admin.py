from django.contrib import admin
from .models import Consejos, Enfermedad, PersonalM

# Register your models here.

admin.site.register(Enfermedad)
admin.site.register(Consejos)
admin.site.register(PersonalM)
