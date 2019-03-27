from django.urls import path

from . import views

app_name = 'questionnaire'

urlpatterns = [
	path('administer/', views.administer, name = 'administer'),
	path('view_response/', views.viewResponse, name = 'view_response'),
	path('create/', views.create, name = 'create')
]