import praw
from backend.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT

SUBREDDITS = [
"memes",
"funny",
"wholesomememes",
"aww",
"gifs",
"pics",
"showerthoughts",
"todayilearned",
"science",]

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    user_agent=REDDIT_USER_AGENT
)

def get_top_reddit_posts(limit=5):
    all_posts = []

    for sub in SUBREDDITS:
        subreddit = reddit.subreddit(sub)
        print(f"Fetching from r/{sub}...")

        for post in subreddit.hot(limit=limit):
            if not post.stickied:
                all_posts.append({
                    "title": post.title,
                    "url": post.url,
                    "score": post.score,
                    "subreddit": post.subreddit.display_name,
                    "id": post.id,
                    "permalink": f"https://reddit.com{post.permalink}"
                })

    return all_posts

if __name__ == "__main__":
    posts = get_top_reddit_posts(limit=5)
    for post in posts:
        print(f"[{post['subreddit']}] {post['title']} - {post['url']}")