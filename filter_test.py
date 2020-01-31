from telegram.ext import BaseFilter

class FilterAwesome(BaseFilter):
    def filter(self, message):
        return 'python-telegram-bot is awesome' in message.text

# Remember to initialize the class.
#filter_awesome = FilterAwesome()

