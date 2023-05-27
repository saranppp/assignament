from django.shortcuts import render
import csv
from django.core.paginator import Paginator
from django.http import JsonResponse,HttpResponseRedirect
from .models import Student
from django.shortcuts import redirect
from .forms import StudentForm

def load_student_details(request):
    # Assuming CSV file format with headers: id, name, total_marks
    file_path = 'C:/Users/saran p s/Desktop/assignament/stu/student_marks.csv'  # Update with your file path
    page_number = int(request.GET.get('page', 1))
    page_size = int(request.GET.get('page_size', 10))

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        students = []
        for row in reader:
            student = Student(
                id=row['id'],
                name=row['name'],
                total_marks=row['total_marks'],
                # Set other field values accordingly
            )
            students.append(student)

        paginator = Paginator(students, page_size)
        page = paginator.get_page(page_number)
        serialized_students = [
            {
                'id': student.id,
                'name': student.name,
                'total_marks': student.total_marks,
                # Add other fields here
            }
            for student in page
        ]

        return render(request, 'stuapp/student_details.html', {'students': serialized_students})

def filter_student_details(request):
    filter_criteria = request.GET.get('filter_criteria')
    filter_value = request.GET.get('filter_value')

    file_path = 'C:/Users/saran p s/Desktop/assignament/stu/student_marks.csv'  # Update with your file path

    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        students = []
        for row in reader:
            if filter_criteria == 'id' and filter_value != row['id']:
                continue
            if filter_criteria == 'name' and filter_value.lower() not in row['name'].lower():
                continue
            student = Student(
                id=row['id'],
                name=row['name'],
                total_marks=row['total_marks'],
                # Set other field values accordingly
            )
            students.append(student)

        serialized_students = [
            {
                'id': student.id,
                'name': student.name,
                'total_marks': student.total_marks,
                # Add other fields here
            }
            for student in students
        ]

        return JsonResponse({'students': serialized_students})


def home(request):
    return render(request, 'stuapp/home.html')