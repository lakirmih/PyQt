from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Lesson, Student, Attendance

def index(request):
    return render(request, 'lessonapp/index.html')
    #return HttpResponse("Hello, World!")

def students(request):
    _students = Student.objects.all()
    return HttpResponse(_students)

def lessons(request):
    _lessons = Lesson.objects.all()
    return render(request, 'lessonapp/lessons.html', {'lessons': _lessons})

def student(request, student_id):
    return HttpResponse('Student: %s' % student_id)

def lesson(request, lesson_id):
    #try:
    #    _lesson = Lesson.objects.get(pk = lesson_id)
    #except Lesson.DoesNotExist:
    #    raise Http404
    _lesson = get_object_or_404(Lesson, pk = lesson_id)
    return render(request, 'lessonapp/lesson.html', {'lesson': _lesson})
    #return  HttpResponse('Lesson: %s' % lesson_id)

def attendance(request):
    from .forms import AttendanceForm
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        _student = request.POST.get('student')
    else:
        form = AttendanceForm()
    return render(request, 'lessonapp/attendance-form.html', {'form': form})
