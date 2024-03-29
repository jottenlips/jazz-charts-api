from aws_resources.dynamo import table, build_update_attributes_dictionary, build_update_expression
from boto3.dynamodb.conditions import Key
import uuid

def resolve_composer(obj, info, id=None):
    if (obj and 'composer' in obj):
        id = obj['composer']
    composer = table().query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return composer

def create_composer(obj, info, composer):
    id = str(uuid.uuid4())
    composer['id'] = id
    table().put_item(Item=composer)
    return {
        'composer': composer,
        'message': 'success',
        'code': 200,
        'success': True
    }

def get_composers(obj, info, last_evaluated_key):
    composers = table().scan(
        Limit=10,  
        ExclusiveStartKey={'id': last_evaluated_key},
        Select='ALL_ATTRIBUTES', 
        FilterExpression='attribute_exists(fullName)'
    )['Items']
    return composers

def update_composer(obj, info, composer):
    attributes_to_update = build_update_attributes_dictionary(composer)
    update_expression = build_update_expression(composer)
    table().update_item(
        Key={
            'id': composer['id']
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=attributes_to_update,
    )
    updated_composer = table().query(
        KeyConditionExpression=Key('id').eq(composer['id'])
    )['Items'][0]

    return {
        'composer': updated_composer,
        'message': 'success',
        'code': 200,
        'success': True
    }