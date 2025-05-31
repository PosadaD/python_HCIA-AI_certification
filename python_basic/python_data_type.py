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


# NUMERIC: INT, FLOAT, COMPLEX
integer = 1; 
print(type(integer));

flotante = 1.3;
print(type(flotante));

# j es la convención estándar en matemáticas e ingeniería para denotar la unidad imaginaria
complexs = 5 + 6j;
print(complexs + 5);
print(type(complexs));




# TEXT: STR
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
#strings[0] = 'j'; # unchangable

# String operations
a = "hello"
b = "world"
print(a + b);


a  = "hello";
b = 2;
print(a*b)

#Common python strings methods
a = "hola mundo hey"
print(a.split(" "));

a = "hola mundo hey"
a.replace('hola', 'hello');
print(a);

a = "hello mundo hey";
print(a.lower());
print(a.upper());

words = ["Hello", "world", "from", "Python"]
sentence = " ".join(words)  # Join with a space
print(sentence)
parts = ["2025", "05", "30"]
date = "-".join(parts)
print(date)

#string formating
#You should use %s for strings and %d for integers, which are the correct placeholders for formatting.
a = "hola mundo soy %s y tengo %d" % ('pedro', 30)
print(a)





#LISTS 
a = [1,2,3,'abc'];
print(a);
#acces items
print(a[1]);
print(a[0:2]);
print(a[0:3:2]);
#change itme 
a[1] = 3;
print(a);

#list operators 
a = [1,2,3]
b = [4,5,6]
print(a*2);
print(a+b);

#list methods 
#append
animals = ['dog', 'cat'];
animals.append('fish');
print(animals);
#remove
animals.remove('dog');
print(animals);
#insert
animals.insert(1, 'coat');
print(animals);
#pop
animals.pop()
print(animals);
#sort
list1 = [12, 939, 1, 809];
list1.sort()
print(list1);
#reverse
list1.reverse();
print(list1);
#list conprehension 
squares = [a*2 for x in list1];
print(squares);

#Lists slicing and indexing
l = [[1,2],[3,4]];
print(l[1[0]]);

l = [1,2,3,4,5,6,7];
print(l[::4]);
print(l[1:4:2]);






#TUPLES
#tuples are unmutable sequences, typically used to store a colection of heterogeneous data
t = (3,[2,4],"hello");
print(type(t));
#tuple indexing 
print(t[1]);






#DICTIONARIES
#unorder colection of items, each item has a key:value
x1 = {"food":'spam', "quality":4, "color":"pink"};
x2 = dict(food="span", quality=4, color="pink")
x3 = dict([("food",'spam'),( "quality",4), ("color","pink")])
print(x, x2, x3);
#access items 
print(x1["food"]);
#extrct values with get
print(x1.get("food"));
print(x1.get("z")) # returns none using a non-existent key.
print(x1.get("z", "No encontrado"));
#extract all keys 
print(x1.keys());
print(x1.values());
print(x1.items());
#insert value into dictionary
x1["nueva_key"] = "valor_nuevo";
print(x1);
#change item 
x1["nueva_key"] = "otro_valor";
print(x1);










#SETS
#a set is an unorder collection with no duplicate elements 
set1 = {"hola", "world"}
set2 = set(["hola", "world"]);
print(set1);
print(set2);
print("data" in set1);
print("world" in set2);
#add item 
set1.add("data");
print(set1);
#remove item 
set2.remove("world");
print(set2);
#unchangeble set
frozen_set = frozenset([1,2,3,4,5,6,7]);
print(frozen_set);
#frozen_set.add(8); #no atribute add





#OPERATIONS ON DATA
#deep copy and shallow copy
#data assigment 
a = [1,2,3,[4,5,6]];
b = a #asing a to b
b[0] = 99;
print(a); 

a = [1,2,3,[4,5]];
b = a.copy(); #shallow copy
b[0] = 99;
print(a);
b[3][0] = 99;
print(a, b);

import copy
a = [1,2,[3,4]];
b = copy.deepcopy(a);
b[2][0] = 99;
print(a, b);

#OPERATORS
# Operadores Aritméticos
a = 10
b = 3
print("Suma:", a + b)  # 10 + 3
print("Resta:", a - b)  # 10 - 3
print("Multiplicación:", a * b)  # 10 * 3
print("División:", a / b)  # 10 / 3
print("División entera:", a // b)  # 10 // 3
print("Módulo (Residuo):", a % b)  # 10 % 3
print("Exponenciación:", a ** b)  # 10 ** 3
# Operadores de Comparación
x = 5
y = 10
print("x es igual a y:", x == y)  # 5 == 10
print("x no es igual a y:", x != y)  # 5 != 10
print("x es mayor que y:", x > y)  # 5 > 10
print("x es menor que y:", x < y)  # 5 < 10
print("x es mayor o igual a y:", x >= y)  # 5 >= 10
print("x es menor o igual a y:", x <= y)  # 5 <= 10
# Operadores Lógicos
a = True
b = False
print("a and b:", a and b)  # True and False
print("a or b:", a or b)  # True or False
print("not a:", not a)  # not True
# Operadores de Asignación
a = 5
a += 3  # a = a + 3
print(a)
a -= 2  # a = a - 2
print(a)
a *= 2  # a = a * 2
print(a)
a /= 4  # a = a / 4
print(a)
a //= 2  # a = a // 2
print(a)
a %= 3  # a = a % 3
print(a)
a **= 2  # a = a ** 2
print(a)
# Operadores Bitwise
a = 5  
b = 3  
print("AND (a & b):", a & b)  
print("OR (a | b):", a | b) 
print("XOR (a ^ b):", a ^ b) 
print("NOT (~a):", ~a) 
print("Left Shift (a << 1):", a << 1) 
print("Right Shift (a >> 1):", a >> 1)  
# Operadores de Membresía
a = [1, 2, 3, 4, 5]
print("1 está en la lista:", 1 in a)  # Verifica si 1 está en la lista
print("6 no está en la lista:", 6 not in a)  # Verifica si 6 no está en la lista
# Operadores de Identidad
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print("x es y:", x is y)  # Verifica si x es el mismo objeto que y
print("x es z:", x is z)  # Verifica si x es el mismo objeto que z
print("x no es y:", x is not y)  # Verifica si x no es el mismo objeto que y
# Operador Ternario
x = 5
result = "Par" if x % 2 == 0 else "Impar"
print("El número es:", result)
# Operador Lambda
suma = lambda x, y: x + y
print("La suma de 5 y 3 es:", suma(5, 3))
cuadrado = lambda x: x ** 2
print("El cuadrado de 4 es:", cuadrado(4))
