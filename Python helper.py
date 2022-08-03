# Основные команды
# Basic commands

print() # Команда для вывода данных 
        # Data output command

input() # Команда для ввода данных
        # Data entry command

len() # Считает длину строки
      # Counts the length of a string

min() # Находит минимальное значение
      # Finds the minimum value

max() # Находит максимальное значение
      # Finds the maximum value

sum() # Функция sum() принимает в качестве параметра список чисел и вычисляет сумму его элементов
      # The sum() function takes a list of numbers as a parameter and calculates the sum of its elements

merge() # Слияние отсортированных списков в один
        # Merging sorted lists into one

ord() # Позволяет определить код некоторого символа в таблице символов Unicode. Аргументом данной функции является одиночный символ
      # Allows you to determine the code of some character in the Unicode character table. The argument to this function is a single character

chr() # Позволяет определить по коду символа сам символ. Аргументом данной функции является численный код
      # Allows you to determine the character itself by the character code. The argument of this function is a numerical code

type() # Выводит тип переменной
       # Displays the type of a variable

isinstance(object, type) # Проверка соответствия типа объекта какому-либо типу данных
                         # Check if the object type matches some data type

_ is None # Проверка на тип NoneType
          # Check for type NoneType

from _ import * # _ - какой файл импортируем (без .py), вместо * можно вписать только те функции и/или переменные, которые нужны (* - всё, что есть)
                # _ - which file we import (without .py), instead of *, you can enter only those functions and/or variables that are needed (* - everything that is)

"\\" # Для вывода \
     # To output \
(f"{}") # Добавление переменной в строку, для добавление переменную нужно писать в {}
  # Adding a variable to a string, to add a variable need to write in {}



# Типы данных
# Data types


# Тип string (строка)
# Type string (string)

str() # Преобразование цифры в строку
      # Converting a digit to a string

line = "1"


# Тип integer (целое число)
# Type integer (integer)

int() # Преобразование строки в цифру (целое число)
      # Convert string to digit (integer)

line = 1


# Тип float (число с плавающей запятой)
# Type float (floating point number)

float() # Преобразование строки в цифру с плавающей запятой
        # Convert string to float

line = 1.0


# Тип list (список)
# Type list (list)

list() # Создаёт пустой список и превращает некоторые типы объектов в список
       # Creates an empty list and turns some types of objects into a list

list = [1, "1"]


# Тип tuple (кортеж)
# Type tuple (tuple)

tuple() # Из списка в кортеж
        # From list to tuple

tuple = (1,"1")

# Неизменяемая версия списка
# Immutable list version


# Тип set (множество)
# Type set (set)

set() # Создаёт пустое множество или преобразовывает некоторые типы объектов в множества
      # Creates an empty set or converts some object types to sets

set = {1, "1"}

dictionary = {} # Таки образом создаётся словарь, а не множество
                # This creates a dictionary, not a set

# Множество не может содержать список
# A set cannot contain a list

# Множество не может содержать множество
# A set cannot contain a set

# Множество может содержать кортеж
# Set can contain a tuple


# Тип frozenset (замороженной множество)
# Type frozenset (frozen set)

frozenset() # Создаёт замороженной множество (неизменяемое), принимает другую коллекцию
            # Creates a frozen set (immutable), accepts another collection

# Неизменяемая версия обычного множества
# An immutable version of a normal set
        
        
# Тип dict (словарь)
# Type dict (dictionary)

dictionary = dict() # = {}
dictionary = {} # = dict()

# Словарь - изменяемая упорядоченная коллекция, у которой элементы имеют произвольные индексы - ключи
# Dictionary is a mutable ordered collection whose elements have arbitrary indexes - keys

_.fromkeys() # Если необходимо создать словарь, каждому ключу которого соответствует одно и то же значение (Если второго значени нет, передаётся значение типа None)
             # If you need to create a dictionary, each key of which corresponds to the same value (If there is no second value, a value of type None is passed)

# Индесация словаря происходит по ключу
# Dictionary indexing occurs by key


# Тип NoneType (пустота)
# Type NoneType (blank)

var = None # None присваивает тип NoneType
           # None assigns type to NoneType



# Функции ord и chr являются взаимно обратными. Для них выполнены равенства
# The ord and chr functions are mutually inverse. They satisfy the equalities

chr(ord('A')) = 'A', ord(chr(65)) = 65

_ in _   # Позволяет проверить, что одна строка находится внутри другой или нет
         # Allows you to check if one string is inside another or not



# Параметры
# Parameters

sep="" # Разделитель при выводе
       # Output delimiter

end="" # Специальное окончание при выводе
       # Special ending on withdrawal

"\n" # Перевод строки (newline) или """_"""
     # Line feed (newline) or """_"""

"\r" # Перемещает курсор в начало строки (return)
     # Moves the cursor to the beginning of the line (return)

"\t" # Отступ (без кавычек) (tab)
     # Indentation (no quotes) (tab)

"\b" # Перевод на один символ назад (backspace)
     # Translation back one character (backspace)



# Арифметика
# Arithmetic

+ # Плюс
  # Plus

- # Минус
  # Minus

* # Умножить
  # Multiply

/ # Делить
  # Divide

** # Степень
   # Degree

// # Целочисленное деление
   # Integer division

% # Остаток от деления 
  # Remainder of the division

x += 4 # Равнозначен x = x + 4
       # Equivalent x = x + 4



# Модуль math
# Math module

import math # Надо использовать math.ключевое слово
            # Must use math.keyword

from math import * # Дальше нужно только ключевое слово
                   # All you need is a keyword

from math import команды # Без math.ключевое слово только указанные ключевые слова
                         # Without math.keyword only specified keywords


# Округления
# Rounding

round(x) # Округляет число x до ближайшего целого. Если дробная часть числа равна 0.5, то число округляется до ближайшего четного числа
         # Rounds x to the nearest integer. If the fractional part of the number is 0.5, then the number is rounded up to the nearest even number

round(x, n) # Округляет число x до n знаков после точки
            # Rounds a number x to n decimal places

floor(x) # Округляет число x вниз ("пол")
         # Rounds the number x down ("floor")

