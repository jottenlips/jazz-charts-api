from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key
import uuid

def resolve_composer(obj, info, id=None):
    if (obj and 'composer' in obj):
        id = obj['composer']
    composer = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return composer

def create_composer(obj, info, composer):
    id = str(uuid.uuid4())
    composer['id'] = id
    table.put_item(Item=composer)
    return {
        'song': composer,
        'message': 'success',
        'code': 200,
        'success': True
    }

def update_composer(obj, info, composer):
    table.update_item(
        Key={
            'id': composer['id']
        },
        UpdateExpression="set name=:n",
        ExpressionAttributeValues={
            ':n': composer['name'],
        },
    )
    updated_composer = table.query(
        KeyConditionExpression=Key('id').eq(composer['id'])
    )['Items'][0]

    return {
        'composer': updated_composer,
        'message': 'success',
        'code': 200,
        'success': True
    }