import os
from .logger import log
import tomli
import yaml

# Creates the debug folder to save information
def createDebugFolder(debug:bool=False):
    if debug == True:
        log().info("starting program in debug mode")
        pathDir = os.path.dirname(os.path.realpath(__file__))
        listOfFolders = os.listdir(pathDir)
        debugFolder = os.path.join(pathDir, "debug")
        debugFile = os.path.join(debugFolder,'debug.log')
        resultFile = os.path.join(debugFolder,'result.yml')
        if 'debug' in listOfFolders:
            log().info(f"creating new debug.log file on {debugFolder}")
            file = open(debugFile, 'w+')
            file.close()
            log().info(f"creating new result.yml file on {debugFolder}")
            file = open(resultFile, 'w+')
            file.close()
        else:
            try:
                log().info(f"creating debug folder to store files at {debugFolder}")
                os.mkdir(debugFolder)
                file = open(debugFile, 'w+')
                file.close()
                file = open(resultFile, 'w+')
                file.close()
            except Exception as error:
                log().error(error)
    else:
        pass

# Confirms the appliance returned a 200 and not an error
def confirmReturn(func , dictionary:dict, debug:bool):
    if debug == True:
        try:
            if dictionary['status_code'] != 200:
                log().error({func : dictionary})
        except:
            pass
    else:
        pass

def writeResult(func, result, debug):
    if debug:
        pathDir = os.path.dirname(os.path.realpath(__file__))
        debugFolder = os.path.join(pathDir, "debug")
        resultFile = os.path.join(debugFolder,'result.yml')
    
        with open(resultFile, "a") as ymlFile:
            data = { func : result}
            yaml.dump(data, ymlFile)


# Wrapper to except errors
def errorHandler(func):
    def wrapper(*args):
        try:
            out = func(*args)
            result = True
        except Exception as error:
            log().error({func : error})
            out = error
            result = False
        return {func.__name__ : out,
                'result' : result}
    return wrapper


# Returns the function that needs to be called for a given feature
def checkCollector(feature,collectorMap):
    for f,s in collectorMap.items():
        for k in feature.keys():
            if f == k:
                return s

           
# Returns the NE_PK of the appliance base on the name
def getApplianceID(name,applianceDict:dict):
    try:
        applianceID = applianceDict.get(name)
    except Exception as error:
        log().error(f"error getting the appliance ID for {name}")
        log().error(error)
    return applianceID


# Reads the toml file to find out application version
#def getAppVersion():
#    pathDir = os.path.dirname(os.path.realpath("pyproject.toml"))
#    tomlFile = os.path.join(pathDir,'pyproject.toml')
#    with open(tomlFile, "rb") as f:
#        data = tomli.load(f)
#        return data['tool']['poetry']['version']