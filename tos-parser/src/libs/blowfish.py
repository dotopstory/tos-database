# ****************************************************************************
#
# Copyright (c) 2007 Novell, Inc.
# All Rights Reserved.
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of version 2 of the GNU General Public License as
# published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#   |
# You should have received a copy of the GNU General Public License
# along with this program; if not, contact Novell, Inc.
#
# To contact Novell about this file by physical or electronic mail,
# you may find current contact information at www.novell.com
#
#  Author: Russ Young
#  Thanks to: Bruce Schneier / Counterpane Labs
#  for the Blowfish encryption algorithm and
#  reference implementation. http://www.schneier.com/blowfish.html
# ***************************************************************************
# Adapted by rjgtav from C# to python taking as a base
#   https://github.com/celophi/Arboretum/blob/master/Arboretum.Lib/Libraries/Blowfish.cs
#
# Note: the default key schedules have been replaced by the ones used by IMCGames in Tree of savior

N = 16
KEYBYTES = 8

P =\
[
    0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
    0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
    0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F
]

S =\
[
    [
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F
    ],
    [
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F
    ],
    [
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F
    ],
    [
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F,
        0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F, 0x5F5F5F5F
    ]
]


def F(x):
    d = (x & 0x00FF)
    x >>= 8
    c = (x & 0x00FF)
    x >>= 8
    b = (x & 0x00FF)
    x >>= 8
    a = (x & 0x00FF)
    # y = ((S[0][a] + S[1][b]) ^ S[2][c]) + S[3][d];
    y = S[0][a] + S[1][b]
    y = y ^ S[2][c]
    y = y + S[3][d]

    return y


# Encrypts a byte array in place
def Encipher(data, offset, length):
    if (length % 8) != 0:
        raise ValueError('Invalid Length')

    for i in range(offset, length + offset, 8):
        # Encode the data in 8 byte blocks.
        xl = ((data[i] << 24) | (data[i + 1] << 16) | (data[i + 2] << 8) | data[i + 3])
        xr = ((data[i + 4] << 24) | (data[i + 5] << 16) | (data[i + 6] << 8) | data[i + 7])

        xl, xr = Encipher__internal(xl, xr)
        data[i] = (xl >> 24)
        data[i + 1] = (xl >> 16)
        data[i + 2] = (xl >> 8)
        data[i + 3] = (xl)
        data[i + 4] = (xr >> 24)
        data[i + 5] = (xr >> 16)
        data[i + 6] = (xr >> 8)
        data[i + 7] = (xr)


# Encrypts 8 bytes of data (1 block)
def Encipher__internal(xl, xr):
    Xl = xl
    Xr = xr

    for i in range (0, N, 1):
        Xl = Xl ^ P[i]
        Xr = F(Xl) ^ Xr

        temp = Xl
        Xl = Xr
        Xr = temp

    temp = Xl
    Xl = Xr
    Xr = temp

    Xr = Xr ^ P[N]
    Xl = Xl ^ P[N + 1]

    return Xl, Xr


# Decrypts a byte array in place
def Decipher(data, offset, length):
    if (length % 8) != 0:
        raise ValueError('Invalid Length')

    for i in range(offset, length + offset, 8):
        # Encode the data in 8 byte blocks.
        xl = ((data[i] << 24) | (data[i + 1] << 16) | (data[i + 2] << 8) | data[i + 3])
        xr = ((data[i + 4] << 24) | (data[i + 5] << 16) | (data[i + 6] << 8) | data[i + 7])

        xl, xr = Decipher__internal(xl, xr)

        # Now Replace the data.
        data[i] = (xl >> 24) & 0xFF
        data[i + 1] = (xl >> 16) & 0xFF
        data[i + 2] = (xl >> 8) & 0xFF
        data[i + 3] = (xl) & 0xFF
        data[i + 4] = (xr >> 24) & 0xFF
        data[i + 5] = (xr >> 16) & 0xFF
        data[i + 6] = (xr >> 8) & 0xFF
        data[i + 7] = (xr) & 0xFF


# Decrypts 8 bytes of data (1 block)
def Decipher__internal(xl, xr):
    Xl = xl
    Xr = xr

    for i in range(N + 1, 1, -1):
        Xl = Xl ^ P[i]
        Xr = F(Xl) ^ Xr

        # Exchange Xl and Xr
        temp = Xl
        Xl = Xr
        Xr = temp

    # Exchange Xl and Xr
    temp = Xl
    Xl = Xr
    Xr = temp

    Xr = Xr ^ P[1]
    Xl = Xl ^ P[0]

    return Xl, Xr