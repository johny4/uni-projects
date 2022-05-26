def corrigir_palavra(surto):
    """
    Esta função recebe uma string e, caso esteja corrompida, remove as junções de letras maiúsculas e minúsculas.
    Para isso, compara a posição 0 e a posição 1 de uma lista, e caso sejam a mesma letra mas em maiúscula
    ou vice-versa, elimina ambas as entradas da lista, restaurando as posições. No final a lista é convertida a string.
    """

    p = list(surto)
    posx, posy = 0, 1
    while posy < len(p):
        if abs(ord(p[posx]) - ord(p[posy])) == 32:
            del p[posx:posy + 1]
            posx, posy = 0, 1
        else:
            posx += 1
            posy += 1
    return "".join(p)


def eh_anagrama(p1, p2):
    """
    Esta função recebe duas strings e converte-as a minúscula para de seguida comparar se têm o mesmo tamanho.
    Se tiverem, é verificado se o número de ocorrência de cada letra é igual em ambas as strings e devolve um valor
    booleano sobre o facto de as strings serem anagrama uma da outra ou não.
    """

    p1, p2 = p1.lower(), p2.lower()

    if not len(p1) == len(p2):
        return False
    for char in p1:
        if not p1.count(char) == p2.count(char):
            return False
    return True


def corrigir_doc(frase):
    """
    Esta função recebe uma string e devolve-a filtrada, removendo anagramas ou ocorrências seguidas da mesma
    letra em maiúscula-minúscula ou vice-versa. Para isso utiliza as funções previamente definidas e exibe
    tambéum um ValueError caso o input não seja válido, tendo as palavras de estar separadas por apenas 1 espaço,
    o texto de conter uma ou mais palavras, e as palavras de ser formadas apenas por letras (no mínimo 1).
    """

    val = False
    if isinstance(frase, str):
        if not frase.isspace() or frase != "":
            for check in frase:
                if check.isalpha() or check.isspace():
                    for spaces in range(len(frase)):
                        if not (frase[spaces].isspace() and frase[spaces + 1].isspace()):
                            val = True
                        else:
                            val = False
                            break
                else:
                    val = False
                    break

    if val is False:
        raise ValueError("corrigir_doc: argumento invalido")

    frase = corrigir_palavra(frase)
    frase = frase.split()

    for p in frase:
        for i in range(len(frase)):
            if i < len(frase):
                if eh_anagrama(p, frase[i]):
                    if p.lower() != frase[i].lower():
                        del frase[i]
                    i -= 1

    return " ".join(frase)


def obter_posicao(mov, pos):
    """
    Esta função recebe uma string com uma letra que representa um movimento no keypad, que pode ser para cima (C),
    para baixo (B), para a direita (D) e para a esquerda (E) (impedindo que se "saia" do keypad) e um número
    inteiro correspodnente à posiçãoa atual e devolve a nova posição após o movimento.
    """

    if (pos == 2 or pos == 3 or pos == 5 or pos == 6 or pos == 8 or pos == 9) and mov == "E":
        pos -= 1
    elif (pos == 1 or pos == 2 or pos == 4 or pos == 5 or pos == 7 or pos == 8) and mov == "D":
        pos += 1
    elif (pos == 1 or pos == 2 or pos == 3 or pos == 4 or pos == 5 or pos == 6) and mov == "B":
        pos += 3
    elif (pos == 4 or pos == 5 or pos == 6 or pos == 7 or pos == 8 or pos == 9) and mov == "C":
        pos -= 3
    return pos


def obter_digito(seq, posini):
    """
    Esta função recebe uma string com uma sequência de pelo menos 1 letra, que representam os movimentos a aplicar
    e um número inteiro correspodnente à posiçãoa atual e devolve a nova posição após o(s) movimento(s).
    """

    pos = posini
    for mov in seq:
        pos = obter_posicao(mov, pos)
    return pos


def obter_pin(chave):
    """
    Esta função recebe um tuplo de 4 a 10 sequências de movimentos e devolve um tuplo com o pin correspondente.
    Para isso utiliza as funções previamente definidas e imepede argumentos inválidos, ou seja, sequências que
    não sejam exclusivamente constituídas pelas letras B, C, D e E.
    """

    if isinstance(chave, tuple) and 4 <= len(chave) <= 10:
        code = ()
        pos = 5
        for seq in chave:
            if seq == "":
                raise ValueError("obter_pin: argumento invalido")
            for letra in seq:
                if not 65 < ord(letra) < 70:
                    raise ValueError("obter_pin: argumento invalido")
            pos = obter_digito(seq, pos)
            code += (pos,)
    else:
        raise ValueError("obter_pin: argumento invalido")
    return code


