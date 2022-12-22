import argparse
from .logger import log

def parser():
    parser = argparse.ArgumentParser()
##############################################################################    
#                            Exporter CLI Inputs
##############################################################################
    parser.add_argument('-d', '--debug',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="debug the cli")
    parser.add_argument('-v', '--version',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="shows cli tool version")

    parser.add_argument('-p', '--port',
                                  required=False,
                                  type=int,
                                  nargs="?",
                                  help="port for prometheus exporter")
    parser.add_argument('-o', '--orch',
                                  required=False,
                                  nargs="?",
                                  help="Silverpeak orchestrator url")

    parser.add_argument('-k', '--key',
                                  required=False,
                                  nargs="?",
                                  help="Silverpeak orchestrator api key")
    parser.add_argument('-f', '--file-path',
                                  required=False,
                                  nargs="?",
                                  help="Configuration file path")
    parser.add_argument('-b', '--Break',
                                  required=False,
                                  #choices='ec',
                                  action='store_true',
                                  help="run once or infinite")

    options = parser.parse_args()    # This is the return of the function and what is passed to other functions
    outOptions = parser.parse_args() # This are the input that will be printed to the screen if debug flag is enable


    if (outOptions.debug == True):
        del outOptions.key
        log().info(outOptions)

    if (options.version == True):
        from importlib_metadata import version
        print(f'version...installed:',version('silverpeak-exporter'))

    return options
    