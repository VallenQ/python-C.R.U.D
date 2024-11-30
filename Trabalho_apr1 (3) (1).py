class usuario:
    cpf=''
    nome=''
    rua=''
    nro=''
    cep=''
    emails=[]
    telefones=[]
    data_de_nasc=''
    profissao=''
class livro:
    isbn=''
    titulo=''
    genero=''
    autores=[]
    num_de_pag=''
class emprestimo:
    cpf=''
    isbn=''
    data_ret=''
    data_dev=''
    valor_dia_multa=''
def menu():
    print('Menu de opções:')
    print('Digite 1 para acessar o Submenu de Usuários.')
    print('Digite 2 para acessar o Submenu de Livros.')
    print('Digite 3 para acessar o Submenu de Empréstimos.')
    print('Digite 4 para acessar o Submenu Relatórios.')
    print('Digite 0 para encerrar o programa.')
    return int(input('digite a opção desejada (de 0 a 4): '))
def submenu_usuarios():
    print('Submenu de Usuários:')
    print('Digite 1 para listar todos os usuários.')
    print('Digite 2 para consultar um usuário.')
    print('Digite 3 para cadastrar um novo usuário.')
    print('Digite 4 para alterar um usuário.')
    print('Digite 5 para excluir um usuário.')
    print('Digite 0 para voltar ao menu príncipal.')
    return int(input('digite a opção desejada (de 0 a 5): '))
def submenu_livros():
    print('Submenu de Livros:')
    print('Digite 1 para listar todos os livros.')
    print('Digite 2 para consultar um livro.')
    print('Digite 3 para cadastrar um novo livro.')
    print('Digite 4 para alterar um livro.')
    print('Digite 5 para excluir um livro.')
    print('Digite 0 para voltar ao menu príncipal.')
    return int(input('digite a opção desejada (de 0 a 5): '))
def submenu_emprestimos():
    print('Submenu de Empréstimos:')
    print('Digite 1 para listar todos os empréstimos.')
    print('Digite 2 para consultar um empréstimo.')
    print('Digite 3 para cadastrar um novo empréstimo.')
    print('Digite 4 para alterar um empréstimo.')
    print('Digite 5 para excluir um empréstimo.')
    print('Digite 0 para voltar ao menu príncipal.')
    return int(input('digite a opção desejada (de 0 a 5): '))
def submenu_relatorios():
    print('Submenu Relatórios:')
    print('Digite 1 para listar todos os usuários maiores de X anos de idade.')
    print('Digite 2 para listar todos os livros com mais de X autores.')
    print('Digite 3 para listar todos os emprestimos realizados entre dd/mm/aaaa e dd/mm/aaaa.')
    print('Digite 0 para voltar ao menu príncipal.')
    return int(input('digite a opção desejada (de 0 a 3): '))
def existe_arquivo(nome_arquivo):
    import os
    if os.path.exists(nome_arquivo):
        return True
    else:
        return False
def escrever_arquivo_user(usuarios, arquivo_user):
    arq=open(arquivo_user, 'w')
    i=0
    while i<len(usuarios):
        arq.write(usuarios[i].cpf+';'+usuarios[i].nome+';'+usuarios[i].rua+';'+usuarios[i].nro+';'+usuarios[i].cep+';')
        cont=0
        while cont<len(usuarios[i].emails):
            if cont!=0:
                arq.write('_')
            arq.write(usuarios[i].emails[cont])
            cont+=1
        arq.write(';')
        cont=0
        while cont<len(usuarios[i].telefones):
            if cont!=0:
                arq.write('_')
            arq.write(usuarios[i].telefones[cont])
            cont+=1
        arq.write(';'+usuarios[i].data_de_nasc+';'+usuarios[i].profissao+'\n')
        i+=1
    arq.close()
def escrever_arquivo_livro(livros, arquivo_livro):
    arq=open(arquivo_livro, 'w')
    i=0
    while i<len(livros):
        arq.write(livros[i].isbn+';'+livros[i].titulo+';'+livros[i].genero+';')
        cont=0
        while cont<len(livros[i].autores):
            if cont!=0:
                arq.write('_')
            arq.write(livros[i].autores[cont])
            cont+=1
        arq.write(';'+livros[i].num_de_pag+'\n')
        i+=1
    arq.close()
