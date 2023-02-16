import inspect
from pyedgeconnect import Orchestrator
from time import sleep as wait
from .logger import log,logToFile
from .utls import confirmReturn,errorHandler,writeResult
from .metrics import *
import threading

#--------------------------------------------------#
# Application Metrics Collections
#--------------------------------------------------#

class collectApplicationMetrics():
    def __init__(self,debug, Break):
        self.debug = debug
        self.Break = Break
        while True:
            # get a list of all the methods in this class
            # loops over the list starting at index 1 to bypass __init__
            # calls the method
            methodList = inspect.getmembers(self, predicate=inspect.ismethod)
            for m in range(1, len(methodList)):
                i = methodList[m][1]()

                logToFile().debug(message=dict({methodList[m][1].__name__ : i}), debug=self.debug) 
                confirmReturn(func=methodList[m][1].__name__ ,dictionary=i, debug=self.debug) 
                writeResult(func=list(i.keys())[0], result=i['result'], debug=self.debug)
            if self.Break == False:
                wait(60)
            else:
                break


    @errorHandler
    def _getactiveThreads(self):
        activeThread = threading.active_count()
        sysOut = {"activeThreads" : activeThread}
        activeThreads.set(activeThread)
        return sysOut
       

#--------------------------------------------------#
# Metrics Collections for the Orchestrator
#--------------------------------------------------#
class collectOrchestratorMetrics():
    def __init__(self,url,key,verify_ssl,interval,debug, Break):
        self.url = url
        self.key = key
        self.verify_ssl = verify_ssl
        self.interval = interval
        self.debug = debug
        self.Break = Break
        self.orch = Orchestrator(url=self.url, verify_ssl=self.verify_ssl, api_key=self.key )
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
                writeResult(func=list(i.keys())[0], result=i['result'], debug=self.debug)
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
    def _getTotalTunnelCount(self):
        orch_return = self.orch.get_total_tunnel_count()
        totalTunnelCount.labels(orchName=self.hostname).set(orch_return['totalTunnelCount'])
        return orch_return

#--------------------------------------------------#
# Metrics Collections for the Appliances
#--------------------------------------------------#

def applianceCollector(**kwargs):
    applianceName = kwargs['applianceName']
    ne_pk = kwargs['ne_pk']
    interval = kwargs['feature']['interval']

    if 'system' in kwargs['feature']:
        try:
            log().info(f'starting system metric collection on {applianceName,ne_pk} every {interval} seconds')

            collectApplianceSystem(
            url = kwargs['url'],
            ne_pk = ne_pk,
            applianceName = applianceName,
            key = kwargs['key'],
            verify_ssl = kwargs['verify_ssl'],
            interval = interval,
            debug = kwargs['debug'],
            Break = kwargs['Break'],
            )
        except Exception as error:
            log().error(f'failed to set argument {error}')

    if 'bgp' in kwargs['feature']:
        try:
            log().info(f'starting bgp metric collection on {applianceName,ne_pk} every {interval} seconds')

            collectApplianceBGP(
            url = kwargs['url'],
            ne_pk = ne_pk,
            applianceName = applianceName,
            key = kwargs['key'],
            verify_ssl = kwargs['verify_ssl'],
            interval = interval,
            debug = kwargs['debug'],
            Break = kwargs['Break'],
            )
        except Exception as error:
            log().error(f'failed to set argument {error}')

    if 'flows' in kwargs['feature']:
        try:
            log().info(f'starting flows metric collection on {applianceName,ne_pk} every {interval} seconds')

            collectApplianceFlows(
            url = kwargs['url'],
            ne_pk = ne_pk,
            applianceName = applianceName,
            key = kwargs['key'],
            verify_ssl = kwargs['verify_ssl'],
            interval = interval,
            debug = kwargs['debug'],
            Break = kwargs['Break'],
            )
        except Exception as error:
            log().error(f'failed to set argument {error}')

def getAllAppliances(url,verify_ssl,api_key):
    try:
        #
        log().info('getting appliances NE_PK')
        sp_dict = {}
        orch = Orchestrator(url=url, verify_ssl=verify_ssl, api_key=api_key)
        orch_return = orch.get_appliances()
        for device in orch_return:
            sp_dict.update({device['hostName']: device['id']})
    except Exception as error:
        log().error(f'failed to get appliances NE_PK {error}')

    return sp_dict



