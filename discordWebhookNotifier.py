from discord import Webhook, RequestsWebhookAdapter, Embed

printWebhookURL = "https://discord.com/api/webhooks/1003080661936123945/6aYkOHRIQA1UrikSFkw82ZkIyapgcUv3BXPEwM22YhjoA46P7k0XbzIAJVATKfMCtI_U"

###########################
PROJECTNAME = "Instagram Bot"
AVATARURL = "https://www.pngmart.com/files/21/Instagram-Logo-PNG-Transparent.png"
###########################

def sendLog(value):
    webhook = Webhook.from_url(printWebhookURL, adapter=RequestsWebhookAdapter())
    colore = 0xededed
    if value.startswith("[MESSAGE]"):
        colore = 0x1eff00
    if value.startswith("[ACTION]"):
        colore = 0xb90bbc
    if value.startswith("[WARNING]"):
        colore = 0xbc7b0b
    if value.startswith("[ERROR]"):
        colore = 0xff0000
    e = Embed(title=value, color=colore)
    webhook.send(embed=e, avatar_url=AVATARURL, username=PROJECTNAME)