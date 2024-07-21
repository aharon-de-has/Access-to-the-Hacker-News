import requests
import pandas as pd
import matplotlib.pyplot as plt

url_main = 'https://hacker-news.firebaseio.com/v0'

def fech_top_stories(num):
    top_stories_url = f'{url_main}/topstories.json'
    try:
        response = requests.get(top_stories_url)
        story_ids = response.json()[:num]
        stories = []
        for story_id in story_ids:
            story_url = f'{url_main}/item/{story_id}.json'
            story_response = requests.get(story_url)
            story_data = story_response.json()
            stories.append(story_data)
        return stories
    except:
        return
    
def analyze_stories(stories):
    df = pd.DataFrame(stories)
    df_stories = df[['id', 'title', 'by', 'score','descendants', 'time', 'url']]
    df_stories['time'] = pd.to_datetime(df_stories['time'], unit='s')
    df_comments = df['kids']
    return df_stories, df_comments

def get_details(id_comment):
    comment_url = f'{url_main}/item/{id_comment}.json'
    response = requests.get(comment_url)
    return response.json()

def fech_data_comment(ids_comments):
    comment_data = []
    for ids in ids_comments:
        for id_comment in ids:
            comment_details = get_details(id_comment)
            if comment_details:
                comment_data.append({
                    'author': comment_details.get('by'),
                    'time': comment_details.get('time'),
                    'parent': comment_details.get('parent'),
                    'text': comment_details.get('text')
                })
    comment_df = pd.DataFrame(comment_data)
    comment_df['time'] = pd.to_datetime(comment_df['time'], unit='s')
    return comment_df

def plot_pie_chart(df):
    # plt.annotate("The atribution of scores", xy=(0.5, 1), ha='center', va='center', fontsize=16)
    plt.figure(figsize=(20, 7))
    plt.subplots_adjust(left=0.3, right=1.1)
    wedges, texts, aototext = plt.pie(df['score'], autopct='%1.1f%%', startangle=140, textprops=dict(color='w'))
    plt.legend(wedges, df['title'], title="Titles", loc="center left", bbox_to_anchor=(-0.3, 0.5))
    plt.axis('equal')
    plt.show()
  
def save_csv(df, filename):
    df.to_csv(filename, index=True)

def get_stories_and_comment(num):
    '''args:
    The function receives the requested number of top stories from the Hacker News website.
    Returns for each such story the id, title, author, score, descendants' , time, url in a CSV document.
    In addition, for each comment to these stories, the aothor, parent, time and text returns an additional CSV document.'''
    stories = fech_top_stories(num) 
    stories_df, comment_df = analyze_stories(stories) #Returns the informations in the Data Fram
    plot_pie_chart(stories_df) #Visually displays the distribution of scores
    avrege_score = stories_df['score'].mean() 
    stories_df[avrege_score] = avrege_score #Adds the avrage of the scores
    data_comment = fech_data_comment(comment_df) #Information for the comment
    save_csv(stories_df, 'top_stories.csv')
    save_csv(data_comment, 'comment.csv')
  

get_stories_and_comment(10)

