from django.shortcuts import render


def projects(request):
    """Get projects page"""
    return render(request, 'projects/index.html')