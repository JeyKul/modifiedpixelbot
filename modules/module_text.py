# Pixelbot
# Text for all modules
# © 2021 Narek Torosyan

ETA_ASKING = [
	"Flooding group chats...",
	"Starting time machine...",
	"Spamming XDA-general...",
	"Spamming the dev...",
	"Going to an oracle...",
	"Activating machine learning...",
	"Brute forcing password..."
]

ROOT = """
Check your devices XDA forum for detailed rooting instructions, but the general procedure is:
Unlock bootloader
Flash twrp
Flash magisk.zip inside twrp
Reboot phone
Profit

Or in case twrp isn't available:
Unlock bootloader
Download magisk manager apk from github
Install the app to patch your devices boot.img
Flash that patched boot.img
Bam... enjoy rooted phone
"""

ROOT_SAMSUNG = """
Check your devices XDA forum for detailed rooting instructions, but the general procedure (for Samsung's) is:
Unlock bootloader
Flash twrp
Flash magisk.zip inside twrp
Reboot phone
Profit

Or in case twrp isn't available:
Unlock bootloader
Download magisk manager apk from github
Install the app to patch your devices boot.img
Repack the patched boot.img to boot.img.tar
Flash that patched boot.img.tar
Bam... enjoy rooted phone

(Alternatively if you have nobody to send you your devices boot.img, download your devices stock firmware and patch the whole AP file)
"""

AB = """
A/B system updates use two sets of partitions referred to as slots (normally slot A and slot B). The system runs from the current slot while the partitions in the unused slot are not accessed by the running system during normal operation. This approach makes updates fault resistant by keeping the unused slot as a fallback: If an error occurs during or immediately after an update, the system can rollback to the old slot and continue to have a working system. To achieve this goal, no partition used by the current slot should be updated as part of the OTA update (including partitions for which there is only one copy).

Each slot has a bootable attribute that states whether the slot contains a correct system from which the device can boot. The current slot is bootable when the system is running, but the other slot may have an old (still correct) version of the system, a newer version, or invalid data. Regardless of what the current slot is, there is one slot that is the active slot (the one the bootloader will boot form on the next boot) or the preferred slot.

Each slot also has a successful attribute set by the user space, which is relevant only if the slot is also bootable. A successful slot should be able to boot, run, and update itself. A bootable slot that was not marked as successful (after several attempts were made to boot from it) should be marked as unbootable by the bootloader, including changing the active slot to another bootable slot (normally to the slot running immediately before the attempt to boot into the new, active one).
"""

BLOKADA = """
**How to Install Blokada**

By default, Android will block the installation of non-Play store APKs. They do this to prevent any malicious apps from being installed under your nose. So first we will tell Android to allow apps from unknown sources. To do this, go to Settings > Security > Unknown sources.
Next, you’ll want to download the latest APK from [here](https://blokada.org/#download) and install it like normal.
Now you should have successfully installed Blokada from the APK on their website.

**How to Activate Ad-Block**

When you launch Blokada for the first time, you’ll be greeted with the main screen that shows a power button icon. When you tap it, you’ll activate the ad-block service.
A notification will pop up asking about starting a VPN connection. Select “ok” and the ad-block service will begin.
At the bottom of the home screen, you’ll be able to keep track of how many ads have been blocked successfully. You’ll be surprised at how many background connections your device makes on just about any website.
"""

FLASH = """
*How to flash with the Android Flash Tool*

_NOTE: This guide is for Pixel phones only. For other devices a guide is just a Google search away._

\- Connect your device directly to your PC (no hubs, adapters, extenders, or monitors).
\- Open flash.android.com in a browser. It opens to the Welcome page.
\- Allow the flash tool to communicate with your device through ADB by accepting the popup that says "Allow site access to your ADB keys in order to communicate with devices".
\- Click Add new device.
\- Select your device from the list and click Connect. This list may not contain the full device name.
\- On your device’s screen, select Always allow from this computer and click OK to accept the USB debugging connection.
\- Select the connected device in your browser.
\- Search for and select your desired build from the list. You can also select options, such as wiping the device or force flashing all partitions.
\- Click Install to start the process. The device reboots and enters fastboot mode.
\- After Flash Complete appears, disconnect the device from the USB cable.
"""

