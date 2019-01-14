from qgis.PyQt import uic
from qgis.PyQt.QtGui import *
from qgis.PyQt.QtCore import *

'''The dialog structure is defined in a separate ui file.
We load it here and use it to create base classes that are 
then used to inherit from them'''
WIDGET, BASE = uic.loadUiType(
    os.path.join(os.path.dirname(__file__), 'regexdialog.ui'))

'''The class that contains the logic of the plugin dialog.'''
class RegexDialog(BASE, WIDGET):

    def __init__(self):
        super(RegexDialog, self).__init__(None)
        self.layer = None
        self.setupUi(self)
        self.layerCombo.layerChanged.connect(layerChanged)
        self.buttonSelect.clicked.connect(self.selectClicked)

    def layerChanged(self, layer):
        self.fieldCombo.setLayer(layer)

    def selectByRegex(layer, field, regex):
        exp = re.compile(regex)
        features = layer.getFeatures()
        ids = []
        for feature in features:
            if exp.search(feature[field]):
                ids.append(feature.id())
        layer.selectByIds(ids)

    def selectClicked(self):
        layer = self.layerCombo.currentLayer()
        field = self.fieldCombo.currentField()
        expression = self.textExpression.text()
        self.selectByRegex(layer, field, expression)