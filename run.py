import importlib.util
import os
import sys

from Helpers.common_shitz import start
#from distutils.dir_util import copy_tree
import shutil

# Commands:
YEAR = ['-y=','-year=']
DAY = ['-d=','-day=']

# Locationz
ROUTE_MAIN = "./{0}/Solutions/day{1}/main.py"
ROUTE_INPUT = "./{0}/Solutions/day{1}/input.data"

# Copy parameters
COPY_FROM = './TemplateToCopy/'
COPY_TO = "./{0}/Solutions/day{1}/"

STARTING_MESSAGE = "Starting Year: {0} Day: {1}"

def import_from_path(module_name: str, file_path: str):
    """import a module given its name and file path"""
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

def run():
    """rework this shit and make it better"""
    arguments = sys.argv[1:]

    year = str(next((x for x in arguments if x.startswith(YEAR[0]) or x.startswith(YEAR[1])), '')).replace(YEAR[0],'').replace(YEAR[1],'')
    day = next((x for x in arguments if x.startswith(DAY[0]) or x.startswith(DAY[1])), '').replace(DAY[0],'').replace(DAY[1],'')

    if year == '' or day == '':
        print('To run this garbage, add arguments "-y=XXXX" for year and "-d=XX" for days.')
        return
    
    if not os.path.isfile(ROUTE_MAIN.format(year,day)):
        print("Couldn't find Main.py for Year: {0} Day: {1}".format(year,day))
        print("Creating from template for Year: {0} Day: {1}".format(year,day))
        shutil.copytree(COPY_FROM, COPY_TO.format(year,day))

    module = import_from_path("main",ROUTE_MAIN.format(year,day))
    
    start(module.part1, module.part2, ROUTE_INPUT.format(year,day), STARTING_MESSAGE.format(year,day))

run()