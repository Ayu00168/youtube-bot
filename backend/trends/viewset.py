from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from .tasks.reddit_content import get_top_reddit_posts
from .utils import get_best_videos

class TrendViewSet(ViewSet):
    @action(detail=False, methods=['get'], url_path='data')
    def get_data(self, request):

        reddit_post = get_top_reddit_posts(limit=5)
        top_videos = get_best_videos(reddit_post, top_n=3)

        return Response({"message": top_videos}, status=status.HTTP_200_OK)
