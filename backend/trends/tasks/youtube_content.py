import requests
import isodate
from backend.settings import YOUTUBE_SECRET_KEY, REGION, MAX_RESULTS
from yt_dlp import YoutubeDL



def isShortsVideo(item):
    for items in item.items:
        print( f"https://www.youtube.com/watch?v={item.id}")


def get_youtube_trending_videos():
    url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode={REGION}&maxResults={MAX_RESULTS}&key={YOUTUBE_SECRET_KEY}"
    ydl_opts = {
        'quiet': True,
        'extract_flat': False,  # Needed to get full metadata
        'skip_download': True,
        'dump_single_json': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
    
    
        response = ydl.extract_info(url, download=False)
        data_url = response["url"] 
        data = requests.get(data_url)
        print(data.json())
        # if response.status_code == 200:
        #     for items in response.json().get('items', []):
        #         duration = items['contentDetails']['duration']
        #         if isShortsVideo(duration):
        #             print(f"https://www.youtube.com/watch?v={items['id']}")

if __name__ == "__main__":
    get_youtube_trending_videos()