class collectApplianceSystem():
    def __init__(self,url,ne_pk,applianceName,key,verify_ssl,interval,debug, Break):
        self.url = url
        self.ne_pk = ne_pk
        self.applianceName = applianceName
        self.key = key
        self.verify_ssl = verify_ssl
        self.interval = interval
        self.debug = debug
        self.Break = Break
        self.orch = Orchestrator(url=self.url, verify_ssl=self.verify_ssl, api_key=self.key )
        while True:
            # get a list of all the methods in this class
            # loops over the list starting at index 1 to bypass __init__
            # calls the method
            methodList = inspect.getmembers(self, predicate=inspect.ismethod)
            for m in range(1, len(methodList)):
                i = methodList[m][1]()
                logToFile().debug(message=dict({methodList[m][1].__name__ : i}), debug=self.debug) 
                confirmReturn(func=methodList[m][1].__name__ ,dictionary=i, debug=self.debug)
                writeResult(func=list(i.keys())[0], result=i['result'], debug=self.debug)
            if self.Break == False:
                wait(self.interval)
            else:
                break

    @errorHandler
    def _getApplianceAlarms(self):
        path = '/alarm'
        orch_return = self.orch.appliance_get_api(self.ne_pk, path) 
        for key,value in orch_return['summary'].items():
            applianceAlarm.labels(applianceName=self.applianceName,severity=key).set(value)
        return orch_return

    @errorHandler
    def _getApplianceCPU(self):
        path = '/cpustat'
        orch_return = self.orch.appliance_get_api(self.ne_pk, path) 
        latestTime = orch_return['latestTimestamp']
        lastStats = orch_return['data'][-1]
        cpuStats = lastStats[str(latestTime)]

        for cpu in cpuStats:
            cpu_name = cpu['cpu_number']
            del cpu['cpu_number']
            for k,v in cpu.items():
                applianceCPU.labels(applianceName=self.applianceName,cpu_core=cpu_name,metric=k).set(v)

        return orch_return

    @errorHandler
    def _getApplianceDiskUsage(self):
        path = '/diskUsage'
        orch_return = self.orch.appliance_get_api(self.ne_pk, path) 
        for k,v in orch_return.items():
            mount = k
            del v['filesystem']
            for a,b in v.items():
                applianceDiskUsage.labels(applianceName=self.applianceName,mount=mount,metric=a).set(b)
        return orch_return

    @errorHandler
    def _getApplianceRebootRequiered(self):
        path = '/license/isRebootRequired'
        orch_return = self.orch.appliance_get_api(self.ne_pk, path)
        applianceRebootRequiered.labels(applianceName=self.applianceName).state(str(orch_return['isRebootRequired'])) #Setting Metric
        return orch_return

    @errorHandler
    def _getApplianceMemory(self):
        path = '/memory'
        orch_return = self.orch.appliance_get_api(self.ne_pk, path)
        for k,v in orch_return.items():
            applianceMemory.labels(applianceName=self.applianceName,metric=k).set(v)
        return orch_return

    @errorHandler
    def _getApplianceSystemInfo(self):
        path = '/systemInfo'
        orch_return = self.orch.appliance_get_api(self.ne_pk, path)
        try:
            applianceHostname.labels(applianceName=self.applianceName).info({'hostName' : orch_return['hostName']}) #Setting Metric
        except:
            applianceHostname.labels(applianceName=self.applianceName).info({'hostName' : 'null'}) #Setting Metric
        try:
            applianceModel.labels(applianceName=self.applianceName).info({'modelShort' : orch_return['modelShort']}) #Setting Metric
        except:
            applianceModel.labels(applianceName=self.applianceName).info({'modelShort' : 'null'}) #Setting Metric
        try:
            appliancePlatform.labels(applianceName=self.applianceName).info({'platform' : orch_return['platform']}) #Setting Metric
        except:
            appliancePlatform.labels(applianceName=self.applianceName).info({'platform' : 'null'}) #Setting Metric
        try:
            applianceUptime.labels(applianceName=self.applianceName).set(orch_return['uptime']) #Setting Metric
        except:
            applianceUptime.labels(applianceName=self.applianceName).set(0) #Setting Metric
        try:
            applianceUptimeString.labels(applianceName=self.applianceName).info({'uptimeString' : orch_return['uptimeString']}) #Setting Metric
        except:
            applianceUptimeString.labels(applianceName=self.applianceName).info({'uptimeString' : 'null'}) #Setting Metric
        try:
            applianceRelease.labels(applianceName=self.applianceName).info({'release' : orch_return['release']}) #Setting Metric
        except:
            applianceRelease.labels(applianceName=self.applianceName).info({'release' : 'null'}) #Setting Metric
        try:
            applianceDeploymentMode.labels(applianceName=self.applianceName).info({'deploymentMode' : orch_return['deploymentMode']}) #Setting Metric
        except:
            applianceDeploymentMode.labels(applianceName=self.applianceName).info({'deploymentMode' : 'null'}) #Setting Metric
            
        return orch_return

