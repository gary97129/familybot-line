import requests
import re
import random
import configparser
from markupsafe import escape
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

line_bot_api = LineBotApi('iEAetylAYUFoGDUepIXWxK1ZGuSSDULb3ZeGAsZRKVqo43+FTVTiY+UuPM7f9w0S+4aXglAsjFipJsYeN8Hqji84mHUMb/fxidtVECFPNk/YWc1KTbzYdGuKHIPUj1PEkpWsi99WQC8SdH+ldVwQ1AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('467efe25376266631ed0638b0fb85c8d')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))




if __name__ == '__main__':
    app.run()
