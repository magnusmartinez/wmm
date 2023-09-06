from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.utils import generate_random_code
from uuid import uuid4
from django.db.models.signals import post_save
from django.dispatch import receiver

class User(AbstractUser):
    """Custom user model that extends the AbstractUser model provided by Django.

    Inherits the following fields from AbstractUser:
    - username: Required. 150 characters or fewer.
    - first_name: First name of the user (optional).
    - last_name: Last name of the user (optional).
    - email: Email address of the user (optional).
    - is_staff: Designates whether the user can access the admin site.
    - is_active: Designates whether the user is active.
    - date_joined: Date and time when the user joined.

    Additional field:
    - code: Code of the user (optional).

    Meta:
        db_table (str): Name of the table in the database.
    """
    
    code = models.CharField(max_length=7, null=False, blank=False, unique=True, default=generate_random_code)
    
    class Meta:
        db_table = 'user'
        verbose_name_plural = 'users'



class ReportCode(models.Model):
    # G1-RPT-1000001  
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='report_user')
    consecutive = models.BigIntegerField(null=False, blank=False, default=1000001, editable=False) 
    generation = models.CharField(max_length=7, null=False, blank=False, default='G1-RPT-', editable=False)
    code = models.UUIDField(null=False, blank=False, default=uuid4)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'report_code'
        verbose_name_plural = 'report codes'
    
    def get_code(self):
        return f"{self.generation}{self.consecutive}"

    def __str__(self):
        return self.code

@receiver(post_save, sender=User)
def create_default_report_code(sender, instance, **kwargs):
    query = ReportCode.objects.filter(owner_id=instance.id)
    if query.count() == 0:
        ReportCode.objects.create(owner=instance)
