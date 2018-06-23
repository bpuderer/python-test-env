"""Read test settings and init logger"""

import configparser
import json
import logging
import logging.config
import os
import sys


logging.config.fileConfig('framework/logging.cfg')
log = logging.getLogger(__name__)

test_env = os.getenv('PY_TEST_ENV', 'DEFAULT')

cp = configparser.ConfigParser()
cp.read('framework/test_settings.cfg')
try:
    #getboolean(), getfloat(), getint() are for ConfigParser, not section
    settings = dict(cp.items(test_env))
except configparser.NoSectionError as e:
    print(e)
    print('Test run aborted')
    sys.exit()

log.info('Loaded test settings for {}: {}'.format(test_env,
         json.dumps(settings), indent=4, sort_keys=True))
