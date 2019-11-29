from aws_resources.dynamo import build_update_expression, build_update_attributes_dictionary, table
from boto3.dynamodb.conditions import Key
from features.Composers.composer import resolve_composer
import uuid

def resolve_song(obj, info, id):
    song = table().query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return song

def resolve_songs(obj, info):
    ids = obj['songs']
    return map(lambda id: resolve_song(obj, info, id), ids)

def create_song(obj, info, song):
    id = str(uuid.uuid4())
    song['id'] = id
    table().put_item(Item=song)
    return {
        'song': song,
        'message': 'success',
        'code': 200,
        'success': True
    }

def update_song(obj, info, song):
    attributes_to_update = build_update_attributes_dictionary(song)
    update_expression = build_update_expression(song)
    table().update_item(
        Key={
            'id': song['id']
        },
        UpdateExpression=update_expression,
        ExpressionAttributeValues=attributes_to_update,
    )
    updated_song = table().query(
        KeyConditionExpression=Key('id').eq(song['id'])
    )['Items'][0]

    return {
        'song': updated_song,
        'message': 'success',
        'code': 200,
        'success': True
    }