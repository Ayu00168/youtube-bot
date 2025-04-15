import requests
import isodate
from backend.settings import YOUTUBE_SECRET_KEY, REGION, MAX_RESULTS



def isShortsVideo(duration):
    is_shorts = isodate.parse_duration(duration)
    print (is_shorts.total_seconds())
    return is_shorts.total_seconds() <=400


def get_youtube_trending_videos():
    url = f"https://youtube.googleapis.com/youtube/v3/videos?part=snippet,contentDetails,statistics&chart=mostPopular&regionCode={REGION}&maxResults={MAX_RESULTS}&key={YOUTUBE_SECRET_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        for items in response.json().get('items', []):
            duration = items['contentDetails']['duration']
            if isShortsVideo(duration):
                print(f"https://www.youtube.com/watch?v={items['id']}")

if __name__ == "__main__":
    get_youtube_trending_videos()