import os
from flask import Flask, request, abort
from linebot.models import MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,TemplateSendMessage,ButtonsTemplate,MessageTemplateAction
from utils import send_text_message
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, ImageSendMessage ,LocationSendMessage,TemplateSendMessage
)
from transitions.extensions import GraphMachine
from initial import app
from utils import send_text_message,send_button_message,send_button_carousel_l,send_button_carousel_bf,send_button_carousel_d,line_bot_api
#import pyimgur

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )

    def is_going_to_introduction(self, event):
        text = event.message.text
        return text.lower() == '說明'

    def is_going_to_eat(self, event):
        text = event.message.text
        return text == '肚子餓了' or text.lower() == 'go'
    
    def is_going_to_breakfast(self, event):
        text = event.message.text
        return text == '早餐'
    
    def is_going_to_lunch(self, event):
        text = event.message.text
        return text == '午餐，我好餓喔'
    
    def is_going_to_dinner(self, event):
        text = event.message.text
        return text == '晚餐'
    
    def is_going_to_lunch(self, event):
        text = event.message.text
        return text == '午餐，我好餓喔'
    
    def is_going_to_b_choose(self, event):
        text = event.message.text
        return text == '就選這個吧'

    def is_going_to_l_choose(self, event):
        text = event.message.text
        return text == '就選這個吧'
    
    def is_going_to_d_choose(self, event):
        text = event.message.text
        return text == '就選這個吧'
    
    def is_going_to_recommand(self, event):
        text = event.message.text
        return text == '有甚麼推薦的'
    
    def is_going_to_kfc(self, event):
        text = event.message.text
        return text == '肯德基' or text == '肯得基' or text == '肯德雞'
    
    def is_going_to_mcdnd(self, event):
        text = event.message.text
        return text == '麥當勞' or text == '麥當勞優惠'

    def on_enter_introduction(self, event):
        print("I'm entering introduction")
        reply_token = event.reply_token
        message = "每餐吃什麼這個問題，從大學生活\n就開始啦！\n萬年不變的煩惱，由我來幫你解決!\n\n 請打 \"說明\" 會有使用資訊 \n 請打 \"肚子餓了\"或\"go\" 會有早餐、午餐、晚餐時段，再請依照推薦進行選擇~\n 請打\"fsm\"會輸出本系統fsm圖片"
        #message_to_reply = FlexSendMessage("說明", message)
        #line_bot_api = LineBotApi('GB4Nbe46wQipUV1Jl88drMPiZusTljgsCNpLly8/SKnMno2Y7YzvPJ3Hg4MdIXCIOL5+XtTdOipJIEFWRGFYo7ioW8h6Bha3TojWwZmuUJAfIm7xX9/gnwTbeDvb00ySmCMXKhwutNsEj/747BMkFAdB04t89/1O/w1cDnyilFU=')
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        self.go_back()

    def on_enter_eat(self, event):
        print("I'm entering eat")
        reply_token = event.reply_token
        send_button_message(reply_token)
        #line_bot_api.reply_message(event.reply_token, buttons_template_message)
    

    def on_enter_breakfast(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        message = "想要吃早餐"
        #message_to_reply = FlexSendMessage("說明", message)
        send_button_carousel_bf(reply_token)

    def on_enter_b_choose(self, event):
        print("I'm entering b_choose")
        reply_token = event.reply_token
        message = "好的 早上吃好才有精神努力喔~"
        #message_to_reply = FlexSendMessage("說明", message)
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        self.go_back()


    def on_enter_lunch(self, event):
        print("I'm entering state3")
        reply_token = event.reply_token
        send_button_carousel_l(reply_token)

    def on_enter_l_choose(self, event):
        print("I'm entering l_choose")
        reply_token = event.reply_token
        message = "好的 祝你用餐愉快~"
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        self.go_back()
    
    def on_enter_dinner(self, event):
        print("I'm entering state2")
        reply_token = event.reply_token
        send_button_carousel_d(reply_token)

    def on_enter_d_choose(self, event):
        print("I'm entering d_choose")
        reply_token = event.reply_token
        message = "好的 今天辛苦了 好好放鬆一下吧~"
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        self.go_back()

    def on_enter_kfc(self, event):
        print("I'm entering state kfc")
        reply_token = event.reply_token
        message = "肯德基點餐\nhttps://www.kfcclub.com.tw/ShopSearch"
        #message_to_reply = FlexSendMessage("說明", message)
        #line_bot_api = LineBotApi('GB4Nbe46wQipUV1Jl88drMPiZusTljgsCNpLly8/SKnMno2Y7YzvPJ3Hg4MdIXCIOL5+XtTdOipJIEFWRGFYo7ioW8h6Bha3TojWwZmuUJAfIm7xX9/gnwTbeDvb00ySmCMXKhwutNsEj/747BMkFAdB04t89/1O/w1cDnyilFU=')
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        self.go_back()

    def on_enter_mcdnd(self, event):
        print("I'm entering state mcdnd")
        reply_token = event.reply_token
        message = "麥當勞點餐\nhttps://www.mcdelivery.com.tw/tw/browse/menu.html?locale=zh"
        #message_to_reply = FlexSendMessage("說明", message)
        line_bot_api.reply_message(reply_token,TextSendMessage(text=message))
        self.go_back()




    