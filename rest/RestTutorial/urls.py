from django.urls import path

from . import views

urlpatterns = [
    path('course/', views.CourseList.as_view()),
    path('course/<int:pk>', views.DetailCourse.as_view()),
]
