from django.contrib import admin
from .models import Student, Subject, Grade


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('first_name',)


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'date')
    list_filter = ('subject', 'date', 'grade')
    search_fields = ('studentfirst_name', 'studentlast_name', 'subject__name')
    date_hierarchy = 'date'
    ordering = ('-date',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('student', 'subject')