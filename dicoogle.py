#!/usr/bin/env python
# -*- coding: utf-8 -*-

__title__ = 'dicoogle'
__version__ = '2.0-dev'
__author__ = 'Luís A. Bastião Silva, Tiago Marques Godinho'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2013, Luís Bastião, Universidade de Aveiro'
__url__ = 'http://bastiao.github.io/dicoogle-python/'

__maintainer__ = 'Luís A. Bastião Silva, Tiago Marques Godinho'
__email__ = 'bastiao@ua.pt, tmgodinho@ua.pt'

__all__ = ()

import requests


class Dicoogle:
    def __init__(self, url='demo.dicoogle.com'):
        self.ENDPOINT = "http://" + url

    # Validated
    def search_dim(self, query, provider=None, keyword=True):
        #http://localhost:8080/searchDIM?query=Modality:CR&keyword=true
        url = self.ENDPOINT + "/searchDIM"
        data = {"query": query, "keyword": keyword}
        if provider:
            data["provider"] = provider

        r = requests.get(url, params=data)
        return r

    #Validated
    def export_csv(self, query, fields=[], providers=[], file=None):
        url = self.ENDPOINT + "/export"
        data = {"query": query, "fields": fields, "providers": providers}
        r = requests.get(url, params=data, stream=True)
        if file:
            file.write(r.content)
            file.flush()

        return r

    def search(self, query, provider, keyword=False):
        url = self.ENDPOINT + "/search"
        data = {"query": query, "provider": provider, "keyword": keyword}
        r = requests.get(url, params=data);
        return r

    def dump(self, uid):
        url = self.ENDPOINT + "/dump"
        data = {"uid": uid}
        r = requests.get(url, params=data)
        return r
