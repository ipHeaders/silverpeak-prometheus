
import logging
import os


class log():
    # create logger
    logger = logging.getLogger('silverpeak-prometheus')
    logger.setLevel(logging.DEBUG)
    
    # create console handler and set level to debug
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    
    # create formatter
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # add formatter to ch
    ch.setFormatter(formatter)
    
    # add ch to logger
    logger.addHandler(ch)

    def __init__(self):
        pass
    def debug(self,message):
        self.logger.debug(message)
    def info(self,message):
        self.logger.info(message)
    def error(self,message):
        self.logger.error(message)


class logToFile():
    # Setting directory for debug files
    pathDir = os.path.dirname(os.path.realpath(__file__))
    debugFile = os.path.join(pathDir, "debug/debug.log")

    def __init__(self):
        pass

    def debug(self,message,debug=False):
        if debug == True:
             logging.basicConfig(filename=self.debugFile, 
             encoding='utf-8', 
             format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
             level=logging.DEBUG)
             logging.debug(message)
