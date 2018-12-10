Processing algorithms
=======================

You can create your own Processing algorithms by writing the corresponding Python code and
adding a few extra lines to supply additional information needed to define the
semantics of the algorithm.

Processing algorithms are the preferred way of adding new analytical functionality to QGIS, since they will be available in all the Processing components, such as the Toolbox, the Graphical Modeler or the Batch Processing Interface

The best way of creating a Processing algorithm is to use a template. That can be done by calling the ``Create new script from template`` menu.

    .. figure:: createtemplate.png

The template is fully commented, and should be enough to guide you.

