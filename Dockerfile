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
RUN python3 -m venv myvenv
RUN pip install --upgrade pip
ENV PATH="/myvenv/bin:$PATH"
COPY . .
RUN pip3 install mlflow flask pandas joblib requests argparse tensorflow scikit-learn
# RUN python3 artifact_downloader.py --model_version=$model_version --MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI

RUN ls -la ./artifacts

RUN pip install -r ./artifacts/requirements.txt
CMD python3 app.py --model_uri=$model_uri --model_version=$model_version --MLFLOW_TRACKING_URI=$MLFLOW_TRACKING_URI --MLFLOW_TRACKING_USERNAME=$MLFLOW_TRACKING_USERNAME --MLFLOW_TRACKING_PASSWORD=$MLFLOW_TRACKING_PASSWORD