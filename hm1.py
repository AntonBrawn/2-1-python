# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет
# ------------------------------------------------
# def day_yeekend():
#     chislo=int(input('Введите число: '))
#     if chislo==6:
#         print("Ура, это выходой, еще гуляем!")
#     elif chislo==7:
#         print("Это выходной, завтра на работу:( ")
#     else:
#         print("Это не выходной")
# day_yeekend()

# ------------------------------------------------

# ------------------------------------------------
# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


# def chetvert():
#     abscissa_x=int(input("Введите x: "))
#     ordinate_y=int(input("Введите y: "))
#     if abscissa_x==0 and ordinate_y==0:
#         print("Числа равны нулю, ошибка!")
#     if abscissa_x>0 and ordinate_y>0:
#         print("Это 1 четверть")
#     elif abscissa_x>0 and ordinate_y<0:
#             print("Это 4 четверть")
#     elif abscissa_x<0 and ordinate_y>0:
#         print("Это 2 четверть")
#     elif abscissa_x<0 and ordinate_y<0:
#         print("Это 3 четверть")
# chetvert()
# ----------------------------------------------

# ----------------------------------------------
# 4- Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


# def diap():
#     num=int(input("Введите номер четверти: "))
#     if num==1:
#         print("Возможные координаты в 1 четверти : X∈(0,ထ ), Y∈(0,ထ )")
#     elif num==2:
#         print("Возможные координаты в 2 четверти : X∈(-ထ ,0), Y∈(0,ထ )")
#     elif num==3:
#         print("Возможные координаты в 3 четверти : X∈(-ထ ,0), Y∈(-ထ ,0)")
#     elif num==4:
#         print("Возможные координаты в 4 четверти : X∈(0,ထ ), Y∈(-ထ ,0)")
#     else:
#         print("Введенный номер четверти не существует! Повторите попытку")
# diap()
# #------------------------------------------------

#--------------------------------------------------
# 5-Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# *Пример:*

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


# from cmath import sqrt
# print("Введите значение для А: ")
# num_a = [(input()), (input())]
# print("Введите значения для B: ")
# num_b = [(input()), (input())]

# def distance():
#     import math
#     sum_1 = (int(num_a[0])-int(num_b[0]))
#     sum_2 = (int(num_a[1])-int(num_b[1]))
#     dist_all = (math.sqrt((sum_1**2)+(sum_2**2)))
#     print(f"Расстояние между двумя точками в 2D пронстранстве равна: {round(dist_all,2)}")


# distance()
#------------------------------------------------------------------


# -------------------------------------------------------------------

# 2-Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. Предикату можно заменить на понятие "бит".
# Должна получиться таблица истинности.

#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """



# def tabl_1():
#     print("-"*15)
#     print("X", "Y", "Z", "result", sep=" ")
#     print("-*15")
#     for X in range(2):
#         for Y in range (2):
#             for Z in range(2):
#                 if not (X or Y or Z)==(not(X) and not(Y) and not (Z)):
#                     print(f"{X} {Y} {Z}- True")
#                 else:
#                     print(f"{X} {Y} {Z}- False")
# tabl_1()
#------------------------------------------------------------------




