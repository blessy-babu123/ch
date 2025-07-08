from django.shortcuts import render,redirect,get_object_or_404

from student.models import Marks,Student
from .models import Subject
from .forms import subjectForm
from django.http import HttpResponse
def home(request):
    return render(request, 'subject.html')
   
def subject(request):
    return render(request, 'create_subject.html')

def create_subject(request):
    if request.method == 'POST':
        name=request.POST.get("name")
        subCode=request.POST.get("subCode")
        Subject.objects.create(
            name=name,
            subCode=subCode,
        )
        return redirect('subject_list')

    return render(request,'create_subject.html')    
          
def subject_success(request):
    return HttpResponse("subject created successfully!")

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'subject.html', {'subjects': subjects})

def subject_detail(request, subject1_id):
    subject = get_object_or_404(Subject, id=subject1_id)
    return render(request, 'subject_detail.html', {'subject': subject})

def edit_subject(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    if request.method == 'POST':
       subject.name=request.POST.get("name")
       subject.subCode=request.POST.get("subCode")
       subject.save()
       return redirect('subject_detail',subject1_id=subject.id)
    
    return render(request, 'edit_subject.html', {'subject': subject})


def add_multiple_marks(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    subjects = Subject.objects.all()[:5]  # fetch only 5 subjects (you can also filter as needed)

    if request.method == 'POST':
        for subject in subjects:
            mark_value = request.POST.get(f'mark_{subject.id}')
            if mark_value:  # Only save if a mark is entered
                Marks.objects.update_or_create(
                    student=student,
                    subject=subject,
                    defaults={'mark': mark_value}
                )
        return redirect('student_detail',student_id=student_id)  # or student detail
    
    return render(request, 'add_multiple_marks.html', 
    {
        'student': student,
        'subjects': subjects
    })