class collectApplianceBGP():
    def __init__(self,url,ne_pk,applianceName,key,verify_ssl,interval,debug, Break):
        self.url = url
        self.ne_pk = ne_pk
        self.applianceName = applianceName
        self.key = key
        self.verify_ssl = verify_ssl
        self.interval = interval
        self.debug = debug
        self.Break = Break
        self.orch = Orchestrator(url=self.url, verify_ssl=self.verify_ssl, api_key=self.key )
        while True:
            # get a list of all the methods in this class
            # loops over the list starting at index 1 to bypass __init__
            # calls the method
            methodList = inspect.getmembers(self, predicate=inspect.ismethod)
            for m in range(1, len(methodList)):
                i = methodList[m][1]()

                logToFile().debug(message=dict({methodList[m][1].__name__ : i}), debug=self.debug) 
                confirmReturn(func=methodList[m][1].__name__ ,dictionary=i, debug=self.debug) 
                writeResult(func=list(i.keys())[0], result=i['result'], debug=self.debug)
            if self.Break == False:
                wait(self.interval)
            else:
                break

    @errorHandler
    def _getApplianBGPState(self):
        orch_return = self.orch.get_appliance_bgp_state(self.ne_pk)
        bgpNumVrfs.labels(applianceName=self.applianceName).set(orch_return['summary']['num_vrfs']) #Setting Metric
        bgpProcessState.labels(applianceName=self.applianceName).info({'bgpProcessState' : orch_return['summary']['bgp_state_str']}) #Setting Metric
        bgpRejectMismatches.labels(applianceName=self.applianceName).set(orch_return['summary']['reject_mismatches']) #Setting Metric
        bgpNumPeers.labels(applianceName=self.applianceName).set(orch_return['summary']['num_bgp_peers']) #Setting Metric
        bgpSubsInstalled.labels(applianceName=self.applianceName).set(orch_return['summary']['num_subs_installed']) #Setting Metric
        bgpOspfRoutes.labels(applianceName=self.applianceName).set(orch_return['summary']['num_ospf_rtes']) #Setting Metric
        bgpIBGPRoutes.labels(applianceName=self.applianceName).set(orch_return['summary']['num_ibgp_rtes']) #Setting Metric
        bgpEBGPRoutes.labels(applianceName=self.applianceName).set(orch_return['summary']['num_ebgp_rtes']) #Setting Metric

        for neighbor in orch_return['neighbor']['neighborState']:
            peer_ip = neighbor['peer_ip']
            bgpNeighborState.labels(applianceName=self.applianceName, peer_ip=peer_ip).set(neighbor['peer_state']) #Setting Metric
            bgpNeighborStateStr.labels(applianceName=self.applianceName, peer_ip=peer_ip, asn=neighbor['asn']).info({'bgpNeighborStateStr' : neighbor['peer_state_str']}) #Setting Metric
            bgpNeighborUptime.labels(applianceName=self.applianceName, peer_ip=peer_ip).set(neighbor['time_established']) #Setting Metric
            bgpNeighborReceivedPrefix.labels(applianceName=self.applianceName, peer_ip=peer_ip).set(neighbor['rcvd_pfxs']) #Setting Metric
            bgpNeighborSentPrefix.labels(applianceName=self.applianceName, peer_ip=peer_ip).set(neighbor['sent_pfxs']) #Setting Metric

        return orch_return
    


