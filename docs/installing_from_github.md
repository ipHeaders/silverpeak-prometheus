# Installing using Pypi.
 
To install using Pypi make sure the running python version is >= to python3.9.
 
First we need to install the package via pip.
 
```
Please note that that to install the latest version you must update the release version 
pip3 install git+https://github.com/ipHeaders/silverpeak-prometheus.git@v0.1.1  <--- Here
```
 
You can verify that the installation was successful by checking the installed libraries using `pip3 freeze | grep silverpeak-exporter`
 
After the installation was successful. You need to define certain variables in order for the exporter to launch successfully. You can do this either running the tool using cli flags or exporting them as environment variables.
 
### Using environment variables.
 
The only required environment variable is the **SP_FILE_PATH**, the rest can be also set as a variable in the vars.yml configuration file. Please note that environment variables take ***precedence*** over file variables and cli flags
 
**Available environment variables **
| Name  | Required  |
| ------------ | ------------ |
| SP_FILE_PATH  | **True**  |
| SP_PORT  | False  |
| SP_ORCH_URL  |  False |
| SP_ORCH_KEY  | **True**  |
| SP_ORCH_SSL  |  False | |
 
** Example of setting environment variables **
```
export SP_PORT=15693
export SP_ORCH_URL=orch.silverpeak.cloud
export SP_ORCH_KEY=XXXXXXXXXXXX
export SP_ORCH_SSL=True
export SP_FILE_PATH=/path/to/test_vars.yml
```
If you want to take a look at an example vars.yml [file](../test/test_vars.yml). Check the test folder.
After setting the environment variables, just run the exporter by entering in the terminal.
 
```
spexporter
```
 
Below is an example of a successful exporter launch.
 
```
╰─➤  spexporter
2022-12-22 14:56:47,245 - silverpeak-prometheus - INFO - starting prometheus exporter on 15693
2022-12-22 14:56:47,245 - silverpeak-prometheus - INFO - starting orchestrator metric collection on orch.silverpeak.cloud
2022-12-22 14:56:47,245 - silverpeak-prometheus - INFO - starting orchestrator metric collection every 30 seconds
```
 
 
### Using command flags.
The spexporter has a cli command as well that can be used to set certain configurations. To check all the options run
 
```
spexporter -h
```
 
Below is an example of how to start the tool passing cli flags.
 
```
╰─➤  spexporter --file-path /path/to/vars.yml --orch orch.silverpeak.cloud --key 123123 --port 15693
 
2022-12-22 14:56:47,245 - silverpeak-prometheus - INFO - starting prometheus exporter on 15693
2022-12-22 14:56:47,245 - silverpeak-prometheus - INFO - starting orchestrator metric collection on orch.silverpeak.cloud
2022-12-22 14:56:47,245 - silverpeak-prometheus - INFO - starting orchestrator metric collection every 30 seconds
```
 
### Checking exposed metrics
To check that the exporter is up and running and the exporter metrics go to http://localhost:15693
Note if you use a different port besides 15693 change that accordingly.