from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key
from features.Composers.composer import resolve_composer
import uuid

def resolve_song(obj, info, id):
    song = table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return song

def resolve_songs(obj, info):
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

    updated_song = table.update_item(
        Key={
            'id': song['id']
        },
        UpdateExpression="set title = :title",
        ExpressionAttributeValues={
            ':title': song['title']
        },
    )

    return {
        'song': updated_song,
        'message': 'success',
        'code': 200,
        'success': True
    }

    #    composer= :composer,
    #     chordChart= :chordChart