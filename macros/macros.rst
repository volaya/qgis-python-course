Project macros
===============

QGIS allows you to define custm behaviours as a response to certain events.

For instance, when a project is opened, closed or saved, you can define a project macro using python code.

We will see two examples in this section.

To define project macros, go to your project properties dialog and move to the ``Macros`` section.

      .. figure:: macrosdialog.png

Enable macros by clicking on the checkbox at the top of the dialog.

Now you can define your macros filling the body of the three functions that you see in the text box.

We will start with a simple one, which shows a warning when the project is open.

::

	from qgis.utils import iface
	from qgis.core import Qgis

	' A simple project macro to show a warning message when the project is open.'
	def openProject():
		iface.messageBar().pushMessage(
			"Warning",
			"This project contains classified data. Don't distribute it",
			Qgis.Warning,
			10
		)


Here, we are just using the QGIS message bar to show the message. Each time the project is used, the user will see that warning.

We can add a more complex macro, as shown in the next example, for the project close operation.

::

	from qgis.core import QgsProject
	import shutil
	from subprocess import call

	REPO_FOLDER = "repo_folder"

	def saveProject():
		projFile = QgsProject.instance().fileName()
		scope = QgsExpressionContextUtils.projectScope()
		if not scope.hasVariable(REPO_FOLDER):
				return
			call("git pull".split(" ")) #Git is assumed to be installed in your system
			
			repoFolder = scope.variable(REPO_FOLDER):
			destFile = os.path.join(repoFolder, os.path.basename(projFile))
			shutil.copyfile(projFile, destFile)

			call("git add .".split(" "))
			call("git commit -m 'Updated QGIS project file'".split(" "))
			call("git push".split(" "))


This project macro updates a copy of the project a git repository supposed to be used to store its history.

The macro assumes that there is a project variable named ``repo_folder`` which contains the path to the repository folder.

