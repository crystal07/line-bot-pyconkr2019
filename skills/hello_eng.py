from linebot.models import TextSendMessage

from skills import add_skill


@add_skill(r'hello'|r'hi')
def get_location(message):
    return TextSendMessage(text='hello')