#include  <iostream> // input/output stream (main commands)
#include <stdio.h> // input/output
#include <vector> // Для хранение и изменения элементов схожих типов
                  // To store and modify elements of similar types
#include <fstream> // Working with files
#include <string> // To work with strings


#include // Обращение к библиотеке
         // Accessing the library

<_> // В "<" и ">" в них записывается название библиотеки
    // In "<" and ">" they contain the name of the library

using namespace std; // Использует стандартное пространство имён (std)
                     // Uses the standard namespace (std)

int main(){ // Функция
            // Function
    return 0; // Программа успешно завершилась
              // Program completed successfully
}


// Типы данных
// Data types

string line; // Строка
             // Line

char _; // От 128 до 127
        // From 128 to 127

unsigned char _; // От 0 до 255
                 // 0 to 255

signed char _; // От -128 до 127
               // -128 to 127

int _; // От -2147483648 до 2147483647
       // From -2147483648 to 2147483647

unsigned int _; // От 0 до 4294967295
                // From 0 to 4294967295

signed int _; // От -2147483648 до 2147483647
              // From -2147483648 to 2147483647

short int _; // От -32768 до 32767
             // -32768 to 32767

unsigned short int _; // От 0 до 65535
                      // 0 to 65535

signed short int _; // От -32768 до 32767
                    // -32768 to 32767

long int _; // От -2147483648 до 2147483647
            // From -2147483648 to 2147483647

unsigned long int _; // От 0 до 4294967295
                     // From 0 to 4294967295

signed long int _; // От -2147483648 до 2147483647
                   // From -2147483648 to 2147483647

float _; // От 3.4e-38 до 3.4е+38
         // From 3.4e-38 to 3.4e+38

double _; // От 1.7е-308 до 1.7е+308
          // From 1.7e-308 to 1.7e+308

long double _; // От 3.4е-4932 до 1.1e+4932
               // From 3.4e-4932 to 1.1e+4932

bool flag; // True or False

int n = 0x4 // 4 в шестнадцатиричной системе счисления
            // 4 in hexadecimal
         
int list[_]; // Список длиной _
             // List of length _
             
auto _; // Автоматически устанавливает тип переменной
        // Automatically sets the type of the variable

int nums = 1234;
string line = (string)(nums); // Изменение типа int > string
                              // Change type int > string


// Математические операции
// Math operations

a + b // Сложение a и b
      // Add a and b

a - b // Вычесть b из a
      // Subtract b from a

a / b // a делится на b (при float), целочисленное деление (при int)
      // a is divisible by b (for float), integer division (for int)

a * b // a умножается на b
      // a is multiplied by b

a % b // Остаток от деления a на b
      // Remainder of dividing a by b
         
         

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
             


"\n" // Переводит на следующую строку
     // Moves to the next line

"\0" // Установка конца строки
     // Set the end of the string
     

// Ввод и вывод (<stdio.h>)
// Input and output (<stdio.h>)


scanf("%i %i", &a, &b) // Запрашивает целое число
               // Requests an integer

printf("Hi!", "%i" a) // Выводит Hi! и число из переменной a
                      // Outputs Hi! and number from variable a

// Объяснения для scanf
// Explanations for scanf


"%с"	// Считать один символ
      // Count one character

"%d"	// Считать десятичное число целого типа
      // Read decimal number of integer type

"%i"	// Считать десятичное число целого типа
      // Read decimal number of integer type

"%е"	// Считать число с плавающей запятой
      // Read floating point number

"%f"	// Считать число с плавающей запятой
      // Read floating point number

"%.3f" // Считать число с плавающей запятой, выводит число с тремя цифрами после запятой
       // Read floating point number, outputs a number with three decimal places

"%g"	// Считать число с плавающей запятой
      // Read floating point number

"%о"	// Считать восьмеричное число
      // Read octal number

"%s"	// Считать строку
      // Read string

