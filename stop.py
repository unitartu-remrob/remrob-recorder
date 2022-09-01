#!/usr/bin/python3

import os
import signal
import json
import subprocess

import urllib.request as Request

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
from gi.repository import Notify as notify

APPINDICATOR_ID = 'myappindicator'

def main():
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('path_to_icon.svg'), appindicator.IndicatorCategory.SYSTEM_SERVICES)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu():
    menu = gtk.Menu()

    item_myapp = gtk.MenuItem(label='Start recording 1 minute')
    item_myapp.connect('activate', myapp)
    menu.append(item_myapp)
    

    item_quit1 = gtk.MenuItem(label='Quit')
    item_quit1.connect('activate', quit1)
    menu.append(item_quit1)

    menu.show_all()
    return menu

def myapp(_):
    subprocess.call("path_to_stop_1_min.sh", shell=False)
    return myapp

def quit1(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
