from django.shortcuts import render


def resume(request):
    """Get resume page"""
    return render(request, 'resume/index.html')