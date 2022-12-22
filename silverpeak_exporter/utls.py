import os
from .logger import log

def createDebugFolder(debug:bool=False):
    if debug == True:
        log().info("starting program in debug mode")
        pathDir = os.path.dirname(os.path.realpath(__file__))
        listOfFolders = os.listdir(pathDir)
        debugFolder = os.path.join(pathDir, "debug")
        debugFile = os.path.join(debugFolder,'debug.log')
        if 'debug' in listOfFolders:
            log().info(f"creating new debug.txt file on {debugFolder}")
            file = open(debugFile, 'w+')
            file.close()
        else:
            try:
                log().info(f"creating debug folder to store files at {debugFolder}")
                os.mkdir(debugFolder)
                file = open(debugFile, 'w+')
                file.close()
            except Exception as error:
                log().error(error)
    else:
        pass


def confirmReturn(func , dictionary:dict, debug:bool):
    if debug == True:
        try:
            if dictionary['status_code'] != 200:
                log().error({func : dictionary})
        except:
            pass
    else:
        pass

def errorHandler(func):
    def wrapper(*args):
        try:
            out = func(*args)
        except Exception as error:
            log().error({func : error})
        return {func : out}
    return wrapper
