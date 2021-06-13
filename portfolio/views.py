from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Project, ContactMe
from .serializers import RegisterSerializer, ListUserSerializer, ProjectSerializer, ContactSerializer


# user registration view


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


# user list view
class ListUserView(generics.ListAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ListUserSerializer


class ProjectView(generics.CreateAPIView):
    queryset = Project.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer


class ListProjectsView(generics.ListAPIView):
    queryset = Project.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ProjectSerializer


class ContactMeView(generics.CreateAPIView):
    queryset = ContactMe.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer


class ListContactMeView(generics.ListAPIView):
    queryset = ContactMe.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = ContactSerializer