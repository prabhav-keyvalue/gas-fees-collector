from datetime import datetime
from slack_sdk import WebClient
import os


class SlackService:

    def __init__(self) -> None:
        self._client = WebClient(token=os.environ['SLACK_BOT_TOKEN'])

    
    def send_message(self, message, channel):

        try:
            self._client.chat_postMessage(channel=f'#{channel}', text=message)
            print(f'Send send message to slack channel - {channel} message - {message}')
        except Exception as e:
            print(f'Error sending message to slack channel: {channel} message:{message} at: {datetime.now()}')