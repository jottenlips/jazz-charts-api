from ariadne import QueryType, make_executable_schema, graphql_sync, MutationType
from ariadne import load_schema_from_path
from features.Songs.songTypes import songTypes, songObjectType, songQueries, songMutations
from ariadne.constants import PLAYGROUND_HTML
from features.Composers.composerTypes import composerTypes, composerObjectType, composerQueries, composerMutations
from flask import Flask, request, jsonify
from features.Composers.composer import resolve_composer, update_composer, resolve_composer, create_composer
from features.Songs.song import create_song, resolve_song, update_song
queryTypes = load_schema_from_path("./root_types/queries.gql")
mutationTypes = load_schema_from_path("./root_types/mutations.gql")

schema = make_executable_schema(
    [mutationTypes, queryTypes, songTypes, composerTypes],
    [songObjectType, composerObjectType, songQueries, songMutations, composerQueries, composerMutations]
)

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