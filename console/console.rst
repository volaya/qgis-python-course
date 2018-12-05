The Python console
===================

The first place to start working with Python is the Python console. You can open it using the ``Plugins/Python console`` menu.

    .. figure:: console.png

You have all the common Python elements, plus the QGIS API ones and the Qt library classes.

We will do some simple examples now, to demonstrate the kind of work that can be done from the console, and how to interact with QGIS elements from it. You should already be familiar with the QGIS API documentation, in other to browse it and find the corresponding classes and methods as we advance.

We will be working with data, so you should load the provided `countries` layer. Make it also 

You have access to the QGIS interface using the ``iface``. It's an object of class ``qgis.gui.QgisInterface`` (type ``type(iface)``  to check it), and you can see in its `API page <https://qgis.org/api/2.18/classQgisInterface.html>`_ that it has many methods. Among them, there is a ``activeLayer()`` one that gives us the layer currently selected in the layer list.

::

	>>> layer = iface.activeLayer()
	>>> type(layer)
	<class 'qgis._core.QgsVectorLayer'>


We have a ``QgsVectorLayer`` object. Again, we can go to the corresponding `QGIS API page <https://qgis.org/api/2.18/classQgsVectorLayer.html>`_  to check the available methods. Among them we find one to get the number of features in the layer.

::

	>>> layer.featureCount()
	177L

We can explore the data contained in the vector layer with more detail. Here is an example that computes the total population of the world, by adding the values in the ``pop_est`` field, which contain the population of each country.

::

	layer = iface.activeLayer()
	features = layer.getFeatures()
	totalPopulation = 0
	for feat in features: #we iterate over features in the layers
		pop = feat["pop_est"] #retrieve the population value using the feature as a dictionary and the field name as key.
		if pop > 0:
			totalPopulation += pop

	print (totalPopulation)


When our code snippet has several lines of code, it is more practical to creat a script file instead of typing those lines directly in the console. You can open the script editor by clicking on the ``Show editor`` button.

    .. figure:: showeditor.png

Now you can enter your script there and then click on the ``Run script`` button to execute it.

    .. figure:: runscript.png

Knowing that there is a field that contains the continent that each country belongs to, we can improve our previous script and compute the population of each continent.

::

	layer = iface.activeLayer()
	features = layer.getFeatures()
	totalPopulation = {}
	for feat in features:
		pop = feat["pop_est"]
		continent = feat["continent"]
		if pop > 0:
			if continent in totalPopulation:
				totalPopulation[continent] += pop
			else:
				totalPopulation[continent] = pop
	print (totalPopulation)

We can define functions in our script, and use all Python elements in it. Here's a more complex example showing that:

::


	'''
	This scripts adds a new field to the current active layer, 
	indicating if the feature is in the (N)orthern hemisphere, (S)outhern or (B)oth
	'''
	from qgis.PyQt.QtCore import QVariant

	'''
	We define the function that computes the hemisphere for a given geometry.
	The geometry is assumed to have geographical coordinates.
	'''
	def hemisphere(geom):
		#To compute the hemisphere, we just see where the top and bottom coordinates of the feature fall.
		box = geom.boundingBox()
		if box.yMinimum() > 0 and box.yMaximum() > 0:
			return "N"
		if box.yMinimum() <= 0 and box.yMaximum() <= 0:
			return "S"
		else:
			return "B"

	layer = iface.activeLayer()
	'''We get the layer provider, which we wil use to modify the layer features.
	Changes can be made directly to the layer object, using an edit buffer,
	but we do it directly with the provider for the sake of simplicity'''
	provider = layer.dataProvider() 
	#We add the field and update the layer for the change to take effect
	provider.addAttributes([QgsField("hemisphere", QVariant.String)])
	layer.updateFields()
	idxField = layer.fieldNameIndex("hemisphere")
	features = layer.getFeatures()
	'''Now we iterate over the features of the layer, 
	and for each of them we add the corresponding value to the new field'''
	for feat in features:
		geom = feat.geometry()            
		hemi = hemisphere(geom)
		provider.changeAttributeValues({feat.id() : {idxField: hemi}})


As an exercise, try to adapt the above script, so it can work on layers that have any type of CRS, not just geographical coordinates. Here are a few hints.

- You can obtain the CRS of a layer by calling its crs() method
- To transform between CRSs, use a `QgsCoordinateTransform <https://qgis.org/api/2.18/classQgsCoordinateTransform.html>`_ object.