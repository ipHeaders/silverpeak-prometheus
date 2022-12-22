FROM python:3.10.9
#Set the working directory
RUN mkdir /opt/exporter
RUN mkdir /opt/vars
WORKDIR /opt/exporter
#Copy python requirements and install them using pip3 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
# Copy code
COPY silverpeak_exporter silverpeak_exporter
# Defining Env variables
ENV SP_DEBUG ""
ENV SP_PORT ""
ENV SP_ORCH_URL ""
ENV SP_ORCH_KEY ""
ENV SP_ORCH_SSL ""
ENV SP_FILE_PATH ""
# Creating entrypoint
ENTRYPOINT ["python3" , "silverpeak_exporter/main.py"]