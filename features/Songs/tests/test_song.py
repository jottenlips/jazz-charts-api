
from features.Songs.song import resolve_song, resolve_songs
from aws_resources.mock_dynamo import setup_mocks, mock_song, another_mock_song
from moto import mock_dynamodb2

@mock_dynamodb2
def test_resolve_song():
    setup_mocks()
    song = resolve_song({}, {}, "1")
    assert song == mock_song
    
@mock_dynamodb2
def test_resolve_song():
    setup_mocks()
    songs = list(resolve_songs({'songs': ["1", "2"]}, {}))
    assert songs == [mock_song, another_mock_song]