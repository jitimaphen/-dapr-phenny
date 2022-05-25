from django.http import HttpResponse, JsonResponse
from tenant.models import Member
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
import requests
import json

from tenant.serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def create(self, request, *args, **kwargs):
        print("Django: create func--------------------", request.data)
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            print("Django: create success")
            state = [{"key": "user", "value": new_user.id}]
            print("Django: send state")
            requests.post("http://localhost:3500/v1.0/state/statestore", data=json.dumps(state))
            print("Django: send to bird in pythonapp")
            requests.post("http://localhost:3500/v1.0/invoke/pythonapp/method/bird", data=json.dumps(state))
            print("Django: Finish-------------------------")
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)