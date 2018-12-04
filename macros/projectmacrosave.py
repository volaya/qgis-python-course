from qgis.core import QgsProject
import shutil
from subprocess import call

REPO_FOLDER = "repo_folder"

'''
A project macro that, whenever the project is saved, it updates a copy 
of it in a git repository supposed to be used to store its history

The macro assumes that there is a project variable named REPO_FOLDER, 
which contains the path to the repository folder'''

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
		call("git commit -m 'updated QGIS project file'".split(" "))
		call("git push".split(" "))
