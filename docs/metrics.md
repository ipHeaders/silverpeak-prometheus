# Exposed Metrics

## Orchestrator 

| Name  | Type  | Description  |
| ------------ | ------------ | ------------ |
| uptime_info  | Label  | silverpeak orchestrator uptime  |
| release_info  | Label  | silverpeak orchestrator release version  | 
| platform_info  | Label  | silverpeak orchestrator platform  | 
| numActiveUsers  | Gauge  | number of active users logged in  | 
| activeAlarms  | Gauge  | summary of active alarms for Orchestrator and all appliances  | 
| totalAppliances  | Gauge  | number of total appliances in your orchestrator  | 
| licenseNumMini  | Gauge  | number of mini licenses  | 
| licenseNumBase| Gauge  | number of base licenses  | 
| licenseNumBoost | Gauge  | number of boost licenses  | 
| licenseNumPlus  | Gauge  | number of plus licenses  | 
| licenseNumTier20M  | Gauge  | number of 20M licenses  | 
| licenseNumTier50M  | Gauge  | number of 50M licenses  | 
| licenseNumTier100M  | Gauge  | number of 100M licenses   | 
| licenseNumTier200M  | Gauge  | number of 200M licenses | 
| licenseNumTier500M| Gauge  | number of 500M licenses  | 
| licenseNumTier1G| Gauge  | number of 1G licenses  | 
| licenseNumTier2G| Gauge  | number of 2G licenses  | 
| licenseNumTierUM| Gauge  | number of Unlimited licenses  | 
| totalOverlays| Gauge  | number of overlays configured  | 
| totalRegions| Gauge  | number of regions configured  | 
| totalSaasApps| Gauge  | list of unique SaaS applications in the internet services database  | 
| totalAppDefinition| Gauge  | count for application definition data for Address Map from Cloud Portal  | 
| totalOrchSaasApps| Gauge  | count of internet services defined on Orchestrator  | 
| orchPortalStatus| Enum   | current connectivity status between Orchestrator and Cloud Portal  | 
| cloudPortalServices| Gauge  | silverpeak cloud portal service and status  | 
| totalTunnelCount| Gauge  | get total tunnel count across all appliances  | 
| totalCPUs| Gauge  | the total amount of CPU on the orchestrator, works only when orch is not running in container  | 
| loadAverage| Gauge  | orchestrator load average, works only when orch is not running in container  | 
| totalMemSize| Gauge  | total memory of the server, works only when orch is not running in container  | 
| maintenaceModeAppliances| Gauge  | appliances currently in maintenance mode  | 

## Appliances System

| Name  | Type  | Description  |
| ------------ | ------------ | ------------ |
| applianceHostname_info  | Label  | name of the silverpeak edge connect  |
| applianceModel_info  | Label  | mode of the silverpeak appliance  |
| appliancePlatform_info  | Label  | platform of the silverpeak appliance  |
| applianceUptime  | Gauge  | uptime in milliseconds for the silverpeak appliance  |
| applianceUptimeString_info  | Label  | uptime in string format for the silverpeak appliance  |
| applianceRelease_info  | Label  | appliance release version  |
| applianceDeploymentMode_info  | Label  | the deployment mode of the appliance  |
| applianceAlarm  | Gauge  | summary of active alarms for given appliance  |
| applianceCPU  | Gauge  | cpu utilization in porcentage for each appliance core  | 
| applianceDiskUsage  | Gauge  | appliance disk utilization for each mount point  | 
| applianceRebootRequiered  | Enum  | check with appliance if a reboot is required from changes  | 
| applianceMemory  | Gauge  | get appliance memory related information  | 


## Appliances BGP

| Name  | Type  | Description  |
| ------------ | ------------ | ------------ |
| bgpNumVrfs  | Gauge  | total number of vrf using bgp  | 
| bgpProcessState_info  | Label  | state of the bgp process  |
| bgpRejectMismatches  | Gauge  | bgp neighbors rejected by a mismatch  | 
| bgpNumPeers  | Gauge  | total number of bgp peers  | 
| bgpSubsInstalled  | Gauge  | total numbers of subnets installed in the bgp process  | 
| bgpOspfRoutes  | Gauge  | total number of routes originated by OSPF  | 
| bgpIBGPRoutes  | Gauge  | total number of routes originated by iBGP  | 
| bgpEBGPRoutes  | Gauge  | total number of routes originated by eBGP  | 
| bgpNeighborState  | Gauge  | state of bgp neighbor  | 
| bgpNeighborStateStr_info  | Label  | state of bgp neighbor in string  |
| bgpNeighborUptime  | Gauge  | uptime of the bgp neighbor  | 
| bgpNeighborReceivedPrefix  | Gauge  | total number of prefixes received from the neighbor  | 
| bgpNeighborSentPrefix  | Gauge  | total number of prefixes advertised to the neighbor  | 


## Appliances Flows

| Name  | Type  | Description  |
| ------------ | ------------ | ------------ |
| activeTotalFlows  | Gauge  | number of active flows  | 
| activeStaleFlows  | Gauge  | number of active stale flows  | 
| activeInconsistentFlows  | Gauge  | number of active inconsistent flows  | 
| activeFlowsWithIssues  | Gauge  | number of active flows with issues  | 
| activeFlowsOptimized  | Gauge  | number of active optimized flows  | 
| activeFlowsWithIgnores  | Gauge  | no description in swagger  | 
| activeFlowsPassthrough  | Gauge  | number of active passthrough flows  | 
| activeFlowsManagement  | Gauge  | number of active management flows  | 
| activeFlowsAsymmetric  | Gauge  | number of active asymmetric flows  | 
| activeFlowsRouteDropped  | Gauge  | number of active flows dropped due to route  | 
| activeFlowsFirewallDropped  | Gauge  | number of active flows dropped due to firewall  | 
| inactiveTotalFlows  | Gauge  | number of inactive flows  | 
| inactiveStaleFlows  | Gauge  | number of inactive stale flows  | 
| inactiveInconsistentFlows  | Gauge  | number of inactive inconsistent flows  | 
| inactiveFlowsWithIssues  | Gauge  | number of inactive flows with issues  | 
| inactiveFlowsOptimized  | Gauge  | number of inactive optimized flows  | 
| inactiveFlowsWithIgnores  | Gauge  | no description in swagger  | 
| inactiveFlowsPassthrough  | Gauge  | number of inactive passthrough flows  | 
| inactiveFlowsManagement  | Gauge  | number of inactive management flows  | 
| inactiveFlowsAsymmetric  | Gauge  | number of inactive asymmetric flows  | 
| inactiveFlowsRouteDropped  | Gauge  | number of inactive flows dropped due to route  | 
| inactiveFlowsFirewallDropped  | Gauge  | number of inactive flows dropped due to firewall  | 