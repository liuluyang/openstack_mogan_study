#coding:utf8
import jsonschema


def json_schema(date, schema):

    validator = jsonschema.Draft4Validator(schema, format_checker=jsonschema.FormatChecker())
    try:
        validator.validate(date)
    except Exception as e:
        print e

schema = {
            'type': 'array', 'minItems': 1,
            'items': {
                'type': 'object',
                'properties': {
                    'net_id': 'string',
                    'port_id': 'string',
                },
                'oneOf': [
                    {'required': ['net_id']},
                    {'required': ['port_id']}
                ],
                'additionalProperties': False,
            },
        }

schema_2 = {"type":"array","items":{
    'type': ['integer', 'string'],
    'pattern': '^[0-9]*$', 'minimum': 0, 'minLength': 1
}}

hostname = {
    'type': 'string', 'minLength': 1, 'maxLength': 255,
    # NOTE: 'host' is defined in "services" table, and that
    # means a hostname. The hostname grammar in RFC952 does
    # not allow for underscores in hostnames. However, this
    # schema allows them, because it sometimes occurs in
    # real systems.
    'pattern': '^[a-zA-Z0-9-._]*$',
}
name_with_leading_trailing_spaces = {
    'type': 'string', 'minLength': 1, 'maxLength': 255,
    'format': 'name_with_leading_trailing_spaces'
}

name = {
    'type': 'string', 'minLength': 1, 'maxLength': 255,
    'format': 'name'
}

metadata = {
    'type': 'object',
    'patternProperties': {
        '^[a-zA-Z0-9-_:. ]{1,255}$': {
            'type': 'string', 'maxLength': 255
        }
    },
    'additionalProperties': False
}

json_schema({"h":" "}, metadata)