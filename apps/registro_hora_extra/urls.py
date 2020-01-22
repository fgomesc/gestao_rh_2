from django.urls import path
from .views import HoraExtraListList

urlpatterns = [
    path('', HoraExtraListList.as_view(), name='list_hora_extra'),
]
