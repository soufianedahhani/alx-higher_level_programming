a = 1
b = 2

exec_str = "from add import add"
exec(exec_str)

result = add(a, b)
print('{} + {} = {}'.format(a, b, result))
