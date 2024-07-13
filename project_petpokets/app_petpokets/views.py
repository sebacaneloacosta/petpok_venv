from django.shortcuts import render

def index(request):
    return render(request, 'app_petpokets/index.html')

def perros(request):
    return render(request, 'app_petpokets/perros.html')

def gatos(request):
    return render(request, 'app_petpokets/gatos.html')

def comidaperros(request):
    return render(request, 'app_petpokets/comidaperros.html')

def comidagatos(request):
    return render(request, 'app_petpokets/comidagatos.html')

def registro(request):
    return render(request, 'app_petpokets/registro.html')

from django.shortcuts import render, get_object_or_404, redirect
from .models import Usuario
from .forms import UsuarioForm

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render(request, 'usuario_list.html', {'usuarios': usuarios})

def usuario_detail(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    return render(request, 'usuario_detail.html', {'usuario': usuario})

def usuario_nuevo(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm()
    return render(request, 'usuario_edit.html', {'form': form})

def usuario_editar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            usuario = form.save()
            return redirect('usuario_detail', pk=usuario.pk)
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, 'usuario_edit.html', {'form': form})

def usuario_eliminar(request, pk):
    usuario = get_object_or_404(Usuario, pk=pk)
    if request.method == 'POST':
        usuario.delete()
        return redirect('usuario_list')
    return render(request, 'usuario_confirm_delete.html', {'usuario': usuario})

from django.shortcuts import render, redirect
from .models import Usuario
from .forms import UsuarioForm

def registrar_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro_exitoso')  # Redirigir a una página de registro exitoso o a donde desees
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})