APIs
=====

QGIS is built using the Qt platform. Both QT and QGIS itself have well-documented APIs that should be used when writing Python code to be run within QGIS. You dont need to *know* the API, but instead to be able to browse it and search it, so you can find what you need in each case.

This section describes both APIs, so you can understand how they are structured and use them efficiently. If you have used other API documentation, this might sound familiar to you, since they follow a rather standard format.

Qt
---

Since QGIS is built using Qt, a large number of QGIS classes inherit from the base Qt class (QObject), even if they have no GUI component. For this reason, it's interesting to know how to use the Qt API to work with QGIS objects.

The PyQt API is available at http://pyqt.sourceforge.net/Docs/PyQt4/classes.html

You will see a list of all Qt classes

	.. figure:: pyqt.png

Let's select the base `QObject <http://pyqt.sourceforge.net/Docs/PyQt4/qobject.html>`_ class.

	.. figure:: qobject.png

The structure of this page will be the same one for all classes. 

First, it contains some information about the relation of this class with other available classes. Since this is the base class of all Qt objects, it doesn't inherit from any other class, but a large number of them inherit from it.

You will find next the list of available methods.

These are the methods that you can call on objects of this class. By clicking on a given method, you will be taken to its detailed description. Here's for instance, the description of the ``moveToThread`` method.

	.. figure:: movetothread.png

As you can see, it includes the detailed syntax of the method, describing the type of parameters that have to be passed. When the type of that parameter is itself a Qt object, you will have a link to quickly go to the corresponding page where that class is defined (in this case, you can see that for the ``QThread`` class).

If the method returns a value, the type of the value will be shown, and a corresponding link will be available as well in case the return object is a Qt object.

By following these links, you can explore methods and classes and find out how to call and use Qt objects and their methods.

Along with methods, you will find a list of so-called *signals*. Qt objects can emit signals, as part of the Qt mechanism of signals and slots, used to allow objects to communicate with other objects. 

	.. figure:: signals.png

You can connect to all signals available for a given object, so whenever the signal is emitted by the object, it will call the method you have connected the object to. To know more about signals and slots, and to understand how this mechanism works, check the corresponding `Qt documentation <http://doc.qt.io/archives/qt-4.8/signalsandslots.html>`_.

Notice that the list of methods and signals available for a given class in its API page might not include all the ones available for it. Methods and signals that come from parent classes will not be listed there. Instead, you have to look in the documentation of the parent class.

As an example, here's the list of methods and signals shown in the page corresponding to the ``QPushButton`` class.

	.. figure:: pushbutton.png

As you can see, there are no signals at all. We should expect at least one signal to be emited when the button is clicked. That signal exist, but is not defined in this class, but instead in the parent ``QAbstractButton``class. You can find a link to it in the upper part of the ``QPushButton`` API page, where the information about classes it inherits from is shown

Here is the signal definition in the parent class documentation.

	.. figure:: buttonsignals.png