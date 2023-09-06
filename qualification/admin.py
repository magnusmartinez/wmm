from django.contrib import admin
from django import forms
from .models import Qualification, FundamentalCompetencies, AchievementIndicator
from django.urls import reverse
from django.utils.html import format_html
from django.http import HttpResponse
from django.urls import reverse
from django.template.loader import render_to_string

class AchievementIndicatorAdmin(admin.ModelAdmin):
    list_display = ('edit_link','owner', 'name', 'description', 'is_active', 'created_at', 'updated_at')

    def edit_link(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk])
    
        return format_html('<a href="{}">Editar</a>', edit_url)
    edit_link.short_description = 'Editar'

class FundamentalCompetenciesAdmin(admin.ModelAdmin):
    list_display = ('edit_link','owner', 'name', 'description', 'is_active', 'created_at', 'updated_at')

    def edit_link(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk])
    
        return format_html('<a href="{}">Editar</a>', edit_url)
    edit_link.short_description = 'Editar'



class QualificationAdmin(admin.ModelAdmin):
    list_display = ('edit_link','owner', 'student', 'date', 'participation_note', 'notebook_note', 'practice', 'exercise', 'presentation', 'final_work', 'value', 'penalty',  'comment', 'is_active', 'created_at', 'updated_at')
    list_per_page = 20
    change_list_template = 'report-month-link.html'
    list_filter = ("student", "date", "is_active")

 


    def edit_link(self, obj):
        edit_url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name),  args=[obj.pk])
    
        return format_html('<a href="{}">Editar</a>', edit_url)
    edit_link.short_description = 'Editar'

admin.site.register(AchievementIndicator, AchievementIndicatorAdmin)
admin.site.register(FundamentalCompetencies, FundamentalCompetenciesAdmin)
admin.site.register(Qualification, QualificationAdmin)
