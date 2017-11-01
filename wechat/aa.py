from wxpy import *

bot = Bot()
my_friend = bot.friends().search('jacklee',sex=MALE)[0]
my_friend.send('hello jacklee')

@bot.register()
def print_others(msg):
    print(msg)

@bot.register(my_friend)
def reply_my_friend(msg):
    return 'received: {} ({})'.format(msg.text, msg.type)


embed()