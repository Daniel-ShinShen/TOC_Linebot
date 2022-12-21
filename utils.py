
import os

from linebot import LineBotApi, WebhookParser
from linebot.models import TextSendMessage, ImageSendMessage, TemplateSendMessage, ImageCarouselColumn, ImageCarouselTemplate,ConfirmTemplate, ButtonsTemplate, MessageTemplateAction, URITemplateAction, ImageSendMessage, CarouselTemplate, CarouselColumn


channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
line_bot_api = LineBotApi(channel_access_token)

def send_text_message(reply_token, text):
    line_bot_api = LineBotApi(channel_access_token)
    line_bot_api.reply_message(reply_token, TextSendMessage(text=text))

    return "OK"


def send_button_message(reply_token):

    message = TemplateSendMessage(
        alt_text='Buttons template',
        template=ButtonsTemplate(
            text='你在為哪一餐煩惱呢？',
            actions=[
                MessageTemplateAction(
                    label='早餐',
                    text='早餐',
                ),
                MessageTemplateAction(
                    label='午餐',
                    text='午餐，我好餓喔',
                ),
                MessageTemplateAction(
                    label='晚餐',
                    text='晚餐',
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)
    return "OK"

def send_button_carousel_bf(reply_token):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                
                CarouselColumn(
                    thumbnail_image_url='https://www.alberthsieh.com/webp/wp-content/uploads/611smk_0234.jpg.webp',
                    title='中式早餐',
                    text='蛋餅、鐵板麵、飯糰，或是一碗粥暖暖身心',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E4%B8%AD%E5%BC%8F%E6%97%A9%E9%A4%90&bih=961&biw=1920&hl=zh-TW&ei=rISjY56iAtGT-AaG_rmADQ&ved=0ahUKEwieqKi53Yv8AhXRCd4KHQZ_DtAQ4dUDCA8&uact=5&oq=%E4%B8%AD%E5%BC%8F%E6%97%A9%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDIECAAQQzIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEOgoIABBHENYEELADSgQIQRgASgQIRhgAULMJWLMJYN0RaANwAXgAgAF0iAF0kgEDMC4xmAEAoAECoAEByAEKwAEB&sclient=gws-wiz-serp'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.alicdn.com/imgextra/i1/2952368183/TB23cYgu9XlpuFjy0FeXXcJbFXa_!!2952368183-0-headline_editor.jpg',
                    title='西式早餐',
                    text='麥片、鬆餅、貝果、再來一份培根炒蛋',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E8%A5%BF%E5%BC%8F%E6%97%A9%E9%A4%90&bih=961&biw=1920&hl=zh-TW&ei=fYWjY8PGKpSRoATMkYfIDQ&ved=0ahUKEwiD-aSd3ov8AhWUCIgKHczIAdkQ4dUDCA8&uact=5&oq=%E8%A5%BF%E5%BC%8F%E6%97%A9%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIECAAQQzIFCAAQgAQyBAgAEEMyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQ6BQgAEKIESgQIQRgASgQIRhgAUABYuwNggQtoAHABeACAAXKIAaUCkgEDMi4xmAEAoAEBwAEB&sclient=gws-wiz-serp'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://doqvf81n9htmm.cloudfront.net/data/shenlin_127/shutterstock_1031743420.jpg',
                    title='超商',
                    text='簡單解決',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E8%B6%85%E5%95%86&bih=961&biw=1920&hl=zh-TW&ei=fISjY-e3NJvr-QbJ97mQDQ&ved=0ahUKEwjn5eii3Yv8AhWbdd4KHcl7DtIQ4dUDCA8&uact=5&oq=%E8%B6%85%E5%95%86&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIECAAQQzIICAAQsQMQgwEyCAgAELEDEIMBMggIABCABBCxAzIICAAQgAQQsQMyBAgAEEMyBAgAEEMyCAgAELEDEIMBMggIABCxAxCDAToLCAAQgAQQsQMQgwE6CwguEIAEEMcBEK8BOgUIABCABDoFCC4QgAQ6BwgAEB4Q8QQ6CQgAEB4QDxDxBDoLCC4QgAQQxwEQ0QM6CAguEIAEELEDOgUIABCiBEoECEEYAEoECEYYAFAAWN0JYLANaABwAXgAgAF0iAHmBJIBAzMuM5gBAKABAcABAQ&sclient=gws-wiz-serp'
                        )
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_button_carousel_l(reply_token):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://storage.googleapis.com/www-cw-com-tw/article/202101/article-5ff76e12dff12.jpg',
                    title='日式料理',
                    text='來一碗拉麵?',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E6%97%A5%E5%BC%8F%E5%8D%88%E9%A4%90&bih=961&biw=1920&hl=zh-TW&ei=WnujY4DVJYSpoASQ8KOIDw&ved=0ahUKEwiA6u3H1Iv8AhWEFIgKHRD4CPEQ4dUDCA8&uact=5&oq=%E6%97%A5%E5%BC%8F%E5%8D%88%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQguEIAEMgUIABCABDIJCAAQBxAeEPEEMgkIABAHEB4Q8QQyCQgAEAcQHhDxBDIJCAAQBxAeEPEEMgsIABAHEB4QDxDxBDILCAAQBxAeEA8Q8QQyCQgAEAcQHhDxBDoFCAAQogQ6BwgAEB4Q8QQ6CQgAEB4QDxDxBDoLCAAQBRAeEA8Q8QRKBAhBGABKBAhGGABQAFiBDGCDEGgBcAF4AYABxwGIAcgEkgEDMS4zmAEAoAEBwAEB&sclient=gws-wiz-serp'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://live.staticflickr.com/65535/51692427051_472893637a_c.jpg',
                    title='中式料理',
                    text='水餃、小籠包、還是便當?',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E4%B8%AD%E5%BC%8F%E5%8D%88%E9%A4%90&bih=961&biw=1920&hl=zh-TW&ei=Ln6jY5W9Ncj--QajuoyIDQ&ved=0ahUKEwiVjJuh14v8AhVIf94KHSMdA9EQ4dUDCA8&uact=5&oq=%E4%B8%AD%E5%BC%8F%E5%8D%88%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBAgAEEMyBAgAEEMyCQgAEB4QDxDxBDIHCAAQHhDxBDIJCAAQHhAPEPEEMgkIABAeEA8Q8QQyCQgAEAUQHhDxBDILCAAQBRAeEA8Q8QQyCwgAEAUQHhAPEPEEOgUIABCiBEoECEEYAEoECEYYAFAAWNUWYNkhaAFwAXgBgAFviAG5BZIBAzMuNJgBAKABAcABAQ&sclient=gws-wiz-serp'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img.ihappyday.tw/2018/02/1518519498-a7ee56745585a55a4703baadfbd9f5c1.jpg',
                    title='西式料理',
                    text='義大利麵、牛排、或輕食?',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E8%A5%BF%E5%BC%8F%E5%8D%88%E9%A4%90&source=lmns&bih=961&biw=1920&hl=zh-TW&sa=X&ved=2ahUKEwjvoOLj04v8AhWyNaYKHXMPB6sQ_AUoAHoECAEQAA'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def send_button_carousel_d(reply_token):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://janicoco.com/wp-content/uploads/2020/08/eZy-Watermark_28-07-2020_18-06-21-scaled.jpg',
                    title='日式料理',
                    text='定食、壽司、壽喜燒',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E6%97%A5%E5%BC%8F%E6%99%9A%E9%A4%90&ei=3oejY6r6C9inoASAiqKQDQ&ved=0ahUKEwiq4bi_4Iv8AhXYE4gKHQCFCNIQ4dUDCA8&uact=5&oq=%E6%97%A5%E5%BC%8F%E6%99%9A%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBQgAEIAEMgUIABCABDIHCAAQHhDxBDIHCAAQHhDxBDIHCAAQHhDxBDIJCAAQHhAPEPEEMgcIABAeEPEEMgkIABAeEA8Q8QQyCQgAEB4QDxDxBDoLCAAQgAQQsQMQgwE6BQguEIAEOgsILhCABBDHARCvAToICC4QgAQQsQM6CAgAEIAEELEDOhEILhCABBCxAxCDARDHARCvAToFCAAQogQ6BAgAEEM6CAgAELEDEIMBOgUIABCxAzoKCAAQ8QQQHhCiBEoECEEYAEoECEYYAFAAWKDWHmDE2h5oA3ABeACAAX2IAcQOkgEEOC4xMJgBAKABAaABAsABAQ&sclient=gws-wiz-serp'
                        )
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://tokyo-kitchen.icook.network/uploads/recipe/cover/174122/5a7d6e6451518224.jpg',
                    title='中式料理',
                    text='炒飯、滷肉飯...',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E4%B8%AD%E5%BC%8F%E6%99%9A%E9%A4%90&ei=I4qjY4CQKNmkwAPgvJ64DQ&ved=0ahUKEwjArdrU4ov8AhVZEnAKHWCeB9cQ4dUDCA8&uact=5&oq=%E4%B8%AD%E5%BC%8F%E6%99%9A%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIECAAQQzILCAAQBxAeEA8Q8QQyCwgAEAcQHhAPEPEEMgsIABAHEB4QDxDxBDIFCAAQgAQyBQgAEIAEMgUIABCABDILCAAQCBAHEB4Q8QQyCwgAEAgQBxAeEPEESgQIQRgASgQIRhgAUABYAGCCB2gAcAF4AIABngKIAZ4CkgEDMi0xmAEAoAECoAEBwAEB&sclient=gws-wiz-serp'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://janicoco.com/wp-content/uploads/2022/02/janicoco-menu-western-dinner-for-two-beef-wellington-butter-garlic-clams-pasta-cheesey-creamed-spinach-3.jpg',
                    title='西式料理',
                    text='燉飯、火鍋、或沙拉?',
                    actions=[
                        MessageTemplateAction(
                            label='選擇',
                            text='就選這個吧'
                        ),
                        MessageTemplateAction(
                            label='附近好料',
                            text='有甚麼推薦的'
                        ),
                        URITemplateAction(
                            label='查看詳細資訊',
                            uri='https://www.google.com.tw/search?q=%E8%A5%BF%E5%BC%8F%E6%99%9A%E9%A4%90&ei=DYqjY8TEBpbahwO7-oiYDQ&ved=0ahUKEwiE__nJ4ov8AhUW7WEKHTs9AtMQ4dUDCA8&uact=5&oq=%E8%A5%BF%E5%BC%8F%E6%99%9A%E9%A4%90&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIECAAQQzIFCAAQgAQyBQgAEIAEMgcIABAeEPEEMgkIABAeEA8Q8QQyCQgAEB4QDxDxBDIJCAAQHhAPEPEEMgcIABAeEPEEMgkIABAFEB4Q8QQyCwgAEAUQHhAPEPEEOgUIABCiBDoKCAAQ8QQQHhCiBEoECEEYAEoECEYYAFAAWOEFYOgPaABwAXgAgAGXAYgBnwOSAQMwLjOYAQCgAQHAAQE&sclient=gws-wiz-serp'
                        )
                    ]
                )
            ]
        )
    )
    line_bot_api.reply_message(reply_token, message)

    return "OK"

def push_message(userid, msg):
    line_bot_api.push_message(userid, TextSendMessage(text=msg))
    return "OK"

"""
def send_image_url(id, img_url):
    pass
def send_button_message(id, text, buttons):
    pass
"""