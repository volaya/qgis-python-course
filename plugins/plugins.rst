Plugins
=======================

This section describes the main ideas about creating QGIS plugins. It assumes that you are already familiar with the QGIS and PyQT API's. It only describes the structure of a plugin and how plugins are prepared installed and packaged.

Recommended plugins
--------------------

It's recommended to have the following plugins installed in your QGIS, to help you with the testing and debugging of your plugin

    - `Plugin reloader <https://github.com/borysiasty/plugin_reloader>`_: To update plugins when you make changes in the code, without having to restart QGIS. 

    - `First aid plugin <https://github.com/wonder-sk/qgis-first-aid-plugin>`_: Plugin with useful tools for plugin developers, including debugging tools.


Using a plugin template
------------------------

Instead of starting from scratch, it is better to use a template. Two alternatives are recommended:

    - Using the `Minimal QGIS plugin template <https://github.com/wonder-sk/qgis-minimal-plugin>`_. It contains just the bare minimum required to have a functional plugin, and it's the best way of writing your first plugins or any plugin that does not require more complex elements.

    - Using the `Plugin Creator <https://github.com/volaya/qgis-plugincreator-plugin/>`_ plugin. You can set up many different paramenters in its interface, and it will create the plugin skeleton tailored to your needs. It can include not just the Python code of the plugin, but also other elements suchs as tests, CI integration, setup scripts, and much more. The description of those elements is provided in the `plugin documentation <https://github.com/volaya/qgis-plugincreator-plugin/blob/master/README.md>`_.


A sample plugin
----------------

An example of a minimal functional plugin can be found in the `plugins/selectbyregex` folder of this repository. This plugin is based on the minimal plugin templated described above.

Here is a description of its files and their content.

- ``metadata.txt``:

    This file is used to describe the plugin. QGIS will use this to manage plugins versions and show the information in the Plugin Manager.

    The file contains the following lines:

    ::

        [general]
        name=SelectByRegex
        description=Select By regular expressions
        version=1.0
        qgisMinimumVersion=2.0
        author=Victor Olaya
        email=volaya@boundlessgeo.com

    Additional items can be added. The above are just the minimum required ones for the plugin to be run. 


- ``__init__.py``: 

    This file just contains one function. Even in larger plugin, this file just has this content, which is used to inform QGIS of the plugin class that it has to load to instantiate the plugin.

    - ``classFactory()`` function. A mandatory function in the ``__init__.py`` file. It should return and object of the class that represents the plugin.

        .. code-block:: python

            def classFactory(iface):
                return RegexPlugin(iface)

- ``plugin.py``:

    This file contains the main plugin class ``RegexPlugin``. All plugin classes must contain the following three methods.

    - ``__init__(self, iface)``

        It should contain all code required to initialize the plugin, except for the GUI elements. GUI elements are initialized in the ``initGui()`` method.

        In our example case, we just store the QgisInterface object that is passed to plugins when they are instantiated, so we can use it in other methods of the class.

        .. code-block:: python

            def __init__(self, iface):
                self.iface = iface

    - ``initGui(self)`` 

        This is where GUI content has to be initialized. In our example, we add here the plugin menu to the QGIS menu bar.

        .. code-block:: python

            def initGui(self):
                self.action = QAction(u'Regex', self.iface.mainWindow())
                self.action.triggered.connect(self.run)
                self.iface.addToolBarIcon(self.action)  

    - ``unload(self)``

        Cleanup operations must be performed here. They will be run when the plugin is disabled using the Plugin Manager or when QGIS shuts down). In our case, we case, we simply remove the plugin menu that was added in the ``initGui()`` method, and delete its associated action.
                
        .. code-block:: python

            def unload(self):
                self.iface.removeToolBarIcon(self.action)
                del self.action

- ``regexdialog.py``:

    This file contains the main UI class, ``RegexDialog``. 

    This class loads the main dialog UI, which has been created using QtDesigner and is stored in the ``regexdialog.ui`` file. It adds the logic for that UI, and contains the method that performs the selection when the user clicks on the ``Select`` button.

    .. code-block:: python

        WIDGET, BASE = uic.loadUiType(
            os.path.join(os.path.dirname(__file__), 'regexdialog.ui'))

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

- ``regexdialog.ui``. The file that contains the UI of the regex dialog, as generated by QtDesigner.

How to install a plugin
-------------------------

Once you have the code of your plugin written, you must install it into your QGIS application. To do that, the plugin folder has to be under the user plugins folder. In QGIS 2, the users plugin folder is located at `[userfolder]/.qgis2/python/plugins/`. For the example plugin that we have been describing (which is in a folder named `selectbyregex`), we should have it in a `[userfolder]/.qgis2/python/plugins/selectbyregex` folder in your system, in order to be found and loaded by QGIS.

You can copy the sample plugin or, better, create a symlink to the folder where it is stored. The start your QGIS and your plugin should already be there to be executed. If it's not, you might need to enable it in the QGIS Plugin Manager.
