from django.shortcuts import render, redirect
from django.views import View
from mi_aplicacion.models import Escuela, Maestro
from mi_aplicacion.form import EscuelaForm, MaestroForm

class Home(View):
    def get(self, request):
        cdx={
        "titulo":"Home",
        "subtitulo":"Bienvenido a mi primer aplicacion"
        }
        return render(request , "base.html", cdx)
    
class Escuelas(View):
    def get(self, request):
        escuelas = Escuela.objects.all()
        cdx={
        "titulo":"Escuelas",
        "subtitulo":"Lista de escuelas",
        "escuelas":escuelas
        }
        return render(request , "escuelas/escuelas.html", cdx)
    
class EscuelaAlta(View):
    def get(self, request):
        form = EscuelaForm()
        cdx={
        "subtitulo":"Escuela Alta",
        "form":form
        }
        return render(request , 'escuelas/CRUD.html', cdx)
    
    
    def post(self, request):
        form = EscuelaForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")

class EscuelaEditar(View):
    def get(self , request, id):
        escuelas = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuelas)
        cdx={
        "subtitulo":"Editar escuela",
        "form":form
        }
        return render(request , 'escuelas/CRUD.html', cdx)
    
    def post(self, request, id):
        escuelas = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST , request.FILES, instance=escuelas)
        if form.is_valid():
            form.save()
            return redirect('escuelas')
        return redirect("home")
    

class EscuelaEliminar(View):
    def get(self, request, id):
        escuelas = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(instance=escuelas)
        cdx={
        "subtitulo":"Eliminar escuela",
        "form":form
        }
        return render(request , 'escuelas/CRUD.html', cdx)
    
    
    def post(self, request, id):
        escuelas = Escuela.objects.filter(id=id).first()
        form = EscuelaForm(request.POST , request.FILES, instance=escuelas)
        if form.is_valid():
            escuelas.delete()
            return redirect('escuelas')
        return redirect("home")
    
class Maestros(View):
    def get(self, request):
        maestros = Maestro.objects.all()
        cdx={
        "titulo":"Mestros",
        "subtitulo":"Lista de maestros",
        "maestros":maestros
        }
        return render(request , "maestros/maestros.html", cdx)

class MaestroAlta(View):
    def get(self, request):
        form = MaestroForm()
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Alta Maestro",
        "form":form
        }
        return render(request , 'maestros/CRUD.html', cdx)