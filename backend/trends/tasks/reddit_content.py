import praw
from backend.settings import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_USER_AGENT

SUBREDDITS = ["onepiece", "luffy", "anime", "manga", "ShingekiNoKyojin", "AttackOnTitan", "Bleach", "Naruto", "MyHeroAcademia", "TokyoGhoul", "JujutsuKaisen"]

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

        for post in subreddit.hot(limit=limit):
            if not post.stickied:
                if post.is_video:
                    all_posts.append({
                        "source": "reddit",
                        "title": post.title,
                        "url": post.url,
                        "score": post.score,
                        "subreddit": post.subreddit.display_name,
                        "id": post.id,
                        "permalink": f"https://reddit.com{post.permalink}",
                        "comments":post.num_comments,
                        "created": post.created_utc,
                        "upvote_ratio": post.upvote_ratio,
                    })

    return all_posts

if __name__ == "__main__":
    posts = get_top_reddit_posts(limit=5)
    for post in posts:
        print(f"[{post['subreddit']}] {post['title']} - {post['url']}")