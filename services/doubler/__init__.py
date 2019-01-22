import os
import sys


# issue is that the current working directory is where run_tests.py is run
# thus import doubler_pb2 as doubler__pb2
# fails but import services.doubler.doubler_pb2 as doubler__pb2 works

# https://stackoverflow.com/a/5137509
dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)