# no, this doesn't mean pony features are coming to pixelbot
NSFW = [
	"nsfw group",
	"nsfw allowed",
	"18+ group",
	"18+ allowed",
	"porn group",
	"porn allowed",
	"pony group",
	"hentai fan",
	"hentai group",
	"hentai allowed",
	"🔞 group",
	"🔞 allowed",
	"🔞"
]

SLAP = [
	"a Pixel 5",
	"a Samsung",
	"a Pixel 4 bezel",
	"a Galaxy S20 FE",
	"One UI 3",
	"a Galaxy A02s",
	"an iPhone",
	"end of support",
	"an incomplete API",
	"an Exynos 990",
	"a Xiaomi",
	"a Huawei",
	"a Vivo",
	"the Death Star",
	"Android 11",
	"a Redmi",
	"RetardOS",
	"PE for sunfish",
	"bootloader unlock",
	"a potion of retardation",
	"SafetyNet failing",
	"basic attestation",
	"a Galaxy A02s",
	"a brick",
	"official TWRP",
	"bootloops",
	"an ETA request",
	"Magisk",
	"a piece of wood",
	"KG prenormal",
	"Android 12 beta",
	"Android 11 for Mi A3",
	"a free 1000% legit no virus free download link",
	"a permanently locked bootloader",
	"HWC fix",
	"a cracked APK",
	"sudo",
	"official pixel room",
	"DeX port",
	"a Nokia 3310"
]

SLAPPING = [
	"{0} grabs {2} and throws it at {1}.",
	"{0} lights {1} up like dynamite using {2}.",
	"{0} gets stick bugged by {1} lol.",
	"{0} takes {2} and throws it at {1}.",
	"{0} takes {2} and slaps {1} with it.",
	"{0} grabs {2} and chucks it at {1}.",
	"{0} takes {2} and sends it in {1}'s face.",
	"{0} launches {2} in {1}'s general direction."
	"{0} starts slapping {1} with {2}.",
	"{0} repeatedly slaps {1} with {2}.",
	"{0} repeatedly throws {2} at {1}.",
	"{0} flings {2} at {1}.",
	"{0} enables Discord light mode and throws it at {1}.",
	"{0} takes their cock, jumps and slaps it in {1}'s face."
]

PUNCH = [
	"{0} gets ran over with a bulldozer.",
	"{0} gets split in half with an axe.",
	"{0} updates his Mi A3 to Android 11.",
	"{0} gets lit up like dynamite.",
	"{0} switches to a Galaxy A02s.",
	"{0} drinks a potion of retardation.",
	"{0} gets stick bugged lol.",
	"{0} gets rickrolled.",
	"{0} gets tased to death.",
	"{0} gets shot with a nail gun.",
	"{0} gets squished with an anvil.",
	"A million Galaxy Homes get thrown at {0}. They survived.",
	"{0} gets dissected alive.",
	"{0} gets shred into dust.",
	"{0} was murdered. *FATALITY*",
	"{0} gets thrown into a volcano.",
	"{0} becomes a retard.",
	"{0} gets locked up in jail.",
	"{0} stands up, takes {1}'s hand, then u follow him, and they forces them to listen to WAP BAP, by Bibi H."
]

MANAGERS = [
	"MissRose_bot",
	"GroupHelpBot",
	"GroupHelpOfficialCloneBot",
	"IzumiUchihaBOT",
	"PawneeGoddess_Bot",
	"CalsiBot",
	"lindahotbot",
	"corsicanu_bot",
	"SayaAman_bot",
	"kigyorobot",
	"ThePikachuBot",
	"TheRealShadyBot"
]