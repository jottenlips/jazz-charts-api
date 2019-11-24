from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key

def resolve_composer(obj, info, id=None):
    print(obj, info, id, ':::COMPO')
    if (obj['skey'] and ('song_composer' in obj['skey'])):
        id = obj['skey'].split('song_composer:')[1]
    composer = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return composer