import matplotlib.pyplot as plt

def grafica_pie(x, y):
    explode = (0, 0.1, 0, 0)
    plt.pie(y, labels=x, autopct='%1.1f%%', explode=explode,  shadow=True, startangle=90)
    plt.show()

def muestra_grafica_linea(x,y, ylabel="", title=""):    
    fig, ax = plt.subplots()
    ax.grid()
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.plot(x,y, color='red', linewidth = '3')
    plt.show()

def muestra_tabla(data, column_labels):
    fig, ax = plt.subplots()
    ax.axis('tight')
    ax.axis('off')
    ax.table(cellText=data, colLabels=column_labels,loc="center") 
    plt.show()

def main():
    x = ['Lola', 'Alejandra', 'Fernando', 'José']
    y = [5.6, 9.4, 4.7, 6]
    grafica_pie(x, y)
    muestra_grafica_linea(x,y)
    titulos = ['Nombre', 'Edad', 'Estatura', 'Peso']
    datos = [['Pedro', 35, 1.71, 80],['Juan', 21, 1.89, 75], ['Alejandra', 16, 1.65, 57]]
    muestra_tabla(datos, titulos)
if __name__ == '__main__':
    main()