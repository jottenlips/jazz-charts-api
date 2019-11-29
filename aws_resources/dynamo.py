import boto3
import os

def table():
    dynamodb = boto3.resource('dynamodb')
    table_name = os.environ['TABLE_NAME']
    table = dynamodb.Table(table_name)
    return table

def build_update_expression(items):
    keys = items.keys()
    filtered_items = { key: items[key] for key in keys if key != 'id'}
    filtered_keys = filtered_items.keys()
    return "set " + " ".join([key+"=:"+key+"," for key in filtered_keys])[:-1]

def build_update_attributes_dictionary(items):
    keys = items.keys()
    return { ":"+key: items[key] for key in keys if key != 'id'}



