from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Marks

class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'studentapp/student_detail.html'

class StudentCreateView(CreateView):
    model = Student
    template_name = 'studentapp/student_form.html'
    fields = ['name', 'age', 'grade', 'address', 'course']
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.course.set(self.request.POST.getlist('course'))
        return response

class StudentUpdateView(UpdateView):
    model = Student
    template_name = 'studentapp/student_form.html'
    fields = ['name', 'age', 'grade', 'address', 'course']
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.course.set(self.request.POST.getlist('course'))
        return response

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
class CourseListView(ListView):
    model = Course
    template_name = 'studentapp/course_list.html'

class CourseDetailView(DetailView):
    model = Course
    template_name = 'studentapp/course_detail.html'

class CourseCreateView(CreateView):
    model = Course
    template_name = 'studentapp/course_form.html'
    fields = ['name']
    success_url = reverse_lazy('course_list')

class CourseUpdateView(UpdateView):
    model = Course
    template_name = 'studentapp/course_form.html'
    fields = ['name']
    success_url = reverse_lazy('course_list')

class CourseDeleteView(DeleteView):
    model = Course
    template_name = 'studentapp/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
