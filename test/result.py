#!/usr/bin/env python3
import os
import yaml
import logging
import sys

class log():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    CHANGE = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    # create logger
    logger = logging.getLogger('automated-test')
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
        self.logger.debug(self.OKBLUE + message + self.ENDC)
    def info(self,message):
        self.logger.debug(self.OKGREEN + message + self.ENDC)
    def error(self,message):
        self.logger.debug(self.FAIL + message + self.ENDC)

pathDir = os.path.dirname(os.path.realpath("README.md"))
resultFile = os.path.join(pathDir,'silverpeak_exporter/debug/result.yml')

def readFile(filePath):
    with open(filePath, "r") as stream:
        f = stream.read().split("\n")
        return f

result = readFile(resultFile)
for i in result:
    log().debug(i)


finalResult = []
for i in result:
    k = i.split(" ")
    try:
        if k[1] == 'false':
            finalResult.append(1)
        elif k[1] == 'False':
            finalResult.append(1)
        else:
            finalResult.append(0)
    except IndexError as error:
        pass

if 1 in finalResult:
    log().error("errors in some of the api calls")
    sys.exit(1)
else:
    log().info("all api calls completed successfully")