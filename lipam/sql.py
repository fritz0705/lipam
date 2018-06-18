# coding: utf-8

import lipam.ipam

import lglass_sql.nic


class IPAMDatabase(lglass_sql.nic.NicDatabase,
                   lipam.ipam.IPAMDatabaseMixin):
    def __init__(self, *args, **kwargs):
        lglass_sql.nic.NicDatabase.__init__(self, *args, **kwargs)
        lipam.ipam.IPAMDatabaseMixin.__init__(self)
