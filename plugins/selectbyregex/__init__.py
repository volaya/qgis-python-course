from selectbyregex.plugin import RegexPlugin

'''
This method has to be in the __init__.py file, and return
an object of the class that contains the main plugin body.
'''
def classFactory(iface):
    return RegexPlugin(iface)

