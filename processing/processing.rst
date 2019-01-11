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

Here you have the code of a simple algorithm that saves to a new file the selected features of a given vector layer. 

.. code-block:: python

  ##Vector=group
  ##input=vector
  ##output=output vector

  from qgis.core import *
  from processing.tools.vector import VectorWriter

  vectorLayer = processing.getObject(input)

  writer = VectorWriter(output, None, vectorLayer.dataProvider().fields(),
                        vectorLayer.dataProvider().geometryType(), vectorLayer.crs())

  features = processing.features(vectorLayer)
  for feat in features:
      writer.addFeature(feat)

  del writer


As you can see, it looks like a regular script that uses the QGIS API, but it contain a set of lines at the beginning, with double hashtags. Those lines define the semantics of the algorithm, indicating which values (and their types) are required to run the algorithm, and what kind of output it produces. With that, Processing will be able to generate the correspodning graphical interfaces for interacting with the algorithm. Also, it will create the variables to contain the values selected by the user when executing the algorithm, which can later be used in the algorithm.

Let's analyze the code in detail.

.. code-block:: python

  ##Vector=group
  ##input=vector
  ##output=output vector

As explained above, this first lines define the variables that we use in the algorithm, and that the user will have to enter. With this information Processing can create the UI of the algorithm, with the corresponding selection boxes. 

In our case, we are declaring two parameters: ``input`` and ``output``. The first one is a vector layer (the user will be prompted to select one of the available ones), while the second one is an output vector layer (the user will be prompted to enter a path to select the resulting layer to). The first line (``##Vector=group``) does not declare any variable. Instead, it declares the group into which the algorithm will appear in the toolbox. This line has no effect on the UI of the algorithm, and will not cause a new variable to be created.

.. code-block:: python

  vectorLayer = processing.getObject(input)

Here we are using the ``input`` variable. You can see it is not defined before we reach this line, but Processing will have defined it with the input provided by the user.

For a vector layer, the value of the variable will be the path to the source of the layer selected by the user. That is of little use in our case, and we should work with the layer object instead, to be able to query it for its features. To convert the value of the ``input`` variable into a layer object, we use the ``getObject`` method from the processing class.

This class is imported by default, and contains useful functions commonly used in Processing algorithms. Since Processing is a Python plugin and is not part of the core C++ code of QGIS, these functions are not documented in the API. You will find most of them in the source python files `here <https://github.com/qgis/QGIS/tree/release-2_18/python/plugins/processing/tools>`_.

The ``getObject`` method will return in this case an object of class ``QgsVectorLayer``, which we already know (and which we can find in the QGIS API documentation).


.. code-block:: python

  writer = VectorWriter(output, None, vectorLayer.dataProvider().fields(),
                        vectorLayer.dataProvider().geometryType(), vectorLayer.crs())

Since the algorithm produces a new layer, we need to create it. We can do it using the QGIS core classes directly, but it is recommended to use the Processing helper methods and classes instead, because the output value selected by the user doesn't have to be a file path (it can be a database URI, for instance), and these classes can handle that.

In this case, we create a ``VectorWriter`` object. The constructor of these class requires passing the characteristics of the layer to create (fields, crs, geometry type), along with the output destination. For the first ones, we use the values directly taken from the input layer, since we want the output layer to be exactly like the input one. For the output destination, we use the value of the ``output`` variable.

We can now add features to the layer, using the ``addFeature`` method of the ``VectorWrite`` class.

.. code-block:: python

  features = processing.features(vectorLayer)
  for feat in features:
      writer.addFeature(feat)

  del writer

Finally, we have the actual algorithm body, that is, the code that perform the task that the algorithm is supposed to do. In this case, we just iterate through the 

As it happened before, we could iterate over the layer feature using the methods provided by the ``QgsVectorLayer`` class, but it's better to do it using the convenience methods provided by Processing. In this case, that will allow us to easily honor the Processing setting ``Use only selected features``, since the ``processing.features`` function will return an iterator that only returns the selected features in case that option is enabled. If using the ``QgsVectorLayer`` method, we would have to implement this behaviour ourselves in the algorithm.

We add each feature returned by the iterator to the ``VectorWriter`` object. Before finishing the algorithm, we delete the writer object.


Once you understand the code above, use it to create a new algorithm, and save it as explained at the beginning of this section. Your algorithm will be available in the Processing Toolbox, and you can open it to test it on the provided sample layer.

More detailed information about how to write Processing algorithms is found in the `corresponding section <https://docs.qgis.org/2.18/en/docs/user_manual/processing/scripts.html>`_ in the QGIS user manual.

When a set of scripts has been created, it can be packaged into a plugin that adds those scripts. That can be done from the Processing toolbox, as explained `here <https://docs.qgis.org/2.18/en/docs/pyqgis_developer_cookbook/processing.html#id2>`_

