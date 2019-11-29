
import boto3
from moto import mock_dynamodb2

mock_song = {
            'id': '1',
            "title": "It don't mean a thing",
            "chordChart": "Gm | ...",
            "composer": "c1"
        }

mock_composer = {
            'id': 'c1',
            'songs': [
                '1',
            ],
            'name': 'Duke Ellington'
        }

@mock_dynamodb2
def setup_mocks():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName='posts',
        KeySchema=[
            {
                'AttributeName': 'id',
                'KeyType': 'HASH'  # primary key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'id',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    table.put_item(
        Item=mock_composer
    )

    table.put_item(
        Item=mock_song
    )