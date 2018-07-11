from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('add/',views.addTodo,name='add'),
    path('complete/<todo_id>',views.todocomplete,name='complete'),
    path('deleteall/',views.deleteAll,name='deleteall'),
    path('deletecomplete/',views.deleteComplete,name='deletecomp')
]