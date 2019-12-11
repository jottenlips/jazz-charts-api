from ariadne import load_schema_from_path, ObjectType, QueryType, MutationType
from features.Composers.composer import resolve_composer, create_composer, update_composer, get_composers
from features.Songs.song import resolve_songs

composerQueries = QueryType()
composerMutations = MutationType()

composerTypes = load_schema_from_path("./features/Composers/composer.gql")
composerObjectType = ObjectType('FBComposer')
composerObjectType.set_field("songs", resolve_songs)
composerQueries.set_field('getComposer', resolve_composer)
songQueries.set_field('getComposers', get_composers)

composerMutations.set_field('createComposer', create_composer)
composerMutations.set_field('updateComposer', update_composer)

