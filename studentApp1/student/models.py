from django.db import models

from subject.models import Subject

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.IntegerField()
    email = models.EmailField()
    joined_date = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    joined_date = models.DateField()
    subject = models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True)
    experience = models.IntegerField()

    def __str__(self):
        return self.name    
    
    


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    mark = models.IntegerField()

    # class Meta:
    #     unique_together = ('student', 'subject')  # Prevent duplicate entries

    def __str__(self):
        return f"{self.student.name} - {self.subject.name}: {self.mark}"
    
    