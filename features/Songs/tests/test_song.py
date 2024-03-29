
from features.Songs.song import resolve_song, resolve_songs, create_song, update_song, get_songs
from aws_resources.mock_dynamo import setup_mocks, mock_song, another_mock_song, mock_create_song
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


@mock_dynamodb2
def test_get_songs():
    setup_mocks()
    songs = get_songs({}, {}, "")
    assert songs == [mock_song, another_mock_song]

@mock_dynamodb2
def test_create_song():
    setup_mocks()
    response = create_song({}, {}, mock_create_song)
    assert response['message'] == 'success' and response['song']['title'] == 'It don\'t mean a thing'

@mock_dynamodb2
def test_update_song():
    setup_mocks()
    new_attr = {'title': 'new song title'}
    updated_song = {**mock_song, **new_attr}
    response = update_song({}, {}, updated_song)
    assert response['message'] == 'success' and response['song']['title'] == 'new song title'