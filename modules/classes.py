
#*************
# Sena, Mosquera CBA
# Brayan Esteban Penagos Gutierrez
# Version 2.0
# 02/05/2024
# Ficha: 2877795
#Funcionalidad: Clases y Objetos con Herencia
#*************


class Persona:
    def __init__(self,id = 0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.__fecha_nacimiento = fecha_nacimiento
        self.__ciudad_nacimiento = ciudad_nacimiento
        self.genero = genero
        self.estrato = estrato

    def get_id(self):
        return self.id
    
    def set_id(self, value):
        self.id = value

    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, value):
        self.nombre = value

    def get_apellido(self):
        return self.apellido
    
    def set_apellido(self, value):
        self.apellido = value

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento
    
    def set_fecha_nacimiento(self, value):
        self.__fecha_nacimiento = value

    def get_genero(self):
        return self.genero

    def set_genero(self,value):
        self.genero = value

    def get_estrato(self):
        return self.estrato
    
    def set_estrato(self, value):
        self.estrato = value

    def get_ciudad_nacimiento(self):
        return self.__ciudad_nacimiento
    
    def set_ciudad_nacimiento(self, value):
        self.__ciudad_nacimiento = value
    
    def datos_generales(self):
        id = input('\n''Ingrese su id: ')
        self.set_id(id)
        opcion = input('\n''Ingrese su nombre: ')
        self.set_nombre(opcion)
        apellido = input('\n''Ingrese su apellido: ')
        self.set_apellido(apellido)
        nacimiento= input('\n''Ingrese su fecha de nacimeinto: ')
        self.set_fecha_nacimiento(nacimiento)
        lugar = input('\n''Ingrese donde nacio: ')
        self.set_ciudad_nacimiento(lugar)
        genero = input('\n''Ingrese su genero: ')
        self.set_genero(genero)
        estrato = input('\n''Ingrese su estrato: ')
        self.set_estrato(estrato)


    def informacion_persona(self):
        print('\n''El Id de la persona es {0}, su nombre es {1}, su apellido es {2}, la fecha de nacimiento es {3}, el lugar donde nació es {4}, su genero es {5} y el estrato es {6}.'.format(self.get_id(), self.get_nombre(), self.get_apellido(), self.get_fecha_nacimiento(), self.get_ciudad_nacimiento(), self.get_genero(), self.get_estrato()))
class Docentes(Persona):
    def __init__(self, area_formacion= ' ', tituloprofesional=' ', unidadacademica = ' ',id = 0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0):
        super().__init__(id,nombre,apellido,fecha_nacimiento,ciudad_nacimiento,genero,estrato)
        self.area_formacion = area_formacion
        self.tituloprofesional = tituloprofesional
        self.unidadacademica = unidadacademica
        
        
    def get_area_formacion(self):
        return self.area_formacion
    
    def set_area_formacion(self, value):
        self.area_formacion = value

    def get_tituloprofesional(self):
        return self.tituloprofesional
    
    def set_tituloprofesional(self, value):
        self.tituloprofesional = value

    def get_unidadacademica(self):
        return self.unidadacademica
    
    def set_unidadacademica(self, value):
        self.unidadacademica = value


    
    def mostrar_informacion_docente(self):
        return super().mostrar_informacion()
    
class Tiempo_Completo(Docentes):
    def __init__(self, categoria=' ', puntos=0, salario=0,area_formacion= ' ', tituloprofesional=' ', unidadacademica = ' ',id = 0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0):
        super().__init__(area_formacion, tituloprofesional,unidadacademica, id,nombre,apellido,fecha_nacimiento,ciudad_nacimiento,genero,estrato)
        self.categoria = categoria
        self.puntos = puntos
        self.salario = salario


    def get_categoria(self):
        return self.categoria
    
    def set_categoria(self, value):
        self.categoria = value

    def get_puntos(self):
        return self.puntos
    
    def set_puntos(self, value):
        self.puntos = value

    def get_salario(self):
        return self.salario
    

class Ocasionales(Docentes):
    def __init__(self, ultimo_titulo=' ', num_meses=0, salario=0,area_formacion= ' ', titulo_profesional=' ', unidad_academica = ' ',id = 0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0):
        super().__init__(area_formacion, titulo_profesional, unidad_academica, id, nombre, apellido, fecha_nacimiento, ciudad_nacimiento, genero, estrato)
        self.ultimo_titulo = ultimo_titulo
        self.num_meses = num_meses
        self.salario = salario

    def get_ultimo_titulo(self):
        return self.ultimo_titulo
    
    def set_ultimo_titulo(self, value):
        self.ultimo_titulo = value

    def get_num_meses(self):
        return self.num_meses
    
    def set_num_meses(self, value):
        self.num_meses = value

    def  get_salario(self):
        return self.salario
    
    def set_salario(self,value):
        self.salario = value