ceil(x) # Округляет число x вверх ("потолок")
        # Rounds x up ("ceiling")

abs(x) # Модуль числа x (абсолютная величина)
       # Modulus of x (absolute value)


# Корни, логарифмы, степени и факториал
# Roots, logarithms, powers, and factorial

sqrt(x)	# Квадратный корень числа x
        # The square root of x

pow(x, n) # Возведение числа x в степень n, можно заменить на x**n
          # Raising a number x to the power n, can be replaced by x**n

log(x) # Натуральный логарифм числа x. Основание натурального логарифма равно числу e
       # The natural logarithm of the number x. The base of the natural logarithm is equal to the number e

log10(x) # Десятичный логарифм числа x. Основание десятичного логарифма равно числу 10
         # Decimal logarithm of x. The base of the decimal logarithm is equal to the number 10

log(x, b) # Логарифм числа x по основанию b
          # Logarithm of x to base b

factorial(n) # Факториал натурального числа n
             # Factorial of a natural number n


# Тригонометрия
# Trigonometry

degrees(x) # Преобразует угол x, заданный в радианах, в градусы
           # Converts an x angle given in radians to degrees

radians(x) # Преобразует угол x, заданный в градусах, в радианы
           # Converts an x angle given in degrees to radians

cos(x) # Косинус угла x, задаваемого в радианах
       # Cosine of angle x given in radians

sin(x) # Синус угла x, задаваемого в радианах
       # Sine of angle x given in radians

tan(x) # Тангенс угла x, задаваемого в радианах
       # Tangent of angle x given in radians

acos(x) # Возвращает угол в радианах от 0 до π, cos которого равен x
        # Returns the angle in radians from 0 to π whose cos is x

asin(x) # Возвращает угол в радианах от - π/2 до π/2, sin которого равен x
        # Returns the angle in radians from - π/2 to π/2, whose sin is equal to x

atan(x) # Возвращает угол в радианах от - π/2 до π/2, tan которого равен x
        # Returns the angle in radians from - π/2 to π/2, whose tan is equal to x


# Константа
# Constant

pi # Число π = 3.141592653589793
   # Number π = 3.141592653589793

e # Число e = 2.718281828459045 (константа Эйлера)
  # Number e = 2.718281828459045 (Euler constant)



# Условия
# Terms

if _: # Если
      # If

elif _: # Иначе если
        # Otherwise, if

else: # Иначе
      # Otherwise


# Сравнение
# Compare

== # Равно
   # Equally

!= # Не равно
   # Not equally

> # Больше
  # More

< # Меньше
  # Less

>= # Больше или равно
   # More than or equal to

<= # Меньше либо равен
   # Less than or equal to

# Логические операторы
# Logical operators

and # И
    # And

or # Или
   # Or

not # Не
    # Not



# Цикл for
# Cycle for

for условие:
    блок кода

for condition:
     code block

range() # Количество повтора цикла
        # Number of cycle repeat

range(x, y, z) # x - старт последовательности (обязательно), y - стоп последовательности (не обязательно), z - величина шага (не обязательно)
               # x - sequence start (mandatory), y - sequence stop (optional), z - step size (optional)

# Цикл while
# Cycle while

# Циклы, повторяющиеся до наступления определенного события
# Cycles that repeat until a certain event occurs

while условие:
    блок кода

while condition:
     code block


# Операторы циклов
# Loop statements

if pass: # Skip it!
      break # Прерывает выполнение цикла
            # Breaks the loop

      continue # Переходит к следующей итерации цикла
               # Moves to the next iteration of the loop

else # Выполняется, когда штатным образом завершается цикл
# Executed when the cycle ends normally



# Индексация
# Indexing

# 'AB' + 'cd' = 'ABcd'
# 'A' + '7' + 'B'	= 'A7B'
# 'Hi'* 4	= 'HiHiHiHi'

s = Python
s[0] = s[-6] # P
s[1] = s[-5] # y
s[2] = s[-4] # t
s[3] = s[-3] # h
s[4] = s[-2] # o
s[5] = s[-1] # n



# Срезы
# Slices

s = 'abcdefghij'

s[2:5] # cde - строка состоящая из символов с индексами 2, 3, 4
       # cde - string consisting of characters with indexes 2, 3, 4

s[:5] # abcde - первые пять символов строки
      # abcde - the first five characters of the string

s[5:] # fghij - строка состоящая из символов с индексами от 5 до конца
      # fghij - a string consisting of characters with indices from 5 to the end

s[-2:] # ij - последние два символа строки
       # ij - the last two characters of the string

s[:] # abcdefghij - вся строка целиком
     # abcdefghij - entire string

s[1:7:2] # bdf - строка состоящая из каждого второго символа с индексами от 1 до 6
         # bdf - a string consisting of every second character with indices from 1 to 6

s[::-1] # jihgfedcba - строка в обратном порядке, так как шаг отрицательный
        # jihgfedcba - string in reverse order, since step is negative

s[4] = 'X' # заменяет символ с индексом 4 на 'X'
           # replaces character at index 4 with 'X'

s = s[:4] + 'X' + s[5:] # Мы создаем два среза: от начала строки до 3 символа и с 5 символа по конец строки, а между ними вставляем нужный нам символ, который встанет на 4 позицию
                        # We create two slices: from the beginning of the line to the 3rd character and from the 5th character to the end of the line, and between them we insert the character we need, which will take the 4th position



# Методы строк
# String Methods

# Строковый тип данных, основные методы конвертации регистра
# String data type, basic case conversion methods

_.capitalize() # Возвращает копию строки, в которой первый символ имеет верхний регистр, а все остальные символы имеют нижний регистр
               # Returns a copy of a string where the first character is uppercase and all other characters are lowercase

_.swapcase() # Возвращает копию строки, в которой все символы, имеющие верхний регистр, преобразуются в символы нижнего регистра и наоборот
             # Returns a copy of a string in which all uppercase characters are converted to lowercase characters and vice versa

_.title() # Возвращает копию строки, в которой первый символ каждого слова переводится в верхний регистр
          # Returns a copy of the string in which the first character of each word is converted to uppercase

