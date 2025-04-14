from django.db import models
from django.contrib.auth import get_user_model

class TrendSource(models.TextChoices):
    REDDIT = "REDDIT", "Reddit"
    TIKTOK = "TIKTOK", "TikTok"
    INSTAGRAM = "INSTAGRAM", "Instagram"

class Trend(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=20, choices=TrendSource.choices)
    source_url = models.URLField()
    subreddit = models.CharField(max_length=100, blank=True, null=True)
    score = models.IntegerField(default=0)
    media_type = models.CharField(max_length=20, default="video")  # or image
    downloaded_file = models.FileField(upload_to='memes/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    fetched_by = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True, blank=True)
    

    def __str__(self):
        return f"{self.title} from {self.source}"