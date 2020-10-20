from .models import Course
from .serializers import CourseSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class CourseList(APIView):

    def get(self, request):
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)

    def post(self, request):
        createCourse = CourseSerializer(data=request.data)
        if createCourse.is_valid():
            createCourse.save()
        return Response(request.data)


class DetailCourse(APIView):
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        course.delete()
        return Response('deleted')
