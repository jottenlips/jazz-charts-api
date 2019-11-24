from ariadne import load_schema_from_path
from ariadne import ObjectType, QueryType
from features.Composers.composer import resolve_composer
from features.Songs.song import resolve_songs

composerTypes = load_schema_from_path("./features/Composers/composer.gql")
composerObjectType = ObjectType('FBComposer')
composerObjectType.set_field("songs", resolve_songs)
