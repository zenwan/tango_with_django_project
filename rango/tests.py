from django.test import TestCase

# Create your tests here.

from rango.models import Category

print(Category.objects.get(slug='python'))
