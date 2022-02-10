import hikari
import lightbulb
import requests
import json, urllib.request

kiwi = lightbulb.BotApp(
    token="",
    default_enabled_guilds=(),
)


# Group - Cute Animals
@kiwi.command
@lightbulb.command("cute", "Post random images of animals")
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def cute_group(context):
    pass


@cute_group.child
@lightbulb.command("doggo", "Posts random image of doggo")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def doggo(context):
    while True:
        dog_response = urllib.request.urlopen(
            "https://dog.ceo/api/breeds/image/random"
        ).read()
        image = json.loads(dog_response)
        await context.respond(image["message"])
    doggo(context)


@cute_group.child
@lightbulb.command("shibe", "Posts random image of shibes")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def shibe(context):
    shibe_response = urllib.request.urlopen("http://shibe.online/api/shibes").read()
    image = json.loads(shibe_response)
    await context.respond(image["image"])


@cute_group.child
@lightbulb.command("cat", "Posts random image of catto")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def cat(context):
    cat_response = urllib.request.urlopen("https://aws.random.cat/meow").read()
    image = json.loads(cat_response)
    await context.respond(image["file"])


@cute_group.child
@lightbulb.command("fox", "Posts random image of foxxo")
@lightbulb.implements(lightbulb.SlashSubCommand)
async def fox(context):
    fox_response = urllib.request.urlopen("https://randomfox.ca/floof/").read()
    image = json.loads(fox_response)
    await context.respond(image["image"])


kiwi.run()
