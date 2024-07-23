<h1 align="center" style="font-weight: bold;">mysqldump-lambda-s3 💻</h1>

<div align="center">

  ![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
  ![lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=awslambda&logoColor=white)
  ![amazon s3](https://img.shields.io/badge/amazon_s3-amazons3?style=for-the-badge&logo=amazons3&logoColor=white)

</div>

<p align="center">
    <b>Create an AWS Lambda to backup MySQL databases into a S3 bucket.</b>
</p>

<h2 id="started">🚀 Getting started</h2>

1. [Create a Lambda](https://console.aws.amazon.com/lambda/home#) function with any Python version as runtime
2. Make sure to assign a permission that allows files to be inserted into S3
3. [Create a Layer](https://console.aws.amazon.com/lambda/home#/layers) with [`mysqldump5.7-cli.zip`](https://github.com/Lima-e-Silva/mysqldump-lambda-s3/blob/main/mysqldump5.7-cli.zip)
4. Paste the code from [`lambda_function.py`](https://github.com/Lima-e-Silva/mysqldump-lambda-s3/blob/main/lambda_function.py) into your Lambda
5. Setup your Environment Variables <sup>[details](#env)</sup>
6. Done!

<h2 id="env">Environment Variables</h2>

- `HOST`: from your MySQL database
- `PORT`: from your MySQL database
- `DATABASE_NAME`: from your MySQL database
- `PASSWORD`: from your MySQL database
- `BUCKET_NAME`: from your S3
- `BUCKET_FOLDER`: from your S3

