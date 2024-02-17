FROM python:3.11-bullseye


ARG model_uri
ARG model_version
ARG MLFLOW_TRACKING_URI
ARG MLFLOW_TRACKING_USERNAME
ARG MLFLOW_TRACKING_PASSWORD

ENV MLFLOW_TRACKING_URI = $MLFLOW_TRACKING_URI
ENV MLFLOW_TRACKING_USERNAME = $MLFLOW_TRACKING_USERNAME
ENV MLFLOW_TRACKING_PASSWORD = $MLFLOW_TRACKING_PASSWORD


WORKDIR /

RUN pip install --upgrade pip
RUN python3 -m venv myvenv
ENV PATH="/myvenv/bin:$PATH"

RUN pip3 install mlflow
RUN ls -la
COPY /model_artifact .
RUN pip install -r ./model_artifact/requirements.txt
CMD ["python3","app.py","--model_uri = $model_uri","--model_version = $model_version"]
