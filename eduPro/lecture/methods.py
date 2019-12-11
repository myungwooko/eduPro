from itertools import chain
from rest_framework.serializers import ValidationError
import xml.etree.cElementTree as et


class Methods:
    def to_dict(self, instance):
        opts = instance._meta
        data = {}
        for f in chain(opts.concrete_fields, opts.private_fields):
            data[f.name] = f.value_from_object(instance)
        for f in opts.many_to_many:
            data[f.name] = [i.id for i in f.value_from_object(instance)]
        return data

