import threading
from prometheus_client import start_http_server
from .logger import log
from .file import settings
from .utls import getApplianceID
from .collectors import collectOrchestratorMetrics,getAllAppliances,applianceCollector,collectApplicationMetrics
from time import sleep as s


def main():
# Loads the application version and logs it
#    appVersion = getAppVersion()
#    log().info(f'starting application on version exporter {appVersion}')
# Loading user inputs via CLI
    fileConfig = settings()
# Setting common used varaibles
    prometheusPort = fileConfig.port()['port']
    orchConfig = fileConfig.orch()
    silverpeakUrl = orchConfig["url"]
    silverpeakKey = orchConfig['key']
    silverpeakSSL = orchConfig['verify_ssl']
    metricsOrchestratorInterval = fileConfig.metricsOrchestrator()['interval']
    debug = fileConfig.debug()['debug']
    Break = fileConfig.Break()['Break']

# Start up the server to expose the metrics.
    start_http_server(prometheusPort)
    log().info(f'starting prometheus exporter on {prometheusPort}')
# Start the thread to collect application metrics.
    t = threading.Thread(target=collectApplicationMetrics, args=(
            debug,
            Break,
        ))
    log().info('starting collection of application metrics')
    t.start()   

    

# Triggering the thread that will collect orchestrator metrics
    if fileConfig.metricsOrchestrator()['collect']:
        log().info(f'starting orchestrator metric collection on {silverpeakUrl}')
        log().info(f'starting orchestrator metric collection every {metricsOrchestratorInterval} seconds ')
        x = threading.Thread(target=collectOrchestratorMetrics, args=(
            silverpeakUrl,
            silverpeakKey,
            silverpeakSSL,
            metricsOrchestratorInterval,
            debug,
            Break,
        ))
        x.start()   
        s(2)     
    else:
        log().info(f'skipping orchestrator metric collection')    

# Triggering the thread that will collect appliance metrics
    if fileConfig.metricsAppliance()['appliances'] != False:
        appliances = getAllAppliances(silverpeakUrl,silverpeakSSL,silverpeakKey)
    
        for key in fileConfig.metricsAppliance()['appliances'].keys():
            applianceName = key
            applianceID = getApplianceID(name=applianceName,applianceDict=appliances)
    
            for feature in fileConfig.metricsAppliance()['appliances'][key]:
                z = threading.Thread(target=applianceCollector, kwargs={
                    'feature' : feature,
                    'url' : silverpeakUrl,
                    'ne_pk' : applianceID,
                    'applianceName' : applianceName,
                    'key' : silverpeakKey,
                    'verify_ssl' : silverpeakSSL,
                    'debug' : debug,
                    'Break' : Break,
                })
                z.start()
            s(2)
    else:
        log().info(f'skipping appliance metric collection')    


if __name__ == '__main__':
    main()