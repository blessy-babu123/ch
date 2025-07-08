from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse

from .models import Student,Teacher,Marks
from subject.models import Subject
from .forms import StudentForm,TeacherForm
def home(request):
    paragraph = """
        <h1>Welcome to My Django Website</h1>
        <p>
            Django is a high-level Python web framework that encourages rapid development 
            and clean, pragmatic design. It’s built by experienced developers to help you take 
            applications from concept to completion as quickly as possible.
        </p>
        <p>
            This page demonstrates how you can return an HTML paragraph directly from a Django view.
        </p>
    """
    return HttpResponse(paragraph)

def home1(request):
    return render(request, 'home1.html')
def home2(request):
    return render(request, 'home2.html')
def about(request):
    return render(request, 'about.html')


def create_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('student_success')
    else:
        form = StudentForm()
    return render(request, 'create_student.html', {'form': form})

def student_success(request):
    return HttpResponse("Student created successfully!")

from django.shortcuts import render, redirect, get_object_or_404
from .models import Teacher
from .forms import TeacherForm  # Assuming you're using a Django form

def create_Teacher(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age =request.POST.get('Age')
        joined_date = request.POST.get('joined_date')
        subject_id = request.POST.get('subject')
        experience =request.POST.get('experience')
        subjectObj=Subject.objects.get(id= subject_id)
        Teacher.objects.create(
            name=name, 
            age=age,
            joined_date=joined_date,
            subject=subjectObj, 
            experience=experience, 
        )
        return redirect('teacher_list') 
    
    subjects = Subject.objects.all()     
    return render(request, 'create_teacher.html',{'subjects':subjects})


def Teacher_success(request):
    return HttpResponse("Teacher created successfully!")

def student_list(request):
    students = Student.objects.all()
    return render(request, 'view_students.html', {'students': students})
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'view_teachers.html', {'teachers': teachers})


def teacher_detail(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'teacher_detail.html', {'teacher': teacher})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    marks=Marks.objects.filter(student=student_id)
    return render(request, 'student_detail.html', {'student': student,'marks':marks})

def edit_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)
    
    if request.method == 'POST':
        teacher.name = request.POST.get('name')
        teacher.age =request.POST.get('Age')
        teacher.joined_date = request.POST.get('joined_date')
        subject_id = request.POST.get('subject')
        teacher.experience =request.POST.get('experience')
        teacher.subject=Subject.objects.get(id=subject_id)
        teacher.save()
        return redirect('teacher_detail',teacher_id=teacher_id)
    subjects=Subject.objects.all()
    return render(request, 'edit_teacher.html', {'teacher': teacher,'subjects':subjects})
   
def edit_student(request, student_id):
    student= get_object_or_404(Student, id=student_id)
    
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.roll_no =request.POST.get('roll_no')
        student.email= request.POST.get('email')
        student.joined_date = request.POST.get('joined_date')
        student.save()
        return redirect('student_detail',student_id=student_id)
    return render(request, 'edit_student.html', {'student':student})    


def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')  
    return render(request, 'delete_student.html', {'student': student})

def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')  
    return render(request, 'delete_teacher.html', {'teacher': teacher})

def images(request):
    students = Student.objects.all()
    return render(request, 'images.html', {'students': students})