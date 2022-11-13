from django.shortcuts import render


def view_resume(request):
    return render(request, 'resume_page.html')

def home_page(request):
    return render(request, 'home.html')
