from datetime import datetime
import inspect
import json


class DictMixin(object):

    @classmethod
    def from_dict(cls, d):
        return cls(**d)

    @classmethod
    def from_dicts(cls, ds):
        return [cls(**d) for d in ds]

    def to_dict(self, props=None):
        return self._traverse_dict(self.properties(self, props))

    def properties(self, obj, props=None):
        pr = {}
        for name in dir(obj):
            value = getattr(obj, name)
            if props is None:
                if not name.startswith('_') and not inspect.ismethod(value) and name in self.props:
                    pr[name] = value
            else:
                if not name.startswith('_') and not inspect.ismethod(value) and name in props:
                    pr[name] = value
        return pr

    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, DictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            # return self._traverse_dict(value.__dict__)
            return value
        elif type(value) is unicode:
            return value.encode('utf-8')
        else:
            return value


class JsonMixin(DictMixin):
    @classmethod
    def from_json(cls, data):
        return cls.from_dict(json.loads(data))

    def to_json(self, indent=0, props=None):
        return json.dumps(self.to_dict(props=props), indent=indent, ensure_ascii=False, default=marshaler)

    def to_pretty_json(self):
        return self.to_json(4)


def marshaler(o):
    if isinstance(o, datetime):
        return o.isoformat()
    raise TypeError(repr(o) + " is not JSON serializable")
