from django.shortcuts import render

# Create your views here.

def admin_home_page(request):
    return render(request, 'hodapp/index.html')

def admin_add_staff_page(request):
    return render(request, 'hodapp/add_staff_template.html')
