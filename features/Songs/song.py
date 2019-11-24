from ariadne import load_schema_from_path
from ariadne import ObjectType
from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key

songTypes = load_schema_from_path("./features/Songs/song.gql")
songObjectType = ObjectType('FBSong')

def get_song(*_, id=None):
    print(id, '::::id')
    result =  table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    print(result)
    return result