# -*- coding: utf-8 -*-


class DBRouter(object):
    """
    A router to control all database operations on models in the
    cms application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read cms models go to cms DB.
        """
        if model._meta.app_label == 'cms':
            return 'cms'
        return 'default'
 
    def db_for_write(self, model, **hints):
        """
        Attempts to write cms models go to cms DB.
        """
        if model._meta.app_label == 'cms':
            return 'cms'
        return 'default'
 
    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the cms app is involved.
        """
        if obj1._meta.app_label == 'cms' or \
           obj2._meta.app_label == 'cms':
            return True
        return None
 
    def allow_migrate(self, db, model):
        """
        Make sure the cms app only appears in the cms database.
        """
        if db == 'cms':
            return model._meta.app_label == 'cms'
        elif model._meta.app_label == 'cms':
            return False
 
    def allow_syncdb(self, db, model):
        if db == 'cms' or model._meta.app_label == "cms":
            return False  # we're not using syncdb on our cms database
        else:  # but all other models/databases are fine
            return True
        return None
 
