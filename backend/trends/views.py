from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .models import Trend

# Create your views here.

class TrendListView(APIView):
    authentication_classes=[TokenAuthentication]
    
    def post(self, request):
        """
        Fetch trends from the source and save them to the database.
        """
        # Here you would implement the logic to fetch trends from the source
        
        # For now, we'll just return a success message
        return Response({"message": "Trends fetched successfully"}, status=status.HTTP_200_OK)
