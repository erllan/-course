from django.urls import path

from . import views

urlpatterns = [
    path('course/', views.CourseList.as_view(), name='course_list'),
    path('course/<int:pk>', views.DetailCourse.as_view()),
    path('contact/', views.ContactList.as_view()),
    path('contact/<int:pk>', views.ContactDetail.as_view()),
    path('branch/', views.BranchList.as_view()),
    path('branch/<int:pk>', views.BranchDetail.as_view()),
    path('category/', views.CategoryList.as_view(), name='category'),
    path('category/<int:pk>', views.CategoryDetail.as_view())

]
