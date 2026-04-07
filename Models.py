from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    room_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Complaint(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    complaint_text = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.name} - {self.status}"