# Этот метод использует довольно простой алгоритм: он не пытается различить важные и неважные слова и не обрабатывает аббревиатуры и апострофы
# This method uses a fairly simple algorithm: it does not try to distinguish between important and unimportant words, and does not handle abbreviations and apostrophes.

_.lower() # Возвращает копию строки, в которой все символы имеют нижний регистр
          # Returns a copy of the string where all characters are lowercase

_.upper() # Возвращает копию строки, в которой все символы имеют верхний регистр
          # Returns a copy of a string where all characters are uppercase



# Строковый тип данных, основные методы поиска и замены
# String data type, basic search and replace methods

_.count() # count(<sub>, <start>, <end>) считает количество непересекающихся вхождений подстроки <sub> в исходную строк, <start> - начальный символ, <end> - конечный символ
          # count(<sub>, <start>, <end>) counts the number of non-overlapping occurrences of the substring <sub> in the source string, <start> is the start character, <end> is the end character

_.startswith() # startswith(<suffix>, <start>, <end>) определяет начинается ли исходная строка подстрокой <suffix>. Если исходная строка начинается с подстроки <suffix>, метод возвращает значение True, а если нет, то False
               # startswith(<suffix>, <start>, <end>) determines if the source string begins with the <suffix> substring. If the source string starts with the substring <suffix>, the method returns True, and if not, then False

_.endswith() # endswith(<suffix>, <start>, <end>) определяет оканчивается ли исходная строка s подстрокой <suffix>. Метод возвращает значение True если исходная строка оканчивается на подстроку <suffix> и False в противном случае
             # endswith(<suffix>, <start>, <end>) determines whether the source string s ends with the <suffix> substring. The method returns True if the source string ends with the substring <suffix> and False otherwise

_.find() # find(<sub>, <start>, <end>) находит индекс первого вхождения подстроки <sub> в исходной строке. Если строка не содержит подстроки <sub>, то метод возвращает значение -1. Мы можем использовать данный метод наравне с оператором in для проверки: содержит ли заданная строка некоторую подстроку или нет
         # find(<sub>, <start>, <end>) finds the index of the first occurrence of the substring <sub> in the source string. If the string does not contain the substring <sub>, then the method returns -1. We can use this method along with the in operator to check if the given string contains some substring or not

_.rfind() # rfind(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки
          # rfind(<sub>, <start>, <end>) is identical to the find(<sub>, <start>, <end>) method, except that it looks for the first occurrence of the substring <sub> starting from the end of the string

_.index() # index(<sub>, <start>, <end>) идентичен методу find(<sub>, <start>, <end>), за тем исключением, что он вызывает ошибку  ValueError: substring not found во время выполнения программы, если подстрока <sub> не найдена
          # index(<sub>, <start>, <end>) is identical to the find(<sub>, <start>, <end>) method, except that it raises a ValueError: substring not found error at runtime if substring <sub> not found

_.rindex() # rindex(<sub>, <start>, <end>) идентичен методу index(<sub>, <start>, <end>), за тем исключением, что он ищет первое вхождение подстроки <sub> начиная с конца строки
           # rindex(<sub>, <start>, <end>) is identical to the index(<sub>, <start>, <end>) method, except that it looks for the first occurrence of the substring <sub> starting from the end of the string

# Методы find() и rfind() являются более безопасными чем index() и rindex(), так как не приводят к возникновению ошибки во время выполнения программы
# The find() and rfind() methods are safer than index() and rindex() as they don't cause runtime errors

_.strip() # strip() возвращает копию строки у которой удалены все пробелы стоящие в начале и конце строки
          # strip() returns a copy of the string with all whitespace removed from the beginning and end of the string

_.lstrip() # lstrip() возвращает копию строки у которой удалены все пробелы стоящие в начале строки
           # lstrip() returns a copy of the string with all spaces at the beginning of the string removed

_.rstrip() # rstrip() возвращает копию строки у которой удалены все пробелы стоящие в конце строки
           # rstrip() returns a copy of the string with all trailing spaces removed

# Методы strip(), lstrip(), rstrip() могут принимать на вход опциональный аргумент <chars>. Необязательный аргумент <chars>– это строка, которая определяет набор символов для удаления
# The strip(), lstrip(), rstrip() methods can take an optional <chars> argument as input. The optional <chars> argument is a string that specifies the set of characters to remove

_.replace() # replace(<old>, <new>) возвращает копию со всеми вхождениями подстроки <old>, замененными на <new>
            # replace(<old>, <new>) returns a copy with all occurrences of the substring <old> replaced with <new>

# replace() может принимать опциональный третий аргумент <count>,  который определяет количество замен
# replace() can take an optional third <count> argument that specifies the number of replacements



# Строковый тип данных, основные методы классификации символов
# String data type, basic character classification methods

_.isalnum() # isalnum() определяет, состоит ли исходная строка из буквенно-цифровых символов. Метод возвращает значение True если исходная строка является                       непустой и состоит только из буквенно-цифровых символов и False в противном случае
            # isalnum() determines if the input string consists of alphanumeric characters. The method returns True if the source string is non-empty and consists only of alphanumeric characters and False otherwise

_.isalpha() # isalpha() определяет, состоит ли исходная строка из буквенных символов. Метод возвращает значение True если исходная строка является непустой и состоит только из буквенных символов и False в противном случае
            # isalpha() determines if the input string consists of alphabetic characters. The method returns True if the source string is non-empty and consists only of literal characters, and False otherwise

_.isdigit() # isdigit() определяет, состоит ли исходная строка только из цифровых символов. Метод возвращает значение True если исходная строка является непустой и состоит только из цифровых символов и False в противном случае
            # isdigit() determines if the input string consists of only numeric characters. The method returns True if the source string is non-empty and consists only of numeric characters and False otherwise

_.islower() # islower() определяет, являются ли все буквенные символы исходной строки строчными (имеют нижний регистр). Метод возвращает значение True если все буквенные символы исходной строки являются строчными и False в противном случае. Все неалфавитные символы игнорируются
            # islower() determines if all literal characters in the source string are lowercase (lowercase). The method returns True if all literal characters of the source string are lowercase and False otherwise. All non-alphabetic characters are ignored

