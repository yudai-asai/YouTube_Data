import json
import urllib
from urllib import request
from googleapiclient.discovery import build 
import settings
import schedule
import datetime
import time
import slackweb


YouTube_API_KEY = settings.YouTube_API_KEY
YouTube_CHANNEL_ID = settings.YouTube_CHANNEL_ID
SLACK_URL = settings.SLACK_URL
#参考：https://qiita.com/ryoya41/items/dd1fd4c1427ece787eea

def statistics_video():
  API_KEY = YouTube_API_KEY
  YOUTUBE_API_SERVICE_NAME = 'youtube'
  YOUTUBE_API_VERSION = 'v3'
  CHANNEL_ID = YouTube_CHANNEL_ID
  message = "直近5動画の閲覧数成績レポート"

  youtube = build(
      YOUTUBE_API_SERVICE_NAME,
      YOUTUBE_API_VERSION,
      developerKey=API_KEY
  )

  responses = youtube.search().list(
      part = "snippet",
      channelId = CHANNEL_ID,
      maxResults = 5,
      order = "date" #日付順にソート
      ).execute()

  for response in responses['items']:
    id = response['id']['videoId']
    title = response['snippet']['title']
    description = response['snippet']['description']
    publishedAt = response['snippet']['publishedAt']

    statistics = youtube.videos().list(
        part = 'snippet,statistics',
        id = id
        ).execute()
    
    viewCount = statistics['items'][0]['statistics']['viewCount']
    likeCount = statistics['items'][0]['statistics']['likeCount']
    dislikeCount = statistics['items'][0]['statistics']['dislikeCount']
    favoriteCount = statistics['items'][0]['statistics']['favoriteCount']
    commentCount = statistics['items'][0]['statistics']['commentCount']

    message = message + "\nタイトル：" + title + "\n ・投稿日："+ publishedAt + "\n ・視聴数："+ viewCount + "\n ・高評価数："+ likeCount + "\n ・低評価数："+ dislikeCount + "\n ・お気に入り登録数："+ favoriteCount + "\n ・コメント数：" + commentCount
    
  return message

def job():
    message = statistics_video()
    today = datetime.date.today()
    slack = slackweb.Slack(url=SLACK_URL)
    slack.notify(text=f'直近5動画の閲覧数成績レポート\n```{message}```')
    print(f'{today} Done')

if __name__ == '__main__':
    job()