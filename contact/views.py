from django.shortcuts import render


def contact(request):
    """Get contact page"""
    return render(request, 'contact/index.html')