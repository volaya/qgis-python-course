from qgis.utils import iface
from qgis.core import Qgis

' A simple project macro to show a warning message when the project is open.'
def openProject():
	iface.messageBar().pushMessage(
		"Warning",
		"This project contains classified data. Don't distribute it",
		Qgis.Warning,
		10
	)
