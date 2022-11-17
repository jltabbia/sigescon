from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from edificios.models import Edificios
<<<<<<< HEAD
=======

>>>>>>> 1c71acfc4e421a2a797cfa8ed15e0495bd4e0c32

# Create your views here.
@login_required()


def HomeView(request):
    edificios=Edificios.objects.filter(administrador=request.user) 
    return render(request,'ingreso.html',{'edificios':edificios})

def ingreso(request,id):
    
    edificio=Edificios.objects.filter(id=id)
 
    for e in edificio:
    
        datos={
            'id':e.id,
            'nombre':e.nombre,
            'domicilio':e.domicilio,
        }
<<<<<<< HEAD
    
=======
   
>>>>>>> 1c71acfc4e421a2a797cfa8ed15e0495bd4e0c32
    context={
        'edificio':datos
    }
    return render(request,'index.html',context=context)

def cerrarSesion(request):
    logout(request)
    return redirect('index')
