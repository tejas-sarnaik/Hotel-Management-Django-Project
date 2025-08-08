from django.urls import path
from peoplemanagement import views

urlpatterns = [
    path('',views.home),
    path('registration/',views.registration),
    path('record/',views.record),
    path('update/<id>/',views.update),
    path('delete/<id>/',views.delete),

]
