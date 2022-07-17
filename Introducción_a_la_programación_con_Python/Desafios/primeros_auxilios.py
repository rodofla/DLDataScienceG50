print("""Bienvenido a la aplicación sobre primeros auxilios
      Aquí podrás encontrar información sobre los pasos a seguir
      en caso de que el paciente se encuentre en una emergencia\n""")


# This is a program that asks the user a series of questions and based on the answers, it will give
# the user a series of instructions on what to do in case of an emergency.
if input("¿Responde a estímulos? (Si/No): ").lower() == "si":
    print("\nValorar la necesidad de llevarlo al hospital más cercano")
else:
    print("\nAbrir la vía aérea")

if input("\n¿El paciente respira? (si/no): ").lower() == "si":
    print("\nPermitirle posición de suficiente ventilación")
else:
    print("\nAdministrar 5 ventilaciones y llamar a la ambulancia")

while True:
    if input("\n¿El paciente presenta signos de vida?: ").lower() == "si":
        print("\nReevaluar a la espera de la ambulancia")
        if input("\n¿Llegó la ambulaciía? (si/no): ").lower() == "si":
            break
        else:
            continue
    else:
        print("\nAdministrar compresiones torácicas hasta que llegue la ambulancia")
        if input("\n¿Llegó la ambulaciía? (si/no): ").lower() == "si":
            break
        else:
            continue

