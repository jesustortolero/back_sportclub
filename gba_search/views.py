from datetime import datetime
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import Person
from gba_search.serializer import PersonSerializer

class PersonList(generics.ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        queryset = Person.objects.all()

        is_gba = self.request.query_params.get('is_gba')
        if is_gba:
            is_gba = is_gba.lower() == 'true'
            queryset = queryset.filter(is_gba=is_gba)

        start_date_param = self.request.query_params.get('start_date')
        end_date_param = self.request.query_params.get('end_date')

        if start_date_param:
            try:
                start_date = datetime.strptime(start_date_param, '%Y-%m-%d')
                queryset = queryset.filter(birth_day__gte=start_date)
            except ValueError:
                raise ValidationError("Invalid start_date format", code='invalid_start_date')

        if end_date_param:
            try:
                end_date = datetime.strptime(end_date_param, '%Y-%m-%d')
                queryset = queryset.filter(birth_day__lte=end_date)
            except ValueError:
                raise ValidationError("Invalid end_date format", code='invalid_end_date')

        return queryset.order_by('name')