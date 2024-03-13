import sys
import os
from dotenv import load_dotenv


CH = os.path.abspath(os.path.dirname(__file__))
AH = os.path.abspath(f'{CH}/../')


# load envvar
load_dotenv()
ENV_NAME = os.environ.get('ENV_NAME')


# Time
DEFAULT_DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DEFAULT_DATE_FORMAT     = '%Y-%m-%d'


# DB
DB_PORT         = os.environ.get('DB_PORT')
DB_USER         = os.environ.get('DB_USER')
DB_PASS         = os.environ.get('DB_PASS')
DB_NAME         = os.environ.get('DB_NAME')
DB_HOST         = os.environ.get('DB_HOST')
DB_POOL_SIZE    = os.environ.get('DB_POOL_SIZE')

# get DB_NAME
IS_PYTEST       = 'pytest' in sys.modules
XDIST_WORKER    = os.environ.get('PYTEST_XDIST_WORKER')
IS_TEST_SINGLE  = XDIST_WORKER is None or XDIST_WORKER == 'master'
if IS_PYTEST:
    DB_NAME = f'{DB_NAME}Test'
