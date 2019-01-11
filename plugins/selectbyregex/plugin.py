import os
import re
from qgis.PyQt import uic
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *
from selectbyregex.regexdialog import RegexDialog

'''
The main plugin class.
This is where the body of the plugin should be.
It's usually placed on a separate file, but we are putting it here
in the __init__.py file, since it's a small class, and for the sake 
of simplicity.
'''
class RegexPlugin:
    '''
    Do not place any GUI content in this method, but only the code 
    needed to initialized the non-GUI content of the plugin
    '''
    def __init__(self, iface):
        self.iface = iface

    '''
    GUI stuff is initialized in this method.
    This method is called when the QGIS UI is already up and running
    In this case, we use this method to add the plugin menus
    '''
    def initGui(self):
        self.action = QAction(u'Regex', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    '''
    Cleanup operations to be performed when the plugin is unloaded 
    (by the user disabling it in the Plugin Manager or by QGIS closing)
    In this case, we simply remove the plugin menu.
    '''
    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    '''
    This method is connected to the plugin menu, and will be called
    when the users clicks on it.
    It just opens the main plugin dialog, to perform the regex filtering
    '''
    def run(self):
        dialog = RegexDialog()
        dialog.exec_()
        if dialog.layer:
            selectByRegex(dialog.layer, dialog.field, dialog.regex)
