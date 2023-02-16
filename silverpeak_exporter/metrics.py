#Importing prometheus library
from prometheus_client import Info,Gauge,Enum

#---------#---------#---------#---------#---------#
# Application Metrics
#---------#---------#---------#---------#---------#
activeThreads = Gauge('activeThreads', 'number of total python threads')

#---------#---------#---------#---------#---------#
# Orchestrator Metrics
#---------#---------#---------#---------#---------#

uptime = Info('uptime', 'silverpeak orchestrator uptime',['orchName'])
release = Info('release', 'silverpeak orchestrator release version',['orchName'])
platform = Info('platform', 'silverpeak orchestrator platform',['orchName'])
numActiveUsers = Gauge('numActiveUsers', 'number of active users logged in',['orchName'])
activeAlarms = Gauge('activeAlarms', 'summary of active alarms for Orchestrator and all appliances',['orchName','severity'])
totalAppliances = Gauge('totalAppliances', 'number of total appliances in your orchestrator',['orchName'])
licenseNumMini  = Gauge('licenseNumMini', 'number of mini licenses',['orchName'])
licenseNumBase  = Gauge('licenseNumBase', 'number of base licenses',['orchName'])
licenseNumBoost  = Gauge('licenseNumBoost', 'number of boost licenses',['orchName'])
licenseNumPlus  = Gauge('licenseNumPlus', 'number of plus licenses',['orchName'])
licenseNumTier20M = Gauge('licenseNumTier20M', 'number of 20M licenses',['orchName'])
licenseNumTier50M = Gauge('licenseNumTier50M', 'number of 50M licenses',['orchName'])
licenseNumTier100M = Gauge('licenseNumTier100M', 'number of 100M licenses',['orchName'])
licenseNumTier200M = Gauge('licenseNumTier200M', 'number of 200M licenses',['orchName'])
licenseNumTier500M = Gauge('licenseNumTier500M', 'number of 500M licenses',['orchName'])
licenseNumTier1G = Gauge('licenseNumTier1G', 'number of 1G licenses',['orchName'])
licenseNumTier2G = Gauge('licenseNumTier2G', 'number of 2G licenses',['orchName'])
licenseNumTierUM = Gauge('licenseNumTierUM', 'number of Unlimited licenses',['orchName'])
totalOverlays = Gauge('totalOverlays', 'number of overlays configured',['orchName'])
totalRegions = Gauge('totalRegions', 'number of regions configured',['orchName'])
totalSaasApps = Gauge('totalSaasApps', 'list of unique SaaS applications in the internet services database',['orchName'])
totalAppDefinition = Gauge('totalAppDefinition', 'count for application definition data for Address Map from Cloud Portal',['orchName'])
totalOrchSaasApps = Gauge('totalOrchSaasApps', 'count of internet services defined on Orchestrator',['orchName'])
orchPortalStatus = Enum('orchPortalStatus', 'current connectivity status between Orchestrator and Cloud Portal',['orchName'], states=['unable to connect', 'connected', 'connecting'])
cloudPortalServices = Gauge('cloudPortalServices', 'silverpeak cloud portal service and status',['orchName','portalService','status'])
totalTunnelCount = Gauge('totalTunnelCount', 'get total tunnel count across all appliances',['orchName'])

#---------#---------#---------#---------#---------#
# Appliance Metrics
#---------#---------#---------#---------#---------#
applianceHostname = Info('applianceHostname', 'name of the silverpeak edge connect',['applianceName'])
applianceModel = Info('applianceModel', 'mode of the silverpeak appliance',['applianceName'])
appliancePlatform = Info('appliancePlatform', 'platform of the silverpeak appliance',['applianceName'])
applianceUptime = Gauge('applianceUptime', 'uptime in milliseconds for the silverpeak appliance',['applianceName'])
applianceUptimeString = Info('applianceUptimeString', 'uptime in string format for the silverpeak appliance',['applianceName'])
applianceRelease = Info('applianceRelease', 'appliance release version',['applianceName'])
applianceDeploymentMode = Info('applianceDeploymentMode', 'the deployment mode of the appliance',['applianceName'])
applianceAlarm = Gauge('applianceAlarm', 'summary of active alarms for given appliance',['applianceName','severity'])
applianceCPU = Gauge('applianceCPU', 'cpu utilization in porcentage for each appliance core',['applianceName','cpu_core','metric'])
applianceDiskUsage = Gauge('applianceDiskUsage', 'appliance disk utilization for each mount point',['applianceName','mount','metric'])
applianceRebootRequiered = Enum('applianceRebootRequiered', 'check with appliance if a reboot is required from changes',['applianceName'], states=['True', 'False'])
applianceMemory = Gauge('applianceMemory', 'get appliance memory related information',['applianceName','metric'])

