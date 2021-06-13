# Pixelbot
# Useful command module
# © 2021 Narek Torosyan

from .module_text import ROOT, ROOT_SAMSUNG, AB, BLOKADA, FLASH
from telegram.ext import Updater, CommandHandler
import telegram
from androlib import asb
from bs4 import BeautifulSoup
import requests
from config import PIRACY
import os.path
from os import path

ADB_ERROR = """
There is no single /adb command.

Use:
/adbL for Linux
/adbM for Mac
/adbW for Windows
"""

def root(update, context):
	update.message.reply_text(text=ROOT, parse_mode=telegram.ParseMode.MARKDOWN)

def root_sammy(update, context):
	update.message.reply_text(text=ROOT_SAMSUNG, parse_mode=telegram.ParseMode.MARKDOWN)

def ab(update, context):
	update.message.reply_text(text=AB, parse_mode=telegram.ParseMode.MARKDOWN)

def taptap(update, context):
	update.message.reply_text(text="Click [here](https://forum.xda-developers.com/t/app-beta-0-9-tap-tap-double-tap-on-back-of-device-gesture-from-android-11-port.4140573/) to download Tap, Tap", parse_mode=telegram.ParseMode.MARKDOWN)

def blokada(update, context):
	update.message.reply_text(text=BLOKADA, parse_mode=telegram.ParseMode.MARKDOWN)

def fastboot(update, context):
	update.message.reply_text(text=FLASH, parse_mode=telegram.ParseMode.MARKDOWN)

def modules(update, context):
	f = open("magisk.txt","r")
	update.message.reply_text(text=f.read(), parse_mode=telegram.ParseMode.MARKDOWN_V2)
	f.close()

def bulletin(update, context):
	data = asb.getLatestASB()
	spl = ""
	if len(data["spl"][0]) == 1:
		spl = data["spl"]
	else:
		for l in data["spl"]:
			spl = f"{spl},{l}"
		spl = spl.lstrip(",")
	crunch = f'*Latest Android Security Bulletin - {data["date"]}*\n*Published on:* {data["publishedOn"]}\n*SPL(s):* {spl}\n[Read more]({data["url"]})'
	update.message.reply_text(text=crunch, parse_mode=telegram.ParseMode.MARKDOWN)

def bulletin_pixel(update, context):
	data = asb.getLatestPixelSB()
	spl = ""
	if len(data["spl"][0]) == 1:
		spl = data["spl"]
	else:
		for l in data["spl"]:
			spl = f"{spl},{l}"
		spl = spl.lstrip(",")
	crunch = f'*Latest Pixel Update Bulletin - {data["date"]}*\n*Published on:* {data["publishedOn"]}\n*SPL(s):* {spl}\n[Read more]({data["url"]})'
	update.message.reply_text(text=crunch, parse_mode=telegram.ParseMode.MARKDOWN)

def freezer(update, context):
	# legal safeguard
	if not PIRACY:
		print("/freezer has been disabled due to law.")
		print("If storing piracy apps is legal in your country set PIRACY to True in config.py.")
		update.message.reply_text(text="Enabling /freezer requires extra steps by the bot's hoster.")
		return
	# though is storing instructions on how to download said apps legal?
	ms = update.message.reply_text(text="_Downloading Freezer..._", parse_mode=telegram.ParseMode.MARKDOWN)
	x = requests.get("https://www.freezer.life/")
	soup = BeautifulSoup(x.content, 'html.parser')
	dl = soup.select("#android > div > div > div:nth-child(2) > p:nth-child(5) > a:nth-child(3)")
	url = dl[0].get("href")
	fn = "freezer/"+url.split("/")[len(url.split("/"))-1]
	if not path.exists(fn):
		print(f"New Freezer version {fn.replace('freezer/','').replace('.apk','')}!")
		ms.edit_text(text=f"Found new Freezer version `{fn.replace('freezer/','').replace('.apk','')}`!\n_Downloading..._", parse_mode=telegram.ParseMode.MARKDOWN)
		print("Downloading...", end='')
		r = requests.get(url, allow_redirects=True)
		print(" done.\nWriting...", end='')
		open(fn, 'wb').write(r.content)
		print(" done.")
	ms.edit_text(text="_Uploading APK...\nThis might take a while. You will get a new reply when it's done._", parse_mode=telegram.ParseMode.MARKDOWN)
	update.message.reply_document(document=open(fn, 'rb'), caption="The latest Freezer APK for `arm64`.\n*Do not use it if playing copyrighted music for personal use is illegal in your country! IF YOU GET IN TROUBLE, THE PIXELBOT DEVS WON'T BE RESPONSIBLE! USE AT YOUR OWN RISK!*", timeout=60, parse_mode=telegram.ParseMode.MARKDOWN)
	ms.delete()

