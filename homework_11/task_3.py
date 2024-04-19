def inches_to_cm(inches):
    return inches * 2.54

def cm_to_inches(cm):
    return cm / 2.54

def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def pounds_to_kg(pounds):
    return pounds * 0.453592

def kg_to_pounds(kg):
    return kg / 0.453592

def ounces_to_grams(ounces):
    return ounces * 28.3495

def grams_to_ounces(grams):
    return grams / 28.3495

def gallons_to_liters(gallons):
    return gallons * 3.78541

def liters_to_gallons(liters):
    return liters / 3.78541

def pints_to_liters(pints):
    return pints * 0.473176

def liters_to_pints(liters):
    return liters / 0.473176

def choose_operation():
    print("Выберите операцию:")
    print("1. Дюймы в сантиметры")
    print("2. Сантиметры в дюймы")
    print("3. Мили в километры")
    print("4. Километры в мили")
    print("5. Фунты в килограммы")
    print("6. Килограммы в фунты")
    print("7. Унции в граммы")
    print("8. Граммы в унции")
    print("9. Галлон в литры")
    print("10. Литры в галлоны")
    print("11. Пинты в литры")
    print("12. Литры в пинты")
    operation = int(input("Введите номер операции: "))
    number = float(input("Введите число для преобразования: "))
    return operation, number

result = choose_operation()
operation = result[0]
number = result[1]
if operation == 1:
    print(f"{number} дюймов = {inches_to_cm(number)} сантиметров")
elif operation == 2:
    print(f"{number} сантиметров = {cm_to_inches(number)} дюймов")
elif operation == 3:
    print(f"{number} миль = {miles_to_km(number)} километров")
elif operation == 4:
    print(f"{number} километров = {km_to_miles(number)} миль")
elif operation == 5:
    print(f"{number} фунтов = {pounds_to_kg(number)} килограммов")
elif operation == 6:
    print(f"{number} килограммов = {kg_to_pounds(number)} фунтов")
elif operation == 7:
    print(f"{number} унций = {ounces_to_grams(number)} грамм")
elif operation == 8:
    print(f"{number} грамм = {grams_to_ounces(number)} унций")
elif operation == 9:
    print(f"{number} галлонов = {gallons_to_liters(number)} литров")
elif operation == 10:
    print(f"{number} литров = {liters_to_gallons(number)} галлонов")
elif operation == 11:
    print(f"{number} пинт = {pints_to_liters(number)} литров")
elif operation == 12:
    print(f"{number} литров = {liters_to_pints(number)} пинт")
else:
    print("Неверный номер операции")
