from pyrogram import Client,filters

app_id = your api hash
app_key = 'your api id'
token = "api token"



app = Client("antiservicemessage", app_id, app_key, bot_token=token)

DONATESTARTTEXT = """Hello User, i am a bot that deletes service messages from your group or channel, just add to a group and make me an admin"""




@app.on_message(filters.private)
def start(c,m):
    m.reply(DONATESTARTTEXT,
)

@app.on_message(filters.group & filters.command("command@botname"))
def main(c,m):
    m.reply("""text""")

@app.on_message(filters.group & filters.command("command"))
def main(c,m):
    m.reply("""text""")



@app.on_message(filters.service)
def service(c,m):
    m.delete()


app.run()
