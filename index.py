from ariadne import QueryType, make_executable_schema
from ariadne import load_schema_from_path

from ariadne.asgi import GraphQL
from starlette.applications import Starlette
from features.Songs.song import songTypes
from features.Composers.composer import composerTypes

queryTypes = load_schema_from_path("./queries.gql")
mutationTypes = load_schema_from_path("./mutations.gql")
# mutationTypes = load_schema_from_path("./mutations.graphql")
query = QueryType()

schema = make_executable_schema([mutationTypes, queryTypes, songTypes, composerTypes])

# Create executable schema instance
# schema = make_executable_schema(type_defs, query)

app = Starlette(debug=True)
app.mount("/graphql", GraphQL(schema, debug=True))