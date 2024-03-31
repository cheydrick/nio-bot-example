import niobot

class MyFunModule(niobot.Module):  # subclassing niobot.Module is mandatory for auto-detection.
    def __init__(self, bot):
        self.bot = bot  # bot is the NioBot instance you made in main.py!

    # The command !hello will make the bot reply directly to the sender.
    @niobot.command(name='hello')
    async def hello(self, ctx: niobot.Context):
        print("Hello?")
        await ctx.respond("Hello %s!" % ctx.event.sender)

    # The command !hello will make the bot reply to the room.
    # client.send_message() has an argument called message_type. The options are "m.text" (normal text)
    # or "m.notification", which formats the text a bit differently (and is the default).
    @niobot.command(name='althello')
    async def althello(self, ctx: niobot.Context):
        print("This should be a response not in reply")
        await self.client.send_message(ctx.room, "This is a response that isn't a direct reply.", message_type="m.text")
