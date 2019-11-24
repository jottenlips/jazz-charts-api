from ariadne import load_schema_from_path
from ariadne import ObjectType
from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key
from features.Composers.composer import resolve_composer

songTypes = load_schema_from_path("./features/Songs/song.gql")
songObjectType = ObjectType('FBSong')

def get_song(*_, id=None):
    return resolve_song(id)

def resolve_song(id):
    song =  table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    composerId = song['skey'].split('song_composer:')[1]
    composer = resolve_composer(composerId)
    song['composer'] = composer
    return song
