from ariadne import QueryType, make_executable_schema, graphql_sync
from ariadne import load_schema_from_path
from features.Songs.songTypes import songTypes, songObjectType
from ariadne.constants import PLAYGROUND_HTML
from features.Composers.composerTypes import composerTypes, composerObjectType
from flask import Flask, request, jsonify
from features.Composers.composer import resolve_composer
from features.Songs.song import resolve_song

queryTypes = load_schema_from_path("./queries.gql")
mutationTypes = load_schema_from_path("./mutations.gql")
# mutationTypes = load_schema_from_path("./mutations.graphql")
query = QueryType()
query.set_field('getComposer', resolve_composer)
query.set_field('getSong', resolve_song)

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