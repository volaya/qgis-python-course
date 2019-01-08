APIs
=====

QGIS is built using the Qt platform. Both QT and QGIS itself have well-documented APIs that should be used when writing Python code to be run within QGIS. You dont need to *know* the API, but instead to be able to browse it and search it, so you can find what you need in each case.

This section describes both APIs, so you can understand how they are structured and use them efficiently. If you have used other API documentation, this might sound familiar to you, since they follow a rather standard format.

Qt
---

Since QGIS is built using Qt, a large number of QGIS classes inherit from the base Qt class (QObject), even if they have no GUI component. For this reason, it's interesting to know how to use the Qt API to work with QGIS objects.

The PyQt API classes can be found at http://doc.qt.io/qt-5/classes.html

You will see a list of all Qt classes

	.. figure:: pyqt.png

Let's select the base `QObject <https://doc.qt.io/qt-5/qobject.html>`_ class.

	.. figure:: qobject.png

The structure of this page will be the same one for all classes. 

First, it contains some information about the relation of this class with other available classes. Since this is the base class of all Qt objects, it doesn't inherit from any other class, but a large number of them inherit from it.

You will find next the list of available methods.

	.. figure:: qobject2.png

These are the methods that you can call on objects of this class. By clicking on a given method, you will be taken to its detailed description. Here's for instance, the description of the ``moveToThread`` method.

	.. figure:: movetothread.png

As you can see, it includes the detailed syntax of the method, describing the type of parameters that have to be passed. When the type of that parameter is itself a Qt object, you will have a link to quickly go to the corresponding page where that class is defined (in this case, you can see that for the ``QThread`` class).

If the method returns a value, the type of the value will be shown, and a corresponding link will be available as well in case the return object is a Qt object.

By following these links, you can explore methods and classes and find out how to call and use Qt objects and their methods.

Along with methods, you will find a list of so-called *signals*. Qt objects can emit signals, as part of the Qt mechanism of signals and slots, used to allow objects to communicate with other objects. 

	.. figure:: signals.png

You can connect to all signals available for a given object, so whenever the signal is emitted by the object, it will call the method you have connected the object to. To know more about signals and slots, and to understand how this mechanism works, check the corresponding `Qt documentation <http://doc.qt.io/qt-5/signalsandslots.html>`_.

Notice that the list of methods and signals available for a given class in its API page might not include all the ones available for it. Methods and signals that come from parent classes will not be listed there. Instead, you have to look in the documentation of the parent class.

In the documentation of the ``QPushButton`` class you won't see any signal described, but we should expect at least one signal to be emited when the button is clicked. That signal exists, but is not defined in this class, but instead in the parent ``QAbstractButton``class. You can find a link to it in the upper part of the ``QPushButton`` API page, where the information about classes it inherits from is shown

Here is the signal definition in the parent class documentation.

	.. figure:: buttonsignals.png

QGIS
-----

The QGIs API follows a similar approach. If you know how to navigate the Qt API, you will not have problems understanding the QGIS one.

The QGIS API base documentation, generated from the C++ code, is available at https://qgis.org/api/

A Python version of the API (the one you will be using when calling QGIS objects from Python) is available at https://qgis.org/pyqgis/3.0. At the moment, it contains less functionality than the core C++ documentation, so we will describe this last one here.

You can get the list of classes in the QGIS API at https://qgis.org/api/annotated.html

	.. figure:: qgis.png

Let's see the documentation for a given class. For instance the ``QgsVectorLayer`` class, which is the base for all vector layers within QGIS.

	.. figure:: vectorlayer.png

You can see an inheritance diagram, which gives you information about the classes inherited by this class and which other ones inherit from it (this was given in plain text in the Qt API).

Underneath you will find the methods of the class, along with signals and slots. QGIS classes inherit from the base Qt ``QObject`` class, and they also use the signals and slots approach mentioned above.

	.. figure:: vectorlayersignals.png

When return values or function parameters have a type that is itself a QGIS class, the type is shown and you can click on it to go to the corresponding documentation page.

