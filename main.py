import hashlib
"""
TODOS:
  >Timestamps
  >Criptografia (chave SHA-512), hash (SHA-256)
  >Editar arquivos ao invés de sobrescrever
"""


def wra_file(filename: str, mode: str):
  if mode == 'r':
    with open(filename, mode) as f:
      allines: list = f.readlines()
      return allines


def edit(file_name: str):
  linhas = []

  with open(file_name, "w") as f:
    while True:
      linha = input()
      linhas.append(linha)
      if linha.endswith(";END"):
        break
    for l in linhas:
      if l.endswith(";END"):
        f.write(l.strip(";END") + "\n")
      else:
        f.write(l + "\n")
  return linhas


def main():
  fname = input("Digite o nome do arquivo: ")
  fname = fname + ".txt"
  if fname.startswith("crypt_"):
    chave = input(
        "Arquivo protegido por criptografia, digite a chave de acesso: ")
    linhas_arq = wra_file("chaves.txt", "r")
    for linha in linhas_arq:
      if hashlib.sha512(chave.encode()).hexdigest() == linha:
        linhas = wra_file(fname, "r")
        for linha in linhas:
          print(linha)
      else:
        raise Exception("Chave não encontrada")
  linhas: list = edit(fname)

  o = input("Você quer criptografar o arquivo? (s/n) ")
  if o.lower() == "s":
    m = int(
        input(
            "Escolha o método: \n1-Criptografia (chave)\n2-Hash (SHA-256)\n=>")
    )
    if m == 1:
      chave = input("Digite a chave: ")
      with open("chaves.txt", "a") as f:
        f.write(hashlib.sha512(chave.encode()).hexdigest() + "\n")
      with open("crypt_" + fname, "w") as f:
        allines = wra_file("crypt_" + fname, "r")
        for linha in allines:
          if linha.endswith(";END"):
            f.write(linha.strip(";END") + "\n")
          else:
            f.write(linha[::-1])
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