"%х"	// Считать шестнадцатиричное число
      // Read hexadecimal number

"%р"	// Считать указатель
      // Read pointer

"%n"	// Принимает целое значение, равное количеству считанных до текущего момента символов
      // Takes an integer value equal to the number of characters read so far

"%u"	// Считывает беззнаковое целое
      // Reads an unsigned integer

"%[]"	// Просматривает набор символов
      // Looks up character set

"%%"	// Считывает символ %
      // Reads the % character



// Ввод и вывод (<iostream>)
// Input and output (<iostream>)


<< /*or*/ >> // Путь данных
             // Data path

cout // Вывод 
     // Console output

cin // Ввод
    // Console input

cout << "Hello, World!"; // Hello, World!

cin >> a >> b;

endl // End line and flush

cout << _ << endl;



// Ввод и вывод в файл (<fstream>)
// File input and output (<fstream>)


ifstream _(/*"File name"*/); // Ввод из файла
                             // Input from file

_ >> var;

ofstream _(/*"File name"*/); // Вывод в файл
                             // Output to file

_ << var;



// Условия
// Terms

if (_) {

}

else if (_) {
    
}

else {
    
}



& // Побитовое И
  // Bitwise And

&& // И, если первое значение не верно, второе проверяется
   // And, if the first value is not correct, the second is checked

| // Побитовое ИЛИ
  // Bitwise Or

|| // Или, если первое значение верно, второе не проверяется
   // Or, if the first value is true, the second is not checked

^ // Исключение
  // Exception

~ // Инверсия (отрицание)
  // Inversion (negation)

>> // Сдвиг вправо
   // Shift Right

<< // Сдвиг влево
   // Shift Left
         


// Сравнение
// Compare


== // Равно
   // Equally

!= // Не равно
   // Not equally

> // Больше
  // More

< // Меньше
  // Less

>= // Больше или равно
   // More than or equal to

<= // Меньше либо равен
   // Less than or equal to

! // Не
  // Not



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



// Цикл for
// Cycle for


for (условие /*condition*/; вопрос /*question*/; изменение /*change*/){
    решение /*solution*/
}

for (int i; вопрос /*question*/; i++){
    решение /*solution*/
}



// Цикл while
// Cycle while


// Циклы, повторяющиеся до наступления определенного события
// Cycles that repeat until a certain event occurs

while (_) {
    
}


break; // Заканчивает что-то
       // Finishing something

continue; // Пропускает только один проход
          // Only skips one pass

return; // Выгоняет при активации
        // Kicks out on activation

goto _; // Переходит к метке _:
        // Goes to label _:

void _(); // Функция не возвращает значение
          // Function does not return a value

int _(); // Функция возвращает значение типа int
         // The function returns a value of type int


freopen(/*file*/, /*mode*/, std/*in / out*/); // Работа с файлами

FILE *IN, *OUT; // For freopen_s()

freopen_s(&/*IN / OUT*/, /*file*/, /*mode*/, std/*in / out*/) // Более безопасный вариант freopen()
                                                              // Safer version of freopen()

// Режимы для freopen and freopen_s
// Modes for freopen and freopen_s

"r" // Read
"w" // Write
"e" // Exercise

int& _; // Ссылание
        // Reference

int* _; // Указание
        // Indication

int* nullptr; // Фиктивный 0
              // Dummy 0

_.size() // Длина _
         // Length _

struct _ { // Public
      
}

class { // Private

}

public: // Публичный модификатор доступа
        // Public access modifier

private: // Приватный модификатор доступа
         // Private access modifier

/*type*/ _ = new _; // Выделяет и инициализирует объект или массив объектов указанного типа
                    // Allocates and initializes an object or array of objects of the specified type

delete _; // Отменяет выделение блока памяти
          // Unallocates a block of memory

/*type*/ _ = new[] _; // Для маcсивов
                      // For arrays

delete[] _; // Для маcсивов
          // For arrays