class collectApplianceOSPF():
    def __init__(self):
        pass


class collectApplianceFlows():
    def __init__(self,url,ne_pk,applianceName,key,verify_ssl,interval,debug, Break):
        self.url = url
        self.ne_pk = ne_pk
        self.applianceName = applianceName
        self.key = key
        self.verify_ssl = verify_ssl
        self.interval = interval
        self.debug = debug
        self.Break = Break
        self.orch = Orchestrator(url=self.url, verify_ssl=self.verify_ssl, api_key=self.key )
        while True:
            # get a list of all the methods in this class
            # loops over the list starting at index 1 to bypass __init__
            # calls the method
            methodList = inspect.getmembers(self, predicate=inspect.ismethod)
            for m in range(1, len(methodList)):
                i = methodList[m][1]()

                logToFile().debug(message=dict({methodList[m][1].__name__ : i}), debug=self.debug) 
                confirmReturn(func=methodList[m][1].__name__ ,dictionary=i, debug=self.debug) 
                writeResult(func=list(i.keys())[0], result=i['result'], debug=self.debug)
            if self.Break == False:
                wait(self.interval)
            else:
                break

    @errorHandler
    def _getApplianceFlows(self):
        orch_return = self.orch.get_appliance_flows(self.ne_pk,uptime="term5m")

        activeTotalFlows.labels(applianceName=self.applianceName).set(orch_return['active']['total_flows']) #Setting Metric
        activeStaleFlows.labels(applianceName=self.applianceName).set(orch_return['active']['stale_flows']) #Setting Metric
        activeInconsistentFlows.labels(applianceName=self.applianceName).set(orch_return['active']['inconsistent_flows']) #Setting Metric
        activeFlowsWithIssues.labels(applianceName=self.applianceName).set(orch_return['active']['flows_with_issues']) #Setting Metric
        activeFlowsOptimized.labels(applianceName=self.applianceName).set(orch_return['active']['flows_optimized']) #Setting Metric
        activeFlowsWithIgnores.labels(applianceName=self.applianceName).set(orch_return['active']['flows_with_ignores']) #Setting Metric
        activeFlowsPassthrough.labels(applianceName=self.applianceName).set(orch_return['active']['flows_passthrough']) #Setting Metric
        activeFlowsManagement.labels(applianceName=self.applianceName).set(orch_return['active']['flows_management']) #Setting Metric
        activeFlowsAsymmetric.labels(applianceName=self.applianceName).set(orch_return['active']['flows_asymmetric']) #Setting Metric
        activeFlowsRouteDropped.labels(applianceName=self.applianceName).set(orch_return['active']['flows_route_dropped']) #Setting Metric
        activeFlowsFirewallDropped.labels(applianceName=self.applianceName).set(orch_return['active']['flows_firewall_dropped']) #Setting Metric

        inactiveTotalFlows.labels(applianceName=self.applianceName).set(orch_return['inactive']['total_flows']) #Setting Metric
        inactiveStaleFlows.labels(applianceName=self.applianceName).set(orch_return['inactive']['stale_flows']) #Setting Metric
        inactiveInconsistentFlows.labels(applianceName=self.applianceName).set(orch_return['inactive']['inconsistent_flows']) #Setting Metric
        inactiveFlowsWithIssues.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_with_issues']) #Setting Metric
        inactiveFlowsOptimized.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_optimized']) #Setting Metric
        inactiveFlowsWithIgnores.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_with_ignores']) #Setting Metric
        inactiveFlowsPassthrough.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_passthrough']) #Setting Metric
        inactiveFlowsManagement.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_management']) #Setting Metric
        inactiveFlowsAsymmetric.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_asymmetric']) #Setting Metric
        inactiveFlowsRouteDropped.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_route_dropped']) #Setting Metric
        inactiveFlowsFirewallDropped.labels(applianceName=self.applianceName).set(orch_return['inactive']['flows_firewall_dropped']) #Setting Metric

        return orch_return