# python_analysis
This is a repository specifically for storing projects of Formula_IT_Polytech	

В файле task7_2.ipynb представлено решение задания 7_2.  

В решении было использовано 3 функции:	
1) check_input(elements)	
2) get_substring(s)	
3) main(elements)

Функция check_input находит самую длинную строку в массиве, возвращая её и её индекс.	

Функция get_substring находит в переданной в неё строке (найденной в функции check_input) и находит самую длинную подстроку с помощью цикла for, проходя по каждому элементу. Если элемент находится в словаре char_index, длина подстроки начинается с начала, таким образом и находится самая длинная из подстрок.	

Функция main включает в себя использование двух остальных функций и выводит -1 и пустую строку в случае, если в переданном массиве нет строк.	
