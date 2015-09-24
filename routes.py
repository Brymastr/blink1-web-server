from flask import Blueprint, request, Response, stream_with_context
import light

api = Blueprint('buildAPI', __name__)


@api.route("/busy", methods=['POST'])
def busy():
    light.busy()
    return "busy"


@api.route("/success", methods=['POST'])
def success():
    light.success()
    return "success"


@api.route("/failure", methods=['POST'])
def failure():
    light.failure()
    return "failure"


@api.route("/unstable", methods=['POST'])
def unstable():
    light.unstable()
    return "unstable"


# Just to test request arguments
@api.route("/words")
def respond():
    return request.args.get("words")


