import sys
import pyautogui as pag
import time
import os
import webbrowser
start_time = time.time()
fl = (sys.argv[1])
with open(fl, "r") as f:  # Open file for reading
    file_contents = f.read()  # Read file contents
    file_contents = file_contents.strip()
    splittin = file_contents.splitlines()
def find_between( s, first, last ):
        try:
            start = s.index( first ) + len( first )
            end = s.index( last, start )
            return s[start:end]
        except ValueError:
            return ""
pag.FAILSAFE = False
MOUSE_POS = pag.position()
PS_INF = 999999999999999999999999**30
BOUNDS = pag.size()
def anal():
    try:
        idx = line.split("(")[0]

        if idx == "displayf":
            print(eval(find_between(line,"(", ")")))
        
        if idx == "moveto":
            nums = eval(find_between(line, "(", ")"))
            nums = list(nums)
            pag.moveTo(*nums)
        if idx == "dragto":
            nums = eval(find_between(line, "(", ")"))
            nums = list(nums)
            pag.dragTo(*nums)
            pag.mouseUp
        if idx == "sim":
            key = eval(find_between(line, "(", ")"))
            pag.press(key)
        if idx == "exit":
            quit()
        if idx == "simhk":
            key = eval(find_between(line, "(", ")"))
            key = list(key)
            pag.hotkey(*key)
        if idx == "type":
            data = eval(find_between(line, "(", ")"))
            data = list(data)
            pag.typewrite(*data)
        if idx == "wait":
            time2 = eval(find_between(line, "(", ")"))
            time.sleep(time2)
        if idx == "lmb":
            amt = eval(find_between(line, "(", ")"))
            for i in range(amt):
                pag.leftClick()
        if idx == "rmb":
            amt = eval(find_between(line, "(", ")"))
            for i in range(amt):
                pag.rightClick()
        if idx == "mmb":
            amt = eval(find_between(line, "(", ")"))
            for i in range(amt):
                pag.middleClick()
        if idx == "opentab":
            key = eval(find_between(line, "(", ")"))
            webbrowser.open(key)
        if idx == "scroll":
            scrollunits = eval(find_between(line, "(", ")"))
            pag.scroll(scrollunits)
            
        if idx == "locate":
            img = eval(find_between(line, "(", ")"))
            loc = pag.locateCenterOnScreen(img)
            pag.moveTo(loc)
        if idx == "msg":
            message = eval(find_between(line, "(", ")"))
            os.system("msg * "+str(message).strip())
        if idx == "pass":
            cmd = eval(find_between(line, "(", ")"))
            os.system(cmd)
        if idx == "help":
            print("\033[35m\033[3mHelp: To get started with castro see the github page: https://github.com/Cmspeedrunner/Castro \nCastro wake command is built into the Conch shell at: https://github.com/Cmspeedrunner/conch\n")
        if idx == "version":
            print("\033[34m\033[1m"+""""@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@.                &@@@@@@@@@@@
@@@@@*   @@@@@@@@@@@@@@@@@@@@@    @@@@@@
@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@
@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@
@@@@                               @@@@@
@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@
@@@@@                             @@@@@@
@  @@             /@@              @   @
@  @@   @@      @ /@@  @     @@    @@  @
@  @@   @@@@@     /@@     @@@@@    @@  @
@@      @@@@@@@@* /@@  @@@@@@@@      ,@@
@@@@    @@@@   @@@    @@   @@@@  (  @@@@
@@@  @  &@@  @@@@@@@@@@@@@  @@@  @@  @@@
@@@  (@@@@@@@@@@@@@  @,  @@@@@@@@@  @@@@
@@@@ @@@@@@@@@@@@@@@  @@@  ,@@@@@@  @@@@
@@@@   @@@@@@@@@@@@@@@   @@*  @@   @@@@@
@@@@@@  @@@@@@@@@@@@@@@@@  @@&    @    @
@@@@@@@@   @@@@@@@@@@@@@@@@   @@  @@@@@@
@@@@@@@@@@&     @@@@@@@@     @/ @@@@@@@@
@@@@@@@@@@@@@@@@*  @@  (@@@@@@@@@@@@@@@@"""+"\033[35m\033[3m\nCASTRO VERSION: 0.15\nGITHUB: https://github.com/Cmspeedrunner/Castro\nDEV: Cm")
        
    
            
    except SyntaxError as e:
        print("\033[31m\033[1mSYNTAX ERROR FOUND IN FILE: "+fl+"\n                     "+"^"*len(fl))
        print(e.args[0]+"\n")
        print("LN: "+str(e.lineno)+"\nCOL: "+str(e.end_offset))
        print("\033[31m\033[1m"+e.text)
        print("^"*len(e.text))
        print("\033[35m\033[3mHelp: The code that is causing the issue is above. At line "+str(e.end_lineno)+" and column "+ str(e.end_offset)+".")
        print("\033[0m", end="")
        exit()
    except TimeoutError as e:
        print("\033[31m\033[1mT.O ERROR FOUND IN FILE: "+fl+"\n                     "+"^"*len(fl))
        print(e.args[0]+"\n")
        print("\033[31m\033[1m"+e.winerror)
        print("^"*len(e.winerror))
        print("\033[35m\033[3mHelp: The winerror is above. "+ str(e.strerror)+".")
        print("\033[0m", end="")
        exit()
    except TypeError as e:
        print("\033[31m\033[1mTYPE ERROR FOUND IN FILE: "+fl+"\n                     "+"^"*len(fl))
        print(e.args[0]+"\n")
        print("\033[35m\033[3mHelp: "+str(e.args))
        print("\033[0m", end="")
        exit()
    except NameError as e:
        print("\033[31m\033[1mNAME ERROR FOUND IN FILE: "+fl+"\n                     "+"^"*len(fl))
        print(e.args[0]+"\n")
        print("\033[31m\033[1m"+e.name)
        print("^"*len(e.name))
        print("\033[35m\033[3mHelp: The issue is that the name '"+e.name+"' that is named in your code doesnt exist. The only valid variables are:\n\033[34mMOUSE_POS <---\033[35mStores the mouse position\n\033[34mPS_INF <---\033[35mStores a pseudo infinite number\n\033[34mBOUNDS <---\033[35mStores the bounds of your screen\nAny others are not valid.")
        print("\033[0m", end="")
        exit()
    
    
for i, line in enumerate(splittin):
    anal()


end_time = time.time()     
duration = end_time - start_time
print("\033[32m\033[1m"+"Program executed in "+str(duration).strip()+"s\033[0m", end="")

