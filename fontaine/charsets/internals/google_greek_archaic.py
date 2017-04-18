# -*- coding: utf-8 -*-
from gfonts_utils import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Greek Archaic'
    native_name = u''
    abbreviation = 'GREK'

    def glyphs(self):
        glyphs = codepointsInNamelist("google_glyphsets/Greek/GF-greek-archaic.nam")
        return glyphs


