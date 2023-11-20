import hashlib

"""
WIKI:
    +> --stcrmk-- = Marca de criptografia Steditor tm
    +> Chaves de criptografia sáo SHA-512, e Hashes são SHA-256

TODOS:
    >Timestamps
    >Editar arquivos ao invés de sobrescrever
    >Corrigir a 
"""


def wra_file(filename: str, mode: str):
    if mode == 'r':
        with open(filename, 'r') as f:
            return f.readlines()
    elif mode == 'r1':
        with open(filename, 'r') as f:
            return f.readline()

def edit(file_name: str):
    linhas = []

    with open(file_name, "w") as f:
        while True:
            linha = input()
            linhas.append(linha)
            if linha.endswith(";END"):
                linhas.pop()
                break
        # for l in linhas:
            # f.write(l + "\n")
    return linhas


def main():
    fname = input("Digite o nome do arquivo: ")
    fname = fname + ".txt"
    try:
        with open(fname, 'r') as f:
            if f.readline().startswith("--stcrcts--"):
                chave = input("Arquivo protegido por criptografia, digite a chave de acesso: ")
                chave_real: str = wra_file(fname.replace(".txt", "") + ".stkey", "r1")
                if hashlib.sha512(chave.encode()).hexdigest() == chave_real:
                    l_cr = wra_file(fname, "r")
                    print(l_cr)
                    for l in l_cr:
                        if l != "--stcrcts--":
                            print(l[::-1], end='')

        #ADICIONAR AQUI O CÓDIGO PARA EDITAR ARQUIVOS E NÃO CRIAR NOVOS
    except FileNotFoundError:
        linhas_arq: list = edit(fname)
        o = input("Você quer trancar o arquivo? (s/n) ")
        if o.lower() == "s":
            m = int(input("Escolha o método: \n1-Criptografia com chave\n2-Hash (SHA-256)\n=>"))
            if m == 1:
                chave = input("Digite a chave: ")
                with open(fname.replace(".txt", "") + ".stkey", "w") as f:
                    f.write(hashlib.sha512(chave.encode()).hexdigest())
                
                with open(fname, "a") as f:
                    allines: list = wra_file(fname, "r")
                    f.write("--stcrcts--" + "\n")
                    for linha in linhas_arq:
                        f.write(linha[::-1] + "\n")

            elif m == 2:
                linhas_str = ""
                for linha in linhas:
                    linhas_str += linha + ' '
                    with open(fname, 'w') as f:
                        hashed_linhas = hashlib.sha256(linhas_str.encode()).hexdigest()
                        f.write(hashed_linhas)
            else:
                return
        else:
            with open(fname, "w") as f:
                for l in linhas_arq:
                    f.write(l + "\n")


main()
