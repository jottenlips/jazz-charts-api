from ariadne import load_schema_from_path
from ariadne import ObjectType, QueryType
from features.Composers.composer import resolve_composer

songTypes = load_schema_from_path("./features/Songs/song.gql")
songObjectType = ObjectType('FBSong')
songObjectType.set_field("composer", resolve_composer)
