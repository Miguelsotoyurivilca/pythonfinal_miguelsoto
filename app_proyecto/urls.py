# app_proyecto/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="index"),
    path('about/', views.about, name="about"),
    
    
    # cursos
    path('cursos/', views.cursos, name="cursos"),
    path('curso-detalle/<int:id>', views.detalle_curso_view, name="curso-detalle"),
    path('curso-formulario', views.formulario_curso_api, name="curso-formulario"),
    path('curso-editar/<int:id>', views.editar_curso, name="curso-editar"),
    path('curso-eliminar/<int:id>', views.eliminar_curso, name="curso-eliminar"),

    # students
    path('students/', views.students, name="students"),
    path('students-detalle/<int:id>', views.detalle_students_view, name="students-detalle"),
    path('students-formulario', views.formulario_students, name="students-formulario"),
    path('students-editar/<int:id>', views.editar_students_view, name="students-editar"),
    path('students-eliminar/<int:id>', views.eliminar_students_view, name="students-eliminar"),

    # profesores
    path('trainer/', views.trainer, name='trainer'),
    path('trainer-formulario/', views.formulario_trainer, name='trainer-formulario'),
    path('trainer-eliminar/<int:id>/', views.eliminar_trainer, name='trainer-eliminar'),
    path('trainer-editar/<int:id>/', views.editar_trainer, name='trainer-editar'),
    path('trainer-detalle/<int:id>/', views.detalle_trainer_view, name='trainer-detalle'),
    
    # login, registro y logout
    path('login/', views.login_view, name='login'),
    path("register/", views.register_view, name="register"),
    path("logout/", views.user_logout, name="logout"),
 
]