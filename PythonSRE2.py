numero_intervalos_dia = int(2)
intervalos_dia = [{8,17},{9,18},{7,16}]

for _ in range(numero_intervalos_dia):
    hours_range_str = input().split(',')
    hours_range = [int(hour) for hour in hours_range_str]
    intervalos_dia.append(hours_range)


# TODO: Define function to find the shutdown range given
# the number of ranges and the list of usage ranges
def find_shutdown_range(numero_intervalos_dia, intervalos_dia):

    # Ordena todos os intervalos por hora de início para facilitar a comparação
    todos_intervalos = sorted(intervalos_dia, key=lambda x: x[0])

    # Inicializa variáveis para rastrear o intervalo não utilizado
    inicio_nao_utilizado = 0
    fim_nao_utilizado = 23

    # Itera pelos intervalos ordenados
    for intervalo in todos_intervalos:
        inicio, fim = intervalo

        # Se o início do intervalo atual está dentro do intervalo não utilizado,
        # atualiza o fim não utilizado para o início do intervalo atual
        if inicio <= fim_nao_utilizado:
            fim_nao_utilizado = min(fim_nao_utilizado, inicio)  # Garanta o horário de término correto

        # Se houver uma lacuna entre o fim não utilizado atual e o início do próximo intervalo,
        # essa é uma faixa de desligamento potencial
        if fim_nao_utilizado < inicio:
            intervalo_desligamento = f'{fim_nao_utilizado},{inicio - 1}'  # Ajustar para horas 0-23
            return intervalo_desligamento

    # Se nenhum intervalo não utilizado for encontrado dentro dos intervalos, retorne todo o tempo não utilizado
    return f'{fim_nao_utilizado},{inicio_nao_utilizado - 1}'  # Ajustar para horas 0-23

# Obter entrada para intervalos adicionais (conforme especificado no prompt)
for _ in range(numero_intervalos_dia):
    intervalo_horas_str = input().split(',')
    intervalo_horas = [int(hora) for hora in intervalo_horas_str]
    intervalos_dia.append(intervalo_horas)

intervalo_desligamento = encontrar_intervalo_desligamento(numero_intervalos_dia, intervalos_dia)

shutdown_range = find_shutdown_range(numero_intervalos_dia, intervalos_dia)

print(shutdown_range)
