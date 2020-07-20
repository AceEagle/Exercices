import subprocess
class AppsGroups:
    def DiscordTime(self):
        subprocess.Popen([r"C:\Users\math_\AppData\Local\Discord\Update.exe"])
        subprocess.Popen([r'C:\Program Files (x86)\Steam\steam.exe'])
        subprocess.Popen([r'C:\Riot Games\Riot Client\RiotClientServices.exe'])

    def CodingTime(self):
        subprocess.Popen([r'C:\Users\math_\AppData\Local\JetBrains\Toolbox\\apps\PyCharm-C\ch-0\\201.6668.115\\bin\pycharm64.exe'])
        subprocess.Popen([r'C:\Users\math_\AppData\Local\gitkraken\Update.exe'])

mdr = AppsGroups()
mdr.DiscordTime()