from livros import Livros
from usuario import Usuario, Funcionario, Bibliotecario, Aluno, Professor, Administrador
from usuariodao import UsuarioDao
from livrosdao import LivroDao

biblioteca = LivroDao()
funcionarioDao = UsuarioDao()

while True:
  opcao1 = int(input('Digite o seu usuário:\n1- para Bibliotecario\n2- para Usuario\n3- para Administrador\n4- para Cadastrar Usuário\n5- Sair\n'))
  while True:
      if opcao1 == 1:
        print('Você escolheu bibliotecario')
        opcaobibliotecario = int(input('digite o que você deseja fazer:\n 1-cadastrar livro\n 2-consultar livro\n 3-apagar livro\n4-alterar dados de um livro\n5-cadastrar categoria\n6-alterar categoria\n7-remover categoria\n8-listar categorias\n9-cancelar\n'))
        if opcaobibliotecario == 1:
          print('você escolheu cadastrar livro')
          titulo = input("Digite o título do livro : ")
          exemplar = int(input("Informe a quantidade exemplares: "))
          categoria = input('Informe a categoria: ')
          isbn = int(input("Digite o International Standard Book Number: "))
          autores = input("Digite o nome do autor: ")
          edicao = input("Informe a edição do livro: ")
          editora = input("Digite o nome da editora: ")
          ano = int(input("Informe o ano de lançamento: "))
          assunto = input("Informe o assunto do livro: ")
          livro = Livros( titulo, exemplar, categoria, isbn, autores, edicao, editora, ano, assunto)
          biblioteca.cadastrar_livro(livro)

        elif opcaobibliotecario == 2:
          print('você escolheu consultar livro')
          escolhaconsulta = int(input('1-consuta por título\n2-consulta por categoria\n'))
          if escolhaconsulta == 1:
            consulta = input("Digite o título do livro:\n ")
            biblioteca.consultar_titulo(consulta)
          elif escolhaconsulta == 2:
            consulta = input("Digite a categoria do livro:\n ")
            biblioteca.consultar_categoria(consulta)

        elif opcaobibliotecario == 3:
          print('você escolheu apagar livro')
          excluir = input("Digite o título do livro: ")
          biblioteca.excluir_livro(excluir)

        elif opcaobibliotecario == 4:
          print('você escolheu alterar dados de um livro')
          alteracao = int(input('Digite o que deseja alterar: 1-tudo 2-exemplares 3-categoria 4-cancelar\n'))
          if alteracao == 1:
            alterar = input("Digite o título do livro a alterar: ")
            titulo = input("Digite o novo título: ")
            exemplar = int(input("Digite o novo exemplar: "))
            categoria = input("Digite a nova categoria: ")
            isbn = int(input("Digite o novo ISBN: "))
            autores = input("Digite os novos autores: ")
            edicao = input("Digite a nova edição: ")
            editora = input("Digite a nova editora: ")
            ano = int(input("Digite o novo ano: "))
            assunto = input("Digite o novo assunto: ")
            biblioteca.alterar_livro(alterar, titulo, exemplar, categoria, isbn, autores, edicao, editora, ano, assunto)

          elif alteracao == 2:
            alterar = input("Digite o título do livro a alterar: ")
            exemplar = int(input("Digite o novo exemplar: "))
            biblioteca.alterar_exemplar(alterar, exemplar)

          elif alteracao == 3:
            alterar = input("Digite o título do livro a alterar: ")
            categoria = input("Digite a nova categoria: ")
            biblioteca.alterar_categoria(alterar, categoria)

        elif opcaobibliotecario == 5:
          print('você escolheu cadastrar categoria')
          categoria = input("Digite a categoria a ser cadastrada: ")
          biblioteca.cadastrar_categoria(categoria)

        elif opcaobibliotecario == 6:
          print('você escolheu alterar categoria')
          alterar = input("Digite a categoria a ser alterada: ")
          categoria = input("Digite a nova categoria: ")
          biblioteca.alterar_categoria(alterar, categoria)

        elif opcaobibliotecario == 7:
          print('você escolheu remover categoria')
          remover = input("Digite a categoria a ser removida: ")
          biblioteca.remover_categoria(excluir)

        elif opcaobibliotecario == 8:
          print('você escolheu listar categorias')
          biblioteca.listar_categorias()

        elif opcaobibliotecario == 9:
          print('Você escolheu cancelar')
          break



      elif opcao1 == 2:
        print('Você escolheu usuario')
        opcaousuario = int(input('Digite a ação que deseja realizar:\n1-consultar livro\n2-cancelar\n'))
        if opcaousuario == 1:
          print('você escolheu consultar livro')
          escolhaconsulta = int(input('1-consuta por título\n2-consulta por categoria\n'))
          if escolhaconsulta == 1:
            consulta = input("Digite o título do livro:\n ")
            biblioteca.consultar_titulo(consulta)
          elif escolhaconsulta == 2:
            consulta = input("Digite a categoria do livro:\n ")
            biblioteca.consultar_categoria(consulta)
        elif opcaousuario == 2:
          print('Você escolheu cancelar')
          break
        
      if opcao1 == 3:
        print('Você escolheu Gerente\n')
        opcaoadm = int(input('digite o que você deseja fazer:\n 1-Gerar relatório gerencial para aquisição de livro\n2-Gerar relatório de livros\n3-Gerar relatório de usuários\n'))

        if opcaoadm == 1:
          print('Você escolheu gerar relatório gerencial')
          print('Relatório gerado com sucesso!')

        elif opcaoadm == 2:
          print('Você escolheu gerar relatório de livros')
          biblioteca.gerar_lista_livros()

        elif opcaoadm == 3:
          print('Você escolheu gerar relatório de usuários')
          funcionarioDao.gerar_informacao_usuario()
          
      if opcao1 == 4:
        opcaocadastro = int(input('informe o tipo de usuario a cadastrar:\n 1- Aluno\n2- Professor\n3- Funcionário\n4-Bibliotecário\n5-Administrador\n6-cancelar\n'))
        if opcaocadastro == 1:
          print('Você escolheu cadastrar usuário\n')
          nome_aluno = input('Informe o nome do usuário:\n')
          id_aluno = input('Informe o ID\n')
          novo_aluno = Aluno(nome_aluno, id_aluno)
          funcionarioDao.cadastrar_aluno(novo_aluno)
        elif opcaocadastro == 2:
          print('Você escolheu cadastrar Professor')
          nome_professor = input('Informe o nome do usuário:\n')
          id_professor = input('Informe o ID\n')
          novo_professor = Professor(nome_professor, id_professor)
        elif opcaocadastro == 3:
          print('você escolheu cadastrar funcionário')
          nome_funcionario = input('Informe o nome do usuário:\n')
          id_funcionario = input('Informe o ID\n')
          novo_funcionario = Funcionario(nome_funcionario, id_funcionario)
        elif opcaocadastro == 4:
          print('você escolheu cadastrar bibliotecário')
          nome_bibliotecario = input('Informe o nome do usuário:\n')
          id_bibliotecario = input('Informe o ID\n')
          novo_bibliotecario = Bibliotecario(nome_bibliotecario, id_bibliotecario)
        elif opcaocadastro == 5:
          print('você escolheu cadastrar administrador')
          nome_administrador = input('Informe o nome do usuário:\n')
          id_administrador = input('Informe o ID\n')
          novo_administrador = Administrador(nome_administrador, id_administrador)
        elif opcaocadastro == 6:
          print('você escolheu cancelar')
          break

