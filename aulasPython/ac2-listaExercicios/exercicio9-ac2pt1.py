class Instrutor:
    def __init__(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome


class CursoOnline:
    def __init__(self, titulo, carga_horaria, instrutor):
        self.__titulo = titulo
        self.__carga_horaria = carga_horaria
        self.__instrutor = instrutor

    def get_titulo(self):
        return self.__titulo

    def get_carga_horaria(self):
        return self.__carga_horaria

    def get_instrutor(self):
        return self.__instrutor

    def iniciar_aula(self):
        pass


class CursoProgramacao(CursoOnline):
    def iniciar_aula(self):
        print("Iniciando aula de programação.")


class CursoDesign(CursoOnline):
    def iniciar_aula(self):
        print("Iniciando aula de design.")


# Instrutores
instrutor_python = Instrutor("Ana Souza")
instrutor_design = Instrutor("Carlos Lima")

# Lista de cursos (com None simulando posições vazias/inválidas)
cursos = [
    None,
    None,
    CursoProgramacao("Python Avançado", 40, instrutor_python),
    CursoDesign("Design Gráfico", 30, instrutor_design),
]

for curso in cursos:
    if curso is not None:
        curso.iniciar_aula()
