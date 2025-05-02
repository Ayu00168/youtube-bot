from datetime import datetime, timezone

def calculate_score(video):
    if video["source"] == "reddit":
        return (
            video.get("score", 0) * 1.5 +
            video.get("num_comments", 0) * 1.2 +
            video.get("upvote_ratio", 0.0) * 100
        )
    elif video["source"] == "youtube":
        return (
            video.get("views", 0) * 0.001 +
            video.get("likes", 0) * 2 +
            video.get("comments", 0) * 1.5
        )
    return 0

def is_recent(video):
    now = datetime.now(timezone.utc)
    if video["source"] == "reddit":
        video_time = datetime.fromtimestamp(video["created"], tz=timezone.utc)
    elif video["source"] == "youtube":
        video_time = datetime.fromisoformat(video["published_at"].replace("Z", "+00:00"))
    else:
        return False
    delta = now - video_time
    return delta.days <= 5  # Only consider last 5 days

def get_best_videos(reddit_videos, top_n=3):
    combined = reddit_videos

    filtered = [v for v in combined if is_recent(v)]
    scored = [{"video": v, "score": calculate_score(v)} for v in filtered]
    sorted_videos = sorted(scored, key=lambda x: x["score"], reverse=True)

    return sorted_videos[:top_n]