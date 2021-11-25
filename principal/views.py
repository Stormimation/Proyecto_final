from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Medico, UsuarioP3, Hora, Mes, Agendar, Dia, UsuarioM, UsuarioS
from django.core.files.storage import FileSystemStorage
from django.contrib import messages

# Create your views here.


def login(request):
    return render(request, 'login.html')

def loginC(request):
    return render(request, 'loginC.html')  

def loginM(request):
    return render(request, 'loginM.html')

def loginS(request):
    return render(request, 'loginS.html')

def registro(request):
    usuariop=UsuarioP3.objects.all()
    datos = {'usuariosp': usuariop}
    return render(request, 'registro.html', datos)

def validarUsuarioP(request):
    try:
        v_nombre=request.POST.get('nombre')
        v_password=request.POST.get('password')

        usuariop=UsuarioP3.objects.get(password=v_password, nombre=v_nombre)
        
        
            #crear la sesion y redireccionar
        request.session['nombre']=usuariop.nombre
        return redirect('/verM')
        
    except:
        return redirect('/errorloginC') 

def validarUsuarioM(request):
    try:
        v_nombre=request.POST.get('nombre')
        v_password=request.POST.get('password')

        usuariom=UsuarioM.objects.get(password=v_password, nombre=v_nombre)

        request.session['nombre']=usuariom.nombre
        return redirect('/verP')

    except:
        return redirect('/errorloginC')   

def validarUsuarioS(request):
    try:
        v_nombre=request.POST.get('nombre')
        v_password=request.POST.get('password')

        usuariom=UsuarioS.objects.get(password=v_password, nombre=v_nombre)

        request.session['nombre']=usuariom.nombre
        return redirect('/verM2')

    except:
        return redirect('/errorloginC')                 

def errorloginC(request):
    return render(request, 'errorloginC.html')        

def guardarPaciente(request):
    v_rut=request.POST.get('rut')
    v_email=request.POST.get('email')
    v_nombrep=request.POST.get('nombrep')
    v_edad=request.POST.get('edad')
    v_password=request.POST.get('password')

    nuevo=UsuarioP3()
    nuevo.rut=v_rut
    nuevo.email=v_email
    nuevo.nombre=v_nombrep
    nuevo.edad=v_edad
    nuevo.password=v_password

    UsuarioP3.save(nuevo)

    usuariosp=UsuarioP3.objects.all()

    datos={'usuariosp': usuariosp}

    return render(request, 'loginC.html', datos)   
     

def formmedico(request):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']
        medico=Medico.objects.all()
        datos = {'medicos': medico, 'nombre':nombre}
        return render(request, 'formMedico.html', datos)
    else:
        return HttpResponse('No existe la sesion')


def guardarMedico(request):
    v_idMedico=request.POST.get('idMedico')
    v_nombreMedico=request.POST.get('nombreMedico')
    v_apellidoMedico=request.POST.get('apellidoMedico')
    v_especialidad=request.POST.get('especialidad')

    nuevo=Medico()
    nuevo.idMedico=v_idMedico
    nuevo.nombreMedico=v_nombreMedico
    nuevo.apellidoMedico=v_apellidoMedico
    nuevo.especialidad=v_especialidad

    Medico.save(nuevo)

    medicos=Medico.objects.all()

    datos={'medicos': medicos}

    return render(request, 'verM2.html', datos) 

# Metodo que elimina a un Medico de la BD

def eliminarMedico(request, v_idMedico):
    medico=Medico.objects.get(idMedico=v_idMedico)

    Medico.delete(medico)

    return redirect('/verM2')

# Metodo que redirecciona al formulario de modificacion tomando de referencia la id del objeto a modificar   

def modificarMedico(request, v_idMedico):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']

        medico=Medico.objects.get(idMedico=v_idMedico)

        informacion={'datos': medico, 'nombre': nombre}
        return render(request, 'formMM.html', informacion)
    else:
        return HttpResponse('No existe la sesion')     

# Metodo que guarda las modificaciones al objeto

def modificarGuardarMedico(request):
    v_idMedico=request.POST.get('idMedico')
    v_nombreMedico=request.POST.get('nombreMedico')
    v_apellidoMedico=request.POST.get('apellidoMedico')
    v_especialidad=request.POST.get('especialidad')

    #Buscar el medico para modificar
    medico=Medico.objects.get(idMedico=v_idMedico)

    medico.nombreMedico=v_nombreMedico
    medico.apellidoMedico=v_apellidoMedico
    medico.especialidad=v_especialidad

    Medico.save(medico)

    return redirect('/verM2')



