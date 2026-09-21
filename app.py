def classificar_consumo():
    print("=== Sistema de Classificação de Consumo de Água ===")
    
    # Solicita o tipo de imóvel do usuário
    tipo_imovel = input("Digite o tipo de imóvel (comercial, casa ou apartamento): ").strip().lower()
    
    # Valida e solicita o consumo mensal de água
    try:
        consumo = float(input("Digite o consumo mensal de água em metros cúbicos (m3): "))
    except ValueError:
        print("Erro: Por favor, digite um valor numérico válido para o consumo.")
        return

    print("\n--- Resultado da Análise ---")
    
    # Regras de negócio solicitadas pela campanha de conscientização
    if tipo_imovel == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")
    elif tipo_imovel == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")
    elif (tipo_imovel == "apartamento") or (tipo_imovel == "casa" and consumo <= 25):
        print("Consumo moderado – dentro do padrão residencial.")
    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")

if __name__ == "__main__":
    classificar_consumo()