_.isupper() # isupper() определяет, являются ли все буквенные символы исходной строки заглавными (имеют верхний регистр). Метод возвращает значение True если все буквенные символы исходной строки являются заглавными и False в противном случае. Все неалфавитные символы игнорируются
            # isupper() determines if all literal characters in the source string are upper case. The method returns True if all literal characters of the source string are uppercase and False otherwise. All non-alphabetic characters are ignored

_.isspace() # isspace() определяет, состоит ли исходная строка только из пробельных символов. Метод возвращает значение True если строка состоит только из пробельных символов и False в противном случае
            # isspace() determines if the source string consists of only whitespace characters. The method returns True if the string contains only whitespace characters and False otherwise.

'{}'.format(age) # Мы передаем необходимые параметры методу format, а Python форматирует указанную строку и помещает их в строку на место заполнителей {}. Мы можем создавать сколько угодно заполнителей в строке
                 # We pass the required parameters to the format method, and Python formats the specified string and puts them in the string in place of the {} placeholders. We can create as many placeholders as we want per line

'{}, {}, {}'.format(name, age, profession) # Для наглядности и гибкости форматирования мы можем использовать порядковый номер в заполнителе: {0}, {1}, {2},.... Такой номер определяет позицию параметра, переданного методу format (нумерация начинается с нуля)
                                           # For clarity and formatting flexibility, we can use a sequence number in the placeholder: {0}, {1}, {2},.... This number determines the position of the parameter passed to the format method (numbering starts from zero)

'{0}, {1}, {2}'.format(name, age, profession) # Параметр name встает в {0} заполнитель, параметр age встает в {1} заполнитель и т.д. Мы можем использовать одно и тоже число в нескольких заполнителях
                                              # The name parameter goes into the {0} placeholder, the age parameter goes into the {1} placeholder, and so on. We can use the same number in multiple placeholders

'{0}-{0}-{0}'.format(name)



# Списки
# Lists

# Несмотря на всю схожесть списков и строк, есть одно очень важное отличие: строки — неизменяемые объекты, а списки – изменяемые
# Despite all the similarities between lists and strings, there is one very important difference: strings are immutable objects, and lists are mutable


# Методы списков
# List Methods

_.append() # Дабовляет новый элемент в конец списка
           # Adds a new element to the end of the list

# Обратите внимание, для того чтобы использовать метод append(), нужно, чтобы список был создан, при этом он может быть пустым
# Note that in order to use the append() method, the list must be created, and it can be empty

# Мы не можем использовать индексаторы для установки значений элементов списка, если список пустой
# We can't use indexers to set the values of list items if the list is empty

_.extend() # Расширяет список другим списком
           # Extends the list with another list

# Отличие между методами append() и extend() проявляется при добавлении строки к списку
# The difference between the append() and extend() methods comes into play when adding a string to a list

# Метод append() добавляет строку 'python' целиком к списку, а метод extend() разбивает строку 'python' на  символы 'p', 'y', 't', 'h', 'o', 'n' и их добавляет в качестве элементов списка
# The append() method adds the entire string 'python' to the list, and the extend() method splits the string 'python' into the characters 'p', 'y', 't', 'h', 'o', 'n' and adds them as elements of the list

del _[] # С помощью оператора del можно удалять элементы списка по определенному индексу
# Using the del statement, you can remove elements of a list at a specific index

# Оператор del работает и со срезами: мы можем удалить целый диапазон элементов списка
# The del operator also works with slices: we can remove a whole range of list items

_.split() # split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов
# split() splits a string into words using a sequence of whitespace characters as a delimiter

# Обратите внимание, что список будет состоять из строк, а не из чисел. Если требуется получить именно список чисел, то затем нужно элементы списка по одному преобразовать в числа:
# Note that the list will consist of strings, not numbers. If you want to get exactly a list of numbers, then you need to convert the elements of the list one by one to numbers:

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# У метода split() есть необязательный параметр, который определяет, какой набор символов будет использоваться в качестве разделителя между элементами списка. Например, вызов метода split('.') вернет список, полученный разделением исходной строки по символу '.'
# The split() method has an optional parameter that determines which set of characters will be used as a separator between list items. For example, calling the split('.') method will return a list obtained by splitting the source string on the character '.'

_.join() # join() собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод (только для str)
         # join() gathers a string from the elements of a list, using the string on which the method is applied as the delimiter (only for str)

*_ # Для int (превращает список в строку ничего не добавляя)
   # For ште (turns a list into a string without adding anything)

' '.join(_) # Для str (превращает список в строку ничего не добавляя)
            # For str (turns a list into a string without adding anything)

# Строковый метод split() служит для преобразования строки в список, а метод join() — для преобразования списка в строку
# The split() string method is used to convert a string to a list, and the join() method is used to convert a list to a string

_.insert() # insert() позволяет вставлять значение в список в заданной позиции. В него передается два аргумента: index: индекс, задающий место вставки значения; value: значение, которое требуется вставить
           # insert() allows you to insert a value into a list at a given position. Two arguments are passed to it: index: an index that specifies where to insert the value; value: the value to be inserted

_.index() # index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению. Таким образом, в метод передается один параметр: value: значение, индекс которого требуется найти
          # index() returns the index of the first element whose value equals the value passed to the method. Thus, one parameter is passed to the method: value: the value whose index is to be found

# Если элемент в списке не найден, то во время выполнения происходит ошибка
# If the element in the list is not found, then an error occurs at runtime

# Чтобы избежать таких ошибок, можно использовать метод index() вместе с оператором принадлежности in
# To avoid such errors, you can use the index() method along with the in membership operator

_.remove() # remove() удаляет первый элемент, значение которого равняется переданному в метод значению. В метод передается один параметр: value: значение, которое требуется удалить
           # remove() removes the first element whose value equals the value passed to the method. One parameter is passed to the method: value: the value to be removed

