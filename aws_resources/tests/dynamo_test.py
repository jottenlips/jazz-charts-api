from aws_resources.mock_dynamo import mock_song
from aws_resources.dynamo import build_update_expression, build_update_attributes_dictionary

def test_build_update_expression():

    update_exp = build_update_expression(mock_song)
    print(update_exp)
    assert update_exp == 'set title=:title, chordChart=:chordChart, composer=:composer'

def build_update_attributes_dictionary():
    update_attr = pdate_attributes_dictionary(mock_song)
    assert update_attr == {
        ':title': 'It don\'t mean a thing',
        ':chordChart': 'Gm | ...',
        ':composer': 'c1'
    }

