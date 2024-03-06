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
    

    #GtkTextView
    equation_text = Gtk.Template.Child() #Where digit the equation
    #GtkLabel
    equation_output = Gtk.Template.Child() #the result of the equation

    #GtkButtons
    equation_input = Gtk.Template.Child() #the button solve


    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #solve button
        solveEquation_action = Gio.SimpleAction(name="read")
        solveEquation_action.connect("activate", self.solveEquation)
        self.add_action(solveEquation_action)

    def solveEquation(self, action, _):
        buffer = self.equation_text.get_buffer()
        start = buffer.get_start_iter()
        end = buffer.get_end_iter()
        equation = buffer.get_text(start, end, True)
        self.equation_roots(action, equation)

    def equation_roots(self, action, equation):
        superscript = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        root = 0
        for i in range(10):
            if superscript[i] in equation:
                root = i      
        if root == 0:
            self.equation_output.set_text((f'Roots of the equation: {equation} are: {root}'))
        else:    
            self.equation_output.set_text((f'Roots of the equation: {equation} are: {root}'))