# Метод уменьшает размер списка на один элемент. Все элементы после удаленного элемента смещаются на одну позицию к началу списка. Если элемент в списке не найден, то во время выполнения происходит ошибка
# The method reduces the size of the list by one element. All elements after the removed element are moved one position to the beginning of the list. If the element in the list is not found, then an error occurs at runtime

# remove() удаляет только первый элемент с указанным значением. Все последующие его вхождения остаются в списке. Чтобы удалить все вхождения нужно использовать цикл while в связке с оператором принадлежности in и методом remove
# remove() only removes the first element with the specified value. All subsequent occurrences of it remain in the list. To remove all occurrences, you need to use a while loop in conjunction with the in membership operator and the remove method

_.pop() # pop() удаляет элемент по указанному индексу и возвращает его. В метод pop() передается один необязательный аргумент: index: индекс элемента, который требуется удалить
        # pop() removes the element at the specified index and returns it. One optional argument is passed to the pop() method: index: the index of the element to be removed

# Если индекс не указан, то метод удаляет и возвращает последний элемент списка. Если список пуст или указан индекс за пределами диапазона, то во время выполнения происходит ошибка
# If the index is not specified, then the method removes and returns the last element of the list. If the list is empty or an out-of-range index is specified, then a run-time error occurs

_.count() # count() возвращает количество элементов в списке, значения которых равны переданному в метод значению. Таким образом, в метод передается один параметр: value: значение, количество элементов, равных которому, нужно посчитать
          # count() returns the number of elements in the list whose values are equal to the value passed to the method. Thus, one parameter is passed to the method: value: value, the number of elements equal to which must be counted

# Если значение в списке не найдено, то метод возвращает 0
# If the value in the list is not found, then the method returns 0

_.reverse() # reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный
            # reverse() reverses the order of the values in the list, i.e. reverses it

# Существует большая разница между вызовом метода _.reverse() и использованием среза names[::-1]. Метод reverse() меняет порядок элементов на обратный в текущем списке, а срез создает копию списка, в котором элементы следуют в обратном порядке
# There is a big difference between calling the _.reverse() method and using the slice names[::-1]. The reverse() method reverses the order of the elements in the current list, and the slice creates a copy of the list with the elements in reverse order

_.clear() # clear() удаляет все элементы из списка
          # clear() removes all elements from the list

_.copy() # copy() создает поверхностную копию списка
         # copy() creates a shallow copy of the list

# Аналогичного результата можно достичь с помощью срезов или функции list()
# A similar result can be achieved using slices or the list() function

names_copy1 = list(names) # Создаем поверхностную копию с помощью функции list()
                          # Create a shallow copy using the list() function

names_copy2 = names[:] # Создаем поверхностную копию с помощью среза от начала до конца
                       # Create a shallow copy using a slice from start to finish

_.sort() # В Python списки имеют встроенный метод sort(), который сортирует элементы списка по возрастанию или убыванию
         # Python lists have a built-in sort() method that sorts the elements of the list in ascending or descending order

# По умолчанию метод sort() сортирует список по возрастанию. Если требуется отсортировать список по убыванию, необходимо явно указать параметр reverse = True
# By default, the sort() method sorts the list in ascending order. If you want to sort the list in descending order, you must explicitly specify the reverse = True parameter

# С помощью метода sort() можно сортировать списки содержащие не только числа, но и строки. В таком случае элементы списка сортируются в соответствии с лексикографическим порядком
# Using the sort() method, you can sort lists containing not only numbers, but also strings. In this case, the elements of the list are sorted according to the lexicographic order

# Метод sort() использует алгоритм Timsort
# The sort() method uses the Timsort algorithm


# Списочное выражение
# List expression

[выражение for переменная in последовательность]

[expression for variable in sequence]


# Сортировка списков
# Sort lists

# Сортировка пузырьком
# Bubble sort


for i in range(n - 1):
    for j in range(n - i - 1):
        if a[j] > a[j + 1]: # Если порядок элементов пары неправильный
                            # If the order of the elements of a pair is wrong
            a[j], a[j + 1] = a[j + 1], a[j] # Меняем элементы пары местами
                                            # Swap the elements of the pair

# Сортировка простыми вставками
# Sort by simple insertions

# Сортировка простыми вставками наиболее эффективна когда список уже частично отсортирован и элементов массива немного. Если элементов в списке меньше 10, то этот алгоритм — один из самых быстрых
# Insertion sort is most efficient when the list is already partially sorted and there are few array elements. If there are less than 10 elements in the list, then this algorithm is one of the fastest

for i in range(1, n):
    elem = a[i] # Первый элемент из не отсортированной части списка
                # The first element from the unsorted part of the list
    j = i
    while j >= 1 and a[j - 1] > elem:
        a[j] = a[j - 1]
        j -= 1
    a[j] = elem


# Вложенные списки
# Nested lists


# Функции
# Functions

def название_функции():
    блок кода

def function_name():
     code block

def # Функции объявляются с помощью ключевого слова
    # Functions are declared with a keyword

pass # Заглушка для функции
     # Stub for function

# Функции с параметрами
# Functions with parameters

def название_функции(параметры):
    блок кода

def function_name(parameters):
     code block

# Аргумент – это любая порция данных, которая передается в функцию, когда функция вызывается.
# An argument is any piece of data that is passed to a function when the function is called.

# Параметр – это переменная, которая получает аргумент, переданный в функцию.
# A parameter is a variable that receives the argument passed to the function.

# Локальными называются переменные, объявленные внутри функции и доступные только ей самой. Программный код за пределами функции к ним доступа не имеет.
# Local variables are variables declared within a function and only accessible by the function itself. Program code outside the function does not have access to them.

# Термин “локальная” указывает на то, что переменная может использоваться лишь в этом месте — внутри функции, в которой создается.
# The term "local" indicates that the variable can only be used in this place - inside the function in which it is created.

# Область действия переменной – часть программы, в которой можно к ней обращаться, та функция, где она создана. Переменная видима только программному коду в области ее действия. Никакая инструкция за пределами функции не может обращаться к такой переменной.
# The scope of a variable is the part of the program in which it can be accessed, the function where it was created. A variable is visible only to code within its scope. No statement outside the function can access such a variable.

