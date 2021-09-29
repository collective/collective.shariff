# -*- coding: utf-8 -*- vim: sw=4 sts=4 si et ts=8 tw=79 cc=+1
"""
Decorator for upgrade steps
"""

# Python compatibility:
from __future__ import absolute_import

# Standard library:
import logging
from functools import wraps
from time import time

__all__ = [
        # decorators:
        'step',
        # exceptions:
        'StepAborted',
        ]


class StepAborted(Exception):
    """
    Raised by the @step decorator if keyboard-interrupted
    """


def step(func):
    """
    Decorate a migration step:
    - amend the logger argument, if missing
    - log the execution time
    - catch keyboard interrupts to allow the Zope instance to keep on running
    """
    @wraps(func)
    def wrapper(context, logger=None):
        funcname = func.__name__
        if logger is None:
            logger = logging.getLogger('setup:'+funcname)
        _started = time()
        try:
            res = func(context, logger)
        except Exception as e:
            delta = time() - _started
            if isinstance(e, KeyboardInterrupt):
                logger.error('%(funcname)s aborted after %(delta)5.2f seconds',
                             locals())
                logger.exception(e)
                raise StepAborted
            else:
                logger.error('%(funcname)s: %(e)r after %(delta)5.2f seconds',
                             locals())
                logger.exception(e)
                raise
        else:
            delta = time() - _started
            logger.info('%(res)r <-- %(funcname)s (%(delta)5.2f seconds)', locals())
        return res

    return wrapper
