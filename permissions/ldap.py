# -*- coding: utf-8 -*-

import ldap
import logging
from django.conf import settings

log = logging.getLogger("operation.permissions")

class LDAPService(object):
    
    def __init__(self):
        self.ldap_path = settings.LDAPPATH
        self.base_dn = settings.BASE_DN
        self.ldap_user = settings.LDAPUSER
        self.ldap_pass = settings.LDAPPASS
    
    def _validate_ldap_user(self, user):
        try:
            l = ldap.initialize(ldappath)
            l.protocol_version = ldap.VERSION3
            l.simple_bind(self.ldap_user,self.ldap_pass)

            searchScope  = ldap.SCOPE_SUBTREE
            searchFiltername = "sAMAccountName"
            retrieveAttributes = None
            searchFilter = '(' + searchFiltername + "=" + user +')'

            ldap_result_id = l.search(self.base_dn, searchScope, searchFilter, retrieveAttributes)
            result_type, result_data = l.result(ldap_result_id,1)
            if(not len(result_data) == 0):
              r_a,r_b = result_data[0]
              return 1, r_b["distinguishedName"][0]
            else:
              return 0, ''
        except ldap.LDAPError, e:
            log.exception('Error is %s' % e)
            return 0, ''
        finally:
            l.unbind()

    #连接超时，尝试多次连接
    def get_dn(self, user, trynum = 30):
        i = 0
        isfound = 0
        foundResult = ""
        while(i < trynum):
            isfound, foundResult = self._validate_ldap_user(user)
            if(isfound):
              break
            i+=1
        return foundResult


    def ldap_login(self, username, password):
        try:
            dn = self.get_dn(username,10)
            if(dn==''):
                return
            my_ldap = ldap.initialize(ldappath)
            my_ldap.simple_bind_s(dn, password)
        except Exception,e:
            logging.error('login failed,error is %s' % e)
