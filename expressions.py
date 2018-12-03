from qgis.core import *
from qgis.gui import *

@qgsfunction(args="auto", group="Custom", usesgeometry=True)
def hemisphere(geom):
	'''This expression is to be called passing the geometry of a given feature'''
	'''We get the bounding box of the geometry and see if it crosses the equator. Based on the result, we return (N)orth, (S)outh or (B)oth'''
	box = geom.boundingBox()
	if box.yMinimum() > 0 and box.yMaximum() > 0:
		return "N"
	if box.yMinimum() <= 0 and box.yMaximum() <= 0:
		return "S"
	else:
		return "B"
