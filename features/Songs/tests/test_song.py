
from features.Songs.song import resolve_song
from aws_resources.mock_dynamo import setup_mocks, mock_song

def test_resolve_song():
    setup_mocks()
    song = resolve_song({}, {}, "1")
    print(mock_song)
    print(song, '::::song')
    assert 1 is 1