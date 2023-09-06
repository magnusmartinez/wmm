from django.db import models
from user.models import User
from utils.utils import grade_choices
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver

class AchievementIndicator(models.Model):
    owner = models.ForeignKey(User, related_name='achievement_indicator_user', on_delete=models.DO_NOTHING, verbose_name="Docente")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'achievement_indicator'
        verbose_name_plural = 'Achievement Indicators' 

    def __str__(self):
        return self.description

class FundamentalCompetencies(models.Model):
    owner = models.ForeignKey(User, related_name='fundamental_competencies_user', on_delete=models.DO_NOTHING, verbose_name="Docente")
    name = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    achievement_indicators = models.ManyToManyField("AchievementIndicator", verbose_name="Indicadores de logro")
    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'fundamental_competencies'
        verbose_name_plural = 'Fundamental competencies' 

    def __str__(self):
        return self.name

class Qualification(models.Model):
    owner = models.ForeignKey(User, related_name='qualification_user', on_delete=models.DO_NOTHING, verbose_name="Docente")
    
    participation_note = models.FloatField(verbose_name="Participación", null=True, blank=True, default=0,
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=20.0, message="El valor debe ser menor o igual a 20.0")
        ]
    )
    notebook_note = models.FloatField(verbose_name="Cuaderno", null=True, blank=True, default=0,
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=10.0, message="El valor debe ser menor o igual a 10.0")
        ]
    )
    practice = models.FloatField(verbose_name="Prácticas", null=True, blank=True, default=0, 
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=5.0, message="El valor debe ser menor o igual a 5.0")
        ]
    )
    exercise = models.FloatField(verbose_name="Ejercicios", null=True, blank=True, default=0, 
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=5.0, message="El valor debe ser menor o igual a 5.0")
        ]
    )
    presentation = models.FloatField(verbose_name="Exposiciones", null=True, blank=True, default=0,
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=30.0, message="El valor debe ser menor o igual a 30.0")
        ]
    )
    final_work = models.FloatField(verbose_name="Trabajo final", null=True, blank=True, default=0,
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=30.0, message="El valor debe ser menor o igual a 30.0")
        ]
    )

    value = models.FloatField(verbose_name="Calificación mensual acomulada", null=True, blank=True, editable=False)
    penalty = models.FloatField(verbose_name="Penalización", null=True, blank=True, default=0, 
        validators=[ 
            MinValueValidator(limit_value=0.0, message="El valor debe ser mayor o igual a 0.0"),
            MaxValueValidator(limit_value=100.0, message="El valor debe ser menor o igual a 100.0")
        ]
    )
    

    student = models.ForeignKey('student.Student', related_name='student_qualification', on_delete=models.DO_NOTHING, verbose_name="Estudiante")
    fundamental_competencies = models.ForeignKey("FundamentalCompetencies", on_delete=models.DO_NOTHING)
    achievement_indicators = models.ManyToManyField("AchievementIndicator")

    date = models.DateField(verbose_name="Fecha", blank=False, null=False)
    comment = models.TextField(null=True, blank=True, verbose_name="Comentario")

    is_active = models.BooleanField(default=True, verbose_name="Activo")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'qualification'
        verbose_name_plural = 'qualifications' 

    def __str__(self):

        return f"Calificación de {self.student.full_name()} de {self.student.get_grade_human()} en {self.date}"

@receiver(pre_save, sender=Qualification)
def calcular_total_calificaciones(sender, instance, **kwargs):
    
    value = instance.participation_note + instance.notebook_note + instance.practice + instance.exercise + instance.presentation + instance.final_work
    instance.value = value - instance.penalty
    # instance.save()

