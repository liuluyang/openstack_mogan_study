

#liu
add_aggregate_host = {
    'type': 'object',
    'properties': {
        'host_id': {
            'type': 'string', 'format': 'uuid',
        },
    },
    'required': ['host_id'],
    'additionalProperties': False,
}