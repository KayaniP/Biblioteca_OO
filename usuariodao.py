from usuario import Usuario,Aluno,Professor,Administrador,Funcionario,Bibliotecario

class UsuarioDao:
    def __init__(self):
      self.lista_aluno = [
          Aluno('Eduardo', 99824834),
          Aluno('Marcela', 23859659),
          Aluno('Felipe', 20211059)
          ]
      self.lista_professor = [
          Professor('Juca', 9340),
          Professor('João',3405),]
      self.lista_funcionario = [
          Funcionario('Paloma', 24945674),
          Funcionario('Rhuan', 24976977),
          Funcionario('Carla', 24987737)
      ]
      self.lista_bibliotecario = [
          Bibliotecario('Beatriz', 998182404),
          Bibliotecario('Marcio', 99727837)
      ]
      self.lista_administrador = [
          Administrador('Murilo', 3789627)
      ]

    def cadastrar_aluno(self,aluno):
        try:
            if aluno.id not in self.lista_aluno:
                self.lista_aluno.append(aluno)
            return self.lista_aluno.append(aluno)
        except:
            return("Erro ao cadastrar usuário")
    
    def cadastrar_professor(self, professor):
        try:
            if professor.id not in self.lista_professor:
                self.lista_professor.append(professor)
            else:
                return('id já cadastrado')
        except:
            return('Errro ao cadastrar professor')
    
    def cadastrar_funcionario(self, funcionario):
        try:
            if funcionario.id not in self.lista_funcionario:
                self.lista_funcionario.append(funcionario)
            else:
                return('id já cadastrado')
        except:
            return('Erro ao cadastrar funcionário')

    def cadastrar_bibliotecario(self, bibliotecario):
        try:
            if bibliotecario.id not in self.lista_bibliotecario:
                self.lista_bibliotecario.append(bibliotecario)
            else:
                return('id já cadastrado')
        except:
            return('Erro ao cadastrar bibliotecário')
    
    def cadastrar_administrador(self, administrador):
        try:
            if administrador.id not in self.lista_administrador:
                self.lista_administrador.append(administrador)
            else:
                return('id já cadastrado')
        except:
            return('Erro ao cadastrar administrador')

    def gerar_informacao_usuario(self):
        print('Alunos:')
        for Alunos in self.lista_aluno:
            print(f'Nome: {Alunos.nome}\nId: {Alunos.id}\n')
        print('Professores:')
        for Professores in self.lista_professor:
            print(f'Nome: {Professores.nome}\nId: {Professores.id}\n')
        print('Funcionários:')
        for Funcionarios in self.lista_funcionario:
            print(f'Nome: {Funcionarios.nome}\nId: {Funcionarios.id}\n')
        print('Bibliotecários:')
        for Bibliotecarios in self.lista_bibliotecario:
            print(f'Nome: {Bibliotecarios.nome}\nId: {Bibliotecarios.id}\n')
        print('Administradores:')
        for Administradores in self.lista_administrador:
            print(f'Nome: {Administradores.nome}\nId: {Administradores.id}\n')
            
        