def odin(update, context):
	ms = update.message.reply_text(text="_Downloading Odin..._", parse_mode=telegram.ParseMode.MARKDOWN)
	x = requests.get("https://odindownload.com/download/")
	soup = BeautifulSoup(x.content, 'html.parser')
	dl = soup.select("#page > a:nth-child(9)")
	url = dl[0].get("href")
	fn = "freezer/"+url.split("/")[len(url.split("/"))-1]
	if not path.exists(fn):
		print(f"New Odin version {fn.replace('freezer/','').replace('.apk','')}!")
		ms.edit_text(text=f"Found new Odin version `{fn.replace('freezer/','').replace('.apk','')}`!\n_Downloading..._", parse_mode=telegram.ParseMode.MARKDOWN)
		print("Downloading...", end='')
		r = requests.get(url, allow_redirects=True)
		print(" done.\nWriting...", end='')
		open(fn, 'wb').write(r.content)
		print(" done.")
	ms.edit_text(text="_Uploading ZIP...\nThis might take a while. You will get a new reply when it's done._", parse_mode=telegram.ParseMode.MARKDOWN)
	update.message.reply_document(document=open(fn, 'rb'), caption="The latest version of Odin.", timeout=60, parse_mode=telegram.ParseMode.MARKDOWN)
	ms.delete()

def getPT(update, context, platform):
	url = f"https://dl.google.com/android/repository/platform-tools-latest-{platform}.zip"
	human_platform = platform
	if human_platform == "darwin":
		human_platform = "mac"
	human_platform = human_platform[0].upper() + human_platform[1:]
	ms = update.message.reply_text(text=f"_Downloading adb for {human_platform}..._", parse_mode=telegram.ParseMode.MARKDOWN)
	fn = "freezer/"+url.split("/")[len(url.split("/"))-1]
	if not path.exists(fn):
		print(f"Downloading {platform} platform-tools")
		ms.edit_text(text=f"Found new adb version for {human_platform}!\n_Downloading..._", parse_mode=telegram.ParseMode.MARKDOWN)
		print("Downloading...", end='')
		r = requests.get(url, allow_redirects=True)
		print(" done.\nWriting...", end='')
		open(fn, 'wb').write(r.content)
		print(" done.")
	ms.edit_text(text="_Uploading ZIP...\nThis might take a while. You will get a new reply when it's done._", parse_mode=telegram.ParseMode.MARKDOWN)
	update.message.reply_document(document=open(fn, 'rb'), caption=f"The latest platform-tools for {human_platform}. Includes adb, fastboot and some other tools.", timeout=60, parse_mode=telegram.ParseMode.MARKDOWN)
	ms.delete()

def getPTwin(update, context):
	getPT(update, context, "windows")

def getPTlnx(update, context):
	getPT(update, context, "linux")

def getPTmac(update, context):
	getPT(update, context, "darwin")

def adbHelp(update, context):
	update.message.reply_text(text=ADB_ERROR)

CONTENTS = [
	CommandHandler('root', root, run_async=True),
	CommandHandler('rootsam', root_sammy, run_async=True),
	CommandHandler('ab', ab, run_async=True),
	CommandHandler('taptap', taptap, run_async=True),
	CommandHandler('blokada', blokada, run_async=True),
	CommandHandler('flash', fastboot, run_async=True),
	CommandHandler('modules', modules, run_async=True),
	CommandHandler('asb', bulletin, run_async=True),
	CommandHandler('psb', bulletin_pixel, run_async=True),
	CommandHandler('freezer', freezer, run_async=True),
	CommandHandler('odin', odin, run_async=True),
	CommandHandler('adbW', getPTwin, run_async=True),
	CommandHandler('adbL', getPTlnx, run_async=True),
	CommandHandler('adbM', getPTmac, run_async=True),
	CommandHandler('adb', adbHelp, run_async=True)
]