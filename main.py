import tkinter
from tkinter import simpledialog
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.animation import FuncAnimation
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from funciones import trazaConSum

# Crear ventana para pedir valor 'a'
root = tkinter.Tk()
root.withdraw()  # Ocultar la ventana principal
a = simpledialog.askfloat("Valor de a", "Ingrese el valor de a:")
n = simpledialog.askinteger("Valor de n", "Cuantos sub-intervalos (n):")
# Cerrar la ventana emergente
root.destroy()


# Verificar que sea un valor
if a is not None and n is not None:
    #llama a la logica para calcular la traza
    valorTraza = trazaConSum(a,n)
    
    #Interfaz grafica
    fig = plt.figure(figsize=(8,9))
    ax = fig.add_subplot(111, projection='3d')

    def grafCilindro(a):
        # Coordenadas cilindricas
        theta_ = np.linspace(0, 2*np.pi, 100)
        z_ = np.linspace(-10*a,10*a,100)
        theta, z_cili = np.meshgrid(theta_,z_)
        r = a  # Radio del cilindro

        # Coordenadas cartesianas
        x_cili = r * np.cos(theta)
        y_cili = r * np.sin(theta)

        # Graficar el cilindro
        ax.plot_surface(x_cili,y_cili,z_cili, color='crimson',zorder=0,alpha=0.3)

    def grafPlano(a):
        def z(x,y):
            return (8-x-y)/2
        x_plano = np.linspace(-10*a/2,10*a/2)
        y_plano = np.linspace(-10*a/2,10*a/2)
        x_plano,y_plano = np.meshgrid(x_plano,y_plano)
        z_plano = z(x_plano,y_plano)
        ax.plot_surface(x_plano,y_plano,z_plano,color='dodgerblue',zorder=2,alpha=0.45)

    def traza(a):
        t = np.linspace(0,2*np.pi)
        expr_x = a*np.cos(t)
        expr_y = a*np.sin(t)
        expr_z = 4 - (1/2)*(expr_x+expr_y)
        ax.plot(expr_x,expr_y,expr_z,color='black',zorder=1,label="Traza")

    grafCilindro(a)
    grafPlano(a)
    traza(a)
    # Agregar texto dentro de la ventana de Matplotlib
    ax.text2D(0.5, 0, f"El valor de la traza es: {valorTraza}", transform=ax.transAxes,ha='center', va='center', fontsize=14, bbox=dict(boxstyle='round', facecolor='silver', alpha=1))
    
    # Configurar el aspecto del gráfico
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f'Calculo Traza $x^2 + y^2 = {a}^2$ y x+y+2z=8')
    # Ajustar automáticamente la escala de los ejes
    ax.autoscale(enable=False)

    plt.show()
