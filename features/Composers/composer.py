from ariadne import load_schema_from_path
from ariadne import ObjectType

composerTypes = load_schema_from_path("./features/Composers/composer.gql")
composerObjectType = ObjectType('FBComposer')

def get_composer(*_, info, id=None):
    print('hello world')
    return {
        'id': '1',
        'name': 'Duke Ellington'
    }