def escrever_arquivo_emprestimo(emprestimos, arquivo_emp):
    arq=open(arquivo_emp, 'w')
    i=0
    while i<len(emprestimos):
        arq.write(emprestimos[i].cpf+';'+emprestimos[i].isbn+';'+emprestimos[i].data_ret+';'+emprestimos[i].data_dev+';'+emprestimos[i].valor_dia_multa+'\n')
        i+=1
    arq.close()
def ler_arquivo_user(arquivo_user):
    dados_usuarios=[]
    if existe_arquivo(arquivo_user):
        arq=open(arquivo_user, 'r')
        for linha in arq:
            dados=linha.replace('\n', '').split(';')
            user=usuario()
            user.emails=[]
            user.telefones=[]
            user.cpf=dados[0]
            user.nome=dados[1]
            user.rua=dados[2]
            user.nro=dados[3]
            user.cep=dados[4]
            user.emails=dados[5].split('_')
            user.telefones=dados[6].split('_')
            user.data_de_nasc=dados[7]
            user.profissao=dados[8]
            dados_usuarios.append(user)
        arq.close()
    return dados_usuarios
def ler_arquivo_livro(arquivo_livro):
    dados_livros=[]
    if existe_arquivo(arquivo_livro):
        arq=open(arquivo_livro, 'r')
        for linha in arq:
            dados=linha.replace('\n', '').split(';')
            livros=livro()
            livros.autores=[]
            livros.isbn=dados[0]
            livros.titulo=dados[1]
            livros.genero=dados[2]
            livros.autores=dados[3].split('_')
            livros.num_de_pag=dados[4]
            dados_livros.append(livros)
        arq.close()
    return dados_livros
def ler_arquivo_emprestimo(arquivo_emp):
    dados_emprestimos=[]
    if existe_arquivo(arquivo_emp):
        arq=open(arquivo_emp, 'r')
        for linha in arq:
            dados=linha.replace('\n', '').split(';')
            emp=emprestimo()
            emp.cpf=dados[0]
            emp.isbn=dados[1]
            emp.data_ret=dados[2]
            emp.data_dev=dados[3]
            emp.valor_dia_multa=dados[4]
            dados_emprestimos.append(emp)
        arq.close()
    return dados_emprestimos
def check_cpf(usuarios, user_cpf):
    i=0
    while i<len(usuarios):
        if usuarios[i].cpf==user_cpf:
            return i
        i+=1
    return -1
def check_isbn(livros, livro_isbn):
    i=0
    while i<len(livros):
        if livros[i].isbn==livro_isbn:
            return i
        i+=1
    return -1
def check_emp(emprestimos, user_cpf, livro_isbn, data_reti):
    i=0
    while i<len(emprestimos):
        if emprestimos[i].cpf==user_cpf and emprestimos[i].isbn==livro_isbn and emprestimos[i].data_ret==data_reti:
            return i
        i+=1
    return -1
def imprimir_lista(lista):
    i=0
    while i<len(lista):
        print (lista[i], end=' / ')
        i+=1
def listar_usuarios(usuarios):
    i=0
    while i<len(usuarios):
        print(usuarios[i].cpf+'/'+usuarios[i].nome+'/'+usuarios[i].rua+'/'+usuarios[i].nro+'/'+usuarios[i].cep, end=' / ')
        imprimir_lista(usuarios[i].emails)
        imprimir_lista(usuarios[i].telefones)
        print(usuarios[i].data_de_nasc+' / '+usuarios[i].profissao)
        i+=1
def consultar_usuario(usuarios, user_cpf):
    i=check_cpf(usuarios, user_cpf)
    if i==-1:
        print('CPF não cadastrado.')
    else:
        print(usuarios[i].cpf+'/'+usuarios[i].nome+'/'+usuarios[i].rua+'/'+usuarios[i].nro+'/'+usuarios[i].cep, end=' / ')
        imprimir_lista(usuarios[i].emails)
        imprimir_lista(usuarios[i].telefones)
        print(usuarios[i].data_de_nasc+' / '+usuarios[i].profissao)
