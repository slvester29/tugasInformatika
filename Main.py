

#Input User dengan kasus Himpunan
InputUser = float(input("masukan nilai kurang dari 3 atau lebih dari 10: "))
IsiKurangDari3 = (InputUser < 3)
isiLebihDari4 = (InputUser > 10)
#kita bisa memakai konsep OR
isCorrect = IsiKurangDari3 or isiLebihDari4
print("maka nilai yang anda masukan", isCorrect)


#Input-User dengan and

#----3+++++++10-------


inputUser1 = float(input("nilai yang anda masukan: "))

isKurangDari3 = (inputUser1 > 3)
isKurangDari10 = (inputUser1 < 10)
isCorrect = isKurangDari3 and isKurangDari10

print("maka nilai yang anda masukan, bernilai t/f", isCorrect)

