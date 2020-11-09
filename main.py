import json
import urllib
from urllib import request
from googleapiclient.discovery import build 
import settings
import schedule
import datetime
import time


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

def post_slack(message):
    send_data = {
        "text": message,
    }
    send_text = json.dumps(send_data)
    request = urllib.request.Request(
        SLACK_URL, 
        data=send_text.encode('utf-8'), 
        method="POST"
    )
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')

def job():
    message = statistics_video()
    today = datetime.date.today()
    post_slack(f'直近5動画の閲覧数成績レポート\n```{message}```')
    print(f'{today} Done')

def main():
    print('Program Start!')
    schedule.every().day.at("02:19").do(job)
    while True:
        schedule.run_pending()
        time.sleep(30)
if __name__ == '__main__':
    main()
