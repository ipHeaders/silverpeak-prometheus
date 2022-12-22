import inspect
from pyedgeconnect import Orchestrator
from prometheus_client import Info,Gauge
from time import sleep as wait
from .logger import log,logToFile
from .utls import confirmReturn,errorHandler
from .metrics import *


class collectOrchestratorMetrics():
    def __init__(self,url,key,verify_ssl,interval,debug, Break):
        self.url = url
        self.key = key
        self.verify_ssl = verify_ssl
        self.interval = interval
        self.debug = debug
        self.Break = Break
        self.orch = Orchestrator(url=self.url, verify_ssl=self.verify_ssl, api_key=self.key , log_console=self.debug)
        self.hostname = self.orch.get_orchestrator_hostname()['gms_hostname']
        while True:
            # get a list of all the methods in this class
            # loops over the list starting at index 1 to bypass __init__
            # calls the method
            methodList = inspect.getmembers(self, predicate=inspect.ismethod)
            for m in range(1, len(methodList)):
                i = methodList[m][1]()

                logToFile().debug(message=dict({methodList[m][1].__name__ : i}), debug=self.debug) 
                confirmReturn(func=methodList[m][1].__name__ ,dictionary=i, debug=self.debug) 

            if self.Break == False:
                wait(self.interval)
            else:
                break

    @errorHandler
    def _getOrchServerBrief(self):
       orch_return = self.orch.get_orchestrator_server_info()   
       uptime.labels(orchName=self.hostname).info({'uptime' : orch_return['uptime']}) #Setting Metric
       release.labels(orchName=self.hostname).info({'release' : orch_return['release']}) #Setting Metric
       platform.labels(orchName=self.hostname).info({'platform' : orch_return['platform']}) #Setting Metric
       numActiveUsers.labels(orchName=self.hostname).set(orch_return['numActiveUsers']) #Setting Metric
       return orch_return

    @errorHandler
    def _getAlarmCountOrchestratoAndAppliances(self):
        orch_return = self.orch.get_alarm_count_orchestrator_and_appliances() 
        for key,value in orch_return.items():
            activeAlarms.labels(orchName=self.hostname,severity=key).set(value) #Setting Metric
        return orch_return                

    @errorHandler
    def _getTotalAppliances(self):
        orch_return = self.orch.get_appliances() 
        totalAppliances.labels(orchName=self.hostname).set(len(orch_return)) #Setting Metric
        return orch_return


    @errorHandler
    def _getLicenseState(self):
        orch_return = self.orch.get_portal_licensed_summary() 
        licenseState = orch_return['licenseState']['fx']
        
        licenseNumMini.labels(orchName=self.hostname).set(licenseState['numMini']) #Setting Metric
        licenseNumBase.labels(orchName=self.hostname).set(licenseState['numBase']) #Setting Metric
        licenseNumBoost.labels(orchName=self.hostname).set(licenseState['numBoost']) #Setting Metric
        licenseNumPlus.labels(orchName=self.hostname).set(licenseState['numPlus']) #Setting Metric
        numTier = {
            "20000" : licenseNumTier20M,
            "50000" : licenseNumTier50M,
            "100000" : licenseNumTier100M,
            "200000" : licenseNumTier200M,
            "500000" : licenseNumTier500M,
            "1000000" : licenseNumTier1G,
            "2000000" : licenseNumTier2G,
            "1000000000" : licenseNumTierUM,
        }
        for key,value in numTier.items():
            if key in licenseState['numTier']:
                value.labels(orchName=self.hostname).set(licenseState['numTier'][key]) #Setting Metric
            else:
                value.labels(orchName=self.hostname).set(0) #Setting Metric
        return orch_return

    @errorHandler
    def _getTotalOverlays(self):
        orch_return = self.orch.get_all_overlays_config() 
        totalOverlays.labels(orchName=self.hostname).set(len(orch_return)) #Setting Metric
        return orch_return

    @errorHandler
    def _getTotalRegions(self):
        orch_return = self.orch.get_all_regions() 
        totalRegions.labels(orchName=self.hostname).set(len(orch_return)) #Setting Metric
        return orch_return

    @errorHandler
    def _getTotalSaasApps(self):
        orch_return = self.orch.get_all_saas_apps() 
        totalSaasApps.labels(orchName=self.hostname).set(len(orch_return)) #Setting Metric
        return orch_return

    @errorHandler
    def _getTotalAppDefinition(self):
        orch_return = self.orch.get_app_definition_total() 
        totalAppDefinition.labels(orchName=self.hostname).set(orch_return) #Setting Metric
        return orch_return

    @errorHandler
    def _getTotalOrchSaasApps(self):
        orch_return = self.orch.get_count_of_saas_apps() 
        totalOrchSaasApps.labels(orchName=self.hostname).set(orch_return['count']) #Setting Metric
        return orch_return

    @errorHandler
    def _getOrchPortalStatus(self):
        orch_return = self.orch.get_orchestrator_to_cloud_portal_status()
        mapping = {
            0 : 'unable to connect',
            1 : 'connected',
            2 : 'connecting'
        }
        orchPortalStatus.labels(orchName=self.hostname).state(mapping[orch_return['portal']]) #Setting Metric
        return orch_return
            
    @errorHandler
    def _getCloudPortalServices(self):
        orch_return = self.orch.get_portal_services_status() 
        for key,value in orch_return.items():
            cloudPortalServices.labels(orchName=self.hostname,portalService=key, status='ok').set(orch_return[key]['state']['ok'])
            cloudPortalServices.labels(orchName=self.hostname,portalService=key, status='fail').set(orch_return[key]['state']['fail'])

        return orch_return

    @errorHandler
    def _test(self):
        orch_return = self.orch.get_portal_services_status() 
        return orch_return
