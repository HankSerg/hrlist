from .default import *

# Set local_settings if exists
try:
    from .local_settings import *
except ImportError:
    pass
