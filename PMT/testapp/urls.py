from django.urls import path
from testapp import views

urlpatterns = [
    path("create/", views.CreateClientAPIView.as_view(),name="client_create"),
    path("",views.ListClientAPIView.as_view(),name="client_list"),
    path("update/<int:pk>/",views.UpdateClientAPIView.as_view(),name="update_client"),
    path("delete/<int:pk>/",views.DeleteClientAPIView.as_view(),name="delete_client"),
    path("create/<int:pk>/projects/", views.CreateProjectAPIView.as_view(),name="Project_create"),
    path("project/",views.ListProjectAPIView.as_view(),name="project_list"),
]
