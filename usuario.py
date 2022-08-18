from livros import Livros

class Usuario:
    def __init__(self, nome, id) -> None:
        self.nome = nome
        self.id = id

class Funcionario(Usuario):
    def __init__(self, nome, id) -> None:
        super().__init__(nome, id)

class Bibliotecario(Usuario):
    def __init__(self, nome, id) -> None:
        super().__init__(nome, id)

class Aluno(Usuario):
    def __init__(self, nome, id) -> None:
        super().__init__(nome, id)
        
class Professor(Usuario):
    def __init__(self, nome, id) -> None:
        super().__init__(nome, id)

class Administrador(Usuario):
    def __init__(self, nome, id) -> None:
        super().__init__(nome, id)