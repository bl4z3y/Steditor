import hashlib

"""
WIKI:
    +> --stcrmk-- = Marca de criptografia Steditor tm
    +> Chaves de criptografia sáo SHA-512, e Hashes são SHA-256

TODOS:
  >Timestamps
  >Editar arquivos ao invés de sobrescrever
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
        for l in linhas:
            f.write(l + "\n")
    return linhas


def main():
    fname = input("Digite o nome do arquivo: ")
    fname = fname + ".txt"
    try:
        with open(fname, 'r') as f:
            if f.readline().startswith("--stcrmk--"):
                chave = input("Arquivo protegido por criptografia, digite a chave de acesso: ")
                chave_real: str = wra_file(fname.replace(".txt", "") + ".stkey", "r1")
                if hashlib.sha512(chave.encode()).hexdigest() == chave_real:
                    for l in wra_file(fname, "r"):
                        print(l)
                        return

    except FileNotFoundError:
        linhas: list = edit(fname)
        o = input("Você quer trancar o arquivo? (s/n) ")
        if o.lower() == "s":
            m = int(input("Escolha o método: \n1-Criptografia com chave\n2-Hash (SHA-256)\n=>"))
            if m == 1:
                chave = input("Digite a chave: ")
                with open(fname.replace(".txt", "") + ".stkey", "w") as f:
                    f.write(hashlib.sha512(chave.encode()).hexdigest())
                
                with open(fname, "w") as f:
                    allines: list = wra_file(fname, "r")
                    f.write("--stcrmk--" + "\n")
                    for linha in allines:
                        if not linha.endswith(";END"):
                            f.write(linha[::-1])
                        else:
                            f.write(linha.replace(";END", ""))

            elif m == 2:
                linhas_str = ""
                for linha in linhas:
                    linhas_str += linha + ' '
                    with open(fname, 'w') as f:
                        hashed_linhas = hashlib.sha256(linhas_str.encode()).hexdigest()
                        f.write(hashed_linhas)
            else:
                return


main()
