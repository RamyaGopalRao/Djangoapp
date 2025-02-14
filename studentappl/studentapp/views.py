from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student, Course, Marks

class StudentListView(LoginRequiredMixin,ListView):
    model = Student
    template_name = 'student_list.html'

class StudentDetailView(LoginRequiredMixin,DetailView):
    model = Student
    template_name = 'studentapp/student_detail.html'

class StudentCreateView(LoginRequiredMixin,CreateView):
    model = Student
    template_name = 'studentapp/student_form.html'
    fields = ['name', 'age', 'grade', 'address', 'course']
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.course.set(self.request.POST.getlist('course'))
        return response

class StudentUpdateView(LoginRequiredMixin,UpdateView):
    model = Student
    template_name = 'studentapp/student_form.html'
    fields = ['name', 'age', 'grade', 'address', 'course']
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        form.instance.course.set(self.request.POST.getlist('course'))
        return response

class StudentDeleteView(LoginRequiredMixin,DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student_list')
class CourseListView(LoginRequiredMixin,ListView):
    model = Course
    template_name = 'studentapp/course_list.html'

class CourseDetailView(LoginRequiredMixin,DetailView):
    model = Course
    template_name = 'studentapp/course_detail.html'

class CourseCreateView(LoginRequiredMixin,CreateView):
    model = Course
    template_name = 'studentapp/course_form.html'
    fields = ['name']
    success_url = reverse_lazy('course_list')

class CourseUpdateView(LoginRequiredMixin,UpdateView):
    model = Course
    template_name = 'studentapp/course_form.html'
    fields = ['name']
    success_url = reverse_lazy('course_list')

class CourseDeleteView(LoginRequiredMixin,DeleteView):
    model = Course
    template_name = 'studentapp/course_confirm_delete.html'
    success_url = reverse_lazy('course_list')