def eh_entrada(ent):
    """
    Esta função recebe um tuplo de 3 entradas e verifica se este pode ou não ser uma entrada da BDB, ainda que
    corrompida, verificando se a primeira entrada é uma string composta por letras minúsculas e traços, se a
    segunda entrada é uma string que tem 5 letras minúsculas dentro de parênteses retos e se a última entrada é um
    tuplo com 2 ou mais números inteiros positivos e devolvendo um valor booleano.
    """

    val = True

    if not isinstance(ent, tuple) or not len(ent) == 3:
        return False

    if not (isinstance(ent[0], str) and isinstance(ent[1], str) and isinstance(ent[2], tuple) and len(ent[1]) == 7 and
            len(ent[2]) >= 2 and len(ent[0]) > 0):
        return False

    for char in ent[0]:
        if not 96 < ord(char) < 123 and ord(char) != 45:
            val = False
            break

    # Adaptaação da função corrigir_surto para impedir que uma cifra que contenha dois traços consecutivos seja válida
    posx, posy = 0, 1
    while posy < len(ent[0]) and val is True:
        if ord(ent[0][posx]) == ord(ent[0][posy]) == 45:
            val = False
        else:
            posx += 1
            posy += 1

    if ord(ent[0][0]) == 45 or ord(ent[0][len(ent[0]) - 1]) == 45 and val is True:
        val = False

    if ord(ent[1][0]) == 91 and ord(ent[1][len(ent[1]) - 1]) == 93 and val is True:
        for i in range(1, len(ent[1]) - 1):
            if not (96 < ord(ent[1][i]) < 123):
                val = False
                break

    else:
        val = False

    if val is True:
        for num in ent[2]:
            if isinstance(num, int) and num > 0:
                pass
            else:
                val = False
                break

    return val


def validar_cifra(cifra, checksum):
    """
    Esta função devolve um valor booleano sobre o checksum (sequência das 5 letras mais comuns na cifra, ordenada
    alfabeticamente em caso de empate) ser consistente com a cifra recebida pela função.
    """

    cont = {}

    for char in cifra:
        if char in cont:
            cont[char] += 1
        else:
            cont[char] = 1

    if "-" in cont:
        del cont["-"]

    cont = dict(sorted(cont.items(), key=lambda x: (-x[1], x[0])))

    # Ordena o dicionário primeiro por ordem descendente de valores e depois por alfabética de chaves.
    # O cont.items cria um objeto iterável (semelhante a una lista de tuplos) com os pares chave:valor
    # do dicionário cont. Este depois é ordenado, com a função anónima lambda. Uma vez que primeiro
    # queremos ordenar os valores decrescentemente, usamos "-x[1]", o "-" para o descrescente e o x[1]
    # porque no cont.items, o valor está na posição 1 de cada tuplo, ou seja são valores do dicionário.
    # Como queremos também ordenar alfabeticamente, nos casos de empates, usamos o "x[0]", desta vez sem
    # o "-" antes, porque queremos ordenar de forma crescente e usamos o 0, porque as letras se situam na
    # posição 0 dos tuplos do dict.items, ou seja, são chaves do dicionário.

    check = ""

    for key in cont:
        check += key

    check = check[0:5]
    check = "[" + check + "]"

    return checksum == check


def filtrar_bdb(lista):
    """
    Esta função rececbe uma lista com pelo menos 1 entrada da BDB e devolve uma lista com as entradas em que o
    checksum não é coerente com a cifra, utilizando a função validar_cifra anteriormente definida. Também veririca
    a validade do argumento, aceitando apenas listas com pelo menos 1 entrada e utilizando a função eh_entrada,
    também anteriormente definida, para verificar a validade das entradas.
    """

    if not isinstance(lista, list) or len(lista) < 1:
        raise ValueError("filtrar_bdb: argumento invalido")
    for ent in lista:
        if not eh_entrada(ent):
            raise ValueError("filtrar_bdb: argumento invalido")

    filtro = []
    for ent in lista:
        if validar_cifra(ent[0], ent[1]) is False:
            filtro.append(ent)
    return filtro


def obter_num_seguranca(tuplo):
    """
    Esta função recece um tuplo de números inteiros positivos e devolve o inteiro correspondente à menor diferença
    possível entre quaisquer 2 números do tuplo - o código de segurança.
    """

    tuplo = sorted(tuplo, reverse=True)
    # Ordena o tuplo de forma decrescente

    i = 0
    code = 0
    while i < len(tuplo) - 1:
        temp = tuplo[i] - tuplo[i + 1]
        if temp < code or code == 0:
            code = temp
        i += 1
    return code


