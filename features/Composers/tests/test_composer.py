
from features.Composers.composer import resolve_composer, create_composer, update_composer
from aws_resources.mock_dynamo import setup_mocks, mock_composer, mock_create_composer
from moto import mock_dynamodb2

@mock_dynamodb2
def test_resolve_composer():
    setup_mocks()
    composer = resolve_composer({}, {}, "c1")
    assert composer == mock_composer
    
@mock_dynamodb2
def test_create_composer():
    setup_mocks()
    response = create_composer({}, {}, mock_create_composer)
    assert response['message'] == 'success' and response['composer']['fullName'] == 'Duke Ellington'

@mock_dynamodb2
def test_update_composer():
    setup_mocks()
    new_attr = {'fullName': 'Ornett Coleman'}
    updated_composer = {**mock_composer, **new_attr}
    response = update_composer({}, {}, updated_composer)
    print(response)
    assert response['message'] == 'success' and response['composer']['fullName'] == 'Ornett Coleman'