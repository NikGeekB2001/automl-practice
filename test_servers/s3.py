import boto3


def __get_s3_connection():
    config_s3 = {
        "aws_access_key_id": "YCAJEpeA9yDgWru4XETpVNScI",
        "aws_secret_access_key": "YCN27Y40IJ_MZAnGRfjXbP_DaD1KfMrVQMbm89FO",
        "region_name": "ru-central-1",
    }

    s3_connection = boto3.client("s3", **config_s3)

    return s3_connection


print(__get_s3_connection())


# python s3.py