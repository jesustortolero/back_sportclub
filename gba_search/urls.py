from django.urls import path
from .views import PersonList

urlpatterns = [
    path('v1/people/', PersonList.as_view(), name='person-list'),
]
