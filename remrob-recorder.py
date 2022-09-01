#!/usr/bin/python3

# This code is an example for a tutorial on Ubuntu Unity/Gnome AppIndicators:
# http://candidtim.github.io/appindicator/2014/09/13/ubuntu-appindicator-step-by-step.html
# https://gist.github.com/candidtim/7290a1ad6e465d680b68

import os
import signal
import json
import subprocess

import urllib.request as Request

# from urllib2.request import urlopen # URLError
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify



APPINDICATOR_ID = 'myappindicator'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('sample_icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_myapp = gtk.MenuItem(label='Start recording for 1 minute')
    item_myapp.connect('activate', myapp)
    menu.append(item_myapp)
    
    item_myapp_stop = gtk.MenuItem(label='Stop recording')
    item_myapp_stop.connect('activate', myapp_stop)
    menu.append(item_myapp_stop)

    item_quit1 = gtk.MenuItem(label='Quit')
    item_quit1.connect('activate', quit1)
    menu.append(item_quit1)

    menu.show_all()
    return menu

def myapp(_):
    # Call the ffmpeg app to start recording
    #subprocess.call("/home/bio/start_1_min.sh", shell=True)
    subprocess.run(['notify-send', 'Recording started...'])
    return myapp
    
def myapp_stop(_):
    # Stop the process if recording is ongoing
    #subprocess.call("/home/bio/stop.sh", shell=True)
    subprocess.run(['notify-send', 'Recording stopped...'])
    return myapp

def quit1(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
