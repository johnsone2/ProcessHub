from django.http import QueryDict
from jsonpickle import json


def _convert_string_bools_to_bools(dictionary):
        for key, value in dictionary.iteritems():
            if not isinstance(value, str):
                continue
            if value.lower() == 'true' or value.lower() == 'false':
                dictionary[key] = True if value.lower() == 'true' else False
        return dictionary


def parse_request_body(request):
    if request.POST:
        request_body = request.POST.dict()
        # request_body = self._convert_string_bools_to_bools(request_body)
    else:
        try:
            request_body = json.loads(request.body)
        except BaseException as e:
            try:
                request_body = QueryDict(request.body).dict()
                # request_body = self._convert_string_bools_to_bools(request_body)
            except BaseException as e:
                request_body = {}

    return request_body
