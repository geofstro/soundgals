'''
    qobuz.storage
    ~~~~~~~~~~~~~~~~~~

    Package that set our default cache
    
    :copyright: (c) 2012 by Joachim Basmaison, Cyril Leclerc
    :license: GPLv3, see LICENSE for more details.
'''
__all__ = ['cache']

from cache.qobuz import CacheQobuz
cache = CacheQobuz()
