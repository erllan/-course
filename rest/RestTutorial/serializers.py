from rest_framework import serializers
from .models import Category, Course, Contact, Branch


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['user', "latitude", "longitude", "address", "course"]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    contact = ContactSerializer(many=True, read_only=True)
    branch = BranchSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'Category', 'logo', 'branch', 'contact']
