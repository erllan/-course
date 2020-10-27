from .models import *
from .serializers import ContactSerializer, CategorySerializer, BranchSerializer, CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class BranchList(APIView):
    """Class for Branch"""

    def get(self, request,format=None):
        branch = Branch.objects.all()
        serializer = BranchSerializer(branch, many=True)
        return Response(serializer.data)

    def post(self, request):
        branch = BranchSerializer(data=request.data)
        if branch.is_valid():
            branch.save()
            return Response('создано')
        else:
            return Response('ошибка')


class BranchDetail(APIView):
    """Class for Branch"""

    def get(self, request, pk):
        branch = Branch.objects.get(pk=pk)
        serializer = BranchSerializer(branch)
        return Response(serializer.data)

    def delete(self, request, pk):
        branch = Branch.objects.get(pk=pk)
        branch.delete()
        return Response('deleted')


class ContactList(APIView):
    """Class for Contact"""

    def get(self, request):
        contact = Contact.objects.all()
        serializer = ContactSerializer(contact, many=True)
        return Response(serializer.data)

    def post(self, request):
        contact = ContactSerializer(data=request.data)
        if contact.is_valid():
            contact.save()
        return Response(request.data)


class ContactDetail(APIView):
    """Class for Contact"""

    def get(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    def delete(self, request, pk):
        contact = Contact.objects.get(pk=pk)
        contact.delete()
        return Response('deleted')


class CategoryList(APIView):
    """Class for Category"""

    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request):
        category = CategorySerializer(data=request.data)
        if category.is_valid():
            category.save()
            return Response('создано')
        else:
            return Response('ошибка')


class CategoryDetail(APIView):
    """Class for Category"""

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def delete(self, request, pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return Response('deleted')


class CourseList(APIView):
    """Class for Course"""

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        createCourse = CourseSerializer(data=request.data)
        if createCourse.is_valid():
            createCourse.save()
            return Response('coздано')
        else:
            return Response("ошибка")


class DetailCourse(APIView):
    """Class for Course"""

    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response('deleted')