def cadastrar_usuario(usuarios):
    user=usuario()
    user.emails=[]
    user.telefones=[]
    user.cpf=input('Informe o cpf do usuário a ser cadastrado: ')
    check=check_cpf(usuarios, user.cpf)
    if check!=-1:
        print(f'Esse cpf já está cadastrado e pertence a {usuarios[check].nome}.')
    else:
        user.nome=input('Informe o nome do usuário a ser cadastrado: ')
        user.rua=input('Informe a rua onde o usuário a ser cadastrado mora: ')
        user.nro=input('Informe o Nro do usuário a ser cadastrado (usando somente números): ')
        user.cep=input('Informe o cep do endereço do usuário a ser cadastrado: ')
        i=0
        num=int(input('quantos e-mails deseja cadastrar? '))
        while i<num:
            user.emails.append(input('Informe o(um dos) e-mail(s) a ser(em) cadastrado(s): '))
            i+=1
        i=0
        num=int(input('quantos telefones deseja cadastrar? '))
        while i<num:
            user.telefones.append(input('Informe o(um dos) telefone(s) a ser(em) cadastrado(s): '))
            i+=1
        user.data_de_nasc=input('Informe a data de nascimento do usuário a ser cadastrado, no formato dd/mm/aaaa: ')
        user.profissao=input('Informe a profissão do usuário a ser cadastrado: ')
        usuarios.append(user)
def alterar_usuario(usuarios, user_cpf):
    check=check_cpf(usuarios, user_cpf)
    if check==-1:
        print('O cpf fornecido ainda não foi cadastrado.')
    else:
        print('Digite 1 para alterar o nome do usuário.')
        print('Digite 2 para alterar a rua do usuário.')
        print('Digite 3 para alterar o Nro do usuário.')
        print('Digite 4 para alterar o cep do usuário.')
        print('Digite 5 para alterar o(s) email(s) do usuário.')
        print('Digite 6 para alterar o(s) telefone(s) do usuário.')
        print('Digite 7 para alterar a data de nascimento do usuário.')
        print('Digite 8 para alterar a profissão do usuário.')
        print('Digite 9 para alterar todos os dados do usuário(EXCETO CPF).')
        op=int(input('digite a opção desejada (de 1 a 9): '))
        if op==1:
            usuarios[check].nome=input('Informe o novo nome do usuário: ')
        elif op==2:
            usuarios[check].rua=input('Informe a nova rua do usuário: ')
        elif op==3:
            usuarios[check].nro=input('Informe o novo Nro do usuário (usando somente números): ')
        elif op==4:
            usuarios[check].cep=input('Informe o novo cep do usuário: ')
        elif op==5:
            num=int(input('Quantos e-mails deseja fornecer? '))
            i=0
            usuarios[check].emails=[]
            while i<num:
                usuarios[check].emails.append(input('Informe o(um dos) e-mail(s) a ser(em) alterado(s): '))
                i+=1
        elif op==6:
            num=int(input('Quantos telefones deseja fornecer? '))
            i=0
            usuarios[check].telefones=[]
            while i<num:
                usuarios[check].telefones.append(input('Informe o(um dos) telefone(s) a ser(em) alterado(s): '))
                i+=1
        elif op==7:
            usuarios[check].data_de_nasc=input('Informe a nova data de nascimento do usuário: ')
        elif op==8:
            usuarios[check].profissao=input('Informe a nova profissão do usuário: ')
        elif op==9:
            usuarios[check].nome=input('Informe o novo nome do usuário: ')
            usuarios[check].rua=input('Informe a nova rua do usuário: ')
            usuarios[check].nro=input('Informe o novo nro do usuário (usando somente números): ')
            usuarios[check].cep=input('Informe o novo cep do usuário: ')
            num=int(input('Quantos e-mails deseja fornecer? '))
            i=0
            usuarios[check].emails=[]
            while i<num:
                usuarios[check].emails.append(input('Informe o(um dos) e-mail(s) a ser(em) alterado(s): '))
                i+=1
            num=int(input('Quantos telefones deseja fornecer? '))
            i=0
            usuarios[check].telefones=[]
            while i<num:
                usuarios[check].telefones.append(input('Informe o(um dos) telefone(s) a ser(em) alterado(s): '))
                i+=1
            usuarios[check].data_de_nasc=input('Informe a nova data de nascimento do usuário: ')
            usuarios[check].profissao=input('Informe a nova profissão do usuário: ')
        else:
            print('Opção inválida.')
def excluir_usuario(usuarios, user_cpf):
    check=check_cpf(usuarios, user_cpf)
    if check==-1:
        print('O cpf fornecido ainda não foi cadastrado.')
    else:
        del usuarios[check]