# К локальной переменной не может обращаться программный код, который появляется внутри функции до того, как переменная была создана.
# A local variable cannot be accessed by code that appears inside a function before the variable has been created.

# Глобальными называются переменные, объявленные в основной программе и доступные как программе, так и всем ее функциям.
# Global variables are variables declared in the main program and available both to the program and to all its functions.

global _ # Если нужно, чтобы инструкция внутри функции присваивала значение глобальной переменной, то требуется дополнительный шаг. В этом случае, глобальная переменная должна быть объявлена внутри функции
         # If you want an instruction inside a function to assign a value to a global variable, then an extra step is required. In this case, the global variable must be declared inside the function

return _ # Функция с возвратом значения возвращает значение обратно в ту часть программы, которая ее вызвала
         # A return function returns a value back to the part of the program that called it


# Функции с возвратом нескольких значений
# Functions with multiple return values

# В Python функции не ограничены возвратом всего одного значения. После инструкции return можно определить много выражений, разделенных запятыми:
# In Python, functions are not limited to returning just one value. After the return statement, you can define many comma-separated expressions:

return выражение 1, выражение 2, выражение 3, ...

return expression 1, expression 2, expression 3, ...

#   Рассмотрим еще один пример. Пусть требуется написать функцию, которая находит точку пересечения двух непараллельных прямых ax+by=eax+by=e и cx+dy = fcx+dy=f. Другими словами требуется решить систему уравнений:
# Consider another example. Let it be required to write a function that finds the intersection point of two non-parallel lines ax+by=eax+by=e and cx+dy = fcx+dy=f. In other words, it is required to solve the system of equations:

#   Программный код, решающий задачу, имеет вид:
# The program code that solves the problem looks like this:

def solve(a, b, c, d, e, f):
    x = (d * e - b * f)/(a * d - b * c)
    y = (a * f - c * e)/(a * d - b * c)
    return x, y
xsol, ysol = solve(_, _)
print('Решением системы являются числа', 'x =', xsol, 'y =', ysol) # The solution of the system are numbers


# Преимущества использования функций
# Benefits of using functions

# Более простой код, повторное использование кода, более простое тестирование, более быстрая разработка,упрощение командной работы
# Simpler code, code reuse, easier testing, faster development, easier teamwork

# Что выделять в функции?
# What to highlight in a function?

# В функцию можно выделить любой законченный фрагмент программы.
# You can select any complete program fragment into a function.


# Модуль random
# Random module

# Модуль random предоставляет функции для генерации случайных чисел, букв и случайного выбора элементов последовательности (списка, строки и т.д.).
# The random module provides functions for generating random numbers, letters, and random selection of elements of a sequence (list, string, etc.).

# Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:
# To use these functions at the beginning of the program, you must include the module, which is done with the import command:

import random # Надо использовать random.ключевое слово
            # Must use random.keyword

from random import * # Дальше нужно только ключевое слово
                   # All you need is a keyword

from random import команды # Без random.ключевое слово только указанные ключевые слова
                         # Without random.keyword only specified keywords

_.randint() # Принимает два обязательных аргумента a и b и возвращает случайное целое число из отрезка [a;b]
            # Takes two required arguments a and b and returns a random integer from the range [a;b]

# Левая и правая граница a и b включаются в диапазон генерируемых случайных чисел. Результатом вызова функции random.randint(2, 9) может быть любое число от 22 до 99 включительно
# The left and right borders of a and b are included in the range of random numbers generated. The result of calling the random.randint(2, 9) function can be any number from 22 to 99 inclusive

_.randrange() # Принимает такие же аргументы, что и функция range(). Различие состоит в том, что функция randrange() не возвращает саму последовательность чисел. Вместо этого она возвращает случайно выбранное число из последовательности чисел.
# Takes the same arguments as the range() function. The difference is that the randrange() function does not return the actual sequence of numbers. Instead, it returns a randomly selected number from a sequence of numbers.

# randint() и randrange() возвращают случайное целое число. А вот функция random() возвращает случайное число с плавающей точкой (вещественное число).
# randint() and randrange() return a random integer. But the random() function returns a random floating point number (real number).

# В функцию random() никаких аргументов не передается.
# No arguments are passed to the random() function.

_.random() # Возвращает случайное число с плавающей точкой в диапазоне от 0 до 1
           # Returns a random floating point number between 0 and 1

_.uniform() # Тоже возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон для отбора значений
            # Also returns a random floating point number, but it allows you to set a range for selecting values

_.seed() # Всегда генерирует одну и ту же последовательность случайных чисел
         # Always generates the same sequence of random numbers

_.shuffle() # Принимает список в качестве обязательного аргумента и перемешивает его случайным образом
            # Takes a list as a required argument and shuffles it randomly
_.choice() # Принимает список (строку) в качестве обязательного аргумента и возвращает один случайный элемент из переданного списка (строки)
           # Takes a list (string) as a required argument and returns one random element from the given list (string)

_.sample() # Принимает два обязательных аргумента: список (строку) и количество случайных элементов, а возвращает список случайных элементов в указанном количестве
           # Takes two required arguments: a list (string) and the number of random elements, and returns a list of random elements in the specified number

# Количество случайных элементов не должно превышать длину начального списка (строки)
# The number of random elements should not exceed the length of the initial list (string)



# Двоичная, восьмеричная и шестнадцатеричная системы счисления
# Binary, octal and hexadecimal number systems


bin() # Возвращает строку с двоичным представлением указанного целого числа
      # Returns a string with the binary representation of the specified integer

# Обратите внимание на приставку 0b, которая сигнализирует о том, что число представлено в двоичной системе счисления
# Pay attention to the prefix 0b, which signals that the number is represented in the binary number system

oct() # Возвращает строку с восьмеричным представлением указанного целого числа
      # Returns a string with the octal representation of the specified integer

# Обратите внимание на приставку 0o, которая сигнализирует о том, что число представлено в восьмеричной системе счисления
# Pay attention to the prefix 0o, which indicates that the number is represented in the octal number system

