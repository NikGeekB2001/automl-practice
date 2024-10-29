pip install mlflow==2.13.1

export MLFLOW_S3_ENDPOINT_URL=https://storage.yandexcloud.net
export AWS_ACCESS_KEY_ID=YCAJEpeA9yDgWru4XETpVNScI
export AWS_SECRET_ACCESS_KEY=YCN27Y40IJ_MZAnGRfjXbP_DaD1KfMrVQMbm89FO

mlflow server \
    --backend-store-uri postgresql://admin_mlflow:mlflow_postgres_password@localhost:5432/mlflow \
    --registry-store-uri postgresql://admin_mlflow:mlflow_postgres_password@localhost:5432/mlflow \
    --default-artifact-root s3://automl-otus-practice-1 \
    --no-serve-artifacts




# sh run_mlflow_server.sh