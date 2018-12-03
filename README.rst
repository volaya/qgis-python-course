QGIS-Python programming
=========================

Below is the structure of an introductory QGIS-Python course.

The QGIS API
---------------

- Introduce the QGIS API and other APIs. 

	Links:

	- `QGIS API <http://qgis.org/api/>`_
	- `QGIS-Python API <https://qgis.org/pyqgis/3.0/>`_
	- PyQt: `Qt4 <http://pyqt.sourceforge.net/Docs/PyQt4>`_  in the case of QGIS 2, or `Qt5 <http://pyqt.sourceforge.net/Docs/PyQt5>`_ in the case of QGIS 3
	- `GeoAPIs <http://geoapis.sourcepole.com>`_: A more practical solution for browsing the Python, Qt and QGIS APIs.

	The reference text for developing Python plugins and using the QGIS Python Console is the  `PyQGIS cookbook <http://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/>`_.

	Some additional resources that can be used as a reference or as a source of examples:

	- This repository contains densely commented versions of a few QGIS plugins, so their code can be read as a learning tool.

		https://github.com/volaya/commented-qgis-plugins

	- A collection of short snippets can be found here:

		https://github.com/webgeodatavore/pyqgis-samples

- The Python console. The first place to start trying some simple commands. Here are some `some short exercises <./console.py>`_ (code +  comments)

- Expressions. How to create a custom Python expression and later use it in different places in QGIS. 

	Based on the previous point, `here <./expressions.py>`_ is the code for a custom function that can be later used for rendering. Another option would be to use it to create a new field using the field calculator. 

	If the user is not familiar with QGIS expressions, a quick review is recommended. `Here <https://docs.qgis.org/2.18/en/docs/user_manual/working_with_vector/expression.html>`_ is the official documentation (which includes a short section about custom Python expressions as well).

- Custom Python actions. React to user interaction in the canvas or attributes table.

	- `Here <./actions.py>`_ is an example of an action to be added to the countries vector layer that can be found in the `data` folder. The action is added in the `Actions` section of the layer properties.

- Maptips. Custom behaviour of map tips using QGIS expressions with python functions.

	Using the ideas introduced in the previous sections, `here <./maptip.py>`_ is a function that can be used in such an expression. Once the function is added, the maptip can be defined for the countries vector layer, usign `this code <./maptip.txt>`_ in the `Display` section of the layer properties.

- Hooks/Macros. Executing Python code to respond to QGIS events.

	Two macros are proposed, to be added to the project macros in the 'Project/Settings/Macros' section. The `first one <./projectmacroopen.py>`_ shows a warning message whenever the project is opened. The `second one <./projectmacrosave.py>`_ saves a new version of the project file to a git repository each time the project is saved.


- Creating Processing algorithms.

	In case the user needs to add analysis functionality, the best way to do it is to add a Processing algorithm.

	It is reccomended to to start with a template, using the `Create New Script from Template` option in the Processing Toolbox. The template is fully commented and should contain enough information to understand what is needed to create a Processing algorithm.

	When a set of scripts has been created, it can be packaged into a plugin that adds those scripts. That can be done from the Processing toolbox, as explained `here <https://docs.qgis.org/testing/en/docs/pyqgis_developer_cookbook/processing.html#id2>`_

-Creating plugins.

	The following three plugins are recommended for creating a new QGIS plugin:

	- `Plugin Creator <https://github.com/volaya/qgis-plugincreator-plugin/>`_: It generates the plugin skeleton. The description of elements in that skeleton is provided in the `plugin documentation <https://github.com/volaya/qgis-plugincreator-plugin/blob/master/README.md>`_.

	- `Plugin reloader <https://github.com/borysiasty/plugin_reloader>`_: To update plugins when you make changes in the code, without having to restart QGIS. 

	- `First aid plugin <https://github.com/wonder-sk/qgis-first-aid-plugin>`_: Plugin with useful tools for plugin developers, including debugin tools.

	An example of a minimal functional plugin can be found in the `plugin` folder or this repository.

