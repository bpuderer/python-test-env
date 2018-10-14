import json

from google.protobuf import json_format

from services.doubler.doubler_pb2 import Number


def build_request_from_dict(d, request):
    json_str = json.dumps(d)
    return json_format.Parse(json_str, request)

def build_request_from_file(filename, request):
    with open(filename) as f:
        json_str = f.read()
    return json_format.Parse(json_str, request)


def build_number_from_dict(d):
    return build_request_from_dict(d, Number())

def build_number_from_file(filename):
    return build_request_from_file(filename, Number())
