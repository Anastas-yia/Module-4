def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function()

test_function()

# inner_function()

# I:\Project_Python_Urban\pythonProject\.venv\Scripts\python.exe I:\Project_Python_Urban\pythonProject\M4\module_4_2.py
# Traceback (most recent call last):
#   File "I:\Project_Python_Urban\pythonProject\M4\module_4_2.py", line 8, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
#
# Process finished with exit code 1

#При попытке обратиться к функции inner_function() PyCharm выдает ошибку.  Имя 'inner_function' не определено.
#Может вы имели ввиду: 'test_function'?
#inner_function() находится в локальной области видимости функции test_function и поэтому не может быть вызвана
#отдельно из вне
