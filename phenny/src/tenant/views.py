from django.http import HttpResponse, JsonResponse
from tenant.models import Member
from rest_framework import viewsets
from rest_framework.response import Response

from tenant.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

