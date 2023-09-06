from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from student.models import Student
from .models import Qualification
from user.models import ReportCode
from django.forms.models import model_to_dict
from datetime import date
from django.db.models import Sum
import json
from .gen_report import *
from uuid import uuid4
from django.conf import settings
from django.db import transaction





def monthly_report_by_course(request, grade, month, year):

    # Reporte mensual por curso
    grade = grade
    month = month
    year = year
    

    students = Student.objects.filter(
        owner=request.user,
        is_active=True,
        grade=grade,
    )

    if students.count() == 0:
        return JsonResponse({'error': 'No hay calificaciones para el mes y año especificados'}, status=404)

    output = []
    for student in students:
        # Todas las calificaciones del estudiante en el mes y año especificados
        qualifications = Qualification.objects.filter(
            is_active=True,
            date__month=int(month), 
            date__year=int(year),
            student=student
        )
        record_count = qualifications.count()
        
        if record_count == 0:
            output.append({
                'student_id': student.id,
                'student': student.full_name(),
                'participation_note': 0.00,
                'notebook_note': 0.00,
                'practice': 0.00,
                'exercise': 0.00,
                'presentation': 0.00,
                'final_work': 0.00,
                'penalty': 0.00,
                'value': 0.00
            })
            continue


        # Suma de todas las calificaciones para el estudiante en el mes y año especificados
        total_participation_note = qualifications.aggregate(Sum('participation_note'))['participation_note__sum']
        total_notebook_note = qualifications.aggregate(Sum('notebook_note'))['notebook_note__sum']
        total_practice = qualifications.aggregate(Sum('practice'))['practice__sum']
        total_exercise = qualifications.aggregate(Sum('exercise'))['exercise__sum']
        total_presentation = qualifications.aggregate(Sum('presentation'))['presentation__sum']
        total_final_work = qualifications.aggregate(Sum('final_work'))['final_work__sum']
        total_penalty = qualifications.aggregate(Sum('penalty'))['penalty__sum']
        total_value = qualifications.aggregate(Sum('value'))['value__sum']
        
        output.append({
            'student_id': student.id,
            'student': student.full_name(),
            'participation_note': round(total_participation_note / record_count, 2),
            'notebook_note': round(total_notebook_note / record_count, 2),
            'practice': round(total_practice / record_count, 2),
            'exercise': round(total_exercise / record_count, 2),
            'presentation': round(total_presentation / record_count, 2),
            'final_work': round(total_final_work / record_count, 2),
            'penalty': round(total_penalty / record_count, 2),
            'value': round(total_value / record_count, 2)
        })

    return JsonResponse(output, safe=False)


def view_monthly_report_by_course(request):
    return render(request, 'qualification_by_month.html')


def pdf_report(request):
    if request.method == "POST":

        with transaction.atomic():
            document = json.loads(request.body.decode("utf-8"))
            head = document["head"]
            body = document["body"]
            security_code = ReportCode.objects.get(owner=request.user)
            security_code.consecutive += 1
            security_code.save()
            head["security_code"] = security_code.get_code() #"G1-RPT-10000001"
            filename = f"{head['security_code']}-{str(uuid4())}.pdf"
            path = settings.MEDIA_ROOT / filename
            if head["frequency"] == "m":
                to_pdf(str(path), head=head, body=body)
            if head["frequency"] == "p":
                to_pdf_p(str(path), head=head, body=body)

            return JsonResponse({
                "url": f"{settings.MEDIA_URL}{filename}"
            }, status=201)
    return HttpResponseBadRequest()

