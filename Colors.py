#/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame

ALICEBLUE            = pygame.Color(240, 248, 255)
ANTIQUEWHITE         = pygame.Color(250, 235, 215)
AQUA                 = pygame.Color(  0, 255, 255)
AQUAMARINE           = pygame.Color(127, 255, 212)
AZURE                = pygame.Color(240, 255, 255)
BEIGE                = pygame.Color(245, 245, 220)
BISQUE               = pygame.Color(255, 228, 196)
BLACK                = pygame.Color(  0,   0,   0)
BLANCHEDALMOND       = pygame.Color(255, 235, 205)
BLUE                 = pygame.Color(  0,   0, 255)
BLUEVIOLET           = pygame.Color(138,  43, 226)
BROWN                = pygame.Color(165,  42,  42)
BURLYWOOD            = pygame.Color(222, 184, 135)
CADETBLUE            = pygame.Color( 95, 158, 160)
CHARTREUSE           = pygame.Color(127, 255,   0)
CHOCOLATE            = pygame.Color(210, 105,  30)
CORAL                = pygame.Color(255, 127,  80)
CORNFLOWERBLUE       = pygame.Color(100, 149, 237)
CORNSILK             = pygame.Color(255, 248, 220)
CRIMSON              = pygame.Color(220,  20,  60)
CYAN                 = pygame.Color(  0, 255, 255)
DARKBLUE             = pygame.Color(  0,   0, 139)
DARKCYAN             = pygame.Color(  0, 139, 139)
DARKGOLDENROD        = pygame.Color(184, 134,  11)
DARKGRAY             = pygame.Color(169, 169, 169)
DARKGREEN            = pygame.Color(  0, 100,   0)
DARKKHAKI            = pygame.Color(189, 183, 107)
DARKMAGENTA          = pygame.Color(139,   0, 139)
DARKOLIVEGREEN       = pygame.Color( 85, 107,  47)
DARKORANGE           = pygame.Color(255, 140,   0)
DARKORCHID           = pygame.Color(153,  50, 204)
DARKRED              = pygame.Color(139,   0,   0)
DARKSALMON           = pygame.Color(233, 150, 122)
DARKSEAGREEN         = pygame.Color(143, 188, 143)
DARKSLATEBLUE        = pygame.Color( 72,  61, 139)
DARKSLATEGRAY        = pygame.Color( 47,  79,  79)
DARKTURQUOISE        = pygame.Color(  0, 206, 209)
DARKVIOLET           = pygame.Color(148,   0, 211)
DEEPPINK             = pygame.Color(255,  20, 147)
DEEPSKYBLUE          = pygame.Color(  0, 191, 255)
DIMGRAY              = pygame.Color(105, 105, 105)
DODGERBLUE           = pygame.Color( 30, 144, 255)
FIREBRICK            = pygame.Color(178,  34,  34)
FLORALWHITE          = pygame.Color(255, 250, 240)
FORESTGREEN          = pygame.Color( 34, 139,  34)
FUCHSIA              = pygame.Color(255,   0, 255)
GAINSBORO            = pygame.Color(220, 220, 220)
GHOSTWHITE           = pygame.Color(248, 248, 255)
GOLD                 = pygame.Color(255, 215,   0)
GOLDENROD            = pygame.Color(218, 165,  32)
GRAY                 = pygame.Color(128, 128, 128)
GREEN                = pygame.Color(  0, 128,   0)
GREENYELLOW          = pygame.Color(173, 255,  47)
HONEYDEW             = pygame.Color(240, 255, 240)
HOTPINK              = pygame.Color(255, 105, 180)
INDIANRED            = pygame.Color(205,  92,  92)
INDIGO               = pygame.Color( 75,   0, 130)
IVORY                = pygame.Color(255, 255, 240)
KHAKI                = pygame.Color(240, 230, 140)
LAVENDER             = pygame.Color(230, 230, 250)
LAVENDERBLUSH        = pygame.Color(255, 240, 245)
LAWNGREEN            = pygame.Color(124, 252,   0)
LEMONCHIFFON         = pygame.Color(255, 250, 205)
LIGHTBLUE            = pygame.Color(173, 216, 230)
LIGHTCORAL           = pygame.Color(240, 128, 128)
LIGHTCYAN            = pygame.Color(224, 255, 255)
LIGHTGOLDENRODYELLOW = pygame.Color(250, 250, 210)
LIGHTGRAY            = pygame.Color(211, 211, 211)
LIGHTGREEN           = pygame.Color(144, 238, 144)
LIGHTPINK            = pygame.Color(255, 182, 193)
LIGHTSALMON          = pygame.Color(255, 160, 122)
LIGHTSEAGREEN        = pygame.Color( 32, 178, 170)
LIGHTSKYBLUE         = pygame.Color(135, 206, 250)
LIGHTSLATEGRAY       = pygame.Color(119, 136, 153)
LIGHTSTEELBLUE       = pygame.Color(176, 196, 222)
LIGHTYELLOW          = pygame.Color(255, 255, 224)
LIME                 = pygame.Color(  0, 255,   0)
LIMEGREEN            = pygame.Color( 50, 205,  50)
LINEN                = pygame.Color(250, 240, 230)
MAGENTA              = pygame.Color(255,   0, 255)
MAROON               = pygame.Color(128,   0,   0)
MEDIUMAQUAMARINE     = pygame.Color(102, 205, 170)
MEDIUMBLUE           = pygame.Color(  0,   0, 205)
MEDIUMORCHID         = pygame.Color(186,  85, 211)
MEDIUMPURPLE         = pygame.Color(147, 112, 219)
MEDIUMSEAGREEN       = pygame.Color( 60, 179, 113)
MEDIUMSLATEBLUE      = pygame.Color(123, 104, 238)
MEDIUMSPRINGGREEN    = pygame.Color(  0, 250, 154)
MEDIUMTURQUOISE      = pygame.Color( 72, 209, 204)
MEDIUMVIOLETRED      = pygame.Color(199,  21, 133)
MIDNIGHTBLUE         = pygame.Color( 25,  25, 112)
MINTCREAM            = pygame.Color(245, 255, 250)
MISTYROSE            = pygame.Color(255, 228, 225)
MOCCASIN             = pygame.Color(255, 228, 181)
NAVAJOWHITE          = pygame.Color(255, 222, 173)
NAVY                 = pygame.Color(  0,   0, 128)
OLDLACE              = pygame.Color(253, 245, 230)
OLIVE                = pygame.Color(128, 128,   0)
OLIVEDRAB            = pygame.Color(107, 142,  35)
ORANGE               = pygame.Color(255, 165,   0)
ORANGERED            = pygame.Color(255,  69,   0)
ORCHID               = pygame.Color(218, 112, 214)
PALEGOLDENROD        = pygame.Color(238, 232, 170)
PALEGREEN            = pygame.Color(152, 251, 152)
PALETURQUOISE        = pygame.Color(175, 238, 238)
PALEVIOLETRED        = pygame.Color(219, 112, 147)
PAPAYAWHIP           = pygame.Color(255, 239, 213)
PEACHPUFF            = pygame.Color(255, 218, 185)
PERU                 = pygame.Color(205, 133,  63)
PINK                 = pygame.Color(255, 192, 203)
PLUM                 = pygame.Color(221, 160, 221)
POWDERBLUE           = pygame.Color(176, 224, 230)
PURPLE               = pygame.Color(128,   0, 128)
RED                  = pygame.Color(255,   0,   0)
ROSYBROWN            = pygame.Color(188, 143, 143)
ROYALBLUE            = pygame.Color( 65, 105, 225)
SADDLEBROWN          = pygame.Color(139,  69,  19)
SALMON               = pygame.Color(250, 128, 114)
SANDYBROWN           = pygame.Color(244, 164,  96)
SEAGREEN             = pygame.Color( 46, 139,  87)
SEASHELL             = pygame.Color(255, 245, 238)
SIENNA               = pygame.Color(160,  82,  45)
SILVER               = pygame.Color(192, 192, 192)
SKYBLUE              = pygame.Color(135, 206, 235)
SLATEBLUE            = pygame.Color(106,  90, 205)
SLATEGRAY            = pygame.Color(112, 128, 144)
SNOW                 = pygame.Color(255, 250, 250)
SPRINGGREEN          = pygame.Color(  0, 255, 127)
STEELBLUE            = pygame.Color( 70, 130, 180)
TAN                  = pygame.Color(210, 180, 140)
TEAL                 = pygame.Color(  0, 128, 128)
THISTLE              = pygame.Color(216, 191, 216)
TOMATO               = pygame.Color(255,  99,  71)
TURQUOISE            = pygame.Color( 64, 224, 208)
VIOLET               = pygame.Color(238, 130, 238)
WHEAT                = pygame.Color(245, 222, 179)
WHITE                = pygame.Color(255, 255, 255)
WHITESMOKE           = pygame.Color(245, 245, 245)
YELLOW               = pygame.Color(255, 255,   0)
YELLOWGREEN          = pygame.Color(154, 205,  50)
