
from aws_resources.mock_dynamo import setup_mock, mock_song

def test_resolve_song():
    setup_mock()
    song = resolve_song(_, _, "1")
    assert song is mock_song