using System;

using // Вызов деректив
      // Call directives


// Методы
// Methods

Console.WriteLine(); // Команда для вывода данных 
                     // Data output command

Console.ReadLine(); // Команда для ввода данных
                    // Command for entering data

"Data".Length; // Возвращает длину строки (4)
               // Returns the length of the string (4)

(int) 5.1; // 5

Clipboard.SetText() // Сохранение в буфер обмена
                    // Save to clipboard

Convert.To/*type*/(); // Конвертирование одного типа данных в другой
                      // Convert one data type to another

"Data"/*value*/.ToUpper(); // Переводит слово в верхний регистр (DATA)
                           // Converts the word to upper case (DATA)

"Data"/*value*/.ToLower(); // Переводит слово в нижний регистр (data)
                           // Converts the word to lower case (data)

char.ToUpper(/*value*/); // Для типа char
                         // For type char

"D".IsUpper() // Проверка символа на верхний регистр
               // Check character for uppercase

Functions.StringReverse() // Переворачивает строку
                          // Reverse the string

"Data"().IndexOf('D'); // Возвращает индекс символа в скобках (0)
                       // Returns the character index in brackets (0)

_.Insert(<first>, <second>); // <second> дополняет строку с <first>
                                 // <second> completes the string with <first>

_.Replace(<first>, <second>); // Заменяет <first> на <second>
                                  // Replaces <first> with <second>

_.Substring(<first>, <second>); // Извлекает от <first> до <second>
                                // Retrieves from <first> to <second>

_.StartWith(<search>); // Проверяет начинается ли заданная строка или переменная с <search>
                       // Checks if the given string or variable starts with <search>
_.EndWith(<search>); // Проверяет заканчивается ли заданная строка или переменная на <search>
                     // Checks if the given string or variable ends with <search>

_.Trim() // Удаление концевых пробельных символов
         // Removing trailing whitespace characters


// Типы данных
// Data types

byte // От 0 до 255
     // From 0 to 255

sbyte // От -128 до 127
      // From -128 to 127

short // От -32768 до 32767
      // From -32768 to 32767

ushort // От 0 до 65535
       // From 0 to 65535

int // От -2147483648 до 2147483647
    // From -2147483648 to 2147483647

uint // От 0 до 4294967295
     // From 0 to 4294967295

nint // От -9223372036854775808 до 9223372036854775807
     // From -9223372036854775808 to 9223372036854775807

nuint // От 0 до 18446744073709551615
      // From 0 to 18446744073709551615

long // От -9223372036854775808 до 9223372036854775807
     // From -9223372036854775808 to 9223372036854775807

ulong // От 0 до 18446744073709551615
      // From 0 to 18446744073709551615

float // От -3.402823e38 до 3.402823e38
      // From -3.402823e38 to 3.402823e38

double // От -1.79769313486232e308 до 1.79769313486232e308
       // From -1.79769313486232e308 to 1.79769313486232e308

decimal // От -79228162514264337593543950335 до 79228162514264337593543950335
        // From -79228162514264337593543950335 to 79228162514264337593543950335

char // Одиночный символ
     // Single symbol

string // "Текстовая строка"
       // Text string

bool // true или false
     // true or false

object // Некий объект
       // Some object

dynamic // При компиляции переходит в тип object
        // Converts to object when compiled

var // Может заменять собой другие типы
    // Can replace other types


тип переменная = значение;

type variable = value;

const type = value; // Неизменяемая переменная (константа)
                    // Immutable variable (constant)

// Массивы
// Arrays

type[] variable = value_1, value_2, ..., value_n; // Массив
                                                  // Array

int[] nums = {1, 2, 3...}
string[] lines = 
{
    "line 1", // index 0
    "line 2", // index 1
    "line 3" // index 2
    ... // index ...
}
char[] array = {"a", "b", "c"...}


$ // Добавление переменной в строку, для добавление переменную нужно писать в {}
  // Adding a variable to a string, to add a variable need to write in {}

@ // Нормальный вид текста
  // Normal text view

"\r\n" // Члучшенная версия \n и заменяет @
       // Improved version \n and replaces @

"\\" // Для вывода "\"
     // For output "\"


// Код для конвертации Int в String и обратно
// Code to convert Int toString and back

    // Int ---> String
    {
        int age = 33;
        string age = Convert.ToString(age);
    }

    // String ---> Int
    {
        string age = "33";
        int age = Convert.ToInt32(age);
    }


// Свойства
// Properties

