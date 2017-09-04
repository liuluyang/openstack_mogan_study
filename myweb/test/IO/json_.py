
import json

_dict = dict(name='bob',age=21)

j = json.dumps(_dict)
print type(j),j