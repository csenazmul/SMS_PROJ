from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Student
from .forms import StudentForm

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success = 'Student record added successfully!'
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/student_form.html', {'form': form})

def edit_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success = 'Student record updated successfully!'
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/student_form.html', {'form': form})

def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == 'POST':
        student.delete()
        messages.success = 'Student record deleted successfully!'
        return redirect('student_list')
    return render(request, 'students/student_confirm_delete.html', {'student': student})
# The student_list view retrieves all student records from the database and renders them in the student_list.html template.
# The add_student view handles the form submission for adding a new student record to the database.
# It creates a new StudentForm instance with the request data and saves the form if it is valid.
# The edit_student view handles the form submission for editing an existing student record in the database.
# It retrieves the student record with the specified id from the database and populates the form with the student data.
# It then saves the form if it is valid.
# The delete_student view handles the form submission for deleting a student record from the database.
# It retrieves the student record with the specified id from the database and deletes it.
# The views use the StudentForm class from the forms module to handle form validation and submission.
# The form data is validated against the model fields defined in the Student model.
# If the form data is valid, the student record is saved to the database.
# We also use the messages framework to display success messages after adding, editing, or deleting student records.
# Next, we will create the HTML templates for rendering the student records and forms in the browser.
# Create a new file called student_list.html in the templates/students directory and add the following code:
#
# {% extends 'base.html' %}
#
# {% block content %}
# <div class="container">
#     <h1>Student List</h1>
#     <a href="{% url 'add_student' %}" class="btn btn-primary mb-3">Add Student</a>
#     <table class="table">
#         <thead>
#             <tr>
#                 <th>Name</th>
