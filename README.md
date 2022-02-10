
# kiwi-bot Self Hosted Discord Bot

Want a Discord bot you can call your own? Here's how to do it.



## Setting Up

First we're going to want to create a bot within Discord's developer portal

https://discord.com/developers

From here you're going to want to follow these steps:

```
Create New Application (top right)
Give Bot Details

Visit Bot tab (left panel)
Add Bot

Dropdown menu OAuth2 tab (left panel)
Visit URL Generator
Select the options 'bot' and 'applications.commands'

Give permissions to the bot, your choice.
```
Doing this will generate a URL at the bottom of the page that will allow you to invite the bot to any server you want.


## Installation

Now that the bot has been setup, you're going to want to make sure Python 3.8, 3.9 or 3.10 is atleast installed as we're going to be using a Python library known as Hikari.
To install these prequirements, use the following commands.

```python
  pip install hikari-lightbulb
  pip install hikari
```
Documentation for these can be found here:

https://github.com/hikari-py/hikari/ -
https://github.com/tandemdude/hikari-lightbulb

Within the application itself,  near the top you'll see a variable that passes a token.

```python
kiwi = lightbulb.BotApp(token='', default_enabled_guilds=())
```

This token will be your bots. So go back to your bots page within the developer portal. The Bot tab will contain your bots token underneath the name. Paste this into the token within the application.

If you're planning on only using this bot within a few servers, you can use the default_enabled_guilds argument. This is used to allow the commands to show near the top. To get the parameters for this, just right click on your server icon and Copy ID and paste in this argument.

This was only created for personal purpose and is only being used in a couple of servers, so might aswell give the source code to other people for them to use as-well. More commands will be added.
