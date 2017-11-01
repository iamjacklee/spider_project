#!/usr/bin/env python3.5
from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
chatbot = ChatBot("deepThought")
chatbot.set_trainer(ChatterBotCorpusTrainer)
chatbot.train("chatterbot.corpus.chinese")
bot = Bot(cache_path=True)
group_2 = bot.groups("shipping is")[0]
group_2.send("hello everybody!")
@bot.register(group_2)
def reply_my_friend(msg):
    print(msg)
    return chatbot.get_response(msg.text).text

embed()