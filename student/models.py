from django.db import models
from utils.utils import generate_random_code, grade_choices
from user.models import User



class Student(models.Model):

    owner = models.ForeignKey(User, related_name='student_user', on_delete=models.DO_NOTHING, verbose_name='Docente')
    name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Nombre')
    last_name = models.CharField(max_length=100, blank=False, null=False, verbose_name='Apellido')
    email = models.EmailField(null=True, blank=True, verbose_name='Correo Electrónico')
    date_of_birth = models.DateField(null=True, blank=True, verbose_name='Fecha de Nacimiento')
    address = models.CharField(max_length=200, null=True, blank=True, verbose_name='Dirección')
    code = models.CharField(max_length=7, null=False, blank=False, unique=True, default=generate_random_code, verbose_name='Código')
    grade = models.CharField(max_length=3, null=True, blank=True, choices=grade_choices, default=grade_choices[0][0], verbose_name='Grado')
    is_active = models.BooleanField(default=True, verbose_name='Activo')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Fecha de Actualización')
    

    def __str__(self):
        return f"{self.full_name()} de {self.get_grade_human()}"

    def get_grade_human(self):
        return dict(grade_choices)[self.grade]

    def full_name(self):
        return f"{self.name} {self.last_name}"

    class Meta:
        db_table = 'student'
        verbose_name_plural = 'students'
