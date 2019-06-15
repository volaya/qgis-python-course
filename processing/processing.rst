Processing algorithms
=======================

You can create your own Processing algorithms by writing the corresponding Python code and
adding a few extra lines to supply additional information needed to define the
semantics of the algorithm.

Processing algorithms are the preferred way of adding new analytical functionality to QGIS, since they will be available in all the Processing components, such as the Toolbox, the Graphical Modeler or the Batch Processing Interface

The best way of creating a Processing algorithm is to use a template. That can be done by calling the ``Create new script from template`` menu.

    .. figure:: createtemplate.png

The template is fully commented, and the comments should be enough to understand what each method does. 

Here's some explanation about this algorithm. Comments have been removed for the sake of space.

First, let's add the imports for the QGIS classes that we will be using.

.. code-block:: python

from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsField, QgsFeature, QgsFeatureSink, QgsFeatureRequest, QgsProcessing, QgsProcessingAlgorithm, QgsProcessingParameterFeatureSource, QgsProcessingParameterFeatureSink)
    
The code can now be divided into three main blocks:

The first one adds the elements that provide the algorithm's metadata (name, group it belongs to, etc) 

.. code-block:: python

  class SaveSelectedFeaturesAlgorithm(QgsProcessingAlgorithm):

      def __init__(self):
          super().__init__()
   
      def name(self):
          return "saveselectedfeatures"
       
      def tr(self, text):
          return QCoreApplication.translate("saveselectedfeatures", text)
           
      def displayName(self):
          return self.tr("Save selected features")
   
      def group(self):
          return self.tr("Vector tools")
   
      def groupId(self):
          return "vectortools"
   
      def shortHelpString(self):
          return self.tr("Saves the selected features")
   
      def helpUrl(self):
          return "https://qgis.org"
           
      def createInstance(self):
          return type(self)()
   
Check the comments in the template to get a detailed description of each of these methods.

A second block adds the semantics of the algorithm (inputs and outputs, and their corresponding types).

.. code-block:: python

  INPUT = 'INPUT'
  OUTPUT = 'OUTPUT'
   
  def initAlgorithm(self, config=None):
      self.addParameter(QgsProcessingParameterFeatureSource(
          self.INPUT,
          self.tr("Input layer"),
          [QgsProcessing.TypeVectorAnyGeometry]))
      self.addParameter(QgsProcessingParameterFeatureSink(
          self.OUTPUT,
          self.tr("Output layer"),
          QgsProcessing.TypeVectorAnyGeometry))

We add here an input vector layer of any geometry type, and then an output vector layer. That is enough for Processing for creating the corresponding UI to prompt the user to select the input layer and enter the path to the ouput one.

We are defining the names of this parameters as constants within the class (``self.INPUT, self.OUTPUT``), so they can be easily used in case we want to call this algorithm from the Python console or from another Python Processing algorithm.

And finally, we have the body of the algorithm itself, where the actual work of the algorithm is done.

.. code-block:: python

    def processAlgorithm(self, parameters, context, feedback):
        source = self.parameterAsSource(parameters, self.INPUT, context)
        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT, context,
                                               source.fields(), source.wkbType(), source.sourceCrs())
 
        features = source.getFeatures(QgsFeatureRequest())
        for feat in features:
            out_feat = QgsFeature()
            out_feat.setGeometry(feat.geometry())
            out_feat.setAttributes(feat.attributes())
            sink.addFeature(out_feat, QgsFeatureSink.FastInsert)
 
        return {self.OUTPUT: dest_id}

Here, we retrieve the values of the parameters selected by the user, using the methods ``parameterAsSource`` and ``parameterAsSink`` from the ``QgisAlgorithm`` class that our algorithm is based on. Other similar methods exist, and depending on the type of the parameter, we should use one or other of them.

Once we have that, we just iterate over the features of the input layer (the iterator will just give us the selected features, and add them to the output one.

Finally, we return the output values, so they can be used in a different algorithm, thus allowing connecting several of them in a script.

Processing algorithms using decorators
--------------------------------------

As you can see, even for a small algorithm such as this one, we must write a large amount of code. It's possible to reduce it by using decorators to define the metadata and semantics of the algorithm. We would just write the main function where the algorithm is executed (that is, the ``processAlgorithm``function), and use decorators to define the rest.

Here's how the above algorithm would look using this approach.

.. code-block:: python

    from qgis.processing import alg
    from qgis.core import QgsFeatureSink

    @alg("saveselectedfeature", "Save selected features", group="vectortools", group_label="Vector tools")
    @alg.input(type=alg.SOURCE, name="INPUT", label="Input layer")
    @alg.input(type=alg.SINK, name="OUTPUT", label="Output layer")
    def save_selected(instance, parameters, context, feedback):
        ''
        source = instance.parameterAsSource(parameters, "INPUT", context)
        (sink, dest_id) = instance.parameterAsSink(parameters, "OUTPUT", context,
                                               source.fields(), source.wkbType(), source.sourceCrs())

        features = source.getFeatures(QgsFeatureRequest())
        for feat in features:
            out_feat = QgsFeature()
            out_feat.setGeometry(feat.geometry())
            out_feat.setAttributes(feat.attributes())
            sink.addFeature(out_feat, QgsFeatureSink.FastInsert)

        return {instance.OUTPUT: dest_id}

As you can see, there is no need to create a class here, but just the main function, decorated using the corresponding decorators.

The function must have four parameters, just as the ``processAlgorithm`` method if using the full syntax without decorators. The first one is an instance of the algorithm object, so we replace all the ``self`` calls in the method with that ``instance`` parameter.

There is no need to maintain the ``processAlgorithm`` name for the function, since the decorator will take of handling that correctly.

For inputs and outputs, a ``name`` parameter has to be defined (the internal name to be used to refer to the parameter), and also a ``label`` one (the human-readable name to identify the parameter in the UI).

The ``type`` can be a Python built-in type (str, int, float...) or one of the types defined in the ``ProcessingAlgFactory`` class. You can find the allowed values for outputs `here <https://github.com/qgis/QGIS/blob/master/python/processing/algfactory.py#L366>`_ and the ones for inputs `here <https://github.com/qgis/QGIS/blob/master/python/processing/algfactory.py#L413>`_


In the next section, we will see how to create a plugin to select using a regular expression. Here is a similar idea, implemented as a Processing algorithm using decorators



.. code-block:: python
    
    from qgis.processing import alg
    from qgis.core import QgsFeatureSink
    import re
    
    @alg(name="extractbyregex", label="Extract by Regex", group="Tutorial scripts", group_label="tutorialscripts")
    @alg.input(type=alg.VECTOR_LAYER, name="INPUT", label="Input")
    @alg.input(type=alg.FIELD, name="FIELD", label="Field", parentLayerParameterName="INPUT") 
    @alg.input(type=alg.STRING, name="REGEX", label="Regex")
    @alg.input(type=alg.SINK, name="OUTPUT", label="Output")
    def extractbyregex(instance, params, context, feedback, inputs):
      ''
      source = instance.parameterAsSource(params, "INPUT", context)
      (sink, destId) = instance.parameterAsSink(params, "OUTPUT", context, source.fields(), 
                                            source.wkbType(), source.sourceCrs())
      regex = instance.parameterAsString(params, "REGEX", context)
      field = instance.parameterAsString(params, "FIELD", context)
      exp = re.compile(regex)

      features = source.getFeatures()
      for feature in features:            
        if exp.search(feature[field]):  
          sink.addFeature(feature, QgsFeatureSink.FastInsert)

      return {"OUTPUT": destId}
