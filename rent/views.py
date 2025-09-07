from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from .models import Customer
from .serializers import CustomerRegisterSerializer


# POST -> Register
class CustomerRegisterView(generics.CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        return Response(
            {
                "id": user.id,
                "login": user.login,
                "gmail": user.gmail,
                "phone": user.phone,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "message": "User registered successfully ✅"
            },
            status=status.HTTP_201_CREATED
        )


# GET -> List all customers
class CustomerListView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerRegisterSerializer
