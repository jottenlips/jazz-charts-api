from ariadne import load_schema_from_path, ObjectType, QueryType, MutationType
from features.Composers.composer import resolve_composer
from features.Songs.song import resolve_song, create_song, update_song


songQueries = QueryType()
songMutations = MutationType()

songTypes = load_schema_from_path("./features/Songs/song.gql")
songObjectType = ObjectType('FBSong')
songObjectType.set_field("composer", resolve_composer)
songQueries.set_field('getSong', resolve_song)
songMutations.set_field('createSong', create_song)
songMutations.set_field('updateSong', update_song)
