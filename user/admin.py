from django.contrib import admin
from .models import User
from django.urls import reverse
from django.utils.html import format_html

class UserAdmin(admin.ModelAdmin):
    list_display = ('edit_link','id', 'username', 'code', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined')
    search_fields = ("id", "username__startswith", "code", "first_name__startswith", "last_name__startswith")
    list_filter = ("is_active", "is_staff", "is_superuser", 'code')

    def edit_link(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk])
    
        return format_html('<a href="{}">Editar</a>', edit_url)
    edit_link.short_description = 'Editar'


    def virtualDelete(modeladmin, request, queryset):  
        queryset.update(is_active=False)

    virtualDelete.short_description = "Eliminacion parcial (is_active=False)"
    actions = [virtualDelete]

admin.site.register(User, UserAdmin)