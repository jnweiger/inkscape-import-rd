#!/usr/bin/env python
# coding=utf-8
#
# Copyright (C) 2023 jürgen Weigert
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA
#
# References:
# - https://inkscape.gitlab.io/extensions/documentation/tutorial/my-first-import-extension.html
# - https://github.com/jnweiger/ruida-laser/tree/master/src

import inkex
from ruidaparser import RuidaParser

class RdInput(inkex.InputExtension):
    """Load Ruida RD Files"""

    def load(self, stream):
        r = RuidaParser()
        r.decode(r.unscramble_bytes(stream.read()))
        return r.to_svg())

if __name__ == "__main__":
    RdInput().run()
