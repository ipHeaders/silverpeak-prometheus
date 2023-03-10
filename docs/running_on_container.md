Getting Started
---------------
#### Requirements
~~~~~~~~~~~~~~~~~~~~
* User with API KEY
~~~~~~~~~~~~~~~~~~~~

On the server running docker engine create a yml file with the custom vars for this exporter. Example below.
~~~~~~~~~~~~~~~~~~~~
config:
   exporter:
      port: 15693
   silverpeak:
      orch: orch.silverpeak.cloud
      verify_ssl: True

orchestrator:
   collect: True
   interval: 300
   
appliances:
   edge-1:
      - {system: true, interval: 120}
      - {bgp: true, interval: 120} 
   edge-2:
      - {system: true, interval: 120}
      - {bgp: true, interval: 120}
~~~~~~~~~~~~~~~~~~~~

Use the following command as an example to map the folder where the vars are located and add additional environment variables to the container.
##### Make sure to map the yml file to the container location /opt/vars/

~~~~~~~~~~~~~~~~~~~~
docker run -d -v /home/user/vars.yml:/opt/vars/ \
    -e 'SP_PORT=15693' \
    -e 'SP_ORCH_URL=orch.silverpeak.cloud' \
    -e 'SP_ORCH_KEY=XXXXXXXXXXXX' \
    -e 'SP_ORCH_SSL=True' \
    -e 'SP_FILE_PATH=/opt/vars/vars.yml' \
    -p 15693:15693 \
    --restart=unless-stopped \
    ipheaders/silverpeak-prometheus:latest
~~~~~~~~~~~~~~~~~~~~


Required Environments Variables
~~~~~~~~~~~~~~~~~~~~
* SP_FILE_PATH
* SP_ORCH_KEY
~~~~~~~~~~~~~~~~~~~~

Optional Environments Variables
##### If the following environment variables are not defined at launch then they must be in the vars.yml file
~~~~~~~~~~~~~~~~~~~~
* SP_PORT
* SP_ORCH_URL
* SP_ORCH_SSL
~~~~~~~~~~~~~~~~~~~~
