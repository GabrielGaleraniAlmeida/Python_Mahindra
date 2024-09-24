import pandas as pd
import random
import matplotlib.pyplot as plt


def config():
    # altere o caminho aqui
    CAMINHO_CSV = r'C:\Users\gabri\Downloads\projeto FE\projeto FE\csv\formula_e_lap_times.csv'
    return CAMINHO_CSV
def converter_tempo_para_segundos(tempo_str):
    try:
        if isinstance(tempo_str, str):  # Verifica se é string antes de tentar fazer o split
            minutos, segundos = map(float, tempo_str.split(':'))
            return minutos * 60 + segundos
        elif isinstance(tempo_str, (int, float)):  # Caso o valor já seja numérico, retorne diretamente
            return tempo_str
        else:
            print(f"Valor inválido: {tempo_str}")
            return None
    except ValueError:
        print(f"Erro ao converter o tempo: {tempo_str}")
        return None
def converter_segundos_para_tempo(segundos):
    minutos = int(segundos // 60)
    segundos_resto = segundos % 60
    return f"{minutos:02}:{segundos_resto:04.1f}"

def formatar_diferenca(diferenca):
    if diferenca >= 0:
        return f"+{converter_segundos_para_tempo(diferenca)}"
    else:
        return f"-{converter_segundos_para_tempo(abs(diferenca))}"
def ler_dados():
    caminho_csv = config()  # Obtém o caminho do CSV
    try:
        df = pd.read_csv(caminho_csv)

        # Filtra para Nick De Vries e Edoardo Mortara nos anos de 2023 e 2024
        df_nick_de_vries_2023 = df[(df['Driver'] == 'Nick De Vries') & (df['Year'] == 2023)]
        df_nick_de_vries_2024 = df[(df['Driver'] == 'Nick De Vries') & (df['Year'] == 2024)]
        df_edoardo_mortara_2023 = df[(df['Driver'] == 'Edoardo Mortara') & (df['Year'] == 2023)]
        df_edoardo_mortara_2024 = df[(df['Driver'] == 'Edoardo Mortara') & (df['Year'] == 2024)]

        return (df_nick_de_vries_2023, df_nick_de_vries_2024,
                df_edoardo_mortara_2023, df_edoardo_mortara_2024)
    except FileNotFoundError:
        print(f"Arquivo não encontrado no caminho: {caminho_csv}")
        return None, None, None, None
    except pd.errors.EmptyDataError:
        print("O arquivo está vazio.")
        return None, None, None, None
    except pd.errors.ParserError:
        print("Erro ao analisar o arquivo CSV.")
        return None, None, None, None
def consistencia_das_voltas(df_2023, df_2024, piloto):
    plt.figure(figsize=(12, 8))

    # Converte os tempos de volta para segundos
    df_2023['Lap_Time (s)'] = df_2023['Lap_Time (s)'].apply(converter_tempo_para_segundos)
    df_2024['Lap_Time (s)'] = df_2024['Lap_Time (s)'].apply(converter_tempo_para_segundos)

    # Calcula a volta mais rápida para cada ano
    volta_rapida_2023 = df_2023['Lap_Time (s)'].min()
    volta_rapida_2024 = df_2024['Lap_Time (s)'].min()

    # Calcula a diferença de cada volta em relação à volta mais rápida
    df_2023['Diferença para Volta Rápida (s)'] = df_2023['Lap_Time (s)'] - volta_rapida_2023
    df_2024['Diferença para Volta Rápida (s)'] = df_2024['Lap_Time (s)'] - volta_rapida_2024

    # Plot da consistência para 2023 e 2024 usando gráfico de barras
    plt.bar(df_2023['Lap'] - 0.2, df_2023['Diferença para Volta Rápida (s)'], width=0.4, label=f'{piloto} 2023', align='center')
    plt.bar(df_2024['Lap'] + 0.2, df_2024['Diferença para Volta Rápida (s)'], width=0.4, label=f'{piloto} 2024', align='center')

    plt.xlabel('Volta')
    plt.ylabel('Diferença para Volta Rápida (s)')
    plt.title(f'Consistência das Voltas de {piloto} (2024 vs 2023)')
    plt.legend()
    plt.grid(True)
    plt.show()
def calcular_consumo_energia(voltas, carga_maxima=40, consumo_base=1.5, variacao=0.5, desgaste_pneu=0.1,
                             arrasto_vento=0.2, velocidade_maxima=320):
    consumo_por_volta = []
    velocidade_por_volta = []
    carga_restante = carga_maxima
    desgaste_total = 0

    for volta in range(voltas):
        # Simula a velocidade da volta (pode ser um valor aleatório entre 50% e 100% da velocidade máxima)
        velocidade = random.uniform(0.5, 1) * velocidade_maxima
        velocidade_por_volta.append(velocidade)

        # Consumo aumenta com a velocidade
        fator_velocidade = (velocidade / velocidade_maxima) ** 2  # Maior impacto com velocidades mais altas
        desgaste = desgaste_pneu * desgaste_total
        consumo = consumo_base + desgaste + fator_velocidade  # Consumo influenciado pela velocidade

        if volta % 3 == 0:
            consumo += random.uniform(0, variacao) + arrasto_vento
        else:
            consumo -= random.uniform(0, variacao) - arrasto_vento

        if carga_restante >= consumo:
            carga_restante -= consumo
        else:
            consumo = carga_restante
            carga_restante = 0

        consumo_por_volta.append(consumo)
        desgaste_total += desgaste

        if carga_restante == 0:
            break

    return consumo_por_volta, velocidade_por_volta


# Configurações dos cenários
voltas = 31
cenarios = {
    "Maior Gasto": {"consumo_base": 2.5, "variacao": 1.0, "desgaste_pneu": 0.2, "arrasto_vento": 0.5},
    "Gasto Médio": {"consumo_base": 1.5, "variacao": 0.5, "desgaste_pneu": 0.1, "arrasto_vento": 0.2},
    "Economia de Energia": {"consumo_base": 1.0, "variacao": 0.2, "desgaste_pneu": 0.05, "arrasto_vento": 0.1}
}

# Criar subplots um embaixo do outro
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 10))

