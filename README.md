# API Data Analytics Dashboard

An interactive data analytics dashboard built with Python, Streamlit, Pandas, and Plotly.

The application retrieves data from the public [JSONPlaceholder API](https://jsonplaceholder.typicode.com), processes multiple datasets, calculates key statistics, and visualizes the results in an interactive web interface.

## Features

- Fetches users, posts, comments, and TODOs from a public REST API.
- Calculates key metrics:
  - Total users, posts, comments, and tasks.
  - Average number of posts per user.
  - Average number of comments per post.
  - Percentage of completed tasks.
- Visualizes user activity with a bar chart.
- Displays task completion with a pie chart.
- Identifies the five most commented posts.
- Provides detailed data tables and a refresh button.

## Tech Stack

- Python
- Requests
- Pandas
- Streamlit
- Plotly

## Installation

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   cd api-data-analytics
   ```

2. Create and activate a virtual environment.

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:

   ```bash
   python -m streamlit run app.py
   ```

## Data Source

The application uses the JSONPlaceholder public API:

- `/users`
- `/posts`
- `/comments`
- `/todos`

JSONPlaceholder provides sample data for testing and educational purposes.

## Project Structure

```text
api-data-analytics/
├── app.py
├── data.py
├── analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Live Demo

https://api-data-analytics-5guh64xntnklurmcejkwrm.streamlit.app/

## Limitations

The dashboard uses a simulated dataset and should not be interpreted as an analysis of real user behavior.
