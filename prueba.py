
# ---------------------------------------------
# CLASE PUNTO
# ---------------------------------------------
import math

class Punto:
	def __init__(self, x=0, y=0):
		"""Constructor. Si no se recibe una coordenada, su valor será cero."""
		self.x = x
		self.y = y

	def __str__(self):
		"""Sobreescribe el método string para mostrar el punto como (X,Y)."""
		return f"({self.x},{self.y})"

	def cuadrante(self):
		"""Indica a qué cuadrante pertenece el punto."""
		if self.x == 0 and self.y == 0:
			return "Origen"
		elif self.x == 0:
			return "Eje Y"
		elif self.y == 0:
			return "Eje X"
		elif self.x > 0 and self.y > 0:
			return "Primer cuadrante"
		elif self.x < 0 and self.y > 0:
			return "Segundo cuadrante"
		elif self.x < 0 and self.y < 0:
			return "Tercer cuadrante"
		elif self.x > 0 and self.y < 0:
			return "Cuarto cuadrante"

	def vector(self, otro_punto):
		"""Devuelve el vector resultante entre este punto y otro punto como una tupla (dx, dy)."""
		dx = otro_punto.x - self.x
		dy = otro_punto.y - self.y
		return (dx, dy)

	def distancia(self, otro_punto):
		"""Devuelve la distancia entre este punto y otro punto."""
		dx = otro_punto.x - self.x
		dy = otro_punto.y - self.y
		return math.sqrt(dx**2 + dy**2)

# ---------------------------------------------
# CLASE RECTANGULO
# ---------------------------------------------
class Rectangulo:
	def __init__(self, p1=None, p2=None):
		"""Constructor. Si no se envían puntos, ambos serán el origen por defecto."""
		self.p1 = p1 if p1 else Punto()
		self.p2 = p2 if p2 else Punto()

	def base(self):
		"""Devuelve la base del rectángulo."""
		return abs(self.p2.x - self.p1.x)

	def altura(self):
		"""Devuelve la altura del rectángulo."""
		return abs(self.p2.y - self.p1.y)

	def area(self):
		"""Devuelve el área del rectángulo."""
		return self.base() * self.altura()

# ---------------------------------------------
# EXPERIMENTACIÓN Y EJEMPLOS
# ---------------------------------------------
if __name__ == "__main__":
	# Crear los puntos A(2, 3), B(5,5), C(-3, -1) y D(0,0)
	A = Punto(2, 3)
	B = Punto(5, 5)
	C = Punto(-3, -1)
	D = Punto(0, 0)

	print("Puntos:")
	print("A:", A)
	print("B:", B)
	print("C:", C)
	print("D:", D)
	print()

	# Consulta a qué cuadrante pertenecen A, C y D
	print("Cuadrantes:")
	print("A:", A.cuadrante())
	print("C:", C.cuadrante())
	print("D:", D.cuadrante())
	print()

	# Consulta los vectores AB y BA
	print("Vectores:")
	print("Vector AB:", A.vector(B))
	print("Vector BA:", B.vector(A))
	print()

	# Consulta la distancia entre los puntos A y B y B y A
	print("Distancias:")
	print("Distancia A-B:", round(A.distancia(B), 2))
	print("Distancia B-A:", round(B.distancia(A), 2))
	print()

	# Determina cuál de los puntos A, B o C está más lejos del origen
	distancias = {"A": A.distancia(D), "B": B.distancia(D), "C": C.distancia(D)}
	mas_lejos = max(distancias, key=distancias.get)
	print(f"El punto más lejos del origen es: {mas_lejos} con distancia {round(distancias[mas_lejos], 2)}")
	print()

	# Crea un rectángulo utilizando los puntos A y B
	rect = Rectangulo(A, B)
	print("Rectángulo formado por A y B:")
	print("Base:", rect.base())
	print("Altura:", rect.altura())
	print("Área:", rect.area())

# ---------------------------------------------
# REPRESENTACIÓN GRÁFICA CON MATPLOTLIB
# ---------------------------------------------
import matplotlib.pyplot as plt

# Coordenadas de los puntos
x_vals = [A.x, B.x, C.x, D.x]
y_vals = [A.y, B.y, C.y, D.y]
labels = ['A', 'B', 'C', 'D']

# Dibuja los puntos
plt.scatter(x_vals, y_vals, color='red')
for i, txt in enumerate(labels):
	plt.annotate(txt, (x_vals[i], y_vals[i]), textcoords="offset points", xytext=(5,5), ha='center')

# Dibuja el rectángulo formado por A y B
rect_x = [A.x, B.x, B.x, A.x, A.x]
rect_y = [A.y, A.y, B.y, B.y, A.y]
plt.plot(rect_x, rect_y, color='blue')

# Anotaciones de base, altura y área
base_val = rect.base()
altura_val = rect.altura()
area_val = rect.area()

# Coordenadas para las anotaciones
base_x = (A.x + B.x) / 2
base_y = min(A.y, B.y) - 0.5
altura_x = max(A.x, B.x) + 0.5
altura_y = (A.y + B.y) / 2
area_x = (A.x + B.x) / 2
area_y = (A.y + B.y) / 2

plt.text(base_x, base_y, f"Base = {base_val}", color='blue', ha='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue'))
plt.text(altura_x, altura_y, f"Altura = {altura_val}", color='green', va='center', fontsize=10, bbox=dict(facecolor='white', alpha=0.7, edgecolor='green'))
plt.text(area_x, area_y, f"Área = {area_val}", color='purple', ha='center', va='center', fontsize=11, bbox=dict(facecolor='white', alpha=0.7, edgecolor='purple'))

plt.axhline(0, color='gray', linewidth=0.5)
plt.axvline(0, color='gray', linewidth=0.5)
plt.grid(True)
plt.title('Representación de puntos y rectángulo')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
