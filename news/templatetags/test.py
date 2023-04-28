text = 'мы ломим. Разобьём всех редисок!!!'
sens = 'редис'
check = text.split()
for i in check:
   if sens in i:
      text = text.replace(i , i[0:5]+'***')

print(text)
