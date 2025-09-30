from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Student, Grade, Subject
from datetime import datetime
import calendar


def diary_view(request, student_id=None):
    all_students = Student.objects.all()

    if student_id is None:
        if all_students.exists():
            student = all_students.first()
        else:
            student = None
    else:
        student = get_object_or_404(Student, id=student_id)

    subjects = Subject.objects.all()

    grades_query = Grade.objects.filter(student=student)

    selected_month = request.GET.get('month')
    if selected_month:
        try:
            month_num = int(selected_month)
            grades_query = grades_query.filter(date__month=month_num)
        except (ValueError, TypeError):
            selected_month = None

    selected_subject = request.GET.get('subject')
    if selected_subject:
        try:
            subject_id = int(selected_subject)
            grades_query = grades_query.filter(subject_id=subject_id)
        except (ValueError, TypeError):
            selected_subject = None

    grades = grades_query.select_related('subject').order_by('-date')

    statistics = {}
    if grades.exists():
        grade_values = [grade.grade for grade in grades]
        unique_subjects = grades.values('subject').distinct().count()

        statistics = {
            'total_grades': grades.count(),
            'average_grade': sum(grade_values) / len(grade_values),
            'highest_grade': max(grade_values),
            'subjects_count': unique_subjects
        }

    months = [
        (1, 'Січень'), (2, 'Лютий'), (3, 'Березень'), (4, 'Квітень'),
        (5, 'Травень'), (6, 'Червень'), (7, 'Липень'), (8, 'Серпень'),
        (9, 'Вересень'), (10, 'Жовтень'), (11, 'Листопад'), (12, 'Грудень')
    ]

    context = {
        'student': student,
        'all_students': all_students,
        'grades': grades if student else [],
        'subjects': subjects,
        'months': months,
        'selected_month': int(selected_month) if selected_month else None,
        'selected_subject': int(selected_subject) if selected_subject else None,
        'statistics': statistics,
    }

    return render(request, 'portal_look/diary.html', context)