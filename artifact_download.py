import mlflow
from argparse import ArgumentParser

par = ArgumentParser()
par.add_argument("--model_uri", type=str)
par.add_argument("--model_version", type=int)
args = par.parse_args()
model_uri = f"models:/$model_uri/$model_version"
mlflow.artifacts.download_artifacts(dst_path = "artifacts/", artifact_uri = model_uri)