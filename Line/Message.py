from linebot.models import TextSendMessage

def Chat(event, line_bot_api):
    '''
    Line Bot
    '''
    USER_ID = event.source.user_id
    USER_TEXT = event.message.text

    # Repeat
    Reply(event, line_bot_api, USER_TEXT)

def Reply(event, line_bot_api, msg=''):
    if msg=='': return
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=msg)
    )
