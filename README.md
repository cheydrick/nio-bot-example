# nio-bot-example
Example of how to use Nio-Bot. Based on the official documentation's quick start guide.

https://docs.nio-bot.dev/guides/001-getting-started/

The first example in the documentation appears to have deprecated function calls. This examples uses functions that work with Nio-Bot 1.1.0 (modern at the time of this writing). I also added a command (althello) in fun.py to show how to make the bot reply to the room, instead of directly back at the command sender.

I suggest reading through the linked example first, since it has context for why the files are organized and named as they are.

# Installing Nio-Bot Package
Creating and activating a virtual environment is optional, but probably a good idea.

I am using Python 3.10.12. It should work with Python 3.9 to 3.12.
```bash
$ python3 -m venv ./envs/nio-bot
$ source ./envs/nio-bot/bin/activate
(nio-bot) $ python3 -m pip install 'nio-bot[e2ee, cli]'
```

# Configuring and Running
The documentation recommends against using a password, but the tool for generating an access token appears to be broken.

https://docs.nio-bot.dev/guides/001-getting-started/#why-is-logging-in-with-a-password-so-bad

Change the values in config.py to match the server you want the bot to log in to. You should probably add config.py to your .gitignore if you're using source control.

There are function arguments to niobot.NioBot() in main.py that should be changed. device_id is the device ID to log in as (defaults to "nio-bot"). owner_id is the bot owner (probably your username) and allows you to activate owner-specific commands, though this example has none.

To run:
```bash
(nio-bot) $ python3 main.py
```

Use ctrl-c to exit.
