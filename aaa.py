import requests
import pandas as pd
import matplotlib.pyplot as plt

url_main = 'https://hacker-news.firebaseio.com/v0'

def get_top_stories(num):
    top_stories_url = f'{url_main}/topstories.json'
    response = requests.get(top_stories_url)
    story_ids = response.json()[:num]
    stories = []
    for story_id in story_ids:
        story_url = f'{url_main}/item/{story_id}.json'
        story_response = requests.get(story_url)
        story_data = story_response.json()
        if 'kids' in story_data:
            comment_ids = story_data['kids']
            comments = get_cooment(comment_ids)
        stories.append(story_data)
    return stories, comments

def get_cooment(comment_ids):
    comments = []
    for comment_id in comment_ids:
        comment_url = f'{url_main}/itemm{comment_id}.json'
        comment_response = requests.get(comment_url)
        comment_data = comment_response.json()
        if comment_data and 'text' in comment_data:
            comments.append(comment_data)
    return comments


def analyze_stories(stories):
    df = pd.DataFrame(stories)
    df = df[['id', 'title', 'by', 'score', 'time', 'url']]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    return df

# def plot_scores(df):
#     plt.figure(figsize=(20, 7))
#     plt.barh(df['title'], df['score'], color='blue')
#     plt.xlabel('score')
#     plt.ylabel('title')
#     plt.title('scores of top Hacker News Stories')
#     plt.show()

def plot_pie_chart(df):
    plt.figure(figsize=(20, 7))
    plt.subplots_adjust(left=0.3, right=1.1)
    wedges, texts, aototext = plt.pie(df['score'], autopct='%1.1f%%', startangle=140, textprops=dict(color='w'))
    plt.legend(wedges, df['title'], title="Titles", loc="center left", bbox_to_anchor=(-0.3, 0.5))
    plt.axis('equal')
    plt.show()



def save_to_csv(df, filename='top_stories.csv'):
    df.to_csv(filename, index=True)


top_stories, comments = get_top_stories(10)
stories_df = analyze_stories(top_stories)
comments_df = analyze_stories(comments)
avrege_score = stories_df['score'].mean()
stories_df[avrege_score] = avrege_score
plot_pie_chart(stories_df)
# plot_scores(stories_df)

save_to_csv(stories_df)
save_to_csv(comments_df)




