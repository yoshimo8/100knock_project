
def legend(patrol,taxi):
    le = ''
    for i in range(4):
        le += patrol[i]
        le += taxi[i]

    return le

patrol_car, taxi = 'パトカー','タクシー'
print(legend(patrol_car, taxi))
