APIs
=====

QGIS is built using the Qt platform. Both QT and QGIS itself have well-documented APIs that should be used when writing Python code to be run within QGIS. You dont need to *know* the API, but instead to be able to browse it and search it, so you can find what you need in each case.

This section describes both APIs, so you can understand how they are structured and use them efficiently. If you have used other API documentation, this might sound familiar to you, since they follow a rather standard format.

Qt
---

Since QGIS is built using Qt, a large number of QGIS classes inherit from the base Qt class (QObject), even if they have no GUI component. For this reason, it's interesting to know how to use the Qt API to work with QGIS objects.

The PyQt API is available at http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

You will see a list of all Qt classes

	..figure: pyqt.png

Let's select the base `QObject <http://pyqt.sourceforge.net/Docs/PyQt4/qobject.html>`_ class