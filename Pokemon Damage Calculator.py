print("Pokemon Damage Calculator ni JOSE\n")

lvl = 90
atk = 205
pwr = 110
defs = 188

target = 1
weather = 1
badge = 1
crit = 1
random = 1
stab = 1.5
type = 0.5
burn = 1

modifier = target*weather*badge*crit*random*stab*type*burn
dmg = round(((((((2*lvl)/5)+2)*(pwr*(atk/defs)))/50)+2)*modifier)

print("Charizard Lv.90 uses Fire Blast on Feraligatr lv.95")
print("It is not efective!!!")
print("The attack only hits",dmg,"damage.")