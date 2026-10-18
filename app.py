
import streamlit as st
import plotly.express as px

from data import load_all_data
from analysis import calculate_metrics, get_user_activity, get_post_comment_counts


st.set_page_config(
    page_title="API Data Analytics",
    page_icon="📊",
    layout="wide",
)

st.title("📊 API Data Analytics Dashboard")
st.write(
    "An interactive analytics dashboard powered by "
    "the JSONPlaceholder public API."
)

st.sidebar.header("Dashboard settings")
st.sidebar.write(
    "Data source: JSONPlaceholder"
)

if st.sidebar.button("Refresh data"):
    st.cache_data.clear()

try:
    with st.spinner("Loading data from API..."):
        users, posts, comments, todos = load_all_data()

    metrics = calculate_metrics(users, posts, comments, todos)
    activity = get_user_activity(users, posts, todos)
    post_stats = get_post_comment_counts(posts, comments)

except Exception as error:
    st.error(f"Could not load data: {error}")
    st.stop()


# Key performance indicators
st.header("Key metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Users",
    metrics["total_users"],
)

col2.metric(
    "Posts",
    metrics["total_posts"],
)

col3.metric(
    "Comments per post",
    f'{metrics["comments_per_post"]:.2f}',
)

col4.metric(
    "Completed TODOs",
    f'{metrics["completed_percentage"]:.1f}%',
)


# Additional statistics
st.subheader("Overview")

col5, col6, col7 = st.columns(3)

col5.metric(
    "Total comments",
    metrics["total_comments"],
)

col6.metric(
    "Average posts per user",
    f'{metrics["posts_per_user"]:.1f}',
)

col7.metric(
    "Completed tasks",
    f'{metrics["completed_todos"]} / {metrics["total_todos"]}',
)


# Chart 1: posts by user
st.header("User activity")

activity_chart = px.bar(
    activity.sort_values("post_count", ascending=False),
    x="name",
    y="post_count",
    title="Number of posts by user",
    labels={
        "name": "User",
        "post_count": "Number of posts",
    },
)

activity_chart.update_layout(
    xaxis_tickangle=-45,
)

st.plotly_chart(activity_chart, use_container_width=True)


# Chart 2: TODO completion
st.header("Task completion")

completed_count = metrics["completed_todos"]
pending_count = metrics["total_todos"] - completed_count

todo_chart = px.pie(
    names=["Completed", "Not completed"],
    values=[completed_count, pending_count],
    title="Completed vs not completed TODOs",
    hole=0.4,
)

st.plotly_chart(todo_chart, use_container_width=True)


# Chart 3: most commented posts
st.header("Top 5 most commented posts")

top_posts = post_stats.head(5).copy()

top_posts["short_title"] = top_posts["title"].str.slice(0, 35)

top_chart = px.bar(
    top_posts.sort_values("comment_count"),
    x="comment_count",
    y="short_title",
    orientation="h",
    title="Top 5 posts by number of comments",
    labels={
        "comment_count": "Number of comments",
        "short_title": "Post title",
    },
)

st.plotly_chart(top_chart, use_container_width=True)


# Detailed tables
with st.expander("View user activity data"):
    st.dataframe(
        activity[
            [
                "name",
                "post_count",
                "completed_todos",
                "total_todos",
                "todo_completion_pct",
            ]
        ],
        use_container_width=True,
        hide_index=True,
    )

with st.expander("View all posts and comment counts"):
    st.dataframe(
        post_stats,
        use_container_width=True,
        hide_index=True,
    )

with st.expander("View raw API data"):
    st.subheader("Users")
    st.dataframe(users, use_container_width=True)

    st.subheader("Posts")
    st.dataframe(posts, use_container_width=True)

    st.subheader("Comments")
    st.dataframe(comments, use_container_width=True)

    st.subheader("TODOs")
    st.dataframe(todos, use_container_width=True)

st.caption(
    "Data source: JSONPlaceholder. "
    "This is a demo dataset for educational purposes."
)