// Свойства типов
// Type properties

    /*type*/.MaxValue; // Максимальное значение типа
                       // The maximum value of the type

    /*type*/.MinValue; // Минимальное значение типа
                       // The minimum value of the type


namespace // Даёт имя пространству
          // Gives a name to the space

public // Модификатор доступа (публичный)
       // Access modifier (public)

private // Модификатор доступа (приватный)
        // Access modifier (private)

void // Вызывает, но ничего не возвращая
     // Calls, but returns nothing

return // Что-то возвращает
       // Returns something

class // Создаёт класса
      // Creates a class

_e_ // Ебануться, какое большое число
    // Fuck, what a big number

static // Для объявления класса static
       // For class declaration static

_.Exists() // Существует
           // Exist

!_.Exists() // Не существует
            // Doesn't exist

Exception // Исключение
          // Exception


// Срезы 
// Slicing

"Brain".Substring(1); // "rain"
    "Brain".Substring(1, 2); // "ra"
    "Brain".Substring(1, 3); // "rai"
    "Brain".Substring(2, 2); // "ai"


// Индексы
// Indices

    "Brain"[0];  // 'B'
    "Brain"[1];  // 'r'
    "Brain"[2];  // 'a'
    "Brain"[3];  // 'i'
    "Brain"[4];  // 'n'


// Условия
// Terms

    == // Равно
       // Equally

    != // Не равно
       // Not equal

    > // Больше
      // More

    < // Меньше
      // Less

    >= // Больше или равно
       // More than or equal to

    <= // Меньше или равно
       // Less than or equal to

    ! // Не
      // Not

    & // И
      // And

    && // И, но если одно из условий не верно, то остальные не проверяет
       // And, but if one of the conditions isn't true, then the rest doesn't check

    | // Или
      // Or

    || // Или, но если одно из условий верно, то остальные не проверяет
       // Or, but if one of the conditions is true, then rest doesn't check


    if (_) // Если
           // If
    { 
        
    }

    else if (_) // Иначе, если
                // Otherwise, if
    {
            
    }

    else // Иначе
         // Otherwise
    {
        
    }


// switch
// switch — довольно сложная конструкция с точки зрения количества элементов, из которых она состоит
// switch is quite complex in terms of the number of elements it consists of

switch (_)
{
    case _1:
        break; // or another code

    case _2:
        break; // or another code

    case _3:
        break; // or another code

    case _4:
        break; // or another code

    default:
}


// Тернарная операция
// Ternary operation

    int age = 10;
    string fix = age == 10? "Yes":"No";
    int fix = age == 10 ?  0:1;


// MessageBox

MessageBox.Show();


DateTime._ // Дата и время
           // Date and time


// Инкремент
// Increment

i += 1 // i = i + 1
i -= 1 // i = i - 1
_++ // +1
++_ // +1

int _ = _++ // Возвращает, а затем добавляет
             // Returns and then adds

int _ = ++_ // Добавляет и возвращает одновременно
             // Adds and returns at the same time
_-- // -1
--_ // -1

int _ = _-- // Присваивает, а затем вычетает
             // Assings and then subtracts

int _ = --_ // Вычетает и присваивает одновременно
             // Subtracts and assings at the same time


// Обработка исключений
// Exception Handling

try
    { 
        
    }
catch
{

}
finally
{

}
throw new Exception(); // Своя ошибка
                       // Own mistake


// Циклы
// Cycles

while (условие /*condition*/) // Проверяет, делает (лучше)
                              // Checks, makes (better)
{
    решение /*solution*/
}

do // Делает, проверяет
   // Makes, checks
{
    решение /*solution*/
}
while (условие /*condition*/);

for (условие /*condition*/; вопрос /*question*/; изменение /*change*/)
{
    решение /*solution*/
}

foreach (тип массива /*array type*/ имя /*name*/ in массив /*array*/) // Работает с массивами
                                                                      // Works with arrays
{
    решение /*solution*/
}

break; // Заканчивает что-то
       // Finishing something

continue; // Пропускает только один проход
          // Only skips one pass

return; // Выгоняет при активации
        // Kicks out on activation

goto _; // Переходит к метке _:
        // Goes to label _:


// Асинхронная работа
// Asynchronous work

async void _()
{
    await Task.Run(() =>
    {

    }
}
await Task.Delay(); // Задержка
                    // Delay

this.variable = value; // Эта переменная относится именно к тому классу или методу, в котором находится
                       // This variable is specific to the class or method it's in