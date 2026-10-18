import pandas as pd


"""Oblicza podstawowe wskaźniki dotyczące aktywności użytkowników."""
def calculate_metrics(users, posts, comments, todos):

    # Obliczamy liczbę wszystkich użytkowników, postów i komentarzy.
    total_users = len(users)
    total_posts = len(posts)
    total_comments = len(comments)
    total_todos = len(todos)

     # Zliczamy zadania oznaczone jako wykonane.
    completed_todos = int(todos["completed"].sum())

    # Obliczamy średnią liczbę postów przypadających na użytkownika.
    posts_per_user = (
        total_posts / total_users if total_users else 0
    )

    # Obliczamy średnią liczbę komentarzy przypadających na post.
    comments_per_post = (
        total_comments / total_posts if total_posts else 0
    )

    # Obliczamy procent wykonanych zadań.
    completed_percentage = (
        completed_todos / total_todos * 100
        if total_todos else 0
    )

    # Zwracamy wszystkie wskaźniki w jednym słowniku.
    return {
        "total_users": total_users,
        "total_posts": total_posts,
        "total_comments": total_comments,
        "total_todos": total_todos,
        "completed_todos": completed_todos,
        "posts_per_user": posts_per_user,
        "comments_per_post": comments_per_post,
        "completed_percentage": completed_percentage,
    }

"""Przygotowuje zestawienie aktywności każdego użytkownika."""
def get_user_activity(users, posts, todos):

    # Zliczamy posty opublikowane przez poszczególnych użytkowników.
    post_counts = (
        posts.groupby("userId")
        .size()
        .rename("post_count")
    )

    
    todo_stats = (
        todos.groupby("userId")["completed"]
        .agg(["sum", "count"])
        .rename(columns={
            "sum": "completed_todos",
            "count": "total_todos",
        })
    )

    activity = users[["id", "name"]].copy()

    activity = activity.merge(
        post_counts,
        left_on="id",
        right_index=True,
        how="left",
    )

    activity = activity.merge(
        todo_stats,
        left_on="id",
        right_index=True,
        how="left",
    )

    count_columns = [
        "post_count",
        "completed_todos",
        "total_todos",
    ]

    activity[count_columns] = (
        activity[count_columns].fillna(0).astype(int)
    )

    activity["todo_completion_pct"] = (
        activity["completed_todos"]
        / activity["total_todos"].replace(0, float("nan"))
        * 100
    ).fillna(0)

    return activity


def get_post_comment_counts(posts, comments):
    comment_counts = (
        comments.groupby("postId")
        .size()
        .rename("comment_count")
    )

    result = posts[["id", "userId", "title"]].merge(
        comment_counts,
        left_on="id",
        right_index=True,
        how="left",
    )

    result["comment_count"] = (
        result["comment_count"].fillna(0).astype(int)
    )

    return result.sort_values(
        "comment_count",
        ascending=False,
    ).reset_index(drop=True)
