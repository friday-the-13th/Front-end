from django.urls import path

from . import views

app_name = 'patient'

urlpatterns = [
	path('add/', views.add, name = 'add'),
	path('view/', views.view, name = 'view'),
	path('view_all/', views.view_all, name = 'view_all'),
	path('edit/', views.edit, name='edit'),
	path('edit_chart/', views.edit_chart, name='edit_chart'),
	path('delete/', views.delete, name='delete')
]
