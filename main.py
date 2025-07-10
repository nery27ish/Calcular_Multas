def multa_localidade(velocidade: float) -> float:
    if velocidade <= 50:
        return 0
    elif velocidade >= 120:
        return 320
    elif velocidade >= 90:
        return 120
    else:
        return 60

def multa_fora_localidade(velocidade: float) -> float:
    if velocidade <= 90:
        return 0
    elif velocidade >= 120:
        return 120
    else:
        return 60

def multa_autoestrada(velocidade: float) -> float:
    if velocidade <= 120:
        return 0
    elif velocidade > 175:
        return 360
    elif velocidade > 150:
        return 120
    else:
        return 60

def menu():
    print("\n--- SISTEMA DE CÁLCULO DE MULTAS ---")
    print("1 - Circular na localidade")
    print("2 - Circular fora da localidade")
    print("3 - Circular na autoestrada")
    print("0 - Sair")
    print("-------------------------------------")

def main():
    while True:
        menu()
        try:
            opcao = int(input("Escolha a opção de circulação: "))
            if opcao == 0:
                print("Programa encerrado.")
                break

            velocidade = float(input("Insira a velocidade do veículo (km/h): "))

            if opcao == 1:
                multa = multa_localidade(velocidade)
            elif opcao == 2:
                multa = multa_fora_localidade(velocidade)
            elif opcao == 3:
                multa = multa_autoestrada(velocidade)
            else:
                print("Opção inválida.")
                continue

            if multa == 0:
                print("✔️ Sem multa. Condução dentro dos limites.")
            else:
                print(f"⚠️ Multa a pagar: {multa:.2f}€")

        except ValueError:
            print("Erro: Introduza valores numéricos válidos.")

if __name__ == "__main__":
    main()
