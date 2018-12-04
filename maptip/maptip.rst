Maptips
=======

QGIS allows to show map tips when the mouse is hovered over a feature in the QGIS project canvas. The text to show in the map tip supports using expressions, which means that we can use Python code to create that text, giving us great flexibility.

We have already seen how to add an action that allows opening the Wikipedia page corresponding to each feature, selecting a menu from the attributes table. We will now adapt that idea and create a maptip that displays the summary of the Wikipedia page and show it in the QGIS window, without having to use the browser window.


The first thing to do is to enable maptips in the `View` menu.

      .. figure:: enable.png

To define the content of the maptip, open the layer properties and move to the `Display` tab.


      .. figure:: display.png


Select the `HTML` option and enter the following code in the text box:

```
<style>
p {width: 300px;}
</style>
<p>
[% wikipediaSummary("wikipedia") %]
</p>

```

You will see that the section in the paragraph is a QGIS expression, and that it calls a function called `wikipediaSummary`, passing it the value in the `wikipedia` field (the double quotes indicate the value of a field, and will be resolved to that value). We do not have such a method, but we can create it using the expression dialog, which you can open by clicking on the `Insert expression...` button.

The code for that function can be found in `this file <./maptip.txt>`_. Make sure you click on the `Load` button once you have defined it, as explained in a previous section.

Since the text in the maptip is likely to be large, we use some CSS code to ensure that the maptip is wide enough.

You can check that it works correctly by setting the `countries` layer as the active one, and hovering over any of its features.

	.. figure:: hovering.png