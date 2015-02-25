# define a class which has atleast 2 methods
# a get_string () method that obtains a string from console input
# a print_string ()method that prints the string in upper case
# create a separate test file to test the class and its methods
# define a class module with appropriate name




class String(object):

    def __init__(self):
        pass

    def get_string(self):
        self.input = raw_input("Please type in a string >:   ")

    def print_string(self):
        print self.input.upper()


string_object = String()
string_object.get_string()
string_object.print_string()
