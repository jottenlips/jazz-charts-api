from ariadne import load_schema_from_path
from ariadne import QueryType

composerTypes = load_schema_from_path("./features/Composers/composer.gql")

query = QueryType()
@query.field("composer")
def resolve_composer(*_):
    return {
        'id': '1',
        'name': 'Duke Ellington'
    }