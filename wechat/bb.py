from wxpy import *
bot = Bot(console_qr=True)
# bot = Bot(console_qr=True, cache_path=True)
my_friend = bot.friends().search('jacklee',sex=MALE)[0]
# bot.self.send('Hello World!')
bot.file_helper.send('Hello World!123')