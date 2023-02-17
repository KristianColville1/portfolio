from django.shortcuts import render


def get_home(request):
    """Get home page"""
    return render(request, 'home/index.html')