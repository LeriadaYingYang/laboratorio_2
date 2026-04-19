class Alumno:
    def __init__(self, nombre, nota1,nota2,nota3):
        self.nombre = nombre
        self.nota1= nota1
        self.nota2=nota2
        self.nota3=nota3

    def calcular_promedio(self):
        return(self.nota1 + self.nota2 + self.nota3)/3
    
    def estado(self):
        if self.calcular_promedio()>= 11:
            return "Aprobado"
        else:
            return "Desaprobado"
        
    def mostrar_datos(self):
        print("Nombre:", self.nombre)
        print("Notas:",
             int(self.nota1),
             int(self.nota2),
             int(self.nota3))

        print("Promedio:", round(self.calcular_promedio(),2))
        print("Estado:", self.estado())
    
if __name__== "__main__":
        nombre=input("Ingrese el nombre del alumno: ")
        n1 = float(input("Ingrese nota 1: "))
        n2 = float(input("Ingrese nota 2: "))
        n3 = float(input("Ingrese nota 3: "))
        
        alumno1= Alumno(nombre, n1,n2,n3)
        alumno1.mostrar_datos()
