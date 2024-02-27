import mlflow
import os

model_uri = os.getenv("model_uri")
model_version = os.getenv("model_version")
MLFLOW_TRACKING_URI = os.getenv("MLFLOW_TRACKING_URI")
MLFLOW_TRACKING_USERNAME = os.getenv("MLFLOW_TRACKING_USERNAME")
MLFLOW_TRACKING_PASSWORD = os.getenv("MLFLOW_TRACKING_PASSWORD")

# MLFLOW_TRACKING_URI = MLFLOW_TRACKING_URI
# mlflow.set_tracking_uri(args.MLFLOW_TRACKING_URI)

lst = ["Ordinal_encode_bp.pkl", "Ordinal_encode_cho.pkl", "Onehot_encode_sex.pkl", "Std.pkl", "Label_encode.pkl", "requirements.txt"]
for i in lst:
    c_model_uri=f"models:/{str(model_uri)}/{str(model_version)}/{i}"
    artifact_download = mlflow.artifacts.download_artifacts(dst_path="artifacts/", artifact_uri= c_model_uri)