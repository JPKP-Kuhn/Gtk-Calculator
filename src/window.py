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

    def coefA(self, str):
        if str == 'x²':
            return 1.0
        else:
            a = str.split('x')
            return float(a[0])
        
    def coefB(self, str):
        if str == 'x':
            return 1.0
        else:
            b = str.split('x')
            return float(b[0])

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
        if '=' not in equation:
            self.equation_output.set_text('Please, digit a valid equation with =')
            return
        print(equation)
        self.equation_roots(action, equation)

    def equation_roots(self, action, equation):
        superscript = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']
        root = 1
        for i in range(10):
            if superscript[i] in equation:
                root = i      
        if root == 1:
            self.equation_output.set_text((f'Roots of the equation: {equation} are: {root}'))
            self.linear_equation(action, equation)
        elif root == 2:
            self.equation_output.set_text((f'Roots of the equation: {equation} are: {root}'))
            self.quadratic_equation(action, equation)
        else:    
            self.equation_output.set_text((f'Roots of the equation: {equation} are: {root}'))

    def linear_equation(self, action, equation):
        equation = equation.split(' ')
        c = equation[-1]
        c = float(c)
        a = self.coefB(equation[0])
        if equation[1] == '+':
            b = equation[2]
            b = float(b)
        else:
            b = equation[2]
            b = float(b) * -1
        x = (c - b) / a

        return self.equation_output.set_text(f'\n The root of the equation: {equation} is: {x}')

    def quadratic_equation(self, action, equation):
        pass


