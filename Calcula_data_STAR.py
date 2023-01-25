import datetime
x = float(input("Digite o número de dias: "))
hoje = datetime.datetime.now()
hoje.isoformat()
semana = ["Domingo, Segunda, Terça, Quarta, Quinta, Sexta, Sábado"]
# Espero te ajudar-desu :>
daqui_a_30_dias = hoje + datetime.timedelta(days=x)
print(daqui_a_30_dias)
dia_da_semana = daqui_a_30_dias.isoweekday()
print(semana[dia_da_semana])
