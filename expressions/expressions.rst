Expressions
===========

Expressions allow you to use values in QGIS parameters that are not fixed or hardcoded. For instance, you can set the label text to be displayed in the canvas for a given layer to a value that depends on multiple fields, combined according to an expression.

QGIS contains a comprehensive set of functions that can be used to define expressions. However, it also allows you to use Python to define new functions, and more complex calculations can be performed this way.

If you are not familiar with QGIS expressions, `here <https://docs.qgis.org/2.18/en/docs/user_manual/working_with_vector/expression.html>`_ you can find more detailed information.

In the section dedicated to our first examples on the console, we introduced a function to compute the hemisphere a feature was located in, which returned a letter as a result. We can turn that function into a new custom expression function, so it can be used anywhere where QGIS allow to use expressions.

Let's say we want to use that function to label the features in the ``countries``layer. First, open the layer properties and move to the section where labeling is defined.

      .. figure:: labeling.png

In the ``label with`` field, instead of selecting a field, click on the button on the right-hand side, to open the expressions dialog.
      
      .. figure:: expressionsdialog.png

We want to add our own Python function, so we should move to the ``Function editor`` tab.

      .. figure:: functioneditor.png

Click on the plus sign button to create a new file for our function code. Name the file ``hemisphere.py``. It will be added to the list of available expression files.

      .. figure:: addedfile.png

The file will be filled with a template function. Use the code below instead. The code in that file is fully commented, and should give you a good explanation about how python expression functions work.


.. code-block:: python

	'''It's recommended to leave the 'args' parameter with the 'auto' value.
	That will define the function syntax automatically, based on the function definition.
	The 'feature' and 'parent' parameters will always be passed and have to be declared.
	In the 'group' parameter, set the group that you want the function to belong to. 
	It will appear under that group in the list of available functions in the expressions dialog.
	'''
	@qgsfunction(args="auto", group="Custom", usesgeometry=True)
	def hemisphere(geom, feature, parent):
		'''Computes the hemisphere a features falls in. Coordinates are assumed to be geographic'''
		'''
		We get the bounding box of the geometry and see if it crosses the equator. 
		Based on the result, we return (N)orth, (S)outh or (B)oth
		'''
		box = geom.boundingBox()
		if box.yMinimum() > 0 and box.yMaximum() > 0:
			return "N"
		if box.yMinimum() <= 0 and box.yMaximum() <= 0:
			return "S"
		else:
			return "B"


Once that you have written the function code, click on the ``Load`` button to update the list of functions. Now move back and you will see that the 'hemisphere' functions is already available. Enter the following expression: ``hemisphere($geometry)``.

      .. figure:: finalexpression.png

Click on OK to close the expressions dialog. Close the labeling dialog and you should see your layer with the new labels indicating the hemisphere for each country.

      .. figure:: rendering.png

The hemisphere for each feature is computed each time the layer is rendered, at that can be time consuming. A better option would be to add a new field with the hemisphere value. We already did that in one of the first exercises in the console, but now we can do it in a much easier way, using the field calculator and our recently created expression.

Open the attributes table of the layer, and from there open the field calculator. The field calculator dialog contains an expression widget, where you can enter the same formula that we use for the labeling case.

      .. figure:: fieldcalc.png

Click on OK and the field will be added. You can now change the labeling configuration, to use that field instead of the expression.



