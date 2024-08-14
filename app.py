import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage
import Line.Message

app = Flask(__name__)

# Setting
channel_access_token = os.environ.get('CHANNEL_ACCESS_TOKEN')
channel_secret = os.environ.get('CHANNEL_SECRET')

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def Handle_Line_Message(event):
    Line.Message.Chat(event, line_bot_api)

## HTML
@app.route("/")
def home():
    return '<h1>Still working on ...</h1>'

if __name__ == "__main__":
    app.run()
    