def listar_livros(livros):
    i=0
    while i<len(livros):
        print(livros[i].isbn+'/'+livros[i].titulo+'/'+livros[i].genero, end=' / ')
        imprimir_lista(livros[i].autores)
        print(livros[i].num_de_pag)
        i+=1
def consultar_livros(livros, livro_isbn):
    i=check_isbn(livros, livro_isbn)
    if i==-1:
        print('ISBN não cadastrado.')
    else:
        print(livros[i].isbn+'/'+livros[i].titulo+'/'+livros[i].genero, end=' / ')
        imprimir_lista(livros[i].autores)
        print(livros[i].num_de_pag)
def cadastrar_livros(livros):
    book=livro()
    book.autores=[]
    book.isbn=input('Informe o isbn do livro a ser cadastrado: ')
    check=check_isbn(livros, book.isbn)
    if check!=-1:
        print(f'Esse isbn já está cadastrado e pertence a {livros[check].titulo}.')
    else:
        book.titulo=input('Informe o título do livro a ser cadastrado: ')
        book.genero=input('Informe o gênero do livro a ser cadastrado: ')
        i=0
        num=int(input('Quantos autores deseja informar? '))
        while i<num:
            book.autores.append(input('Informe o(um dos) autor(es) do livro a ser cadastrado: '))
            i+=1
        book.num_de_pag=input('Informe o número de páginas do livro a ser cadastrado.')
        livros.append(book)
def alterar_livros(livros, livro_isbn):
    check=check_isbn(livros, livro_isbn)
    if check==-1:
        print('O isbn fornecido ainda não foi cadastrado.')
    else:
        print('Digite 1 para alterar o título do livro.')
        print('Digite 2 para alterar o gênero do livro.')
        print('Digite 3 para alterar os autores do livro.')
        print('Digite 4 para alterar o número de páginas do livro.')
        print('Digite 5 para alterar todos os dados do livro (EXCETO ISBN).')
        op=int(input('digite a opção desejada (de 1 a 5): '))
        if op==1:
            livros[check].titulo=input('Informe o novo título do livro: ')
        elif op==2:
            livros[check].genero=input('Informe o novo gênero do livro: ')
        elif op==3:
            num=int(input('Quantos e-mails deseja fornecer? '))
            i=0
            livros[check].autores=[]
            while i<num:
                livros[check].autores.append(input('Informe o(um dos) autor(es) a ser(em) alterado(s): '))
                i+=1
        elif op==4:
            livros[check].num_de_pag=input('Informe o novo número de páginas do livro: ')
        elif op==5:
            livros[check].titulo=input('Informe o novo título do livro: ')
            livros[check].genero=input('Informe o novo gênero do livro: ')
            num=int(input('Quantos e-mails deseja fornecer? '))
            i=0
            livros[check].autores=[]
            while i<num:
                livros[check].autores.append(input('Informe o(um dos) autor(es) a ser(em) alterado(s): '))
                i+=1
            livros[check].num_de_pag=input('Informe o novo número de páginas do livro: ')
        else:
            print('Opção inválida.')
def excluir_livro(livros, livro_isbn):
    check=check_isbn(livros, livro_isbn)
    if check==-1:
        print('O isbn fornecido ainda não foi cadastrado.')
    else:
        del livros[check]
def listar_emprestimos(emprestimos):
    i=0
    while i<len(emprestimos):
        print(emprestimos[i].cpf+' / '+emprestimos[i].isbn+' / '+emprestimos[i].data_ret+' / '+emprestimos[i].data_dev+' / '+emprestimos[i].valor_dia_multa)
        i+=1
def consultar_emprestimo(emprestimos, user_cpf, livro_isbn, data_reti):
    i=check_emp(emprestimos, user_cpf, livro_isbn, data_reti)
    if i==-1:
        print('Emprestimo não registrado.')
    else:
        print(emprestimos[i].cpf+' / '+emprestimos[i].isbn+' / '+emprestimos[i].data_ret+' / '+emprestimos[i].data_dev+' / '+emprestimos[i].valor_dia_multa)
