#appModules/streamfab64.py
# Ein Teil von NonVisual Desktop Access (NVDA)
# Copyright (C) 2006-2025 NVDA Mitwirkende
# Diese Datei unterliegt der GNU General Public License.
# Weitere Informationen finden Sie in der Datei COPYING.
from NVDAObjects.UIA import UIA
import appModuleHandler
import controlTypes
import api
from scriptHandler import script
import addonHandler
# Entfernen Sie das Kommentarzeichen (#) aus der nächsten Zeile, wenn (und sobald) die Datei zu einem Addon gehört. Dadurch werden Lokalisierungsfunktionen (Übersetzungsfunktionen) in Ihrer Datei aktiviert. Weitere Informationen finden Sie im Entwicklungshandbuch für NVDA-Addons.
#addonHandler.initTranslation()
class streamfab_uiaobj(UIA):
	def _get_name(self):
		return self.UIAAutomationId.split(".")[-1]

class AppModule(appModuleHandler.AppModule):
	def event_NVDAObject_init(self, obj):
		if obj.role in [controlTypes.ROLE_DOCUMENT, controlTypes.ROLE_TABLE, controlTypes.ROLE_EDITABLETEXT]:
			self.trapobj = obj
			self.bindGesture("kb:control+tab", "gotonext")
			self.bindGesture("kb:control+shoft+tab", "gotoprev")
		if obj.role == controlTypes.ROLE_DOCUMENT:
			obj.setFocus()
	def script_gotonext(self, gesture):
		self.trapobj.next.setFocus()
	def script_gotoprev(self, gesture):
		self.trapobj.previous.setFocus()



	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if isinstance(obj, UIA):
			if obj.name == "":
				clslist.insert(0, streamfab_uiaobj)
