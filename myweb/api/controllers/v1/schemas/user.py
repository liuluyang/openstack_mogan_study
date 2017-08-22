from myweb.api.validation import parameter_types

metadata = {
    'type': 'object',
    'patternProperties': {
        '^[a-zA-Z0-9-_:. ]{1,255}$': {
            'type': 'string', 'maxLength': 255, 'minLength':1
        }
    },
    'additionalProperties': False
}

user_add = {
    'type': 'object',
    'properties': {
        'name':parameter_types.name,
        'policy':{ "enum": [ "disk" ,'one'] },
        'metadata':metadata
    },
    'required': ['policy'],
    'additionalProperties': False,
}