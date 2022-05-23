from django.contrib import admin

from taco.models import Alimento


@admin.register(Alimento)
class AlimentoAdmin(admin.ModelAdmin):
    exclude = ()

