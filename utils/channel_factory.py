import logging

import grpc


log = logging.getLogger(__name__)

# https://grpc.io/grpc/python/grpc.html

# https://grpc.io/grpc/core/group__grpc__arg__keys.html#details
channel_options = [('grpc.keepalive_time_ms', 15000),
                   ('grpc.keepalive_timeout_ms', 750),
                   ('grpc.keepalive_permit_without_calls', 1),
                   ('grpc.http2.max_pings_without_data', 0),
                  ]

def get_channel(host, port=50051, authority=None):
    # dont mutate channel_options
    options = channel_options.copy()
    if authority is not None:
        options.append(('grpc.default_authority', authority))
    log.debug(f'Creating insecure gRPC channel: {host}:{port} options={options}')
    return grpc.insecure_channel(host+':'+str(port), options=options)
