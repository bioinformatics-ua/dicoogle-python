#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
How works Dicoogle Webservices in REST?

Search by Date Range – Access images in date 2005/03/29:
URL: http://www.dicoogle.com/services/dws/dim?advq=StudyDate:[20050329 TO 20050329]

Search by Date Range – Access images in date 2005/03/29 and Modality CT (Computer Tomography):
URL: http://www.dicoogle.com/services/dws/dim?advq=Modality:CT AND StudyDate:[20050329 TO 20050329]

Access parameters for each image (use uid):

http://www.dicoogle.com/services/dws/dump?uid=1.3.12.2.1107.5.1.4.54023.30000005032914013107800000965

Search Free Text – looking for CT keyword:

http://www.dicoogle.com/services/dws/dim?q=CT

Get DICOM File:

http://www.dicoogle.com/services/dws/file?uid=1.3.12.2.1107.5.1.4.54023.30000005032914013107800000965

"""

__title__ = 'dicoogle'
__version__ = '0.1-dev'
__author__ = 'Luís A. Bastião Silva'
__license__ = 'GPL v3'
__copyright__ = 'Copyright 2013, Luís Bastião, Universidade de Aveiro'
__url__ = 'http://bastiao.github.io/dicoogle-python/'

__maintainer__ = 'Luís A. Bastião Silva'
__email__ = 'bastiao@ua.pt'

__all__ = ()

ENDPOINT = "http://localhost:6060/"

import sys
import time
import json
try:
    from urllib.parse import quote
except ImportError:
    from urllib import quote  # NOQA
import xmltodict, json

import requests  # urllib2 sucks badly, we depend on requests

def search_freetext(query):
	result = requests.get(ENDPOINT + "dim?q="+ query)
	

	o = xmltodict.parse(result.text)

	return o

def search_advanced(query):
	result = requests.get(ENDPOINT + "dim?advq="+ query)
	o = xmltodict.parse(result.text)
	return result.text

def dump(sop_instance_uid):
	result = requests.get(ENDPOINT + "dim?advq="+ query)
	o = xmltodict.parse(result.text)
	return result.text	

def download(sop_instance_uid, destination="temporary_file"):
	pass

def number_of_results(query):
	result = requests.get(ENDPOINT + "dim?q="+ query)
	return result.text

#def wado(...):#
#	pass


#print search_freetext("*:*")

