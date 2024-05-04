import matplotlib.pyplot as plt
import numpy as np

#### Plotting the bold game strategy

def phi(prob: float, x: float) -> float:
    if x == 0:
        return 0
    elif x == 1:
        return 1
    # Jeśli x jest mniejsze niż 0.5, stosujemy równanie φ(x) = p * φ(2x)
    elif x < 0.5:
        return prob * phi(prob, 2 * x)
    # W przeciwnym razie, stosujemy równanie φ(x) = p + (1-p) * φ(2x - 1)
    else:
        return (1 - prob) * phi(prob, 2 * x - 1) + prob

# Przykład
prob = 0.3 # Przykładowe prawdopodobieństwo wygranej (p)
num_points = 100  # Liczba punktów do obliczenia
x_values = np.linspace(0, 1, num_points)  # Tworzenie równo rozłożonych wartości x

# Obliczanie wartości φ dla każdego poziomu majątku x
phi_values = [phi(prob, x) for x in x_values]

plt.plot(x_values, phi_values)
plt.title('Prawdopodobieństwo sukcesu (φ) - Bold Play Strategy')
plt.xlabel('Majątek (x)')
plt.ylabel('Prawdopodobieństwo sukcesu (φ)')
plt.grid(True)
plt.show()
