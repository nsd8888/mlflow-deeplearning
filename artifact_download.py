import mlflow
from argparse import ArgumentParser

par = ArgumentParser()
par.add_argument("--model_uri", type = str)
par.add_argument("--model_version", type = int)
par.add_argument("--MLFLOW_TRACKING_URI")
par.add_argument("--MLFLOW_TRACKING_USERNAME")
par.add_argument("--MLFLOW_TRACKING_PASSWORD")

args = par.parse_args()

MLFLOW_TRACKING_URI = args.MLFLOW_TRACKING_URI
MLFLOW_TRACKING_USERNAME = args.MLFLOW_TRACKING_USERNAME
MLFLOW_TRACKING_PASSWORD = args.MLFLOW_TRACKING_PASSWORD

print(MLFLOW_TRACKING_USERNAME)
model_uri = f"models:/{str(args.model_uri)}/{str(args.model_version)}"
mlflow.artifacts.download_artifacts(dst_path = "artifacts/", artifact_uri = model_uri)