from qgis.core import *
from qgis.gui import *

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
