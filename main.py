import logging
import niobot
import config

logging.basicConfig(level=logging.DEBUG, filename='bot.log')

bot = niobot.NioBot(
    homeserver=config.HOMESERVER,
    user_id=config.USER_ID,
    device_id='bot',
    store_path='./store',
    command_prefix="!",
    owner_id="@user:server.name"
)
# We also want to load `fun.py`'s commands before starting:
bot.mount_module("fun")  # looks at ./fun.py

@bot.on_event("ready")
async def on_ready(_):
    # That first argument is needed as the first result of the sync loop is passed to ready. Without it, this event
    # will fail to fire, and will cause a potentially catasrophic failure.
    print("Bot is ready!")

@bot.command(name='ping')
async def ping(ctx: niobot.Context):  # can be invoked with "!ping"
    print("Pinging?")
    await ctx.respond("Pong!")

bot.run(password=config.PASSWORD)
