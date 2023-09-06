from django.contrib import admin
from .models import Student
from django.urls import reverse
from django.utils.html import format_html
admin.site.disable_action('delete_selected')


class StudentAdmin(admin.ModelAdmin):
    list_display = ('edit_link', 'name', 'last_name', 'email', 'date_of_birth', 'address', 'code', 'get_grade_display', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'last_name', 'code', 'grade')
    list_filter = ("grade", "is_active")

    list_per_page = 20

    def edit_link(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk])
    
        return format_html('<a href="{}">Editar</a>', edit_url)
    edit_link.short_description = 'Editar'

admin.site.register(Student, StudentAdmin)
