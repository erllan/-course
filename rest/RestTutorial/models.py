from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)
    icon = models.ImageField(verbose_name='icon', upload_to='imgpath/')


class Course(models.Model):
    name = models.CharField(verbose_name='name', max_length=255)
    logo = models.ImageField(verbose_name='logo', upload_to='course_logo', null=True)
    description = models.CharField(verbose_name='description', max_length=255)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Branch(models.Model):
    user = models.ForeignKey(User, verbose_name='user', on_delete=models.CASCADE, null=True)
    latitude = models.CharField(verbose_name='latitude', max_length=255)
    longitude = models.CharField(verbose_name='longitude', max_length=255)
    address = models.CharField(verbose_name='address', max_length=255)
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE, null=True,
                               related_name='branch')

    def __str__(self):
        return self.address


class Contact(models.Model):
    CONTACT_TYPES = (
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL')
    )
    contact_type = models.IntegerField(verbose_name='value', choices=CONTACT_TYPES)
    value = models.CharField(verbose_name='contact', max_length=255)
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE, null=True,
                               related_name='contact')

    def __str__(self):
        return self.value
