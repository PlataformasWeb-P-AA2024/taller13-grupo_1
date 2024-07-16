from django.contrib import admin

from administrativo.models import Edificio, Departamento

class EdificioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'direccion', 'ciudad', 'tipo')
    list_filter = ('tipo',)


admin.site.register(Edificio, EdificioAdmin)

class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'costo', 'nCuartos', 'edificio')
    raw_id_fields = ('edificio',)

admin.site.register(Departamento, DepartamentoAdmin)