import yaml
import os
from .logger import log,logToFile
from .args import parser
from .utls import createDebugFolder

def readConfig(filePath):
    with open(filePath, "r") as stream:
        try:
            ymlVars = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            log().error(exc)
    return ymlVars


class settings():
    @staticmethod
    def getEnvironmentVar(key,debug):
        try:
            out = os.environ[key]
            if len(out) == 0:
                out = False
        except KeyError as error:
            out = False
# Only turn this on when you want to debug on the container
#        log().debug({"environment": key, "value" : out})
        logToFile().debug(message={"environment": key, "value" : out},debug=debug)
        return out

    def __init__(self):
        self.userInput = parser()
# If the debug flag is passed then this function will create the folder and file to write the debug messages
        createDebugFolder(self.userInput.debug)

        checkENV = settings.getEnvironmentVar('SP_FILE_PATH',self.userInput.debug)
        if checkENV == False:
            filepath = self.userInput.file_path
        else:
            filepath = checkENV
        
        jsonConfigs = readConfig(filepath)
        self.config = jsonConfigs




    def debug(self):
        out = {}

        try:
            checkENV = settings.getEnvironmentVar('SP_DEBUG',self.userInput.debug)
            if checkENV == False:
               out.update({"debug" :self.userInput.debug})
            else:
                out.update({"debug" : checkENV})

        except Exception as error:
         #   log().error(error)
            out.update({"debug" : False})

        return out



    def Break(self):
        out = {}

        try:
            checkENV = settings.getEnvironmentVar('SP_BREAK',self.userInput.debug)
            if checkENV == False:
                out.update({"Break" :self.userInput.Break})
            else:
                out.update({"Break" : checkENV})

        except Exception as error:
         #   log().error(error)
            out.update({"Break" : False})

        return out

    def port(self):
        out = {}

        try:
            checkENV = settings.getEnvironmentVar('SP_PORT',self.userInput.debug)
            if checkENV == False:
                out.update({"port" : self.config['config']['exporter']['port']})
            else:
                checkENV = int(checkENV)
                out.update({"port" : checkENV})

        except Exception as error:
         #   log().error(error)
            out.update({"port" :self.userInput.port})

        return out

    def orch(self):
        out = {}
        try:
            checkENV = settings.getEnvironmentVar('SP_ORCH_URL',self.userInput.debug)
            if checkENV == False:
                out.update({"url" : self.config['config']['silverpeak']['orch']})
            else:
                out.update({"url" : checkENV})
        except Exception as error:
            #log().error(error)
            out.update({"url": self.userInput.orch }) 
        try:
            checkENV = settings.getEnvironmentVar('SP_ORCH_KEY', False)
            if checkENV == False:
                out.update({"key": self.userInput.key})
            else:
                out.update({"key": checkENV})
        except Exception as error:
            #log().error(error)
            out.update({"key": self.userInput.key})
        try:
            checkENV = settings.getEnvironmentVar('SP_ORCH_SSL',self.userInput.debug)
            if checkENV == False:
                out.update({"verify_ssl" : self.config['config']['silverpeak']['verify_ssl']})
            else:
                checkENV = bool(checkENV)
                out.update({"verify_ssl" : checkENV})
        except Exception as error:
            #log().error(error)
            out.update({"verify_ssl" : False})

        return out
    
    def metricsOrchestrator(self):
        out = {}
        try:
            out.update({"collect" : self.config['orchestrator']['collect']})
        except Exception as error:
         #   log().error(error)
            out.update({"collect" : False})
        try:
            out.update({"interval" : self.config['orchestrator']['interval']})
        except Exception as error:
         #   log().error(error)
            out.update({"interval" : 60})

        return out