hex() # Возвращает строку с шестнадцатеричным представлением указанного целого числа
      # Returns a string with the hexadecimal representation of the specified integer

# Обратите внимание на приставку 0x, которая сигнализирует о том, что число представлено в шестнадцатеричной системе счисления
# Pay attention to the prefix 0x, which indicates that the number is represented in hexadecimal notation

# Если нам требуется избавиться от приставок 0b, 0o, 0x, то мы можем воспользоваться строковым срезом [2:]
# If we need to get rid of the prefixes 0b, 0o, 0x, then we can use the string slice [2:]

# Обратите внимание, что функция hex() возвращает шестнадцатеричное число с маленькими символами a, b, c, d, e, f. Для преобразования к верхнему регистру можно использовать строковый метод upper()
# Note that the hex() function returns a hexadecimal number with small characters a, b, c, d, e, f. To convert to uppercase, you can use the string method upper()



# Матрица
# Matrix


# Для работы с матрицами нужно уметь получать элемент i-й строки j-го столбца. Для этого обычно заводят список строк матрицы, где каждая строка — список элементов.

_.ljust() # Выравнивает текст по ширине, добавляя пробелы в конец текста
          # Justifies the text by adding spaces to the end of the text

_.rjust() # Выравнивает текст по ширине, добавляя пробелы в начало текста
          # Justifies the text by adding spaces to the beginning of the text

# Исходная строка не обрезается, даже если в ней больше символов, чем нужно
# Source string is not truncated even if it has more characters than needed

# Вместо пробела можно использовать любой другой символ, если передать второй, необязательный параметр
# Instead of a space, you can use any other character if you pass the second, optional parameter

# Матрица с одинаковым количеством строк и столбцов называется квадратной. У квадратной матрицы есть две диагонали:
# A matrix with the same number of rows and columns is called a square matrix. A square matrix has two diagonals:

# Главная: проходит из верхнего левого в правый нижний угол матрицы
# Main: runs from the upper left to the lower right corner of the matrix

# Побочная: проходит из нижнего левого в правый верхний угол матрицы
# Side: runs from the lower left to the upper right corner of the matrix

# Элементы с равными индексами i == j находятся на главной диагонали
# Elements with significant indices i == j are located on the main diagonal

# Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1), где n — размерность матрицы, находятся на побочной диагонали
# Elements with indexes i and j related by i + j + 1 = n (or j = n - i - 1), where n is the dimension of the matrix, are on the secondary diagonal

# Если элемент находится выше главной диагонали, то i < j, если ниже, i > j
# If the element is above the main diagonal, then i < j, if below, i > j

# Если элемент находится выше побочной диагонали, то i + j + 1 < n, если ниже, i + j + 1 > n
# If the element is above the side diagonal, then i + j + 1 < n, if below, i + j + 1 > n



# Кортежи
# Tuples


tuple = (n1, n2, n3)

# Кортеж, в отличие от списка, неизменяем
# A tuple, unlike a list, is immutable

# Для создания кортежа с единственным элементом после значения элемента ставят замыкающую запятую:
# To create a tuple with a single element, put a trailing comma after the element value:

tuple = (1,)

# Если запятую пропустить, то кортеж создан не будет
# If you skip the comma, then the tuple will not be created


# Упаковка кортежей
# Packing tuples

tuple1 = 1, 2, 3
tuple2 = 'b',

# tuple1 и tuple2 превратятся в кортежи
# tuple1 and tuple2 will become tuples


# Распаковка кортежей
# Unpacking tuples

colors = ('red', 'green', 'blue', 'cyan')

(a, b, c, d) = colors # Скобки можно убрать
                      # Parentheses can be removed

# Кортеж распакуется последовательно в переменные a, b, c и d
# The tuple will be unpacked sequentially into variables a, b, c and d

# Если переменных будет меньше или больше чем значений, то компилятор выдаст ошибку
# If there are less or more variables than values, the compiler will generate an error

# Если необходимо получить лишь какие-то отдельные значения, то в качестве "ненужных" переменных позволено использовать символ нижнего подчеркивания _
# If you need to get only some individual values, then you can use the underscore character _ as "unnecessary" variables


# Несколько значений в одной переменной
# Multiple values in one variable


# Несколько значений в одну переменную делается при помощи звездочки перед именем переменной
# Multiple values in one variable is done using an asterisk in front of the variable name

a, b, *tail = 1, 2, 3, 4, 5, 6 # a = [1], b = [2], tail = [3, 4, 5, 6]

# Учтите, что переменная будет иметь тип списка
# Note that the variable will be of type list



# Множества
# Set

_.add() # Добавляет новый элемент в множество
        # Adds a new element to the set

_.remove() # Удаляет переданный элемент, выводит ошибку при не нахождении элемента
           # Removes the passed element, throws an error if the element is not found

_.discard() # Удаляет переданный элемент
            # Removes the passed element

_.pop() # Удаляет и возвращает случайный элемент, выводит ошибку при не нахождении элемента
        # Removes and returns a random element, throws an error if the element is not found

_.clear() # Удаляет все элементы множества
          # Removes all elements of the set

sorted(_) # Возвращает отсортированный список, у множеств функции sort() нет
          # Returns a sorted list, sets don't have a sort() function

set1.union(set2) # Объединяет два множества
                 # Combines sets

set1 | set2 # Равнозначен _.union()
            # Equivalent to _.union()

set1.intersection(set2) # Находит пересечение множеств (общая часть)
                          # Finds the intersection of sets (common part)

set1 & set2 # Равнозначен _.interselection()
            # Equivalent to _.interselection()

set1.difference(set2) # находит часть первого множества, не входящего во второе
                      # finds the part of the first set not included in the second

set1 - set2 # Равнозначен _.difference()
            # Equivalent to _.difference()

# Обратите внимание на порядок множеств
# Pay attention to the order of the sets

set1.symmetric_difference(set2) # Находит все элементы множеств, не входящих в оба множества
                                # Finds all elements of sets not included in both sets

set1 ^ set2 # Равнозначен _.symmetric_difference
            # Equivalent to _.symmetric_difference

set1.update(set2) # Добавляет в множество set1 множество set2
                  # Adds set2 to set1

