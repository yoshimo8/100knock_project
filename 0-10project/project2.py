# my code
def legend(patrol,taxi):
    le = ''
    for i in range(4):
        le += patrol[i]
        le += taxi[i]

    return le

patrol_car, taxi = 'パトカー','タクシー'
print(legend(patrol_car, taxi))

#others

str1 = u'パトカー'
str2 = u'タクシー'
str3 = u''

for a,b in zip(str1, str2):
    str3 = str3 + a + b

print str3
