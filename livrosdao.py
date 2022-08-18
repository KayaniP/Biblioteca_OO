from livros import Livros

class LivroDao:
    def __init__(self):
        self.lista_livros = [
            Livros('o sangue do olimpo', 100, 'Fantasia', 9788580575950, 'Rick Riordan', 'Outubro de 2014', 'Intrínseca', 2014, 'The Blood of Olympus é um romance de fantasia inspirado na mitologia greco-romana escrito por Rick Riordan É o quinto e último livro da série Os Heróis do Olimpo, que sucede a série Percy Jackson & the Olympians'),Livros('O poder do Espírito', 100, 'Fantasia', 9788580575951, 'Rick Riordan', 'Outubro de 2014', 'Intrínseca', 2014, 'O poder do espírito é um romance de fantasia inspirado na mitologia greco-romana escrito por Rick Riordan É o quinto e último livro da série Os Heróis do Olimpo, que sucede a série Percy Jackson & the Olympians'),
            Livros('assassinato no expresso oriente', 50, 'Romance', 9788595080638, 'Agatha Christie', 'Setembro de 2016', 'Harper Collins Brasil', 1934, 'Murder on the Orient Express é um romance policial escrito por Agatha Christie e protagonizado pelo detetive belga Hercule Poirot.'),
            Livros('teto para dois', 80, 'Romance', 9788551005415, 'Beth O Leary', 'Setembro de 2019', 'Intrínseca', 2019, 'Eles dividem um apartamento com uma cama só. Ele dorme de dia, ela, à noite. Os dois nunca se encontraram, mas estão prestes a descobrir que, para se sentir em casa, às vezes é preciso jogar as regras pela janela.' )
            ]
        self.lista_categorias = ['Fantasia','Ficção Científica','Romance','Ação','Aventura','Terror','Suspense','Biografia','Auto-Ajuda','Infantil','Ficção','História','Fantasia','Ficção Científica','Romance','Ação','Aventura','Terror','Suspense','Biografia','Auto-Ajuda','Infantil','Ficção','História']


    def consultar_titulo(self,consulta):
        consulta = consulta.lower()
        for livro in self.lista_livros:
            if livro.titulo == consulta:
                print(f'Titulo: {livro.titulo}\nExemplar: {livro.exemplar}\nCategoria: {livro.categoria}\nISBN: {livro.isbn}\nAutores: {livro.autores}\nEdição: {livro.edicao}\nEditora: {livro.editora}\nAno: {livro.ano}\nAssunto: {livro.assunto}')

    def consultar_categoria(self,consulta):
        consulta = consulta[0].upper() + consulta[1:]
        for livro in self.lista_livros:
            if livro.categoria == consulta:
                print(f'Titulo: {livro.titulo}\nExemplar: {livro.exemplar}\nCategoria: {livro.categoria}\nISBN: {livro.isbn}\nAutores: {livro.autores}\nEdição: {livro.edicao}\nEditora: {livro.editora}\nAno: {livro.ano}\nAssunto: {livro.assunto}')
    
    def cadastrar_livro(self,livro):
        livro = livro.lower()
        if livro.categoria in self.lista_categorias:
            try:
                return self.lista_livros.append(livro)
            except:
                return("Erro ao cadastrar livro")
        else:
            return("Categoria não cadastrada")

    def excluir_livro(self,excluir):
        for livro in self.lista_livros:
            print(excluir)
            if livro.titulo == excluir:
                self.lista_livros.remove(livro)
                return ("Livro excluido com sucesso")

    def alterar_livro(self,alterar,titulo,exemplar,categoria,isbn,autores,edicao,editora,ano,assunto) -> None:
        for livro in self.lista_livros:
            if livro.titulo == alterar:
                livro.titulo = titulo
                livro.exemplar = exemplar
                livro.categoria = categoria
                livro.isbn = isbn
                livro.autores = autores
                livro.edicao = edicao
                livro.editora = editora
                livro.ano = ano
                livro.assunto = assunto
                return ("Livro alterado com sucesso")
    
    def alterar_categoria(self,alterar,categoria):
        for livro in self.lista_livros:
            if livro.titulo == alterar:
                livro.categoria = categoria
                return ("Categoria alterada com sucesso")
    
    def alterar_exemplar(self,alterar,exemplar):
        for livro in self.lista_livros:
            if livro.titulo == alterar:
                livro.exemplar = exemplar
                return ("Exemplar alterado com sucesso")
    
    def cadastrar_categoria(self,categoria):
        categoria = categoria[0].upper() + categoria[1:]
        if categoria not in self.lista_categorias:
            self.lista_categorias.append(categoria)
            return ("Categoria cadastrada com sucesso")
        else:
            return ("Categoria já cadastrada")
    
    def remover_categoria(self,categoria):
        if categoria in self.lista_categorias:
            self.lista_categorias.remove(categoria)
            return ("Categoria removida com sucesso")
    
    def alterar_categoria(self,alterar,categoria):
        for livro in self.lista_livros:
            if livro.titulo == alterar:
                livro.categoria = categoria
                return ("Categoria alterada com sucesso")
    
    def listar_categorias(self):
        for categoria in self.lista_categorias:
            print(categoria)
    
    def gerar_lista_livros(self):
        try:
            total_exemplar = sum(livro.exemplar for livro in self.lista_livros)
            for livro in self.lista_livros:
                print(f"Título: {livro.titulo}\nExemplares: {livro.exemplar}\n")
            print(f'Total no acervo: {total_exemplar}')

                
        except:
            return('Erro ao gerar lista de livros')