from ariadne import load_schema_from_path
from ariadne import ObjectType

songTypes = load_schema_from_path("./features/Songs/song.gql")

songObjectType = ObjectType('FBSong')


def get_song(*_, id=None):
    return {
        'id': '1',
        'chordChart': 'Bbm7 | Eb7 | AbM7'
    }