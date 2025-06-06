import sys

# AV1
teste0 = input("Você já fez a AV1? (True/False): ")
if teste0.lower() == "true":
    uni1 = float(input("Informe a sua nota da AV1: "))
    mediatual0 = round(uni1 * 0.25, 1)
    mediatual00 = round(7.0 - mediatual0, 1)
else:
    print("VÁ FAZER E DEPOIS VOLTA!")
    sys.exit(0)


# EDAG
testedag = input("Você já fez o EDAG? (True/False): ")
if testedag.lower() == "true":
    edag = float(input("Informe a sua nota do EDAG: "))
else:
    edag = 0.0  # Se não fez, considera 0
    mediatual1 = round((uni1 * 0.25) + (edag * 0.2), 1)
    mediatual11 = round(7.0 - mediatual1, 1)
    print("A sua média atual é:", mediatual1,
          ", e você precisa de:", mediatual11)
    sys.exit(0)


# AV2
testeuni2 = input("Você já fez a AV2? (True/False): ")
if testeuni2.lower() == "true":
    uni2 = float(input("Informe a sua nota da AV2: "))
else:
    uni2 = 0.0  # Se não fez, considera 0
    mediatual2 = round((uni1 * 0.25) + (uni2 * 0.25) + (edag * 0.2), 1)
    mediatual22 = round(7.0 - mediatual2, 1)
    notav3 = round(mediatual22 / 0.3, 1)
    print("A sua média atual é:", mediatual2, "e você precisa de:",
          mediatual22, ", ou seja, precisa tirar na AV3:", notav3)
    sys.exit(0)

mediatual2 = round((uni1 * 0.25) + (uni2 * 0.25) + (edag * 0.2), 1)


# AV3
testeuni3 = input("Você já fez a AV3? (True/False): ")
if testeuni3.lower() == "true":
    uni3 = float(input("Informe a sua nota da AV3: "))
    mediatual3 = round((uni1 * 0.25) + (uni2 * 0.25) +
                       (edag * 0.2) + (uni3 * 0.3), 1)
    print("Sua média final é:", mediatual3)
    if mediatual3 >= 7.0:
        print("VOCÊ FOI APROVADO! Média:", mediatual3)
    else:
        AG = mediatual3
        PN = round((50 - (6 * AG)) / 4, 1)
        print("Infelizmente você não passou. Média:", AG,
              ", e precisa da seguinte nota na final:", PN)
        sys.exit(0)
else:
    mediatual33 = round(7.0 - mediatual2, 1)
    notav33 = round(mediatual33 / 0.3, 1)
    print("A sua média atual é:", mediatual2, "e você precisa de:",
          mediatual33, ", ou seja, precisa tirar na AV3:", notav33)
    sys.exit(0)
