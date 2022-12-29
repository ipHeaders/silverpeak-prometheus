FROM python:3.10.9
# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"
#Set the working directory
RUN mkdir /opt/exporter
RUN mkdir /opt/vars
WORKDIR /opt/exporter
#Copy code for poetry build
COPY requirements.txt requirements.txt
COPY silverpeak_exporter silverpeak_exporter
COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock
COPY README.md README.md
# Defining Env variables
ENV SP_DEBUG ""
ENV SP_PORT ""
ENV SP_ORCH_URL ""
ENV SP_ORCH_KEY ""
ENV SP_ORCH_SSL ""
ENV SP_FILE_PATH ""
# Installing the code
WORKDIR /opt/exporter/silverpeak_exporter
RUN poetry install
# Creating entrypoint
ENTRYPOINT ["poetry" , "run", "spexporter"]