def cadastrar_emprestimo(emprestimos):
    emp=emprestimo()
    emp.cpf=input('Informe o cpf do usuário que está realizando o emprestimo: ')
    emp.isbn=input('Informe o isbn do livro: ')
    emp.data_ret=input('Informe a data de retirada (no formato dd/mm/aaaa): ')
    if check_emp(emprestimos, emp.cpf, emp.isbn, emp.data_ret)!=-1:
        print('Esse emprestimo já foi realizado:')
    else:
        emp.data_dev=input('Informe a data de devolução: ')
        emp.valor_dia_multa=input('Infome o valor diário da multa por atraso: ')
        emprestimos.append(emp)
def alterar_emprestimo(emprestimos, user_cpf, livro_isbn, data_reti):
    i=check_emp(emprestimos, user_cpf, livro_isbn, data_reti)
    if i==-1:
        print('O emprestimo ainda não foi cadastrado.')
    else:
        print('Digite 1 para alterar a data de devolução do empréstimo;')
        print('Digite 2 para alterar o valor diário da multa por atraso;')
        print('Digite 3 para alterar ambos.')
        op=int(input('digite a opção desejada (de 1 a 3): '))
        if op==1:
            emprestimos[i].data_dev=input('Informe a nova data de devolução: ')
        elif op==2:
            emprestimos[i].valor_dia_multa=input('Informe o novo valor diário de multa por atraso: ')
        elif op==3:
            emprestimos[i].data_dev=input('Informe a nova data de devolução: ')
            emprestimos[i].valor_dia_multa=input('Informe o novo valor diário de multa por atraso: ')
        else:
            print('Opção inválida.')
def excluir_emprestimo(emprestimos, user_cpf, livro_isbn, data_reti):
    check=check_emp(emprestimos, user_cpf, livro_isbn, data_reti)
    if check==-1:
        print('Os dados fornecidos ainda não foram cadastrados.')
    else:
        del emprestimos[check]
def calc_idade(data_nasc, data):
    if int(data_nasc[3:5])==int(data[3:5]):
        if int(data_nasc[:2])<=int(data[:2]):
           return int(data[6:])-int(data_nasc[6:])
        else:
            return int(data[6:])-int(data_nasc[6:])-1
    if int(data_nasc[3:5])<int(data[3:5]):
        return int(data[6:])-int(data_nasc[6:])
    else:
        return int(data[6:])-int(data_nasc[6:])-1
def relatorio_idade(usuarios, idade):
    i=0
    data=input('Informe a data atual (no formato dd/mm/aaaa): ')
    while i<len(usuarios):
        if calc_idade(usuarios[i].data_de_nasc, data)>idade:
            print(usuarios[i].cpf+'/'+usuarios[i].nome+'/'+usuarios[i].rua+'/'+usuarios[i].nro+'/'+usuarios[i].cep, end=' / ')
            imprimir_lista(usuarios[i].emails)
            imprimir_lista(usuarios[i].telefones)
            print(usuarios[i].data_de_nasc+' / '+usuarios[i].profissao)
        i+=1
def relatorio_livro(livros, min_autores):
    i=0
    while i<len(livros):
        if len(livros[i].autores)>min_autores:
            print(livros[i].isbn+'/'+livros[i].titulo+'/'+livros[i].genero, end=' / ')
            imprimir_lista(livros[i].autores)
            print(livros[i].num_de_pag)
        i+=1
def relatorio_emprestimo(emprestimos, dataX, dataY, usuarios, livros):
    i=0
    while i<len(emprestimos):
        if int(emprestimos[i].data_dev[6:])>=int(dataX[6:]) and int(emprestimos[i].data_dev[6:])<=int(dataY[6:]):
            if int(emprestimos[i].data_dev[3:5])>=int(dataX[3:5]) and int(emprestimos[i].data_dev[3:5])<=int(dataY[3:5]):
                if int(emprestimos[i].data_dev[:2])>=int(dataX[:2]) and int(emprestimos[i].data_dev[:2])<=int(dataY[:2]):
                    nome=usuarios[check_cpf(usuarios, emprestimos[i].cpf)].nome
                    titulo=livros[check_isbn(livros, emprestimos[i].isbn)].titulo
                    print(emprestimos[i].cpf+' / '+nome+' / '+emprestimos[i].isbn+' / '+titulo+emprestimos[i].data_ret+' / '+emprestimos[i].data_dev+' / '+emprestimos[i].valor_dia_multa)
        i+=1
