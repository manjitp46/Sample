import os

import logging
from logging import getLogger, Logger

from pkg_resources import resource_filename  # @UnresolvedImport

logging.basicConfig(level = logging.ERROR)

versionFile =  resource_filename('Sample', 'version.txt')
_LOG = getLogger()

version = None

if not os.path.exists(versionFile):
    _LOG.error('%s does not exist. Considering version as 0.0.0.0' % versionFile)
    version = '0.0.0.0'    
else:    
    try:
        with open(versionFile,'rt') as fp:
            version = fp.read().strip()
    except Exception as e:
        version = '0.0.0.0'
        _LOG.error('Exception while opening version file. Details: %s. Version reset to 0.0.0.0' %str(e))
    
__version__ = version
__description__ = 'Application to server global settings'