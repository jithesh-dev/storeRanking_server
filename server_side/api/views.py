from django.shortcuts import render
from django.db.models.expressions import F, Window
from django.db.models.functions.window import RowNumber
from django.db.models.functions import Rank


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Store

from .serializers import StoreSerializer


class StoreRanking(APIView):
    # API View Class for fetching data from store db and store ranking

    def get(self, request, format=None):

        stores = (
            Store.objects.all()
            .order_by("-st_time_spent")
            .annotate(
                rank=Window(expression=Rank(), order_by=F("st_time_spent").desc())
            )
        )

        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data)
