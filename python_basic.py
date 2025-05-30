# Hello world 
print("Hello world")

# Variables
a=1;
print(a);
print(type(a));

a=2;
print(a)
print(type(a));

# Naming rules, variables names should have a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
aA_B1 = 1
print(aA_B1);

# But your need to create a name that make sense.
prince = 1000;
number_of_shoes = 30;
print(prince, number_of_shoes);


# Don't start a name whit a digit
#20a = "No funciona";

# Keyowrds 
# Keyword are thw reserved words in python. they cannot e used as ordinary identifiers and must be spelled exactly.
import keyword 
print(keyword.kwlist);

#Swiching values 
a = 1;
b = 2;
print(a, b);

a,b = b, a;
print(a, b);

# Execution order in python (from top to bottom)
x = 0;
#print(x+y); #name 'y' is not define
y = 1;

# Indentation 
#A code block starts with indentation and ends whit the first undentation line.
def function(a, b):
    print(a + b);

function(1,2);

#Global variables and local variables 
variable_global = "variable global";
def function1():
    variable_local = variable_local;
    print(variable_local);

#print(variable_global, variable_local); #error variable no decalrada 

# Standar input 
input_nombre = input("nombre: ");
print(input_nombre);

#help() function 
help(print);

# type() fucntion 
a = "Hola";
print(type(a));

# del() function
# del fucntion deletes an object 
a = 1; 
del(a);
#print(a); # objeno is not define

# len() function 
# len fucntion returns the length of an object 
print(len("hello"));

## PYTHON DATA TYPES
# numeric: int, float, complex
integer = 1; 
print(type(integer));

flotante = 1.3;
print(type(flotante));

# j es la convención estándar en matemáticas e ingeniería para denotar la unidad imaginaria
complexs = 5 + 6j;
print(complexs + 5);
print(type(complexs));

# Text: str
texto = "hola es un string";
print(type(texto));

# Escape sequence 
s = "\"python\""
print(s);

# Raw string 
# sometimes we may wish to ignore the escape sequences inside a string, to do this we can place r or R in front of the string.
raw = r"C:\abc\abc\abc.txt"
print(raw);

# Acces character in a string 
strings = "hola"
print(strings[0]);
print(strings[1]);
print(strings[-1]);
#print(strings[99]); # string out of range
print(strings[0:3]);
print(strings[0:4:2]);
strings[0] = 'j'; # unchangable


# String operations
