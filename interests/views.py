from django.shortcuts import render


def interests(request):
    """Get interests page"""
    return render(request, 'interests/index.html')