#---------#---------#---------#---------#---------#
# BGP Metrics
#---------#---------#---------#---------#---------#
bgpNumVrfs = Gauge('bgpNumVrfs', 'total number of vrf using bgp',['applianceName',])
bgpProcessState = Info('bgpProcessState', 'state of the bgp process',['applianceName'])
bgpRejectMismatches = Gauge('bgpRejectMismatches', 'bgp neighbors rejected by a mismatch',['applianceName',])
bgpNumPeers = Gauge('bgpNumPeers', 'total number of bgp peers',['applianceName',])
bgpSubsInstalled = Gauge('bgpSubsInstalled', 'total numbers of subnets installed in the bgp process',['applianceName',])
bgpOspfRoutes = Gauge('bgpOspfRoutes', 'total number of routes originated by OSPF',['applianceName',])
bgpIBGPRoutes = Gauge('bgpIBGPRoutes', 'total number of routes originated by iBGP',['applianceName',])
bgpEBGPRoutes = Gauge('bgpEBGPRoutes', 'total number of routes originated by eBGP',['applianceName',])
bgpNeighborState = Gauge('bgpNeighborState', 'state of bgp neighbor',['applianceName','peer_ip'])
bgpNeighborStateStr = Info('bgpNeighborStateStr', 'state of bgp neighbor in string',['applianceName','peer_ip','asn'])
bgpNeighborUptime = Gauge('bgpNeighborUptime', 'uptime of the bgp neighbor',['applianceName','peer_ip'])
bgpNeighborReceivedPrefix = Gauge('bgpNeighborReceivedPrefix', 'total number of prefixes received from the neighbor',['applianceName','peer_ip'])
bgpNeighborSentPrefix = Gauge('bgpNeighborSentPrefix', 'total number of prefixes advertised to the neighbor',['applianceName','peer_ip'])



#---------#---------#---------#---------#---------#
# Flows Metrics
#---------#---------#---------#---------#---------#

activeTotalFlows = Gauge('activeTotalFlows', 'number of active flows',['applianceName',])
activeStaleFlows = Gauge('activeStaleFlows', 'number of active stale flows',['applianceName',])
activeInconsistentFlows = Gauge('activeInconsistentFlows', 'number of active inconsistent flows',['applianceName',])
activeFlowsWithIssues = Gauge('activeFlowsWithIssues', 'number of active flows with issues',['applianceName',])
activeFlowsOptimized = Gauge('activeFlowsOptimized', 'number of active optimized flows',['applianceName',])
activeFlowsWithIgnores = Gauge('activeFlowsWithIgnores', 'no description in swagger',['applianceName',])
activeFlowsPassthrough = Gauge('activeFlowsPassthrough', 'number of active passthrough flows',['applianceName',])
activeFlowsManagement = Gauge('activeFlowsManagement', 'number of active management flows',['applianceName',])
activeFlowsAsymmetric = Gauge('activeFlowsAsymmetric', 'number of active asymmetric flows',['applianceName',])
activeFlowsRouteDropped = Gauge('activeFlowsRouteDropped', 'number of active flows dropped due to route',['applianceName',])
activeFlowsFirewallDropped = Gauge('activeFlowsFirewallDropped', 'number of active flows dropped due to firewall',['applianceName',])
inactiveTotalFlows = Gauge('inactiveTotalFlows', 'number of inactive flows',['applianceName',])
inactiveStaleFlows = Gauge('inactiveStaleFlows', 'number of inactive stale flows',['applianceName',])
inactiveInconsistentFlows = Gauge('inactiveInconsistentFlows', 'number of inactive inconsistent flows',['applianceName',])
inactiveFlowsWithIssues = Gauge('inactiveFlowsWithIssues', 'number of inactive flows with issues',['applianceName',])
inactiveFlowsOptimized = Gauge('inactiveFlowsOptimized', 'number of inactive optimized flows',['applianceName',])
inactiveFlowsWithIgnores = Gauge('inactiveFlowsWithIgnores', 'no description in swagger',['applianceName',])
inactiveFlowsPassthrough = Gauge('inactiveFlowsPassthrough', 'number of inactive passthrough flows',['applianceName',])
inactiveFlowsManagement = Gauge('inactiveFlowsManagement', 'number of inactive management flows',['applianceName',])
inactiveFlowsAsymmetric = Gauge('inactiveFlowsAsymmetric', 'number of inactive asymmetric flows',['applianceName',])
inactiveFlowsRouteDropped = Gauge('inactiveFlowsRouteDropped', 'number of inactive flows dropped due to route',['applianceName',])
inactiveFlowsFirewallDropped = Gauge('inactiveFlowsFirewallDropped', 'number of inactive flows dropped due to firewall',['applianceName',])