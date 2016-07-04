# WebNotify by Aanand Kainth
#
# WebNotify is a service written in Python that sends a notification to the user when a website they have specified is updated.

import atexit
import urllib.request
import time
import tkinter
import WindowsNotification

INFO = WindowsNotification.registerProgram()
atomClass = INFO['atomClass']
hInstance = INFO['hInstance']
hWindow = INFO['hWindow']
Notfications = 0

def checkWebsites():
	numberToCheck = 1

	sitesFile = open('Configuration\.SITES')

	sitesLines = sitesFile.readlines()

	for lineInFile in sitesLines:
		OldFile = open('Caches\{}.html'.format(str(numberToCheck)), 'r')

		OldRead = OldFile.read()

		OldFile.close()

		try:
			urllib.request.urlretrieve(lineInFile, 'Caches\{}.html'.format(str(numberToCheck)))
		except Exception:
			Error.configure(text='Error Retrieving {}'.format(lineInFile))

		NewFile = open('Caches\{}.html'.format(str(numberToCheck)), 'r')

		NewRead = NewFile.read()

		NewFile.close()

		if OldRead != NewRead:
			try:
				WindowsNotification.addNotification('WebNotify', 'The following site was just updated.', r'Resources\\WebNotify.ico', Notifications, hInstance, hWindow)
			except Exception:
				pass

# def unregisterProgram():
# 	WindowsNotification.unregisterProgram(INFO['atomClass'], INFO['hInstance'], INFO['hWindow'])
#
# INFO = WindowsNotification.registerProgram('WebNotify')

# Copyright © 2016 Aanand Kainth All Rights Reserved.
