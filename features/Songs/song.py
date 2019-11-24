from ariadne import load_schema_from_path
from ariadne import QueryType

songTypes = load_schema_from_path("./features/Songs/song.gql")

query = QueryType()
@query.field("song")
def resolve_song(*_):
    return {
        'id': '1',
        'chordChart': 'Bbm7 | Eb7 | AbM7'
    }