from django.db import transaction
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Counter


class CounterView(APIView):
    permission_classes = [IsAuthenticated]

    @transaction.atomic()
    def get(self, request):
        counter, _ = Counter.objects.get_or_create(user=request.user)
        return Response(data=counter.count)

    @transaction.atomic()
    def post(self, request):
        counter, _ = Counter.objects.get_or_create(user=request.user)
        counter.increment()
        return Response(data='ok')

    @transaction.atomic()
    def delete(self, request):
        counter, _ = Counter.objects.get_or_create(user=request.user)
        counter.decrement()
        return Response(data='ok')


