Processing algorithms
=======================

You can create your own Processing algorithms by writing the corresponding Python code and
adding a few extra lines to supply additional information needed to define the
semantics of the algorithm.

Processing algorithms are the preferred way of adding new analytical functionality to QGIS, since they will be available in all the Processing components, such as the Toolbox, the Graphical Modeler or the Batch Processing Interface


You can find a ``Create new script`` menu under the ``Tools``
group in the ``Script`` algorithms block of the toolbox. Double-click on
it to open the script edition dialog. That's where you should type your code.
Saving the script from there in the ``scripts`` folder (the default one when
you open the save file dialog), with ``.py`` extension, will automatically
create the corresponding algorithm.

The name of the algorithm (the one you will see in the toolbox) is created from
the filename, removing its extension and replacing underscores with blank spaces.

Here you have the code of a simple algorithm that saves to a new file the selected features of a given vector layer. It is fully commented to help you understand what is happening.

.. code-block:: python

  ##Vector=group
  ##input=vector
  ##output=output vector

  from qgis.core import *
  from processing.tools.vector import VectorWriter

  # We get the QgsVectorLayer objet based on the value selected by the user 
  # ('input' will contain the path to the layer source, not the layer object itself)
  vectorLayer = processing.getObject(input)

  # We create a new layer using the VectorWrite helper class, which is par of Processing
  # This output layer has the same characteristics (fields, crs, geometry type) as the input layer
  # The resulting vector layer is saved to the path entered by the user, which will be stored in the 'output' variable
  writer = VectorWriter(output, None, provider.fields(),
                        vectorLayer.dataProvider().geometryType(), vectorLayer.crs())

  # We iterate over the input layer features. 
  # The processing.features function iterates over the selected features in case there is a selection in the passed layer
  # We write each feature to the vector writer created above
  features = processing.features(vectorLayer)
  for feat in features:
      writer.addFeature(feat)

  del writer


As you can see, it looks like a regular script that uses the QGIS API, but it contain a set of lines at the beginning, with double hashtags. Those lines define the semantics of the algorithm, indicating which values (and their types) are required to run the algorithm, and what kind of output it produces. With that, Processing will be able to generate the correspodning graphical interfaces for interacting with the algorithm. Also, it will create the variables to contain the values selected by the user when executing the algorithm, which can later be used en the algorithm (you will notice that we are using variables `input`and `output`, although they are not defined in the above script. That's because Processing will set them based on the user input, before starting running the algorithm code).

Use the code above to create a new algorithm, and save it as explained at the beginning of this section. Your algorithm will be available in the Processing Toolbo, and you can open it to test it on the provided sample layer.

More detailed information about how to write Processing algorithms is found in the `corresponding section <https://docs.qgis.org/2.18/en/docs/user_manual/processing/scripts.html>`_ in the QGIS user manual.

When a set of scripts has been created, it can be packaged into a plugin that adds those scripts. That can be done from the Processing toolbox, as explained `here <https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/processing.html#id2>`_

