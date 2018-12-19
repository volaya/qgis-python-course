Understanding Python in QGIS
=============================

QGIS accepts Python code in many different places, such as in expressions,  or to create Processing algorithms and plugins. It's important to understand how the Python interpreter is connected to QGIS, and how it can be used.

This section provides some insight about this.

Differences between platforms
-----------------------------

An important difference exists between QGIS in Windows and QGIS in Linux or Mac. While the Windows version installs its own Python interpreter, the Linux and Mac ones rely on the system Python. It's important to take that into account, since 

Additional libraries
---------------------

For all operating systems, QGIS adds some Python libraries to the Python interpreter that it wil use. Those are mostly geo libraries such as shapely, etc. The Windows version will contain only those libraries, but if you are installing QGIS in Linux or Mac, you might have other libraries as well, or even different versions of the ones that are installed by QGIS

In case you need to use a library not installed by QGIS from your code (most likely from a plugin), you will have to add that library to the plugin itself. It's not recommended to add it to your system Python in case you are running Linux or Mac (using ``pip``), or to the QGIS Python in case you are using Windows, since that will not work in a different machine. Instead, ship the library with your plugin and then modify the `PYTHONPATH` as part of your plugin code, to be able to use the library.

In case your plugin requires additional libraries, it is recommended to use the Plugin Creator plugin, as explained in the `Creating plugins <../plugins/plugins.rst>`_ section. The plugin skeleton that it generates, already contains code to automate library installation and to make it available to the plugin.