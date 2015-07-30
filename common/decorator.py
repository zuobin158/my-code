# -*- coding: utf-8 -*-

def singleton(cls, *args, **kwargs):
    instances = {}
    def _singleton():
        if not instances.has_key(cls):
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton
