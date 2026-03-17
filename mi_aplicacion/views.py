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
        form = MaestroForm(action_type='Alta')
        cdx={
        "titulo":"Maestros",
        "subtitulo":"Alta Maestro",
        "form":form,
        "accion":"Alta"
        }
        return render(request , 'maestros/CRUD.html', cdx)
    
    def post(self, request):
        form = MaestroForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect("home")
    
class MaestroEliminar(View):
    def get(self, request, id):
        maestros = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestros, action_type='Eliminar')
        cdx={
        "subtitulo":"Eliminar maestro",
        "form":form,
        "accion":"Eliminar"
        }
        return render(request , 'maestros/CRUD.html', cdx)
    
    
    def post(self, request, id):
        maestros = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST , request.FILES, instance=maestros)
        if form.is_valid():
            maestros.delete()
            return redirect('maestros')
        return redirect("home")
    
class MaestroEditar(View):
    def get(self , request, id):
        maestros = Maestro.objects.filter(id=id).first()
        form = MaestroForm(instance=maestros, action_type='Editar')
        cdx={
        "subtitulo":"Editar maestro",
        "form":form,
        "accion":"Editar"

        }
        return render(request , 'maestros/CRUD.html', cdx)
    
    def post(self, request, id):
        maestros = Maestro.objects.filter(id=id).first()
        form = MaestroForm(request.POST , request.FILES, instance=maestros)
        if form.is_valid():
            form.save()
            return redirect('maestros')
        return redirect("home")
    