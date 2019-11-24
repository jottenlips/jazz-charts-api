from ariadne import QueryType, make_executable_schema
from ariadne import load_schema_from_path

from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from features.Songs.song import songTypes, get_song, songObjectType
from features.Composers.composer import composerTypes, get_composer, composerObjectType

queryTypes = load_schema_from_path("./queries.gql")
mutationTypes = load_schema_from_path("./mutations.gql")
# mutationTypes = load_schema_from_path("./mutations.graphql")
query = QueryType()

query.set_field('getSong', get_song)
query.set_field('getComposer', get_composer)

schema = make_executable_schema([mutationTypes, queryTypes, songTypes, composerTypes], [songObjectType, composerObjectType, query])

# Create executable schema instance
# schema = make_executable_schema(type_defs, query)

app = Starlette(debug=True)
app.mount("/graphql", GraphQL(schema, debug=True))