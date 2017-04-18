# -*- coding: utf-8 -*-
from gfonts_utils import codepointsInNamelist

class Charset:
    common_name = u'Google Fonts: Greek Plus'
    native_name = u''
    abbreviation = 'GREK'

    def glyphs(self):
        glyphs = codepointsInNamelist("google_glyphsets/Greek/GF-greek-plus.nam")
        return glyphs


