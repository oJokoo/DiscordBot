import hikari

bot = hikari.GatewayBot(token='MTA2NzIwODkxMjY3NzM4NDMxMg.GvLssB.UFm0koZXkqQ6tBmE7_jGB5kClDeAK20qqNtzn0')


@bot.listen(hikari.GuildMessageCreateEvent)
async def print_message(event):
    print(event.content)


@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started')


bot.run()
