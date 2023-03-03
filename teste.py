from datetime import datetime

# Definindo as variáveis do empréstimo
valor_emprestimo = 500
taxa_juros = 0.10
num_prestacoes = 10

# Definindo as datas de vencimento e pagamento
data_vencimento = "2023-03-10"
data_pagamento = "2023-03-05"

# Convertendo as datas para objetos datetime
dt_vencimento = datetime.strptime(data_vencimento, '%Y-%m-%d')
dt_pagamento = datetime.strptime(data_pagamento, '%Y-%m-%d')

# Calculando o número de dias de antecedência
dias_antecipacao = (dt_vencimento - dt_pagamento).days

# Calculando o valor da prestação
valor_prestacao = valor_emprestimo / num_prestacoes

# Calculando o valor da antecipação de 10 parcelas
valor_antecipacao = sum([valor_prestacao/(1+taxa_juros)**i for i in range(1, 11)])
valor_antecipacao *= (1 + taxa_juros)**dias_antecipacao
print(f"O valor da antecipação de 10 parcelas é R$ {valor_antecipacao:.2f}")