def agendar(request):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']
        dia=Dia.objects.all()
        mes=Mes.objects.all()
        hora=Hora.objects.all()
        medico=Medico.objects.all()
        datos = {'dias': dia, 'meses': mes, 'horas':hora, 'medicos':medico, 'nombre': nombre}
        return render(request, 'agendar.html', datos)
    else:
        return HttpResponse('No existe la sesion')    

def guardarAgendar(request):
    v_idHora=request.POST.get('idHora')
    v_dia=request.POST.get('dia')
    v_mes=request.POST.get('mes')
    v_hora=request.POST.get('hora')
    v_medico=request.POST.get('medico')

    dia=Dia.objects.get(dia=v_dia)
    mes=Mes.objects.get(mes=v_mes)
    hora=Hora.objects.get(hora=v_hora)
    medico=Medico.objects.get(idMedico=v_medico)

    nuevo=Agendar()
    nuevo.idHora=v_idHora
    nuevo.dia=dia
    nuevo.mes=mes
    nuevo.hora=hora
    nuevo.medico=medico

    Agendar.save(nuevo)

    return redirect('/verM')

def eliminarHora(request, v_idHora):
    hora=Agendar.objects.get(idHora=v_idHora)

    Agendar.delete(hora)

    return redirect('/verH')  


# Metodo que redirecciona al formulario de modificacion tomando de referencia la id del objeto a modificar
def modificarHora(request, v_idHora):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']

        hora=Agendar.objects.get(idHora=v_idHora)
        dia=Dia.objects.all()
        mes=Mes.objects.all()
        horas=Hora.objects.all()
        medico=Medico.objects.all()

        informacion={'datos': hora, 'dias': dia, 'meses': mes, 'horas': horas, 'medicos': medico, 'nombre': nombre}
        return render(request, 'formMH.html', informacion)  
    else:
        return HttpResponse('No existe la sesion')    


# Metodo que guarda las modificaciones al objeto
def modificarGuardarHora(request):
    v_idHora=request.POST.get('idHora')
    v_dia=request.POST.get('dia') 
    v_mes=request.POST.get('mes') 
    v_hora=request.POST.get('hora') 
    v_medico=request.POST.get('medico')

    #Buscar dia,mes,hora y medico
    dia=Dia.objects.get(dia=v_dia)
    mes=Mes.objects.get(mes=v_mes)
    hora=Hora.objects.get(hora=v_hora)
    medico=Medico.objects.get(idMedico=v_medico)  

    #Buscar la Hora para modificar
    agendar=Agendar.objects.get(idHora=v_idHora)

    agendar.dia=dia
    agendar.mes=mes
    agendar.hora=hora
    agendar.medico=medico  


    Agendar.save(agendar)

    return redirect('/verH')          

def verHora(request):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']
        #Metodo que trae todos los Medicos
        horas=Agendar.objects.all()
        #Variable que pase los datos del medico al template
        datos ={'horas': horas, 'nombre': nombre}
        return render(request, 'verH.html', datos)
    else:
        return HttpResponse('No existe la sesion')    

def vermedico(request):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']
        nom=request.session.get('nombre')
        #Metodo que trae todos los Medicos
        medicos= Medico.objects.all()
        #Variable que pase los datos del medico al template
        datos ={'nombre':nom,'medicos': medicos, 'nombre': nombre}
        return render(request, 'verM.html', datos)
    else:
        return HttpResponse('No existe la sesion')       

def vermedico2(request):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']
        nom=request.session.get('nombre')
        #Metodo que trae todos los Medicos
        medicos= Medico.objects.all()
        #Variable que pase los datos del medico al template
        datos ={'nombre':nom,'medicos': medicos, 'nombre': nombre}
        return render(request, 'verM2.html', datos) 
    else:
        return HttpResponse('No existe la sesion')    

def verpaciente(request):
    if request.session.get('nombre'):         #Con esta condicion, si un usuario no a iniciado sesion, se previene el acceso forzado a las otras pestañas de la pagina
        nombre=request.session['nombre']
        nom=request.session.get('nombre')
        #Metodo que trae todos los Pacientes
        pacientes= UsuarioP3.objects.all()
        #Variable que pase los datos del paciente al template
        datos ={'nombre':nom, 'pacientes': pacientes, 'nombre': nombre}
        return render(request, 'verP.html', datos)     
    else:
        return HttpResponse('No existe la sesion')
