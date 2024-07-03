from django.shortcuts import render, redirect, get_object_or_404
from .models import Students

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get("name")
        age = data.get("age")
        address = data.get("address")
        marks = data.get("marks")
        student_image = request.FILES.get("student_image")
        Students.objects.create(
            name=name,
            age=age,
            address=address,
            marks=marks,
            student_image=student_image,
        )
    queryset = Students.objects.all()
    context = {'students': queryset}
    return render(request, "index.html", context)

def delete_stds(request, id):
    student = get_object_or_404(Students, id=id)
    student.delete()
    return redirect('/')

def Update_stds(request, id):
    student = get_object_or_404(Students, id=id)
    if request.method == 'POST':
        student.name = request.POST.get('name')
        student.age = request.POST.get('age')
        student.address = request.POST.get('address')
        student.marks = request.POST.get('marks')

        if 'student_image' in request.FILES:
            student.student_image = request.FILES['student_image']
            
        student.save()
        return redirect('/')
    context = {'student': student}
    return render(request, "updtae.html", context)
