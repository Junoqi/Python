import os
import webbrowser
import time

print('What task are you hoping to do?')
print('Options: Chill, Gaming')
options = input('')

def gaming():
    print('What game?')
    print('========')
    game = input()
    print('Discord?')
    print('========')
    discord = input()
    print('AMD Radeon Software?')
    print('========')
    amd = input()
    print('CPU Temp Monitor')
    print('========')
    cpu = input()

    if discord == 'Yes':
        os.startfile('C:/Users/Henry Pope IV/AppData/Local/Discord/app-0.0.305/Discord.exe')
    elif amd == 'Yes':
        os.startfile('C:/Program Files/AMD/CNext/CNext/RadeonSoftware.exe')
    elif cpu == 'Yes':
         os.startfile('C:/Program Files/Core Temp/Core Temp.exe')
    else:
        print('Ok')

    if game == 'Apex Legends':
        os.startfile('C:/Program Files (x86)/Origin/Origin.exe')
        time.sleep(10)
        os.startfile('C:/Program Files (x86)/Origin Games/Apex/R5apex.exe')
    elif game == 'Minecraft':
        os.startfile('C:/Games/Minecraft Launcher/MinecraftLauncher.exe')
    elif game == 'Fortnite':
        os.startfile('C:/Games/Epic Games/Launcher/Portal/Binaries/Win32/EpicGamesLauncher.exe')
    elif game == 'Realm Royale':
        os.startfile('steam://rungameid/813820')
    elif game == 'Terraria':
        os.startfile('steam://rungameid/105600')
    elif game == 'Escape From Tarkov':
        print('It wont let you do that ya muggggggg. THAT GAME IS BOOTY ANYWAY')
    elif game == 'Sea of Theives':
        print('You have to go to the XBOX app. Sorry chimper :(') 
    else:
        print("THERE IS NO SUCH GAME U MUG!")

def chill():
    print('Options: Youtube, Reddit, Twitter, News')
    print('========')
    options = input('What type of chill would you like? ')
    print('========')
    music = input('Would you like music with that? Yes/No ')
    print('========')
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    if options == 'Reddit':
        webbrowser.get(chrome_path).open('reddit.com')
    elif options == 'Youtube':
        webbrowser.get(chrome_path).open('www.youtube.com')
    elif options == 'Twitter':
        webbrowser.get(chrome_path).open('www.twitter.com')
    elif options == 'News':
        webbrowser.get(chrome_path).open('https://news.google.com/?hl=en-US&gl=US&ceid=US:en')
    else:
        print('Cant do that for ya')
    if music == 'Yes':
         os.startfile('C:/Users/Henry Pope IV/AppData/Roaming/Spotify/Spotify.exe')
    elif music == 'No':
        print('Ok')
    else:
        print('That is an invalid response')
   
if options == 'Gaming':
    gaming()
elif options == 'Chill':
    chill()
else:
    print("Theres no such thing ya noob")

input('Press ENTER to exit')

#os.startfile('C:/Program Files/AMD/CNext/CNext/RadeonSoftware.exe')
#os.startfile('C:/Users/Henry Pope IV/AppData/Local/Discord/app-0.0.305/Discord.exe')
#os.startfile('C:/Program Files/Core Temp/Core Temp.exe')


