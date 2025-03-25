import subprocess
import re
def profile():
    profile= subprocess.getoutput("netsh wlan show profile")
    print (profile)
    nethack=input(("what network do you want to hack: ")).strip()
    password= subprocess.getoutput("netsh wlan show profile name="+nethack+" key=clear")
    f = re.search(r"Key Content\s+:\s(.*)", password)
    save = f.group(1)
    try:
        with open("pass.txt", "w") as file:
            file.write(save)
        print( "the password for "+nethack+ " is saved to the <<pass.txt>>")
    except:
        print("wrong")
profile()