def main_usuarios(usuarios):
    op=submenu_usuarios()
    while op!=0:
        if op==1:
            listar_usuarios(usuarios)
        elif op==2:
            user_cpf=input('Digite o cpf do usuário a ser consultado: ')
            consultar_usuario(usuarios, user_cpf)
        elif op==3:
            cadastrar_usuario(usuarios)
        elif op==4:
            user_cpf=input('Digite o cpf do usuário a ser alterado: ')
            alterar_usuario(usuarios, user_cpf)
        elif op==5:
            user_cpf=input('Digite o cpf do usuário a ser excluído: ')
            excluir_usuario(usuarios, user_cpf)
        else:
            print('Opção inválida.')
        op=submenu_usuarios()
def main_livros(livros):
    op=submenu_livros()
    while op!=0:
        if op==1:
            listar_livros(livros)
        elif op==2:
            livro_isbn=input('Digite o isbn do livro a ser consultado: ')
            consultar_livros(livros, livro_isbn)
        elif op==3:
            cadastrar_livros(livros)
        elif op==4:
            livro_isbn=input('Digite o isbn do livro a ser alterado: ')
            alterar_livros(livros, livro_isbn)
        elif op==5:
            livro_isbn=input('Digite o isbn do livro a ser excluído: ')
            excluir_livro(livros, livro_isbn)
        else:
            print('Opção inválida.')
        op=submenu_livros()
def main_emprestimos(emprestimos):
    op=submenu_emprestimos()
    while op!=0:
        if op==1:
            listar_emprestimos(emprestimos)
        elif op==2:
            user_cpf=input('Informe o cpf do usuário que realizou o empréstimo: ')
            livro_isbn=input('Informe o isbn do livro: ')
            data_reti=input('Informe a data de retirada do livro: ')
            consultar_emprestimo(emprestimos, user_cpf, livro_isbn, data_reti)
        elif op==3:
            cadastrar_emprestimo(emprestimos)
        elif op==4:
            user_cpf=input('Informe o cpf do usuário que realizou o empréstimo: ')
            livro_isbn=input('Informe o isbn do livro: ')
            data_reti=input('Informe a data de retirada do livro: ')
            alterar_emprestimo(emprestimos, user_cpf, livro_isbn, data_reti)
        elif op==5:
            user_cpf=input('Informe o cpf do usuário que realizou o empréstimo: ')
            livro_isbn=input('Informe o isbn do livro: ')
            data_reti=input('Informe a data de retirada do livro: ')
            excluir_emprestimo(emprestimos, user_cpf, livro_isbn, data_reti)
        else:
            print('Opção inválida.')
        op=submenu_emprestimos()
def main_relatorios(usuarios, livros, emprestimos):
    op=submenu_relatorios()
    while op!=0:
        if op==1:
            idade=int(input('Informe a idade mínima desejada: '))
            relatorio_idade(usuarios, idade)
        elif op==2:
            min_autores=int(input('Digite a quantidade de autores mínima desejada: '))
            relatorio_livro(livros, min_autores)
        elif op==3:
            dataX=input('qual a data mínima desejada? (digite no formato dd/mm/aaaa)')
            dataY=input('qual a data máxima desejada? (digite no formato dd/mm/aaaa)')
            relatorio_emprestimo(emprestimos, dataX, dataY, usuarios, livros)
        else:
            print('Opção inválida.')
        op=submenu_relatorios()
def main():
    arquivo_user='./dados_usuarios.txt'
    arquivo_livro='./dados_livros.txt'
    arquivo_emp='./dados_emprestimos.txt'
    op=menu()
    usuarios=ler_arquivo_user(arquivo_user)
    livros=ler_arquivo_livro(arquivo_livro)
    emprestimos=ler_arquivo_emprestimo(arquivo_emp)
    while op!=0:
        if op==1:
            main_usuarios(usuarios)
        elif op==2:
            main_livros(livros)
        elif op==3:
            main_emprestimos(emprestimos)
        elif op==4:
            main_relatorios(usuarios, livros, emprestimos)
        else:
            print('Opção inválida.')
        op=menu()
    if len(usuarios)>0:
        escrever_arquivo_user(usuarios, arquivo_user)
    if len(livros)>0:
        escrever_arquivo_livro(livros, arquivo_livro)
    if len(emprestimos)>0:
        escrever_arquivo_emprestimo(emprestimos, arquivo_emp)
main()