# Gerar dados para cada cenário
for nome, params in cenarios.items():
    consumos, velocidades = calcular_consumo_energia(voltas, **params)

    # Plot do consumo de energia
    ax1.plot(consumos, label=nome)

    # Plot da velocidade
    ax2.plot(velocidades, label=nome)

# Personalização do gráfico de consumo
ax1.set_title("Consumo de Energia em Diferentes Cenários")
ax1.set_xlabel("Voltas")
ax1.set_ylabel("Consumo de Energia (kWh)")
ax1.legend()
ax1.grid()

# Personalização do gráfico de velocidade
ax2.set_title("Velocidade em Diferentes Cenários")
ax2.set_xlabel("Voltas")
ax2.set_ylabel("Velocidade (km/h)")
ax2.legend()
ax2.grid()

# Exibir os gráficos
plt.tight_layout()
plt.show()


def exec():
    df_nick_de_vries_2023, df_nick_de_vries_2024, df_edoardo_mortara_2023, df_edoardo_mortara_2024 = ler_dados()

    # Desempenho acumulado e consistência de Nick De Vries
    if not df_nick_de_vries_2023.empty and not df_nick_de_vries_2024.empty:
        consistencia_das_voltas(df_nick_de_vries_2023, df_nick_de_vries_2024, "Nick De Vries")

    # Desempenho acumulado e consistência de Edoardo Mortara
    if not df_edoardo_mortara_2023.empty and not df_edoardo_mortara_2024.empty:
        consistencia_das_voltas(df_edoardo_mortara_2023, df_edoardo_mortara_2024, "Edoardo Mortara")

exec()

