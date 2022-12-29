# Exposed Metrics

## Orchestrator 

| Name  | Type  | Description  |
| ------------ | ------------ | ------------ |
| uptime  | Label  | silverpeak orchestrator uptime  |
| release  | Label  | silverpeak orchestrator release version  | 
| platform  | Label  | silverpeak orchestrator platform  | 
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


## Appliances 

| Name  | Type  | Description  |
| ------------ | ------------ | ------------ |
| applianceAlarm  | Gauge  | summary of active alarms for given appliance  |
| applianceCPU  | Gauge  | cpu utilization in porcentage for each appliance core  | 
| applianceDiskUsage  | Gauge  | appliance disk utilization for each mount point  | 
| applianceRebootRequiered  | Enum  | check with appliance if a reboot is required from changes  | 
| applianceMemory  | Gauge  | get appliance memory related information  | 