def periodically_report_by_course(request, grade, year):

    perids = {
    "P1": (date(year, 9, 1), date(year, 10, 31)), # Septiembre - Octubre 
    "P2": (date(year, 11, 1), date(year + 1, 1, 31)),  # Noviembre - Enero
    "P3": (date(year, 2, 1), date(year, 4, 30)),  # Febrero - Abril
    "P4": (date(year, 5, 1), date(year, 6, 30))  # Mayo - Junio
    }

    students = Student.objects.filter(
        owner=request.user,
        is_active=True,
        grade=grade,
    )

    if students.count() == 0:
        return JsonResponse({'error': 'No hay calificaciones para el mes y año especificados'}, status=404)

    output = []
    for student in students:
        obj = {
                'student_id': student.id,
                'student': student.full_name(),
                'participation_note': 0.00,
                'notebook_note': 0.00,
                'practice': 0.00,
                'exercise': 0.00,
                'presentation': 0.00,
                'final_work': 0.00,
                'penalty': 0.00,
                'value': 0.00,
                '_children': []
                }
        for p in perids.items():
            
            # Todas las calificaciones del estudiante en el mes y año especificados
            qualifications = Qualification.objects.filter(
                is_active=True,
                student=student,
                date__range=(p[1][0], p[1][1])
            )
            record_count = qualifications.count()
            
            if record_count == 0:
                obj["_children"].append({
                    'student_id': student.id,
                    'student': p[0],
                    'participation_note': 0.00,
                    'notebook_note': 0.00,
                    'practice': 0.00,
                    'exercise': 0.00,
                    'presentation': 0.00,
                    'final_work': 0.00,
                    'penalty': 0.00,
                    'value': 0.00
                })
                continue


            # Suma de todas las calificaciones para el estudiante en el mes y año especificados
            total_participation_note = qualifications.aggregate(Sum('participation_note'))['participation_note__sum']
            total_notebook_note = qualifications.aggregate(Sum('notebook_note'))['notebook_note__sum']
            total_practice = qualifications.aggregate(Sum('practice'))['practice__sum']
            total_exercise = qualifications.aggregate(Sum('exercise'))['exercise__sum']
            total_presentation = qualifications.aggregate(Sum('presentation'))['presentation__sum']
            total_final_work = qualifications.aggregate(Sum('final_work'))['final_work__sum']
            total_penalty = qualifications.aggregate(Sum('penalty'))['penalty__sum']
            total_value = qualifications.aggregate(Sum('value'))['value__sum']
            
            obj["_children"].append({
                'student_id': student.id,
                'student': p[0],
                'participation_note': round(total_participation_note / record_count, 2),
                'notebook_note': round(total_notebook_note / record_count, 2),
                'practice': round(total_practice / record_count, 2),
                'exercise': round(total_exercise / record_count, 2),
                'presentation': round(total_presentation / record_count, 2),
                'final_work': round(total_final_work / record_count, 2),
                'penalty': round(total_penalty / record_count, 2),
                'value': round(total_value / record_count, 2)
            })

            obj['participation_note'] += round(total_participation_note / record_count, 2)
            obj['notebook_note'] += round(total_notebook_note / record_count, 2)
            obj['practice'] += round(total_practice / record_count, 2)
            obj['exercise'] += round(total_exercise / record_count, 2)
            obj['presentation'] += round(total_presentation / record_count, 2)
            obj['final_work'] += round(total_final_work / record_count, 2)
            obj['penalty'] += round(total_penalty / record_count, 2)
            obj['value'] += round(total_value / record_count, 2)

        obj['participation_note'] = round(obj['participation_note'] / 4, 2)
        obj['notebook_note'] = round(obj['notebook_note'] / 4, 2)
        obj['practice'] = round(obj['practice'] / 4, 2)
        obj['exercise'] = round(obj['exercise'] / 4, 2)
        obj['presentation'] = round(obj['presentation'] / 4, 2)
        obj['final_work'] = round(obj['final_work'] / 4, 2)
        obj['penalty'] = round(obj['penalty'] / 4, 2)
        obj['value'] = round(obj['value'] / 4, 2)
 
        output.append(obj)


    return JsonResponse(output, safe=False)



 
def report(request):
    frequency = request.GET.get("frequency")
  
    if frequency.lower() == "p":
        grade = request.GET.get("grede")
        year = int(request.GET.get("year"))
        return periodically_report_by_course(request, grade, year)

    elif frequency.lower() == "m":
        grade = request.GET.get("grede")
        month = request.GET.get("month")
        year = request.GET.get("year")
        return monthly_report_by_course(request, grade, month, year)