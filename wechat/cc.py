from wxpy import *

# bot = Bot(console_qr=-2, cache_path=True)
bot = Bot(console_qr=True, cache_path=True)

# friends = bot.friends()

# for friend in friends:
#     print(friend)

@bot.register()
def print_others(msg):
    # print(msg.text)
    # msg.reply('hello boy!!!')
    
    
    if msg.text == 'hi':
        msg.reply('hi ,i am jack')
    else:
        msg.reply('hi ,i am hugo')
    

embed()