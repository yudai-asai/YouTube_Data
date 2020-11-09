import urllib.request
import json
import settings

SLACK_URL = settings.SLACK_URL

url = SLACK_URL

def post_slack(msg):
    set_fileds = [{
        "title": "TITLE",
        "value": msg,
        "short": False
    }]

    data = {
        'attachments':  [{
            #'color': '#FF0000',
            'color': 'danger',
            'fields': set_fileds
        }]
    }

    method = 'POST'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'}
    body = json.dumps(data).encode("utf-8")
    request = urllib.request.Request(
        url=url, 
        data=body, 
        method=method,
        headers=request_headers 
    )
    urllib.request.urlopen(request)

if __name__ == '__main__':
    msg = "My name is yhidetoshi"
    post_slack(msg)