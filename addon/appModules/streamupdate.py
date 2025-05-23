#appModules/streamupdate.py
# Ein Teil von NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2025 NVDA Mitwirkende
# Diese Datei unterliegt der GNU General Public License.
# Weitere Informationen finden Sie in der Datei COPYING.
import appModuleHandler
import controlTypes
import api
from scriptHandler import script
import addonHandler
# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.
#addonHandler.initTranslation()
class AppModule(appModuleHandler.AppModule):
	def event_NVDAObject_init(self, obj):
		if obj.role == controlTypes.ROLE_DATAITEM:
			self.trapobj = obj
			self.bindGesture("kb:control+tab", "gotonext")
			self.bindGesture("kb:control+shift+tab", "gotoprev")
	def script_gotonext(self, gesture):
		self.trapobj.parent.next.setFocus()
	def script_gotoprev(self, gesture):
		self.trapobj.parent.previous.setFocus()



