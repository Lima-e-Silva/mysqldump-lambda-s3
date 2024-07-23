import json
import os
from datetime import datetime

import boto3


def timeStamp() -> str:
    """
    Returns the current time in the format YYYY-MM-DD

    Returns:
    -------
    str
        The current time in the format YYYY-MM-DD
    """
    return datetime.now().strftime("%Y-%m-%d")


def backupMysql(prefix: str = "", suffix: str = "") -> str:
    """
    Creates a backup of the MySQL database

    Parameters:
    -----------
    prefix: str
        The prefix to add to the file name
    suffix: str
        The suffix to add to the file name

    Returns:
    -------
    str
        The path to the backup file
    """
    fileName = "/tmp/" + prefix + timeStamp() + suffix + ".sql"
    os.system(
        f'mysqldump -p{os.getenv("PASSWORD")} --port {os.getenv("PORT")} --host {os.getenv("HOST")} --user root {os.getenv("DATABASE_NAME")} > {fileName}'
    )

    return fileName


def lambda_handler(event, context):
    bucketName = os.getenv("BUCKET_NAME")
    bucketFolder = os.getenv("BUCKET_FOLDER")

    s3 = boto3.client("s3")

    fileName = backupMysql()

    s3.upload_file(fileName, bucketName, fileName.replace("/tmp", bucketFolder))
    return {"statusCode": 200, "body": json.dumps("success")}
