'''The following snippets can be entered line by line in the console.

Later on, the option to create a script file and run it from the console can be explained,
as it is more suitable for longer pieces of code.
'''

'1. Calculate the total population adding the population values of all countries in the countries layer'
layer = iface.activeLayer()
features = layer.getFeatures()
totalPopulation = 0
for feat in features: #we iterate over features in the layers
	pop = feat["pop_est"] #retrieve the population value using the feature as a dictionary.
	if pop > 0:
		totalPopulation += pop

print (totalPopulation)


'2. Calculate population for each continent'
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

'3. Add a new field indicating if the feature is in the (N)orthern hemisphere, (S)outhern or (B)oth'
from qgis.PyQt.QtCore import QVariant

#We define the function that computes the hemisphere for a given geometry
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
#We add the field and updated the layer for the change to take effect
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
