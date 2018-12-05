import os
import re
from qgis.PyQt import uic
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *

def classFactory(iface):
    return RegexPlugin(iface)

def selectByRegex(layer, field, regex):
    exp = re.compile(regex)
    features = layer.getFeatures()
    ids = []
    for feature in features:
        if exp.search(feature[field]):
            ids.append(feature.id())
    layer.selectByIds(ids)


class RegexPlugin:
    def __init__(self, iface):
        self.iface = iface

    def initGui(self):
        self.action = QAction(u'Regex', self.iface.mainWindow())
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)

    def unload(self):
        self.iface.removeToolBarIcon(self.action)
        del self.action

    def run(self):
        dialog = RegexDialog()
        dialog.exec_()
        if dialog.layer:
            selectByRegex(dialog.layer, dialog.field, dialog.regex)
            
WIDGET, BASE = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'plugin.ui'))

class RegexDialog(BASE, WIDGET):

    def __init__(self):
        super(RegexDialog, self).__init__(None)
        self.layer = None
        self.setupUi(self)
        self.layerCombo.layerChanged.connect(layerChanged)
        self.buttonSelect.clicked.connect(self.selectClicked)

    def layerChanged(self, layer):
        self.fieldCombo.setLayer(layer)

    def selectClicked(self):
        layer = self.layerCombo.currentLayer()
        field = self.fieldCombo.currentField()
        expression = self.textExpression.text()
        selectByRegex(layer, field, expression)