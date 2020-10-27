from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory
from .models import Course, Contact, Branch, Category


class CourseTest(APITestCase):
    def test_category(self):
        url = reverse('category')
        data = {'name': 'category'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'test')

    # def test_create_course(self):
    #     url = reverse('course_list')
    #     data = {'name': 'test', 'description': 'desk', "Category": None}
    #     response = self.client.post(url, data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(Course.objects.count(), 1)
    #     self.assertEqual(Course.objects.get().name, 'test')

    # def test_course_list(self):
    #     response = self.client.get(reverse('course_list')
    #     self.assertEqual(len(response.data), 0)
