QGIS-Python programming
=========================

Below is the structure of an introductory QGIS-Python course.

- The QGIS API.

	Introduce the QGIS API and other APIs. 

	- Links:

		- `QGIS API <http://qgis.org/api/>`_
		- `PyQt4 <http://pyqt.sourceforge.net/Docs/PyQt4>`_ 
		- `GeoAPIs <http://geoapis.sourcepole.com>`_: A more practical solution for browsing the Python, Qt and QGIS APIs.

	- The reference text for developing Python plugins and using the QGIS Python Console is the  `PyQGIS cookbook <http://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/>`_.

	- Some additional resources that can be used as a reference or as a source of examples:

		- This repository contains densely commented versions of a few QGIS plugins, so their code can be read as a learning tool.

			https://github.com/volaya/commented-qgis-plugins

		- A collection of short snippets can be found here:

			https://github.com/webgeodatavore/pyqgis-samples

- `The Python console <console/console.rst>`_. The first place to start exploring the QGIS API.

- `Expressions <expressions/expressions.rst>`_. How to create a custom Python expression and later use it in different places in QGIS. 


- `Custom Python actions <actions/actions.rst>`_. React to user interaction in the canvas or attributes table.


- `Maptips <maptips/maptips.rst>`_. Custom behaviour of map tips using QGIS expressions with Python functions.


- `Macros <macros/macros.rst>`_. Executing Python code to respond to QGIS events.


- `Processing algorithms <processing/processing.rst>`_.  In case the user needs to add analysis functionality, the best way to do it is to add a Processing algorithm.

- `Creating plugins <plugins/plugins.rst>`_. How to create QGIS plugins that can be later distributed and installed in other QGIS instances.

