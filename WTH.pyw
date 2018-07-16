import sys, pip, subprocess, time, random, threading
try :
    import pyautogui as gui
except:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'pyautogui'])
try :
    import keyboard
except:
    subprocess.check_call(["python", '-m', 'pip', 'install', 'keyboard'])
import sched

s = sched.scheduler(time.time, time.sleep)

def schedule(arg="") :
    global e
    if tis.find('-')!=-1 :
        a,b = map(int,tis.split("-"))
        tisgen=random.randint(a,b)
    else :
        tisgen=int(tis)
    if arg=="hotkey":
        if len(s.queue)!=0 :
            for e in s.queue :
                s.cancel(e)
            return
        t = threading.Thread(target=s.run)
        bot('call')
    s.enter(tisgen, 1, bot, (s,))
    try :
        t.start()
    except :
        pass

def bot(sc='') :
    keyboard.send('t')
    time.sleep(0.1)
    keyboard.write('%s'%text)
    keyboard.send('enter')
    keyboard.send('esc')
    if sc!='call' : schedule()

gui.alert('Warframe Trade Helper isn\'t responsible for any harm to your computer/account.')

text=gui.prompt("Input the Trade text", "Warframe Trade Helper", "WTS > ")
if text is None :
    exit()
tis=gui.prompt("Input the waiting time", "Warframe Trade Helper (use '-' for random range)", "121-125")
if tis is None :
    exit()
hotkey=gui.prompt("Input the hotkey", "Warframe Trade Helper", "f9")
if hotkey is None :
    exit()
gui.alert('Warframe Trade Helper will now move to the background.')

lastmessage= time.time()-120
keyboard.add_hotkey(hotkey, schedule, args=['hotkey'])
keyboard.wait()
