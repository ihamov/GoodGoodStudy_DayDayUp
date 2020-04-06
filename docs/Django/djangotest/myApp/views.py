from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World!')

from .models import Grades, Students
def grades(request):
    # 去模板获取数据
    gradesList = Grades.objects.all()
    # 将数据传递给模板
    # 模板渲染页面，将渲染好的页面返回给浏览器
    return render(request, 'myAPP/grades.html',{'grades':gradesList})

def students(request):
    studentsList = Students.objects.all()
    return render(request, 'myApp/students.html', {'students':studentsList})