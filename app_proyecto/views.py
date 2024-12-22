from django.shortcuts import render

def inicio(request):
    return render(request, 'app_proyecto/inicio.html')