from django.test import TestCase, Client
from django.urls import reverse
from .models import Student, Course
from django.contrib.auth.models import User

class StudentModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='Math')
        self.student = Student.objects.create(name='John Doe', age=18, grade='A', address='123 Main St')
        self.student.courses.add(self.course)

    def test_student_creation(self):
        self.assertEqual(self.student.name, 'John Doe')
        self.assertEqual(self.student.age, 18)
        self.assertEqual(self.student.grade, 'A')
        self.assertEqual(self.student.address, '123 Main St')
        self.assertIn(self.course, self.student.courses.all())

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(name='History')

    def test_course_creation(self):
        self.assertEqual(self.course.name, 'History')

class AuthenticationTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_login(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': 'testpass'})
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(response.url.startswith('/'))  # Redirect to home page

    def test_logout(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(response.url.startswith('/accounts/login/'))  # Redirect to login page

class StudentViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.course = Course.objects.create(name='Math')
        self.student = Student.objects.create(name='John Doe', age=18, grade='A', address='123 Main St')
        self.student.courses.add(self.course)
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_student_list_view(self):
        response = self.client.get(reverse('student_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

    def test_student_create_view(self):
        response = self.client.post(reverse('student_add'), {
            'name': 'Jane Doe',
            'age': 20,
            'grade': 'B',
            'address': '456 Main St',
            'courses': [self.course.id]
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.last().name, 'Jane Doe')

    def test_student_update_view(self):
        response = self.client.post(reverse('student_edit', args=[self.student.id]), {
            'name': 'John Smith',
            'age': 19,
            'grade': 'A+',
            'address': '789 Main St',
            'courses': [self.course.id]
        })
        self.assertEqual(response.status_code, 302)
        self.student.refresh_from_db()
        self.assertEqual(self.student.name, 'John Smith')

    def test_student_delete_view(self):
        response = self.client.post(reverse('student_delete', args=[self.student.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Student.objects.filter(id=self.student.id).count(), 0)
