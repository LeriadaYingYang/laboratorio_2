class Alumno: 
    def __init__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido
    
    def ver_alumno(self):
        return f"codigo: {self.codigo} - Nombre: {self.nombre} {self.apellido}"
    
    def obtener_codigo(self):
        return self.codigo
    
        