def decifrar_texto(cifra, code):
    """
    Esta função decifra o texto e apresenta-o numa string, recebendo o texto cifrado e o código de segurança, avançando
    no alfabeto um nº de vezes igual ao código de segurança + 1 nas posições pares e -1 nas pares e impedindo que se
    saia do alfabeto, sendo a letra "a" aquela que sucede o "z".
    """

    par = True
    decif = []

    while code > 25:
        code -= 26

    for char in cifra:
        if par is True:
            if ord(char) == 45:
                decif.append(" ")
            else:
                letra = chr(ord(char) + code + 1)
                if ord(letra) > 122:
                    letra = chr(97 + (ord(letra) - 122) - 1)
                decif.append(letra)
            par = False

        else:
            if ord(char) == 45:
                decif.append(" ")
            else:
                letra = chr(ord(char) + code - 1)
                if ord(letra) > 122:
                    letra = chr(97 + (ord(letra) - 122) - 1)
                decif.append(letra)
            par = True

    return "".join(decif)


def decifrar_bdb(lista):
    """
    Esta função recebe uma lista contendo pelo menos uma entrada da BDB e devolve uma lista, contendo o texto dessas
    mesmas entradas decifrado. Para isso utiliza as funções supradefinidas eh_entrada para verificar a validade
    do argumento e obter_num_seguranca e decifrar_texto para desencriptar a cifra.
    """

    if not isinstance(lista, list) or len(lista) < 1:
        raise ValueError("decifrar_bdb: argumento invalido")

    for ent in lista:
        if not eh_entrada(ent):
            raise ValueError("decifrar_bdb: argumento invalido")

    texto = []
    for cifra in lista:
        code = obter_num_seguranca(cifra[2])
        texto.append(decifrar_texto(cifra[0], code))

    return texto


def eh_utilizador(d):
    """
    Esta função recebe um argumento de qualquer tipo e devolve o valor booleano de True se todas as seguintes
    condições se verificarem: o argumento é um dicionário com 3 pares chave:valor; o valor associado às chaves "name"
    e "pass" é uma string constituída por, pelo menos, 1 caracter; o valor associado à chave "rule" é um dicionário com
    2 pares chave:valor; o valor associado à chave "vals" é um tuplo com dois números inteiros positivos em ordem
    crescente; o valor associado à chave "char" é uma e só uma letra minúscula.
    """

    if isinstance(d, dict):
        if len(d) == 3 and isinstance(d["name"], str) and isinstance(d["pass"], str):
            if len(d["name"]) > 0 and len(d["pass"]) > 0:
                if isinstance(d["rule"], dict):
                    if len(d["rule"]) == 2:
                        if isinstance(d["rule"]["vals"], tuple):
                            if len(d["rule"]["vals"]) == 2:
                                if isinstance(d["rule"]["vals"][0], int) and isinstance(d["rule"]["vals"][1], int):
                                    if 0 < d["rule"]["vals"][0] < d["rule"]["vals"][1]:
                                        if isinstance(d["rule"]["char"], str):
                                            if len(d["rule"]["char"]) == 1:
                                                if 96 < ord(d["rule"]["char"]) < 123:
                                                    return True
    return False


def eh_senha_valida(senha, d):
    """
    Esta funçãao recebe uma string correspondente a uma senha e um dicionário contendo a regra individual da senha,
    e devolve o valor booleano de True se e só se cumprir as 3 regras (2 gerais e 1 individual).
    """

    val1, val2, val3 = False, False, False

    # Verifica a primeira regra geral: haver 3 vogais na senha.

    vogais = ["a", "e", "i", "o", "u"]
    cont = 0
    for let in senha:
        if let in vogais:
            cont += 1
    if cont >= 3:
        val1 = True

    # Adaptaação da função corrigir_surto para garantir a segunda regra geral: um dos carácteres tem de aparecer
    # 2 vezes consecutivas

    posx, posy = 0, 1
    while posy < len(senha):
        if senha[posx] == senha[posy]:
            val2 = True
            break
        else:
            posx += 1
            posy += 1

    if d["vals"][0] <= senha.count(d["char"]) <= d["vals"][1]:
        val3 = True

    return val1 and val2 and val3


def filtrar_senhas(lista):
    """
    Esta funçãoo recebe uma lista com um ou mais dicionários com entradas e devolve a lista ordenada alfabeticamente
    com os nomes dos utilizadores com senhas erradas, usando a função eh_senha_valida. Esta função verifica também
    se as entradas são válidas usando a função supradefinida eh_utilizador e retornando um ValueError caso não seja.
    """

    wrong = []

    if not isinstance(lista, list) or len(lista) == 0:
        raise ValueError("filtrar_senhas: argumento invalido")

    for d in lista:
        if eh_utilizador(d):
            if not eh_senha_valida(d["pass"], d["rule"]):
                wrong.append(d["name"])
        else:
            raise ValueError("filtrar_senhas: argumento invalido")

    return sorted(wrong)
