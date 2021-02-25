from django.urls import path
from home import views
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view

API_TITLE = 'Management API'
API_DESCRIPTION = 'An API for managing task within an organization'

urlpatterns = [
    path('',  include_docs_urls(title=API_TITLE)),
    path('projects/', views.ProjectListView.as_view()),
    path('projects/<int:pk>/', views.ProjectListView.as_view()),
    path('documentation/', views.DocumentationListView.as_view()),
    path('documentation/<int:pk>/', views.DocumentationDetailView.as_view()),
]
