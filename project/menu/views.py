from django.shortcuts import render


def menu_example_view(request):
    return render(request, 'menu/example.html')

def about_view(request):
    return render(request, 'menu/about.html')