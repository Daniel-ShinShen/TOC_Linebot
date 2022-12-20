from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)





line_bot_api = LineBotApi('GB4Nbe46wQipUV1Jl88drMPiZusTljgsCNpLly8/SKnMno2Y7YzvPJ3Hg4MdIXCIOL5+XtTdOipJIEFWRGFYo7ioW8h6Bha3TojWwZmuUJAfIm7xX9/gnwTbeDvb00ySmCMXKhwutNsEj/747BMkFAdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('f80fb07f8c69a68601586a99c1be4f5d')


from transitions import Machine
from fsm import TocMachine
machine = TocMachine(
    states=["user", "state1", "state2"],
    transitions=[
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state1",
            "conditions": "is_going_to_state1",
        },
        {
            "trigger": "advance",
            "source": "user",
            "dest": "state2",
            "conditions": "is_going_to_state2",
        },
        {"trigger": "go_back", "source": ["state1", "state2"], "dest": "user"},
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,

)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


    
@app.route("/") #使用route()裝飾器。route()裝飾器可以告訴Flask，緊接在裝飾器下面的函式要載入在哪個url位址中
def home():
    return "This is Home Page"
@app.route("/hello")#我們想要讓hello函式被載入到hello的url位址中，
def hello():
    return "Hello World! This is Hello Page "

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(f"\nFSM STATE: {machine.state}")
    #print(f"REQUEST BODY: \n{body}")
    response = machine.advance(event)
    if response == False:
        #send_text_message(event.reply_token, "請依照指示與按鈕來操作!")
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請依照指示與按鈕來操作\n請打\"說明\"會有使用資訊"))


   
    #line_bot_api.reply_message(
    #    event.reply_token,
    #    TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    #machine.get_graph().draw("fsm.png", prog="dot", format="png")
    app.run()