import sys
import datetime


def set_win(time):
    import pywin32
    dayOfWeek = datetime.datetime(time).isocalendar()[2]
    pywin32.SetSystemTime(time[:2] + (dayOfWeek,) + time[2:])


def set_linux(time):
    import subprocess
    import shlex

    subprocess.call(shlex.split("timedatectl set-ntp false"))  # May be necessary
    subprocess.call(shlex.split("sudo date -s '%s'" % time))
    subprocess.call(shlex.split("sudo hwclock -w"))


def set(time):
    if sys.platform == 'linux2' or sys.platform == 'linux':
        set_linux(time)

    elif sys.platform == 'win32':
        set_win(time)
