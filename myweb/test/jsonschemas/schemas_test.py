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


def multi_params(schema):
    """Macro function for use in JSONSchema to support query parameters that
    may have multiple values.
    """
    return {'type': 'array', 'items': schema}


# NOTE: We don't check actual values of queries on params
# which are defined as the following common_param.
# Please note those are for backward compatible existing
# query parameters because previously multiple parameters
# might be input and accepted.
common_query_param = multi_params({'type': 'string'})


non_negative_integer = {
    'type': ['integer', 'string'],
    'pattern': '^[0-9]*$', 'minimum': 0, 'minLength': 1
}


server_groups_query_param = {
    'type': 'object',
    'properties': {
        'all_projects': common_query_param,
        'limit': multi_params(non_negative_integer),
        'offset': multi_params(non_negative_integer),
    },
    # For backward compatible changes
    'additionalProperties': True
}

#json_schema({"h":" "}, metadata)
json_schema({'all_projects':['True'],'limit':2}, server_groups_query_param)