import boto3
import os
# .resource('dynamodb').Table(os.environ['TABLE_NAME'])
dynamodb = boto3.resource('dynamodb')
table_name = os.environ['TABLE_NAME']
table = dynamodb.Table(table_name)