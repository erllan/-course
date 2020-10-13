from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)
    icon = models.ImageField(verbose_name='icon', upload_to='imgpath/')


class Branch(models.Model):
    latitude = models.CharField(verbose_name='latitude', max_length=60)
    longitude = models.CharField(verbose_name='longitude', max_length=60)
    address = models.CharField(verbose_name='address', max_length=60)


class Course(models.Model):
    name = models.CharField(verbose_name='name', max_length=100)
    description = models.CharField(verbose_name='description', max_length=200)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    CONTACT_TYPES = (
        (1, 'PHONE'),
        (2, 'FACEBOOK'),
        (3, 'EMAIL')
    )
    contact_type = models.IntegerField(verbose_name='contact_type', choices=CONTACT_TYPES)
    contact = models.CharField(verbose_name='contact', max_length=200)
    branches = models.ForeignKey(Branch, on_delete=models.CASCADE)
