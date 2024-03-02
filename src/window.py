# window.py
#
# Copyright 2024 joaopedrokuhn
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# SPDX-License-Identifier: GPL-3.0-or-later

from gi.repository import Adw, Gio, Gtk

@Gtk.Template(resource_path='/org/joaopedrokuhn/GtkCalculator/window.ui')
class GtkCalculatorWindow(Adw.ApplicationWindow):
    __gtype_name__ = 'GtkCalculatorWindow'
    

    label = Gtk.Template.Child()
    solveEquation_input = Gtk.Template.Child()
    
    solveEquation_input.props.can_default = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        solveEquation_input = Gio.SimpleAction(name="solve")
        solveEquation_input.connect("activate", self.solveEquation)
        self.add_action(solveEquation_input)

    def solveEquation(self, action, parameter):
        equation = self.solveEquation_input.get_text()
        self.label.set_text(equation)

