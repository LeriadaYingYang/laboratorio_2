class Alumno: 
    def __init__(self, codigo, nombre, apellido, celular, dni, edad):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
        self.celular = celular
        self.dni = dni
        self.edad = edad
    
    def ver_alumno(self):
        return f"codigo: {self.codigo} - Nombre: {self.nombre} {self.apellido}"
    
    def obtener_codigo(self):
        return self.codigo
    
        
