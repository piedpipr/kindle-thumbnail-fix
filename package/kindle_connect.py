#!/usr/bin/env python3
import pyudev


def kindle_connect():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block')
    for action, device in monitor:
        if ((device.get('ID_FS_LABEL')=='Kindle') & (action == 'change')):
            print("Kindle Connected..")
            status = 1;
        if ((device.get('ID_FS_LABEL')=='Kindle') & (action == 'remove')):
            print("Kindle Disconnected..")
            status = 0;
          
        