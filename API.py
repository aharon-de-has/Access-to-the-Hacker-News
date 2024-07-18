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
        stories.append(story_data)
    return stories
    
def analyze_stories(stories):
    df = pd.DataFrame(stories)
    df_stories = df[['id', 'title', 'by', 'score','descendants', 'time', 'url', ]]
    df['time'] = pd.to_datetime(df['time'], unit='s')
    df_comments = df['kids']
    return df_stories, df_comments


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

def save_csv(df, filename='comment.csv'):
    df.to_csv(filename, index=True)



top_stories = get_top_stories(10)
stories_df, comment_df = analyze_stories(top_stories)
avrege_score = stories_df['score'].mean()
stories_df[avrege_score] = avrege_score
plot_pie_chart(stories_df)
# plot_scores(stories_df)

save_to_csv(stories_df)
save_csv(comment_df)




