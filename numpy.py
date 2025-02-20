import numpy as np
import matplotlib.pyplot as plt

# Generar datos simulando una función senoidal con ruido
x = np.linspace(0, 10, 100)  # 100 puntos entre 0 y 10
y = np.sin(x) + np.random.normal(scale=0.2, size=len(x))  # Señal con ruido

# Ajuste de la curva con una media móvil
window_size = 5
y_smooth = np.convolve(y, np.ones(window_size)/window_size, mode='valid')

# Gráfico
plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o', alpha=0.5, label="Datos con ruido", markersize=4)
plt.plot(x[:len(y_smooth)], y_smooth, '-', linewidth=2, color='r', label="Curva suavizada")

# Estilización
plt.xlabel("Tiempo")
plt.ylabel("Amplitud")
plt.title("Señal con ruido y suavizado")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

# Guardar la imagen como PNG
plt.savefig("grafico_suavizado.png", dpi=300)

# Mostrar el gráfico
plt.show()
