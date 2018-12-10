Actions
========

QGIS allows to add actions that are triggered when the user interacts with a given layer, whether in the canvas or in the attribute table.

Actions can be defined in several ways, one of them being with the use of Python code.

To add an action, open the layer properties and then move to the ``Actions`` tab. We will be working with the ``countries`` layer for this example.

We will add an action that will take the value of a given field (in this case a field named `wikipedia` where the Wikipedia entry name is stored), and open the Wikipedia page corresponding to that value. If such page doesn't exist, an error message will be shown.

In the actions tab, create a new action by clicking on the plus sign.

In the dialog that will appear, paste the following code. 

.. code-block:: python

	import urllib
	import webbrowser 
	from qgis.PyQt import QtWidgets

	'''
	This action is to be used with a vector layer that contains a field named 'wikipedia'.
	When the user triggers the action, a browser will be opened, which shows the corresponding wikipedia entry for the value in that field.

	Here we use the value of the 'wikipedia' field to compose the url.
	We use the expressions notation, and the [%wikipedia%] string will be replaced
	with the value of the 'wikipedia' field before the code is executed.
	'''
	url = "https://en.wikipedia.org/wiki/" + "[%wikipedia%]"

	try:
		response = urllib.request.urlopen(url)
		webbrowser.open(url, new=0, autoraise=True)
	except:
		QtWidgets.QMessageBox.warning(None, "Wrong value", "The corresponding Wikipedia page does not exist")	


Enter a name and check the `Feature scope` box, so the action is available when we are browsing the attributes table.

      .. figure:: definingaction.png

Once the action is defined, close the dialog and then close the properties dialog.

Now go the attributes table and click on a feature row to select it. Right click and you will see the action  that we have just created, available as a menu entry. 

      .. figure:: menu.png

Click on it to run it, and the corresponding Wikipedia page will be opened in your default browser.


