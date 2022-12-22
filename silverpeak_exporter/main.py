import threading
from prometheus_client import start_http_server
from .logger import log
from .file import settings
from .collectors import collectOrchestratorMetrics

def main():
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
    else:
        log().info(f'skipping orchestrator metric collection')    


if __name__ == '__main__':
    main()