from django.contrib import admin
from .models import Medico, UsuarioP3, Hora, Dia, Mes, Agendar, UsuarioM, UsuarioS

# Register your models here.

#class MedicoAdmin(admin.ModelAdmin):                                              #Quitar Simbolo de comentario solo para fines administrativos
    #list_display=("idMedico","nombreMedico", "apellidoMedico","especialidad")

class UsuarioPAdmin(admin.ModelAdmin):
    list_display=("rut","email","nombre","edad","password")   

class UsuarioMAdmin(admin.ModelAdmin):
    list_display=("id","nombre","password")

class UsuarioSAdmin(admin.ModelAdmin):
    list_display=("id","nombre","password")         

#class DiaAdmin(admin.ModelAdmin):            #Quitar Simbolo de comentario solo para fines administrativos
    #list_display=["dia"]

#class HoraAdmin(admin.ModelAdmin):
    #list_display=["hora"]

#class MesAdmin(admin.ModelAdmin):
    #list_display=["mes"]

    


admin.site.register(UsuarioP3,UsuarioPAdmin)
admin.site.register(UsuarioM, UsuarioMAdmin)
admin.site.register(UsuarioS, UsuarioSAdmin)
#admin.site.register(Hora,HoraAdmin)              #Quitar Simbolo de comentario solo para fines administrativos
#admin.site.register(Dia,DiaAdmin)
#admin.site.register(Mes,MesAdmin)
#admin.site.register(Agendar)
#admin.site.register(Medico, MedicoAdmin)