set1 |= set2 # Равнозначен _.updata()
             # Equivalent to _.updata()

set1.intersection_update(set2) # Изменяет set1 так, что в нём остаётся общая часть с set2
                               # Modifies set1 so that it shares a common part with set2

set1 &= set2 # Равнозначен _.intersection_updata()
             # Equivalent to _.intersection_updata()

set1.difference_update(set2) # Изменяет множество set1, оставляя элементы входящие только в множество set1
                             # Changes the set1, leaving the elements included only in the set1

set1 -= set2 # Равнозначен _.difference_update()
             # Equivalent to _.difference_update()

set1.symmetric_difference_update(set2) # Изменяет множество set1, оставляя элементы входящие только в множество set1 и множество set2
                                       # Modifies set1, leaving elements included only in set1 and set2

set1 ^= set2 # Равнозначен _.symmetric_difference_update()
             # Equivalent to _.symmetric_difference_update()

# Все основные операции над множествами выполнятся двумя способами: при помощи метода или соответствующего ему оператора.
# All basic operations on sets are performed in two ways: using a method or its corresponding operator.

# Различие в том, что метод может принимать в качестве аргумента не только множество (тип данных set), но и любой итерируемый объект (список, строку, кортеж).
# The difference is that the method can take as an argument not only a set (set data type), but also any iterable object (list, string, tuple).

# Некоторые методы (union(), intersection(), difference()) и операторы (|, &, -, ^) позволяют совершать операции над несколькими множествами сразу.
# Some methods (union(), intersection(), difference()) and operators (|, &, -, ^) allow you to perform operations on multiple sets at once.

# Оператор ^ симметрической разности позволяет использовать несколько множеств, а метод symmetric_difference() – нет.
# The symmetric difference operator ^ allows multiple sets, but the symmetric_difference() method does not.

# Приоритет операторов (слева направо)
# Operator precedence (left to right)

-, &, ^, |

set1.issubset(set2) # Определяет, является ли множество set1 подмножеством для set2
                    # Determines if set1 is a subset of set2

set1 <= set2 # Равнозначен _.issubset() (нестрогое)
             # Equivalent to _.issubset() (non-strict)

set1 < set2 # Равнозначен _.issubset() (строгое)
             # Equivalent to _.issubset() (strict)

set1.issuperset(set2) # Определяет, является ли множество set1 надмножеством set2
                      # Determines if set1 is a superset of set2

set1 >= set2 # Равнозначен _.issuperset() (нестрогое)
             # Equivalent to _.issuperset() (non-strict)

set1 > set2 # Равнозначен _.issuperset() (строгое)
             # Equivalent to _.issuperset() (strict)

set1.isdisjoint(set2) # Определяет, отсутствуют ли общие элементы у множеств set1 и set2
                      # Determines if set1 and set2 have no common elements



# Словари
# Dictionaries

_.keys() # Возвращает список ключей всех элементов словаря
         # Returns a list of keys of all elements of the dictionary

_.values() # Возвращает список значений всех элементов словаря
          # Returns a list of values of all elements of the dictionary

_.items() # Возвращает список всех элементов словаря, состоящий из кортежей пар (ключ, значение)
          # Returns a list of all elements of the dictionary, consisting of tuples of pairs (key, value)

# Используя магию распаковки кортежей, можно писать так:
# Using the magic of tuple unpacking, you can write:

for key, value in _.items():
    print(key, '-', value)

print(*_, sep='\n') # Операция распаковки славоря выводящая только значения ключей
                    # Slavor unpacking operation outputting only key values

# Словари можно сортировать только по ключам с помощью функции sorted()
# Dictionaries can only be sorted by keys using the sorted() function


_.get() # Индексация без ошибки
        # Indexing without errors

# Может принять двааргумента, второй будет выведен в случае, если нет значение по индексу-ключу (первый аргумент), если второго аргумента нет, то будет выведено None
# Can take two arguments, the second will be displayed if there is no value by index-key (first argument), if there is no second argument, then None will be displayed

_.update() # Объединяет ключи и значения одного словаря с ключами и значениями другого
           # Combines the keys and values of one dictionary with the keys and values of another

# При совпадении ключей в итоге сохранится значение словаря, указанного в качестве аргумента метода
# If the keys match, the value of the dictionary specified as the method argument will be saved as a result

_.setdefault() # Позволяет получить значение из словаря по заданному ключу, автоматически добавляя элемент словаря, если он отсутствует
               # Allows you to get a value from a dictionary by a given key, automatically adding a dictionary element if it is missing
               
# Метод принимает два аргумента:
# The method takes two arguments:

# key: ключ, значение по которому следует получить, если таковое имеется в словаре, либо создать
# key: key, value by which to get, if any, in the dictionary, or create

# default: значение, которое будет использовано при добавлении нового элемента в словарь (необязательный)
# default: the value that will be used when adding a new element to the dictionary (optional)


# Существует несколько способов удаления элементов из словаря:
# There are several ways to remove elements from a dictionary:


# оператор del 
# del statement

# Удаляет элемент по заданному ключу
# Removes the element with the given key


# метод pop()
# pop() method

# Удаляет элемент по заданному ключу и возращает его
# Removes the element with the given key and returns it


# метод popitem()
# popitem() method

# Удаляет из словаря последний добавленный элемент и возвращает удаляемый элемент в виде кортежа (ключ, значение)
# Removes the last added element from the dictionary and returns the removed element as a tuple (key, value)


# метод clear()
# clear() method

# Удаляет все элементы из словаря
# Removes all elements from the dictionary


_.copy() # Создает поверхностную копию словаря
         # Creates a shallow copy of the dictionary
         
# Не стоит путать копирование словаря (метод copy()) и присвоение новой переменной ссылки на старый словарь
# Do not confuse copying a dictionary (the copy() method) and assigning a new variable a reference to the old dictionary

# Оператор присваивания (=) не копирует словарь, а лишь присваивает ссылку на старый словарь новой переменной
# The assignment operator (=) does not copy the dictionary, but only assigns a reference to the old dictionary to the new variable

