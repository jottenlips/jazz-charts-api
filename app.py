from ariadne import QueryType, make_executable_schema, graphql_sync
from ariadne import load_schema_from_path
from features.Songs.song import songTypes, get_song, songObjectType
from ariadne.constants import PLAYGROUND_HTML
from features.Composers.composer import composerTypes, get_composer, composerObjectType
from flask import Flask, request, jsonify

queryTypes = load_schema_from_path("./queries.gql")
mutationTypes = load_schema_from_path("./mutations.gql")
# mutationTypes = load_schema_from_path("./mutations.graphql")
query = QueryType()

query.set_field('getSong', get_song)
query.set_field('getComposer', get_composer)

schema = make_executable_schema([mutationTypes, queryTypes, songTypes, composerTypes], [songObjectType, composerObjectType, query])

app = Flask(__name__)

@app.route("/graphql", methods=["GET"])
def graphql_playgroud():
    return PLAYGROUND_HTML


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    return jsonify(result)