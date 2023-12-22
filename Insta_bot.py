from instabot import Bot

bot = Bot()
bot.login(username="steel1728", password="sonaisantra")
bot.follow("isro.dos")
bot.upload_photo("/media/prantick/New Volume/Wallpaper/lahiru-supunchandra-xE0b_dSVf7A-unsplash.jpg",caption="Lord Buddha")
bot.unfollow("_prerana.ghosh_")
bot.send_message("This message is send to you by Instagram bot, made by me :) :) :)", ["thepalbabu"])
followers = bot.get_user_followers("steel1728")
for follower in followers:
    print(bot.get_user_info(follower))

followings = bot.get_user_following("steel1728")
for following in followings:
    print(bot.get_user_info(following))