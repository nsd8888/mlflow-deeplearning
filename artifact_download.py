import mlflow
from argparse import ArgumentParser
import os
par = ArgumentParser()
par.add_argument("--model_uri", type = str)
par.add_argument("--model_version", type = int)
args = par.parse_args()

MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")

# MLFLOW_TRACKING_URI = MLFLOW_TRACKING_URI
# mlflow.set_tracking_uri(args.MLFLOW_TRACKING_URI)

lst = ["Ordinal_encode_bp.pkl", "Ordinal_encode_cho.pkl", "Onehot_encode_sex.pkl", "Std.pkl", "Label_encode.pkl", "requirements.txt"]
for i in lst:
    model_uri=f"models:/{str(args.model_uri)}/{str(args.model_version)}/{i}"
    artifact_download = mlflow.artifacts.download_artifacts(dst_path="artifacts/", artifact_uri= model_uri)