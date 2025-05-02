# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.authentication import TokenAuthentication
# from .models import Trend
# from .tasks.reddit_content import get_top_reddit_posts
# from .utils import get_best_videos

# # Create your views here.

# class TrendListView(APIView):
#     authentication_classes=[]
    
#     def post(self, request):
#         reddit_post = get_top_reddit_posts(limit=5)
        
#         top_videos = get_best_videos(reddit_post, top_n=3)

#         return Response({"message": top_videos}, status=status.HTTP_200_OK)
    
    

