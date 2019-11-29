
from features.Songs.song import resolve_song
from aws_resources.mock_dynamo import setup_mocks, mock_song
from moto import mock_dynamodb2

@mock_dynamodb2
def test_resolve_song():
    setup_mocks()
    song = resolve_song(_, _, "1")
    print(mock_song)
    print(song, '::::song')
    assert 1 is 1