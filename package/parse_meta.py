#!/usr/bin/env python3
from lxml import etree as ET

namespace_prefix = ['dc',
                    'opf']

namespace_uri    = ['http://purl.org/dc/elements/1.1/',
                    'http://www.idpf.org/2007/opf']

namespaces = dict(zip(namespace_prefix, namespace_uri))
esin = None
def get_esin(opf_file):
    root = ET.parse(opf_file);
    esin = root.xpath('////dc:identifier[@opf:scheme="MOBI-ASIN"]', namespaces=namespaces);
    esin = esin[0].text;
    return esin;
    
  

