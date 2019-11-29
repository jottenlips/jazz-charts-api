
from moto import mock_dynamodb2
import boto3
import os 

mock_create_song = {
            "title": "It don't mean a thing",
            "chordChart": "Gm | ...",
            "composer": "c1"
        }

mock_song = {
            'id': '1',
            "title": "It don't mean a thing",
            "chordChart": "Gm | ...",
            "composer": "c1"
        }

another_mock_song = {
            'id': '2',
            "title": "It don't mean a thing",
            "chordChart": "Gm | ...",
            "composer": "c1"
        }

mock_composer = {
            'id': 'c1',
            'songs': [
                '1',
                '2'
            ],
            'name': 'Duke Ellington'
        }
        
@mock_dynamodb2
def setup_mocks():
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName= os.environ['TABLE_NAME'],
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
    )

    print(table)

    table.put_item(
        Item=mock_composer
    )

    table.put_item(
        Item=mock_song
    )

    table.put_item(
        Item=another_mock_song
    )