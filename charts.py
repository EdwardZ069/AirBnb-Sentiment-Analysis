import re
import string

import plotly.express as px           # ← you still need this for px.bar & px.line
import plotly.graph_objects as go
import pandas as pd

from nltk.corpus import stopwords

# one-time load of English stopwords
STOPWORDS = set(stopwords.words('english'))


# import datetime


def create_graph(df):
    # print the frequency of each review by the top 5 reviewers
    df_top5 = df['reviewer_name'].value_counts().head(5)

    # create the bar chart
    fig = px.bar(df_top5, x=df_top5.index, y=df_top5.values,
                 color=df_top5.values, color_continuous_scale='RdBu')

    # update the layout
    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', margin=dict(l=0, r=0, t=30, b=0)
    )

    # update the x and y axis
    fig.update_xaxes(showgrid=False, showline=True,
                     zeroline=False, linecolor='black')

    fig.update_yaxes(showgrid=False, showline=False,
                     zeroline=False, linecolor='black')

    return fig


def create_graph2(df):
    # print the frequency of each review by the top 5 reviewers
    df_top5 = df['reviewer_name'].value_counts().head(5)

    # make a bar graph showing the top 5 reviewers and their positive, negative and neutral reviews
    # choose diiferent shaeds of red
    fig = go.Figure(data=[
        go.Bar(name='Positive', x=df_top5.index, y=df_top5.values,
               marker_color='#660000'),
        go.Bar(name='Neutral', x=df_top5.index, y=df_top5.values,
               marker_color='#800020'),
        go.Bar(name='Negative', x=df_top5.index, y=df_top5.values,
               marker_color='#C41E3A')
    ])

    # update the layout
    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', barmode='stack', margin=dict(l=0, r=0, t=30, b=0)
    )

    # update the x and y axis
    fig.update_xaxes(showgrid=False, showline=True,
                     zeroline=False, linecolor='black')

    fig.update_yaxes(showgrid=False, showline=False,
                     zeroline=False, linecolor='black')

    return fig


def wordcloud(df):
    """
    Build a treemap of the top 100 words in df['cleaned_comments'] 
    using go.Treemap to avoid the Plotly-Express hierarchy bug.
    """
    # 1) lowercase, drop nulls, strip punctuation
    texts = (
        df['cleaned_comments']
          .dropna()
          .astype(str)
          .str.lower()
          .str.replace(f"[{re.escape(string.punctuation)}]", " ", regex=True)
    )

    # 2) split into words & explode
    words = texts.str.split().explode()

    # 3) filter stopwords
    words = words[~words.isin(STOPWORDS)]

    # 4) count & take top 100
    top = words.value_counts().nlargest(100).reset_index()
    top.columns = ['word', 'count']

    # 5) build a go.Treemap
    fig = go.Figure(
        go.Treemap(
            labels=top['word'],
            parents=[""] * len(top),        # flat hierarchy
            values=top['count'],
            marker=dict(colors=top['count'],
                        colorscale='RdBu',
                        showscale=True),
            hovertemplate="<b>%{label}</b><br>Count: %{value}<extra></extra>"
        )
    )

    fig.update_layout(
        title="Common Words",
        margin=dict(l=0, r=0, t=40, b=0),
        paper_bgcolor='#f7f7f7'
    )
    return fig


def circle(df):
    # use plotly to make a circular graph shwing the positive, negative and neutral reviews
    # not a pie chart but a circular graph which is more visually appealing and is hollow in the middle
    fig = go.Figure(data=[go.Pie(labels=['Positive', 'Neutral', 'Negative'], values=[
        40, 30, 30], hole=.6)])
    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', barmode='stack', margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig


def bubble(df):
    # use plotly to make a bubble graph showing the positive, negative and neutral reviews
    # not a pie chart but a circular graph which is more visually appealing and is hollow in the middle
    fig = go.Figure(data=[go.Scatter(
        x=[1, 2, 3, 4],
        y=[10, 11, 12, 13],
        mode='markers',
        marker=dict(
            size=[40, 60, 80, 100],
            color=[0, 1, 2, 3],
            colorscale='RdBu',
            showscale=True
        )
    )])

    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', barmode='stack', margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig


def polar_area(df):
    # use plotly to make a polar area graph showing the positive, negative and neutral reviews
    # not a pie chart but a circular graph which is more visually appealing and is hollow in the middle
    fig = go.Figure(data=go.Scatterpolar(
        r=[1, 5, 2, 2, 3],
        theta=['Positive', 'Neutral', 'Negative', 'Positive', 'Neutral'],
        fill='toself'
    ))

    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', barmode='stack', margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig


def time_series(df):
    # formate the date column in the dataset is 2016-08-20
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # create a new column with the year and month
    df['year_month'] = df['date'].dt.strftime('%Y-%m')

    # create a new column with the year
    df['year'] = df['date'].dt.strftime('%Y')

    # create a new column with the month
    df['month'] = df['date'].dt.strftime('%m')

    # time series graph showing the number of reviews per month
    # group the data by year and month
    df_time = df.groupby(['year_month']).size().reset_index(name='counts')

    # create the line graph
    fig = px.line(df_time, x='year_month', y='counts')

    # update the layout
    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', barmode='stack', margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig


def time_sentiment(df):
    # formate the date column in the dataset is 2016-08-20
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')

    # create a new column with the year and month
    df['year_month'] = df['date'].dt.strftime('%Y-%m')

    # create a new column with the year
    df['year'] = df['date'].dt.strftime('%Y')

    # create a new column with the month
    df['month'] = df['date'].dt.strftime('%m')

    # plot the time series graph showing the number of positive, negative and neutral reviews per month
    sentiments = ['positive', 'negative', 'neutral']

    # plot the negative, positive and neutral reviews in the same graph not separate graphs but diffferent colour lines
    fig = go.Figure()

    for sentiment in sentiments:
        df_time = df[df['sentiment'] == sentiment].groupby(
            ['year_month']).size().reset_index(name='counts')
        fig.add_trace(go.Scatter(x=df_time['year_month'], y=df_time['counts'],
                                 mode='lines+markers', name=sentiment))

    # update the layout
    fig.update_layout(
        xaxis_title='<b>Reviewer Name<b>', yaxis_title='<b>Frequency<b>',
        font=dict(size=14, family='Arial', color='black'), hoverlabel=dict(
            font_size=14, font_family="Rockwell"), plot_bgcolor='#f7f7f7',
        paper_bgcolor='#f7f7f7', barmode='stack', margin=dict(l=0, r=0, t=30, b=0)
    )

    return fig
