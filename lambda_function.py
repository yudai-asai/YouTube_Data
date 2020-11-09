import json
import urllib
import urllib.request
from googleapiclient.discovery import build 

#参考：https://qiita.com/ryoya41/items/dd1fd4c1427ece787eea

def statistics_video():
  API_KEY = "AIzaSyDvY9ODTYkj3I65NkA3j6QhiAu--89kPE0"
  YOUTUBE_API_SERVICE_NAME = 'youtube'
  YOUTUBE_API_VERSION = 'v3'
  CHANNEL_ID = 'UCpK6nNjC3zMhZlNYReSb9kg'
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

  #responses = {'kind': 'youtube#searchListResponse', 'etag': 'ypy6o3ALUYFOZgHDsfJaqojmTvg', 'nextPageToken': 'CAEQAA', 'regionCode': 'US', 'pageInfo': {'totalResults': 98, 'resultsPerPage': 1}, 'items': [{'kind': 'youtube#searchResult', 'etag': 'X0n7acIlIom6v33po5iux2lNjds', 'id': {'kind': 'youtube#video', 'videoId': 'E6JWiugHv5U'}, 'snippet': {'publishedAt': '2020-11-06T11:00:04Z', 'channelId': 'UCpK6nNjC3zMhZlNYReSb9kg', 'title': '【今すぐ使え】受験勉強に役立つ神アイテムTOP3', 'description': '今回は受験勉強に役立つアイテムを紹介しました！ これらを使って効率的に勉強しましょう！！ ☆動画の感想・やって欲しい企画はコメント欄で！☆ 【現論会チャンネルとは ...', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/E6JWiugHv5U/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/E6JWiugHv5U/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/E6JWiugHv5U/hqdefault.jpg', 'width': 480, 'height': 360}}, 'channelTitle': '現論会チャンネル', 'liveBroadcastContent': 'none', 'publishTime': '2020-11-06T11:00:04Z'}}]}


  for response in responses['items']:
    id = response['id']['videoId']
    title = response['snippet']['title']
    description = response['snippet']['description']
    publishedAt = response['snippet']['publishedAt']

    statistics = youtube.videos().list(
        part = 'snippet,statistics',
        id = id
        ).execute()
    #statistics = {'kind': 'youtube#videoListResponse', 'etag': 'suATNLjwIUQED5CB5zM2_t3quCk', 'items': [{'kind': 'youtube#video', 'etag': 'lRVTXnzNuNIpKdTN3f2ieAIK3cU', 'id': '7K_Gj4JHDYE', 'snippet': {'publishedAt': '2020-10-14T11:00:01Z', 'channelId': 'UCpK6nNjC3zMhZlNYReSb9kg', 'title': '【公開します】現論会式日本史の最強ルート', 'description': '今回は「現論会式日本史の最強ルート」についてご紹介しました！\nまだ日本史全然やってなくてやばい！\nといった方は是非参考にして、効率的に点数を稼いでください！\n※どうしても時間がなければプレ通史の後に基礎演習を入れてください！\n\n☆動画の感想・やって欲しい企画はコメント欄で！☆\n【現論会チャンネルとは？】\n勉強法のことは、勉強法のプロに聞こう。\n数多の受験生を合格に導いてきたスタディサプリ講師や、\n現役東大生・早大生の中から選りすぐられた「勉強法のプロ」達が、\n受験指導の中で効果のあった「本当に意味のある勉強法」を紹介していく\n受験生必見のチャンネルです！\n☆オススメ動画はこちら！\n英語学習の救世主、関正雄が語る英語の勉強法\nhttps://www.youtube.com/watch?v=pLtrlbxrqnc&t=3s\n＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n【現論会とは】\n現論会では「参考書」と「映像授業」を組み合わせ、\nあなたの合格可能性を最大化する勉強計画と勉強法を指導する「学習コーチング塾」です！\n全科目で合格最低点を取れば合格ですから、「全科目定額指導」で最短距離に導きます！\n勉強法でお悩みの方は、ぜひ無料相談にお越しください！\n☆HP・無料相談はこちらから\nhttps://genronkai.com/free-consultation/\n☆フォローするだけで成績が上がる、現論会の公式アカウントはこちら！\nhttps://twitter.com/genronkai\n＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n【現論会の書籍】\n勉強法のプロが多く在籍する現論会では、その勉強法を世に広めていくべく、\n「勉強法に関連する書籍」を多数出版しています！\nぜひご覧ください！\n〜国語〜\nゼロから覚醒\u3000はじめよう現代文：https://www.amazon.co.jp/dp/4761274867/\n大学入試問題集 柳生好之の現代文ポラリス：https://www.amazon.co.jp/dp/4046022183\n完全理系専用\u3000看護医療系のための小論文：https://www.amazon.co.jp/dp/4297108739\n世界一わかりやすい慶應の小論文 合格講座：https://www.amazon.co.jp/dp/4046023937\n〜勉強法〜\n現役東大生が教える 絶対に成績が上がる ハイブリッド勉強法：https://www.amazon.co.jp/dp/4046043199', 'thumbnails': {'default': {'url': 'https://i.ytimg.com/vi/7K_Gj4JHDYE/default.jpg', 'width': 120, 'height': 90}, 'medium': {'url': 'https://i.ytimg.com/vi/7K_Gj4JHDYE/mqdefault.jpg', 'width': 320, 'height': 180}, 'high': {'url': 'https://i.ytimg.com/vi/7K_Gj4JHDYE/hqdefault.jpg', 'width': 480, 'height': 360}, 'standard': {'url': 'https://i.ytimg.com/vi/7K_Gj4JHDYE/sddefault.jpg', 'width': 640, 'height': 480}, 'maxres': {'url': 'https://i.ytimg.com/vi/7K_Gj4JHDYE/maxresdefault.jpg', 'width': 1280, 'height': 720}}, 'channelTitle': '現論会チャンネル', 'tags': ['参考書', '映像授業', '勉強法', '現代文', '英語', '数学', '勉強ルート', '参考書ルート', '国語', '物理', '化学', '生物', '日本史', '世界史', '地理', '大学受験', '現論会', '東京大学', '東大', '早稲田', 'march', '古文', '漢文', '白チャート', '白チャートが教祖になったら'], 'categoryId': '27', 'liveBroadcastContent': 'none', 'localized': {'title': '【公開します】現論会式日本史の最強ルート', 'description': '今回は「現論会式日本史の最強ルート」についてご紹介しました！\nまだ日本史全然やってなくてやばい！\nといった方は是非参考にして、効率的に点数を稼いでください！\n※どうしても時間がなければプレ通史の後に基礎演習を入れてください！\n\n☆動画の感想・やって欲しい企画はコメント欄で！☆\n【現論会チャンネルとは？】\n勉強法のことは、勉強法のプロに聞こう。\n数多の受験生を合格に導いてきたスタディサプリ講師や、\n現役東大生・早大生の中から選りすぐられた「勉強法のプロ」達が、\n受験指導の中で効果のあった「本当に意味のある勉強法」を紹介していく\n受験生必見のチャンネルです！\n☆オススメ動画はこちら！\n英語学習の救世主、関正雄が語る英語の勉強法\nhttps://www.youtube.com/watch?v=pLtrlbxrqnc&t=3s\n＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n【現論会とは】\n現論会では「参考書」と「映像授業」を組み合わせ、\nあなたの合格可能性を最大化する勉強計画と勉強法を指導する「学習コーチング塾」です！\n全科目で合格最低点を取れば合格ですから、「全科目定額指導」で最短距離に導きます！\n勉強法でお悩みの方は、ぜひ無料相談にお越しください！\n☆HP・無料相談はこちらから\nhttps://genronkai.com/free-consultation/\n☆フォローするだけで成績が上がる、現論会の公式アカウントはこちら！\nhttps://twitter.com/genronkai\n＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿＿\n【現論会の書籍】\n勉強法のプロが多く在籍する現論会では、その勉強法を世に広めていくべく、\n「勉強法に関連する書籍」を多数出版しています！\nぜひご覧ください！\n〜国語〜\nゼロから覚醒\u3000はじめよう現代文：https://www.amazon.co.jp/dp/4761274867/\n大学入試問題集 柳生好之の現代文ポラリス：https://www.amazon.co.jp/dp/4046022183\n完全理系専用\u3000看護医療系のための小論文：https://www.amazon.co.jp/dp/4297108739\n世界一わかりやすい慶應の小論文 合格講座：https://www.amazon.co.jp/dp/4046023937\n〜勉強法〜\n現役東大生が教える 絶対に成績が上がる ハイブリッド勉強法：https://www.amazon.co.jp/dp/4046043199'}, 'defaultAudioLanguage': 'ja'}, 'statistics': {'viewCount': '1640', 'likeCount': '46', 'dislikeCount': '1', 'favoriteCount': '0', 'commentCount': '15'}}], 'pageInfo': {'totalResults': 1, 'resultsPerPage': 1}}
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
        "https://hooks.slack.com/services/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", 
        data=send_text.encode('utf-8'), 
        method="POST"
    )
    with urllib.request.urlopen(request) as response:
        response_body = response.read().decode('utf-8')

def lambda_handler(event, context):
    message = statistics_video()
    post_slack(f'直近5動画の閲覧数成績レポート\n```{message}```')