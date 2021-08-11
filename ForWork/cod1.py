import openpyxl

book = openpyxl.open("certification.xlsx",read_only=True) # Открытие файла на чтение

listBook = book.active

print(listBook['E1'].value) # Обращение по номеру ячейки
print(listbook)
