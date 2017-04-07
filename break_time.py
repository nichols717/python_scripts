import time
import webbrowser

repeats = 1

print("This program started on: "+time.ctime())

while repeats<=3:
    time.sleep(5)
    print("Break time starts at: "+time.ctime())
    #webbrowser.open("https://www.youtube.com/watch?v=u1xrNaTO1bI")
    repeats=repeats+1

