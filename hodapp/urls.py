from django.urls import path

from .views import (admin_home_page,admin_add_staff_page)

app_name = 'hodapp'

urlpatterns = [
    path('hodhome/', admin_home_page, name='hodhome'),
    path('addstaff', admin_add_staff_page, name='add-staff')
]