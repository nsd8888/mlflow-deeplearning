FROM python:3.11-bullseye


ARG model_uri
ARG model_version
ARG MLFLOW_TRACKING_URI
ARG MLFLOW_TRACKING_USERNAME
ARG MLFLOW_TRACKING_PASSWORD


RUN echo $MLFLOW_TRACKING_URI $model_uri

WORKDIR /
COPY . .
RUN pip install --upgrade pip
RUN python3 -m venv myvenv
ENV PATH="/myvenv/bin:$PATH"

RUN pip3 install mlflow


ENV MLFLOW_TRACKING_URI = MLFLOW_TRACKING_URIs
ENV MLFLOW_TRACKING_USERNAME = MLFLOW_TRACKING_USERNAME
ENV MLFLOW_TRACKING_PASSWORD = MLFLOW_TRACKING_PASSWORD


RUN model_uri_1 = f"models:/$model_uri/$model_version"
RUN pip install -r artifacts/requirements.txt


CMD ["python3","app.py","--model_uri = $model_uri_1","--model_version = $model_version"]
