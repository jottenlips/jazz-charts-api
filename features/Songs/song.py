from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key
from features.Composers.composer import resolve_composer
import uuid

def resolve_song(obj, info, id):
    song =  table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return song

def resolve_songs(obj, info):
    print(obj)
    ids = obj['songs']
    return map(lambda id: resolve_song(obj, info, id), ids)

def create_song(obj, info, song):
    id = str(uuid.uuid4())
    song['id'] = id
    song['skey'] = ''.join(song['title'].split(' '))
    table.put_item(Item=song)
    return {
        'song': song,
        'message': 'success',
        'code': 200,
        'success': True
    }

def update_song(obj, info, song):
    if (song['composerId']):
        song['skey'] = 'song_composer:'+song['composerId']
    table.update_item(Item=song)
    return {
        'song': song,
        'message': 'success',
        'code': 200,
        'success': True
    }