class Hora_Catedra(Docentes):
    def __init__(self, num_horas=0, ultimo_titulo=' ', valor_contrato=0, salario=0, area_formacion=' ', tituloprofesional=' ', unidadacademica=' ', id=0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0):
        super().__init__(area_formacion, tituloprofesional, unidadacademica, id, nombre, apellido, fecha_nacimiento, ciudad_nacimiento, genero, estrato)
        self.num_horas = num_horas
        self.ultimo_titulo = ultimo_titulo
        self.valor_contrato = valor_contrato
        self.salario = salario
    def get_ultimo_titulo(self):
        return self.ultimo_titulo
    
    def set_ultimo_titulo(self, value):
        self.ultimo_titulo = value

    def get_num_horas(self):
        return self.num_horas
    
    def set_num_horas(self, value):
        self.num_horas = value

    def get_valor_contrato(self):
        return self.valor_contrato
    
    def set_valor_contrato(self,value):
        self.valor_contrato = value

    def get_salario(self):
        return self.salario
    
    def set_salario(self,value):
        self.salario = value

class Administrativos(Persona):
    def __init__(self, dependencia=' ', titulo=0, id=0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0):
        super().__init__(id,nombre,apellido,fecha_nacimiento,ciudad_nacimiento,genero,estrato)
        self.dependencia = dependencia
        self.titulo = titulo

    def get_dependencia(self):
        return self.dependencia
    
    def set_dependencia(self, value):
        self.dependencia = value

    def get_titulo(self):
        return self.titulo
    
    def set_titulo(self, value):
        self.titulo = value

class Planta(Administrativos):
    def __init__(self, fecha_vinculacion=' ', id=0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=0, genero=' ', estrato=0, salario=0):
        super().__init__(fecha_vinculacion, id, nombre, apellido, fecha_nacimiento, ciudad_nacimiento, genero, estrato,salario)
        self.fecha_vinculacion = fecha_vinculacion
    
    def get_fecha_vinculacion(self):
        return self.fecha_vinculacion
    
    def set_fecha_vinculacion(self,value):
        self.fecha_vinculacion = value

class OPS(Administrativos):
    def __init__(self, fecha_vinculacion=0, num_meses=0, valor_contrato=0, salario=0, id=0, nombre=' ', apellido=' ', fecha_nacimiento=0, ciudad_nacimiento=' ', genero=' ', estrato=' '):
        super().__init__(id, nombre, apellido, fecha_nacimiento, ciudad_nacimiento, genero, estrato, salario)
        self.fecha_vinculacion = fecha_vinculacion
        self.num_meses = num_meses
        self.valor_contrato = valor_contrato
    
    def get_fecha_vinculacion(self):
        return self.fecha_vinculacion
    
    def set_fecha_vinculacion(self, value):
        self.fecha_vinculacion = value
    
    def get_num_meses(self):
        return self.num_meses
    
    def set_num_meses(self, value):
        self.num_meses = value
    
    def get_valor_contrato(self):
        return self.valor_contrato
    
    def set_valor_contrato(self, value):
        self.valor_contrato = value
        

class Auxiliar(Planta):
    def __init__(self, fecha_vinculacion=0,nivel=' ', salario=0):
        super().__init__(fecha_vinculacion)
        self.__nivel = nivel
        self.salario = salario
    
    def get_nivel(self):
        return self.__nivel
    
    def set_nivel(self, value):
        self.__nivel = value
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, value):
        self.salario = value
        
class Tecnico(Planta):
    def __init__(self, fecha_vinculacion=0,nivel=' ', salario=0):
        super().__init__(fecha_vinculacion)
        self.__nivel = nivel
        self.salario = salario
    
    def get_nivel(self):
        return self.__nivel
    
    def set_nivel(self, value):
        self.__nivel = value
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, value):
        self.salario = value
        

class Profesional(Planta):
    def __init__(self, fecha_vinculacion=0,nivel=' ', salario=0):
        super().__init__(fecha_vinculacion)
        self.__nivel = nivel
        self.salario = salario
    
    def get_nivel(self):
        return self.__nivel
    
    def set_nivel(self, value):
        self.__nivel = value
    
    def get_salario(self):
        return self.salario
    
    def set_salario(self, value):
        self.salario = value