import grpc

def get_channel(server):
    return grpc.insecure_channel(server)
