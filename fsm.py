from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage 
)
from transitions.extensions import GraphMachine

from utils import send_text_message


class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_state1(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'go to state1'
        return False

    def is_going_to_state2(self, event):
        if event.get("message") and event['message'].get("text"):
            text = event['message']['text']
            return text.lower() == 'go to state2'
        return False

    def on_enter_state1(self, event):
        print("I'm entering state1")
        reply_token = event.reply_token
        message = "請打\"說明\"會有使用資訊 \n請打\"今日匯率\"會有今日美金的匯率資訊 \n請打\"歷史匯率\"後，再須入您要查詢幾個月前的歷史資料，就會跑出走勢圖 \n請打\"預測\"會預測下一個交易日美金的漲跌與售出價格 \n請打\"fsm\"會輸出本系統fsm圖片"
        #message_to_reply = FlexSendMessage("說明", message)
        line_bot_api = LineBotApi('GB4Nbe46wQipUV1Jl88drMPiZusTljgsCNpLly8/SKnMno2Y7YzvPJ3Hg4MdIXCIOL5+XtTdOipJIEFWRGFYo7ioW8h6Bha3TojWwZmuUJAfIm7xX9/gnwTbeDvb00ySmCMXKhwutNsEj/747BMkFAdB04t89/1O/w1cDnyilFU=')
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "I'm entering state1")
        self.go_back()

    def on_exit_state1(self):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "I'm entering state2")
        self.go_back()

    def on_exit_state2(self):
        print('Leaving state2')


    