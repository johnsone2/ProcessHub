from json import JSONEncoder

import jsonpickle


class BindingModelConverter(JSONEncoder):
    def default(self, o):
        return_dictionary = jsonpickle.encode(o, unpicklable=False)
        return jsonpickle.decode(return_dictionary)