import matplotlib.pyplot as plt
import numpy as np

# Gerar dados de exemplo
dados1 = np.random.normal(100, 10, 200)
dados2 = np.random.normal(80, 30, 200)
dados3 = np.random.normal(90, 20, 200)
dados4 = np.random.normal(70, 25, 200)
dados = [dados1, dados2, dados3, dados4]

# Plotar boxplot
plt.boxplot(dados)
# Adicionar títulos e legendas
plt.title('Boxplot de Dados de Exemplo')
plt.ylabel('Valores')

# Exibir gráfico
plt.show()