from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='subject'),
    path("create/",views.create_subject, name="create_subject"),
    path("success/",views.subject_success, name="subject_success"),
    path("view/",views.subject_list, name="subject_list"),
    path("view/<int:subject1_id>", views.subject_detail, name="subject_detail"),
    path("edit/<int:subject_id>", views.edit_subject, name="edit_subject"),
    path("mark/<int:student_id>", views.add_multiple_marks,name="add_multiple_marks")
    ]