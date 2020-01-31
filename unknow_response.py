#unknown cmmand response

def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, this command seems to be unknown to our bot. Please try again!")

#unknown_handler = MessageHandler(Filters.command, unknown)
#dispatcher.add_handler(unknown_handler)