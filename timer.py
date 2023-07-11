import time
from tkinter import *

from pygame import mixer

window = Tk()

clockImage = PhotoImage(file="assets\\clock.png")

mixer.init()
mixer.music.load(filename="assets\\alarm-sound.mp3")

window.title("Timer")
window.geometry("468x380")
window.iconphoto(True, clockImage)
window.resizable(False, False)

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("00")
second.set("00")


def stopsound():
    try:
        mixer.music.stop()
        time.sleep(0.5)
        timesupButton.grid_remove()

    except:
        return


def submit():
    timesupButton.grid_remove()

    try:
        temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

    except:
        hour.set("00")
        minute.set("00")
        second.set("00")

    while temp > -1:
        mins, secs = divmod(temp, 60)
        hours = 0
        if mins > 60:
            hours, mins = divmod(mins, 60)

        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        window.update()
        time.sleep(1)

        if temp == 0:
            timesupButton.grid(row=5, column=1, padx=2, pady=2)
            mixer.music.play()

        temp -= 1


titleLabel = Label(
    window,
    text="Timer ",
    font=("Comic Sans MS", 40, "bold"),
    fg="#00ff00",
    bg="black",
    image=clockImage,
    compound=RIGHT,
)
titleLabel.grid(row=0, column=1, padx=2, pady=2)

setLabel = Label(
    window,
    text="Set a time for the timer:",
    font=("Comic Sans MS", 20, "bold"),
    fg="#00ff00",
    bg="black",
)
setLabel.grid(row=1, column=1, padx=2, pady=2)

hourEntry = Entry(
    window, font=("Comic Sans", 20), width=3, textvariable=hour, bg="#f7ffde"
)
hourEntry.grid(row=2, column=0, sticky=W, padx=2, pady=2)

minuteEntry = Entry(
    window, font=("Comic Sans", 20), width=3, textvariable=minute, bg="#f7ffde"
)
minuteEntry.grid(row=2, column=1, padx=2, pady=2)

secondEntry = Entry(
    window, font=("Comic Sans", 20), width=3, textvariable=second, bg="#f7ffde"
)
secondEntry.grid(row=2, column=3, sticky=E, padx=2, pady=2)

hourLabel = Label(window, text="hours", font=("Comic Sans", 10), width=5)
hourLabel.grid(row=3, column=0, sticky=W, padx=2, pady=2)

minuteLabel = Label(window, text="mins", font=("Comic Sans", 10), width=5)
minuteLabel.grid(row=3, column=1, padx=2, pady=2)

secondLabel = Label(window, text="secs", font=("Comic Sans", 10), width=5)
secondLabel.grid(row=3, column=3, sticky=E, padx=2, pady=2)


submitButton = Button(
    window,
    text="Start Countdown",
    font=("Comic Sans", 12, "bold"),
    bd=5,
    command=submit,
    bg="black",
    fg="#00eaff",
    activebackground="black",
    activeforeground="#00eaff",
    padx=2,
    pady=2,
)
submitButton.grid(row=4, column=1)

timesupButton = Button(
    window,
    text="Time's up!",
    font=("Aerial", 40, "bold"),
    bg="black",
    fg="#fdff00",
    activebackground="black",
    activeforeground="#fdff00",
    pady=5,
    bd=5,
    command=stopsound,
)


window.mainloop()
