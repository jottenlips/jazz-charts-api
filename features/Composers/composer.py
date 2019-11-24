from ariadne import load_schema_from_path
from ariadne import ObjectType
from aws_resources.dynamo import table
from boto3.dynamodb.conditions import Key

composerTypes = load_schema_from_path("./features/Composers/composer.gql")
composerObjectType = ObjectType('FBComposer')


def get_composer(*_, id=None):
    result =  table.query(
        KeyConditionExpression=Key('id').eq(id)
    )['Items'][0]
    return result