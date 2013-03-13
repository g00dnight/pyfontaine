# -*- coding: utf-8 -*-
from fontaine.cmap import library

class Charmap:
    common_name = u'Pablo Impallari\'s latin-ext subset'
    native_name = u''

    def glyphs(self):
        # latin subset from Pablo Impallari's Libre Baskerville Regular
        glyphs  = [0x0020] # space
        glyphs += [0x0021] # exclam
        glyphs += [0x0022] # quotedbl
        glyphs += [0x0023] # numbersign
        glyphs += [0x0024] # dollar
        glyphs += [0x0025] # percent
        glyphs += [0x0026] # ampersand
        glyphs += [0x0027] # quotesingle
        glyphs += [0x0028] # parenleft
        glyphs += [0x0029] # parenright
        glyphs += [0x002A] # asterisk
        glyphs += [0x002B] # plus
        glyphs += [0x002C] # comma
        glyphs += [0x002D] # hyphen
        glyphs += [0x002E] # period
        glyphs += [0x002F] # slash
        glyphs += [0x0030] # zero
        glyphs += [0x0031] # one
        glyphs += [0x0032] # two
        glyphs += [0x0033] # three
        glyphs += [0x0034] # four
        glyphs += [0x0035] # five
        glyphs += [0x0036] # six
        glyphs += [0x0037] # seven
        glyphs += [0x0038] # eight
        glyphs += [0x0039] # nine
        glyphs += [0x003A] # colon
        glyphs += [0x003B] # semicolon
        glyphs += [0x003C] # less
        glyphs += [0x003D] # equal
        glyphs += [0x003E] # greater
        glyphs += [0x003F] # question
        glyphs += [0x0040] # at
        glyphs += [0x0041] # A
        glyphs += [0x0042] # B
        glyphs += [0x0043] # C
        glyphs += [0x0044] # D
        glyphs += [0x0045] # E
        glyphs += [0x0046] # F
        glyphs += [0x0047] # G
        glyphs += [0x0048] # H
        glyphs += [0x0049] # I
        glyphs += [0x004A] # J
        glyphs += [0x004B] # K
        glyphs += [0x004C] # L
        glyphs += [0x004D] # M
        glyphs += [0x004E] # N
        glyphs += [0x004F] # O
        glyphs += [0x0050] # P
        glyphs += [0x0051] # Q
        glyphs += [0x0052] # R
        glyphs += [0x0053] # S
        glyphs += [0x0054] # T
        glyphs += [0x0055] # U
        glyphs += [0x0056] # V
        glyphs += [0x0057] # W
        glyphs += [0x0058] # X
        glyphs += [0x0059] # Y
        glyphs += [0x005A] # Z
        glyphs += [0x005B] # bracketleft
        glyphs += [0x005C] # backslash
        glyphs += [0x005D] # bracketright
        glyphs += [0x005E] # asciicircum
        glyphs += [0x005F] # underscore
        glyphs += [0x0060] # grave
        glyphs += [0x0061] # a
        glyphs += [0x0062] # b
        glyphs += [0x0063] # c
        glyphs += [0x0064] # d
        glyphs += [0x0065] # e
        glyphs += [0x0066] # f
        glyphs += [0x0067] # g
        glyphs += [0x0068] # h
        glyphs += [0x0069] # iogonek
        glyphs += [0x006A] # j
        glyphs += [0x006B] # k
        glyphs += [0x006C] # l
        glyphs += [0x006D] # m
        glyphs += [0x006E] # n
        glyphs += [0x006F] # o
        glyphs += [0x0070] # p
        glyphs += [0x0071] # q
        glyphs += [0x0072] # r
        glyphs += [0x0073] # s
        glyphs += [0x0074] # t
        glyphs += [0x0075] # u
        glyphs += [0x0076] # v
        glyphs += [0x0077] # w
        glyphs += [0x0078] # x
        glyphs += [0x0079] # y
        glyphs += [0x007A] # z
        glyphs += [0x007B] # braceleft
        glyphs += [0x007C] # bar
        glyphs += [0x007D] # braceright
        glyphs += [0x007E] # asciitilde
        glyphs += [0x00A0] # nonbreakingspace
        glyphs += [0x00A1] # exclamdown
        glyphs += [0x00A2] # cent
        glyphs += [0x00A3] # sterling
        glyphs += [0x00A4] # currency
        glyphs += [0x00A5] # yen
        glyphs += [0x00A6] # brokenbar
        glyphs += [0x00A7] # section
        glyphs += [0x00A8] # dieresis
        glyphs += [0x00A9] # copyright
        glyphs += [0x00AA] # ordfeminine
        glyphs += [0x00AB] # guillemotleft
        glyphs += [0x00AC] # logicalnot
        glyphs += [0x00AD] # uni00AD
        glyphs += [0x00AE] # registered
        glyphs += [0x00AF] # macron
        glyphs += [0x00B0] # degree
        glyphs += [0x00B1] # plusminus
        glyphs += [0x00B2] # twosuperior
        glyphs += [0x00B3] # threesuperior
        glyphs += [0x00B4] # acute
        glyphs += [0x00B5] # mu
        glyphs += [0x00B6] # paragraph
        glyphs += [0x00B7] # periodcentered
        glyphs += [0x00B8] # cedilla
        glyphs += [0x00B9] # onesuperior
        glyphs += [0x00BA] # ordmasculine
        glyphs += [0x00BB] # guillemotright
        glyphs += [0x00BC] # onequarter
        glyphs += [0x00BD] # onehalf
        glyphs += [0x00BE] # threequarters
        glyphs += [0x00BF] # questiondown
        glyphs += [0x00C0] # Agrave
        glyphs += [0x00C1] # Aacute
        glyphs += [0x00C2] # Acircumflex
        glyphs += [0x00C3] # Atilde
        glyphs += [0x00C4] # Adieresis
        glyphs += [0x00C5] # Aring
        glyphs += [0x00C6] # AE
        glyphs += [0x00C7] # Ccedilla
        glyphs += [0x00C8] # Egrave
        glyphs += [0x00C9] # Eacute
        glyphs += [0x00CA] # Ecircumflex
        glyphs += [0x00CB] # Edieresis
        glyphs += [0x00CC] # Igrave
        glyphs += [0x00CD] # Iacute
        glyphs += [0x00CE] # Icircumflex
        glyphs += [0x00CF] # Idieresis
        glyphs += [0x00D0] # Eth
        glyphs += [0x00D1] # Ntilde
        glyphs += [0x00D2] # Ograve
        glyphs += [0x00D3] # Oacute
        glyphs += [0x00D4] # Ocircumflex
        glyphs += [0x00D5] # Otilde
        glyphs += [0x00D6] # Odieresis
        glyphs += [0x00D7] # multiply
        glyphs += [0x00D8] # Oslash
        glyphs += [0x00D9] # Ugrave
        glyphs += [0x00DA] # Uacute
        glyphs += [0x00DB] # Ucircumflex
        glyphs += [0x00DC] # Udieresis
        glyphs += [0x00DD] # Yacute
        glyphs += [0x00DE] # Thorn
        glyphs += [0x00DF] # germandbls
        glyphs += [0x00E0] # agrave
        glyphs += [0x00E1] # aacute
        glyphs += [0x00E2] # acircumflex
        glyphs += [0x00E3] # atilde
        glyphs += [0x00E4] # adieresis
        glyphs += [0x00E5] # aring
        glyphs += [0x00E6] # ae
        glyphs += [0x00E7] # ccedilla
        glyphs += [0x00E8] # egrave
        glyphs += [0x00E9] # eacute
        glyphs += [0x00EA] # ecircumflex
        glyphs += [0x00EB] # edieresis
        glyphs += [0x00EC] # igrave
        glyphs += [0x00ED] # iacute
        glyphs += [0x00EE] # icircumflex
        glyphs += [0x00EF] # idieresis
        glyphs += [0x00F0] # eth
        glyphs += [0x00F1] # ntilde
        glyphs += [0x00F2] # ograve
        glyphs += [0x00F3] # oacute
        glyphs += [0x00F4] # ocircumflex
        glyphs += [0x00F5] # otilde
        glyphs += [0x00F6] # odieresis
        glyphs += [0x00F7] # divide
        glyphs += [0x00F8] # oslash
        glyphs += [0x00F9] # ugrave
        glyphs += [0x00FA] # uacute
        glyphs += [0x00FB] # ucircumflex
        glyphs += [0x00FC] # udieresis
        glyphs += [0x00FD] # yacute
        glyphs += [0x00FE] # thorn
        glyphs += [0x00FF] # ydieresis
        glyphs += [0x0100] # Amacron
        glyphs += [0x0101] # amacron
        glyphs += [0x0102] # Abreve
        glyphs += [0x0103] # abreve
        glyphs += [0x0104] # Aogonek
        glyphs += [0x0105] # aogonek
        glyphs += [0x0106] # Cacute
        glyphs += [0x0107] # cacute
        glyphs += [0x0108] # Ccircumflex
        glyphs += [0x0109] # ccircumflex
        glyphs += [0x010A] # Cdotaccent
        glyphs += [0x010B] # cdotaccent
        glyphs += [0x010C] # Ccaron
        glyphs += [0x010D] # ccaron
        glyphs += [0x010E] # Dcaron
        glyphs += [0x010F] # dcaron
        glyphs += [0x0110] # Dcroat
        glyphs += [0x0111] # dcroat
        glyphs += [0x0112] # Emacron
        glyphs += [0x0113] # emacron
        glyphs += [0x0114] # Ebreve
        glyphs += [0x0115] # ebreve
        glyphs += [0x0116] # Edotaccent
        glyphs += [0x0117] # edotaccent
        glyphs += [0x0118] # Eogonek
        glyphs += [0x0119] # eogonek
        glyphs += [0x011A] # Ecaron
        glyphs += [0x011B] # ecaron
        glyphs += [0x011C] # Gcircumflex
        glyphs += [0x011D] # gcircumflex
        glyphs += [0x011E] # Gbreve
        glyphs += [0x011F] # gbreve
        glyphs += [0x0120] # Gdotaccent
        glyphs += [0x0121] # gdotaccent
        glyphs += [0x0122] # Gcommaaccent
        glyphs += [0x0123] # gcommaaccent
        glyphs += [0x0124] # Hcircumflex
        glyphs += [0x0125] # hcircumflex
        glyphs += [0x0126] # Hbar
        glyphs += [0x0127] # hbar
        glyphs += [0x0128] # Itilde
        glyphs += [0x0129] # itilde
        glyphs += [0x012A] # Imacron
        glyphs += [0x012B] # imacron
        glyphs += [0x012C] # Ibreve
        glyphs += [0x012D] # ibreve
        glyphs += [0x012E] # Iogonek
        glyphs += [0x012F] # iogonek
        glyphs += [0x0130] # Idotaccent
        glyphs += [0x0131] # dotlessi
        glyphs += [0x0132] # IJ
        glyphs += [0x0133] # ij
        glyphs += [0x0134] # Jcircumflex
        glyphs += [0x0135] # jcircumflex
        glyphs += [0x0136] # Kcommaaccent
        glyphs += [0x0137] # kcommaaccent
        glyphs += [0x0138] # kgreenlandic
        glyphs += [0x0139] # Lacute
        glyphs += [0x013A] # lacute
        glyphs += [0x013B] # Lcommaaccent
        glyphs += [0x013C] # lcommaaccent
        glyphs += [0x013D] # Lcaron
        glyphs += [0x013E] # lcaron
        glyphs += [0x013F] # Ldot
        glyphs += [0x0140] # ldot
        glyphs += [0x0141] # Lslash
        glyphs += [0x0142] # lslash
        glyphs += [0x0143] # Nacute
        glyphs += [0x0144] # nacute
        glyphs += [0x0145] # Ncommaaccent
        glyphs += [0x0146] # ncommaaccent
        glyphs += [0x0147] # Ncaron
        glyphs += [0x0148] # ncaron
        glyphs += [0x0149] # napostrophe
        glyphs += [0x014A] # Eng
        glyphs += [0x014B] # eng
        glyphs += [0x014C] # Omacron
        glyphs += [0x014D] # omacron
        glyphs += [0x014E] # Obreve
        glyphs += [0x014F] # obreve
        glyphs += [0x0150] # Ohungarumlaut
        glyphs += [0x0151] # ohungarumlaut
        glyphs += [0x0152] # OE
        glyphs += [0x0153] # oe
        glyphs += [0x0154] # Racute
        glyphs += [0x0155] # racute
        glyphs += [0x0156] # Rcommaaccent
        glyphs += [0x0157] # rcommaaccent
        glyphs += [0x0158] # Rcaron
        glyphs += [0x0159] # rcaron
        glyphs += [0x015A] # Sacute
        glyphs += [0x015B] # sacute
        glyphs += [0x015C] # Scircumflex
        glyphs += [0x015D] # scircumflex
        glyphs += [0x015E] # uni015E
        glyphs += [0x015F] # uni015F
        glyphs += [0x0160] # Scaron
        glyphs += [0x0161] # scaron
        glyphs += [0x0162] # uni0162
        glyphs += [0x0163] # uni0163
        glyphs += [0x0164] # Tcaron
        glyphs += [0x0165] # tcaron
        glyphs += [0x0166] # Tbar
        glyphs += [0x0167] # tbar
        glyphs += [0x0168] # Utilde
        glyphs += [0x0169] # utilde
        glyphs += [0x016A] # Umacron
        glyphs += [0x016B] # umacron
        glyphs += [0x016C] # Ubreve
        glyphs += [0x016D] # ubreve
        glyphs += [0x016E] # Uring
        glyphs += [0x016F] # uring
        glyphs += [0x0170] # Uhungarumlaut
        glyphs += [0x0171] # uhungarumlaut
        glyphs += [0x0172] # Uogonek
        glyphs += [0x0173] # uogonek
        glyphs += [0x0174] # Wcircumflex
        glyphs += [0x0175] # wcircumflex
        glyphs += [0x0176] # Ycircumflex
        glyphs += [0x0177] # ycircumflex
        glyphs += [0x0178] # Ydieresis
        glyphs += [0x0179] # Zacute
        glyphs += [0x017A] # zacute
        glyphs += [0x017B] # Zdotaccent
        glyphs += [0x017C] # zdotaccent
        glyphs += [0x017D] # Zcaron
        glyphs += [0x017E] # zcaron
        glyphs += [0x018F] # Schwa
        glyphs += [0x0192] # florin
        glyphs += [0x01C4] # uni01C4
        glyphs += [0x01C5] # uni01C5
        glyphs += [0x01C6] # uni01C6
        glyphs += [0x01C7] # uni01C7
        glyphs += [0x01C8] # uni01C8
        glyphs += [0x01C9] # uni01C9
        glyphs += [0x01CA] # uni01CA
        glyphs += [0x01CB] # uni01CB
        glyphs += [0x01CC] # uni01CC
        glyphs += [0x01EA] # Oogonek
        glyphs += [0x01EB] # oogonek
        glyphs += [0x01F1] # uni01F1
        glyphs += [0x01F2] # uni01F2
        glyphs += [0x01F3] # uni01F3
        glyphs += [0x01FA] # Aringacute
        glyphs += [0x01FB] # aringacute
        glyphs += [0x01FC] # AEacute
        glyphs += [0x01FD] # aeacute
        glyphs += [0x01FE] # Oslashacute
        glyphs += [0x01FF] # oslashacute
        glyphs += [0x0218] # uni0218
        glyphs += [0x0219] # uni0219
        glyphs += [0x021A] # uni021A
        glyphs += [0x021B] # uni021B
        glyphs += [0x0237] # dotlessj
        glyphs += [0x0259] # schwa
        glyphs += [0x02BC] # apostrophe
        glyphs += [0x02C6] # circumflex
        glyphs += [0x02C7] # caron
        glyphs += [0x02D8] # breve
        glyphs += [0x02D9] # dotaccent
        glyphs += [0x02DA] # ring
        glyphs += [0x02DB] # ogonek
        glyphs += [0x02DC] # tilde
        glyphs += [0x02DD] # hungarumlaut
        glyphs += [0x03BC] # uni03BC
        glyphs += [0x1E0C] # Ddotbelow
        glyphs += [0x1E0D] # ddotbelow
        glyphs += [0x1E24] # Hdotbelow
        glyphs += [0x1E25] # hdotbelow
        glyphs += [0x1E44] # Ndotaccent
        glyphs += [0x1E45] # ndotaccent
        glyphs += [0x1E5A] # Rdotbelow
        glyphs += [0x1E5B] # rdotbelow
        glyphs += [0x1E62] # Sdotbelow
        glyphs += [0x1E63] # sdotbelow
        glyphs += [0x1E6C] # Tdotbelow
        glyphs += [0x1E6D] # tdotbelow
        glyphs += [0x1E80] # Wgrave
        glyphs += [0x1E81] # wgrave
        glyphs += [0x1E82] # Wacute
        glyphs += [0x1E83] # wacute
        glyphs += [0x1E84] # Wdieresis
        glyphs += [0x1E85] # wdieresis
        glyphs += [0x1E92] # Zdotbelow
        glyphs += [0x1E93] # zdotbelow
        glyphs += [0x1EB8] # Edotbelow
        glyphs += [0x1EB9] # edotbelow
        glyphs += [0x1EBC] # Etilde
        glyphs += [0x1EBD] # etilde
        glyphs += [0x1ECA] # Idotbelow
        glyphs += [0x1ECB] # idotbelow
        glyphs += [0x1ECC] # Odotbelow
        glyphs += [0x1ECD] # odotbelow
        glyphs += [0x1EE4] # Udotbelow
        glyphs += [0x1EE5] # udotbelow
        glyphs += [0x1EF2] # Ygrave
        glyphs += [0x1EF3] # ygrave
        glyphs += [0x1EF8] # Ytilde
        glyphs += [0x1EF9] # ytilde
        glyphs += [0x2013] # endash
        glyphs += [0x2014] # emdash
        glyphs += [0x2018] # quoteleft
        glyphs += [0x2019] # quoteright
        glyphs += [0x201A] # quotesinglbase
        glyphs += [0x201C] # quotedblleft
        glyphs += [0x201D] # quotedblright
        glyphs += [0x201E] # quotedblbase
        glyphs += [0x2020] # dagger
        glyphs += [0x2021] # daggerdbl
        glyphs += [0x2022] # bullet
        glyphs += [0x2026] # ellipsis
        glyphs += [0x2030] # perthousand
        glyphs += [0x2039] # guilsinglleft
        glyphs += [0x203A] # guilsinglright
        glyphs += [0x2044] # fraction
        glyphs += [0x2070] # zerosuperior
        glyphs += [0x2074] # foursuperior
        glyphs += [0x2075] # fivesuperior
        glyphs += [0x2076] # sixsuperior
        glyphs += [0x2077] # sevensuperior
        glyphs += [0x2078] # eightsuperior
        glyphs += [0x2079] # ninesuperior
        glyphs += [0x2080] # zeroinferior
        glyphs += [0x2081] # oneinferior
        glyphs += [0x2082] # twoinferior
        glyphs += [0x2083] # threeinferior
        glyphs += [0x2084] # fourinferior
        glyphs += [0x2085] # fiveinferior
        glyphs += [0x2086] # sixinferior
        glyphs += [0x2087] # seveninferior
        glyphs += [0x2088] # eightinferior
        glyphs += [0x2089] # nineinferior
        glyphs += [0x20AC] # Euro
        glyphs += [0x2120] # servicemark
        glyphs += [0x2122] # trademark
        glyphs += [0x2153] # onethird
        glyphs += [0x2154] # twothirds
        glyphs += [0x215B] # oneeighth
        glyphs += [0x215C] # threeeighths
        glyphs += [0x215D] # fiveeighths
        glyphs += [0x215E] # seveneighths
        glyphs += [0x2212] # minus
        glyphs += [0x2215] # uni2215
        glyphs += [0x2219] # uni2219
        glyphs += [0xFB00] # f_f
        glyphs += [0xFB01] # f_i
        glyphs += [0xFB02] # f_l
        glyphs += [0xFB03] # f_f_i
        glyphs += [0xFB04] # f_f_l
        return glyphs

library.register(Charmap)