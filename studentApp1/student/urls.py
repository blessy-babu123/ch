from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home1, name='home1'),
    path('home2', views.home2, name='home2'),
    path('about', views.about, name='about'),
    path('create/', views.create_student, name='create_student'),
    path('success/', views.student_success, name='student_success'),
    path("create1/",views.create_Teacher, name="create_Teacher"),
    path("view/<int:student_id>", views.student_detail, name="student_detail"),
    path("edit/<int:student_id>", views.edit_student, name="edit_student"),
    path("success1/",views.Teacher_success, name="Teacher_success"),
    path("view/",views.student_list, name="student_list"),
    path("view1/",views.teacher_list, name="teacher_list"),
    path("view1/<int:teacher_id>/", views.teacher_detail, name="teacher_detail"),
    path("edit1/<int:teacher_id>/", views.edit_teacher, name="edit_teacher"),
    path("delete/<int:student_id>/",views.delete_student, name="delete_student"),
    path("delete1/<int:teacher_id>/",views.delete_teacher, name="delete_teacher"),
    path('student/images/', views.images, name='images'),

    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
