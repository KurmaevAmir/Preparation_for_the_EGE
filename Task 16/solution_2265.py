# Алгоритм вычисления функции F(n) задан следующими соотношениями:
# F(n) = n при n ≤ 3;
# F(n) = n // 4 + F(n–3)  при 3 < n ≤ 32;
# F(n) = 2·F(n–5) при n > 32
# Здесь // обозначает деление нацело. Чему равно значение величины F(100)?


def function(n):
    if n <= 3:
        return n
    elif 3 < n <= 32:
        return n // 4 + function(n - 3)
    else:
        return 2 * function(n - 5)


print(function(100))
