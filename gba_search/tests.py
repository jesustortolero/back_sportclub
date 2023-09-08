from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import datetime

from .models import Person
from gba_search.serializer import PersonSerializer

class PersonListTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.person1 = Person.objects.create(dni="123456789", name="John", birth_day="1990-01-01", is_gba=True)
        cls.person2 = Person.objects.create(dni="987654321", name="Jane", birth_day="1985-06-15", is_gba=False)


    def test_filter_by_is_gba(self):
        # Test filtering by is_gba=True
        url = reverse('person-list')
        response = self.client.get(url, {'is_gba': 'true'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "John")

    def test_filter_by_birth_date_range(self):
        # Test filtering by birth date range
        url = reverse('person-list')
        client = APIClient()
        response = client.get(url, {'start_date': '1980-01-01', 'end_date': '1995-01-01'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_invalid_date_format(self):
        # Test with invalid date format
        url = reverse('person-list')
        client = APIClient()
        response = client.get(url, {'start_date': 'invalid-date'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_no_query_params(self):
        # Test when no query params are provided
        url = reverse('person-list')
        client = APIClient()
        response = client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

