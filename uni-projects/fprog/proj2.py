#####################
# 2.1.1 TAD posicao #
#####################

# O TAD posicao é usado para representar uma posição (x, y) de um prado arbitrariamente grande,
# sendo x e y dois valores inteiros não negativos.
# Representação: R[x, y] = (x, y)


def cria_posicao(x, y):
    """
    cria posicao: int × int -→ posicao

    cria posicao(x,y) recebe os valores correspondentes às coordenadas de uma
    posição e devolve a posiçãao correspondente.
    """

    if isinstance(x, int) and isinstance(y, int) and x >= 0 and y >= 0:
        return x, y
    else:
        raise ValueError("cria_posicao: argumentos invalidos")


def cria_copia_posicao(p):
    """
    cria copia posicao: posicao -→ posicao

    cria copia posicao(p) recebe uma posição e devolve uma cópia nova da posição.
    """

    return cria_posicao(p[0], p[1])


def obter_pos_x(p):
    """
    obter pos x : posicao -→ int

    obter pos x(p) devolve a componente x da posição p
    """

    return p[0]


def obter_pos_y(p):
    """
    obter pos y : posicao -→ int

    obter pos y(p) devolve a componente y da posição p
    """

    return p[1]


def eh_posicao(arg):
    """
    eh posicao: universal -→ booleano

    eh posicao(arg) devolve True caso o seu argumento seja um TAD posicao e False caso contrário.
    """

    if isinstance(arg, tuple):
        if len(arg) == 2 and isinstance(obter_pos_x(arg), int) and isinstance(obter_pos_y(arg), int):
            return 0 <= obter_pos_x(arg) and 0 <= obter_pos_y(arg)
    return False


def posicoes_iguais(p1, p2):
    """
    posicoes iguais: posicao × posicao -→ booleano

    posicoes iguais(p1, p2) devolve True apenas se p1 e p2 são posições e são iguais.
    """

    return p1 == p2


def posicao_para_str(p):
    """
    posicao para str : posicao -→ str

    posicao para str(p) devolve a cadeia de caracteres ‘(x, y)’ que representa o seu argumento,
    sendo os valores x e y as coordenadas de p.
    """

    return str((p[0], p[1]))


def obter_posicoes_adjacentes(p):
    """
    obter posicoes adjacentes: posicao -→ tuplo

    obter posicoes adjacentes(p) devolve um tuplo com as posiçõees adjacentes à posição p,
    começando pela posição acima de p e seguindo no sentido horário.
    """

    if obter_pos_y(p) == 0:
        if obter_pos_x(p) == 0:
            return cria_posicao(1, 0), cria_posicao(0, 1)
        else:
            return cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)), cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1), \
                   cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p))

    if obter_pos_x(p) == 0:
        return cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1), cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)), \
               cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1)
    else:
        return cria_posicao(obter_pos_x(p), obter_pos_y(p) - 1), cria_posicao(obter_pos_x(p) + 1, obter_pos_y(p)), \
               cria_posicao(obter_pos_x(p), obter_pos_y(p) + 1), cria_posicao(obter_pos_x(p) - 1, obter_pos_y(p))


def ordenar_posicoes(p):
    """
    ordenar posicoes: tuplo -→ tuplo

    ordenar posicoes(t) devolve um tuplo contendo as mesmas posições do tuplo fornecido como argumento,
    ordenadas de acordo com a ordem de leitura do prado.
    """

    return tuple(sorted(p, key=lambda x: (obter_pos_y(x), obter_pos_x(x))))


####################
# 2.1.2 TAD animal #
####################

# O TAD animal é usado para representar os animais do simulador de ecossistemas que habitam o prado,
# existindo de dois tipos: predadores e presas. Os predadores são caracterizados pela espécie, idade, frequência de
# reprodução, fome e frequência de alimentação. As presas são apenas caracterizadas pela espécie,
# idade e frequência de reprodução.
# Representação: R[espécie, freq_reprodução, idade, freq_alimentação, fome] =
# [espécie, [freq_reprodução, idade], [freq_alimentação, fome]]


def cria_animal(s, r, a):
    """
    cria animal: str × int × int -→ animal

    cria animal(s, r, a) recebe uma cadeia de caracteres s não vazia correspondente à espécie do animal e
    dois valores inteiros correspondentes à frequência de reprodução r (maior do que 0) e à frequência de
    alimentação a (maior ou igual que 0); e devolve o animal. Animais com frequência de alimentação
    maior que 0 são considerados predadores, caso contrário são considerados presas.
    """

    if isinstance(s, str) and isinstance(r, int) and isinstance(a, int) and s != "" and r > 0 and a >= 0:
        return [s, [r, 0], [a, 0]]
    else:
        raise ValueError("cria_animal: argumentos invalidos")


def cria_copia_animal(a):
    """
    cria copia animal: animal -→ animal

    cria copia animal(a) recebe um animal a (predador ou presa) e devolve uma nova cópia do animal.
    """

    copia = a.copy()
    copia[1], copia[2] = a[1].copy(), a[2].copy()
    return copia


def obter_especie(a):
    """
    obter especie: animal -→ str

    obter especie(a) devolve a cadeia de caracteres correspondente à espécie do animal.
    """

    return a[0]


def obter_freq_reproducao(a):
    """
    obter freq reproducao: animal -→ int

    obter freq reproducao(a) devolve a frequência de reprodução do animal a.
    """

    return a[1][0]


def obter_freq_alimentacao(a):
    """
    obter freq alimentacao: animal -→ int

    obter freq alimentacao(a) devolve a frequência de alimentação do animal a.
    """

    return a[2][0]


def obter_idade(a):
    """
    obter idade: animal -→ int

    obter idade(a) devolve a idade do animal a.
    """

    return a[1][1]


def obter_fome(a):
    """
    obter fome: animal -→ int

    obter fome(a) devolve a idade do aanimal a (as presas devolvem sempre 0).
    """

    return a[2][1]


def aumenta_idade(a):
    """
    aumenta idade: animal -→ animal

    aumenta idade(a) modifica destrutivamente o animal a incrementando o valor da sua idade em uma unidade,
    e devolve o próprio animal.
    """

    a[1][1] += 1
    return a


def reset_idade(a):
    """
    reset idade: animal -→ animal

    reset idade(a) modifica destrutivamente o animal a definindo o valor da sua idade igual a 0,
    e devolve o próprio animal.
    """

    a[1][1] = 0
    return a


def aumenta_fome(a):
    """
    aumenta fome: animal -→ animal

    aumenta fome(a) modifica destrutivamente o animal predador a incrementando o valor da sua fome em uma unidade,
    e devolve o próprio animal. Esta operação não modifica os animais presa.
    """

    if eh_predador(a):
        a[2][1] += 1
    return a


def reset_fome(a):
    """
    reset fome: animal -→ animal

    reset fome(a) modifica destrutivamente o animal predador a definindo o valor da sua fome igual a 0,
    e devolve o próprio animal. Esta operação não modifica os animais presa.
    """

    if eh_predador(a):
        a[2][1] = 0
    return a


def eh_animal(a):
    """
    eh animal: universal -→ booleano

    eh animal(arg) devolve True caso o seu argumento seja um TAD animal e False caso contrário.
    """

    try:
        return isinstance(a, list) and isinstance(a[1], list) and isinstance(a[2], list) and isinstance(a[0], str) \
               and isinstance(a[1][0], int) and isinstance(a[1][1], int) and isinstance(a[2][0], int) \
               and isinstance(a[2][1], int) and a[0] != "" and a[1][0] > 0 and a[1][1] >= 0 and a[2][0] >= 0 \
               and a[2][1] >= 0
    except:
        return False


def eh_predador(a):
    """
    eh predador : universal -→ booleano

    eh predador(arg) devolve True caso o seu argumento seja um TAD animal do tipo predador e False caso contrário.
    """

    return eh_animal(a) and a[2][0] > 0


def eh_presa(a):
    """
    eh presa: universal -→ booleano

    eh presa(arg) devolve True caso o seu argumento seja um TAD animal do tipo presa e False caso contrário.
    """

    return eh_animal(a) and a[2][0] == 0


def animais_iguais(a1, a2):
    """
    animais iguais: animal × animal -→ booleano

    animais iguais(a1, a2) devolve True apenas se a1 e a2 são animais e são iguais.
    """

    return eh_animal(a1) and eh_animal(a2) and a1 == a2


def animal_para_char(a):
    """
    animal para char: animal -→ str

    animal para char(a) devolve a cadeia de caracteres dum único elemento correspondente ao primeiro carácter
    da espécie do animal passada por argumento, em maiúscula para animais predadores e em minúscula para animais presa.
    """

    if eh_presa(a):
        return a[0].lower()[0:1]
    elif eh_predador(a):
        return a[0].upper()[0:1]


def animal_para_str(a):
    """
    animal para str: animal -→ str

    animal para str(a) devolve a cadeia de caracteres que representa o animal.
    """

    if eh_presa(a):
        return a[0] + " [" + str(a[1][1]) + "/" + str(a[1][0]) + "]"
    elif eh_predador(a):
        return a[0] + " [" + str(a[1][1]) + "/" + str(a[1][0]) + ";" + str(a[2][1]) + "/" + str(a[2][0]) + "]"


def eh_animal_fertil(a):
    """
    eh animal fertil: animal -→ booleano

    eh animal fertil(a) devolve True caso o animal a tenha atingido a idade de reprodução e False caso contrário.
    """

    return obter_idade(a) >= obter_freq_reproducao(a)


def eh_animal_faminto(a):
    """
    eh animal faminto: animal -→ booleano

    eh animal faminto(a) devolve True caso o animal a tenha atingindo um valor de fome igual ou superior à sua
    frequência de alimentação e False caso contrário. As presas devolvem sempre False.
    """

    return eh_predador(a) and obter_fome(a) >= obter_freq_alimentacao(a)


def reproduz_animal(a):
    """
    reproduz animal: animal -→ animal

    reproduz animal(a) recebe um animal a devolvendo um novo animal da mesma espécie com idade e fome igual a 0,
    e modificando destrutivamente o animal passado como argumento a alterando a sua idade para 0.
    """

    novo = cria_copia_animal(a)
    reset_idade(novo)
    reset_fome(novo)
    reset_idade(a)
    return novo


###################
# 2.1.3 TAD prado #
###################

# O TAD prado é usado para representar o mapa do ecossistema e as animais que se encontram dentro.
# Representação: R[tamanho, (obstáculos), (animais), (posições)] = [posição, (obstáculos), [animais], [posições]]


def cria_prado(d, r, a, p):
    """
    cria prado: posicao × tuplo × tuplo × tuplo -→ prado

    cria prado(d, r, a, p) recebe uma posição d correspondente à posição que ocupa a montanha do canto inferior direito
    do prado, um tuplo r de 0 ou mais posições correspondentes aos rochedos que não são as montanhas dos limites
    exteriores do prado, um tuplo a de 1 ou mais animais, e um tuplo p da mesma dimensão do tuplo a com as posições
    correspondentes ocupadas pelos animais; e devolve o prado que representa internamente o mapa e os animais
    presentes.
    """

    val = False
    if eh_posicao(d) and isinstance(r, tuple) and isinstance(a, tuple) and isinstance(p, tuple) \
            and 0 < len(a) == len(p):
        val = True

        for ani in a:
            if not eh_animal(ani):
                val = False

        for roc in r:
            if not eh_posicao(roc) or not 0 < obter_pos_x(roc) < obter_pos_x(d) or not \
                    0 < obter_pos_y(roc) < obter_pos_y(d) or r.count(roc) > 1:
                val = False

        for pos in p:
            if not eh_posicao(pos) or any([posicoes_iguais(pos, roc) for roc in r]) or not \
                    0 < obter_pos_x(pos) < obter_pos_x(d) or not 0 < obter_pos_y(pos) < obter_pos_y(d) or\
                    p.count(pos) > 1:
                val = False

    if val:
        return [d, ordenar_posicoes(r), list(a), list(p)]

    raise ValueError("cria_prado: argumentos invalidos")


def cria_copia_prado(m):
    """
    cria copia prado: prado -→ prado

    cria copia prado(m) recebe um prado e devolve uma nova cópia do prado.
    """

    # Os funcionais map são usados para criar uma lista com cópias de animais e posições.
    return [cria_copia_posicao(m[0]), m[1], list(map(lambda x: cria_copia_animal(x), m[2])),
            list(map(lambda x: cria_copia_posicao(x), m[3]))]


def obter_tamanho_x(m):
    """
    obter tamanho x: prado -→ int

    obter tamanho x(m) devolve o valor inteiro que corresponde à dimensão Nx do prado.
    """

    return obter_pos_x(m[0]) + 1


def obter_tamanho_y(m):
    """
    obter tamanho y: prado -→ int

    obter tamanho y(m) devolve o valor inteiro que corresponde à dimensão Ny do prado.
    """

    return obter_pos_y(m[0]) + 1


def obter_numero_predadores(m):
    """
    obter numero predadores: prado -→ int

    obter numero predadores(m) devolve o número de animais predadores no prado.
    """

    return len(list(filter(eh_predador, m[2])))


def obter_numero_presas(m):
    """
    obter numero presas: prado -→ int

    obter numero presas(m) devolve o número de animais presas no prado.
    """

    return len(list(filter(eh_presa, m[2])))


def obter_posicao_animais(m):
    """
    obter posicao animais: prado -→ tuplo posicoes

    obter posicao animais(m) devolve um tuplo contendo as posiçõoes do prado ocupadas por animais,
    ordenadas em ordem de leitura do prado.
    """

    return ordenar_posicoes(m[3])


def obter_animal(m, p):
    """
    obter animal: prado × posicao -→ animal

    obter animal(m, p) devolve o animal do prado que se encontra na posição p.
    """

    i = 0
    for pos in m[3]:
        if posicoes_iguais(pos, p):
            break
        i = i + 1
    return m[2][i]


def eliminar_animal(m, p):
    """
    eliminar animal: prado × posicao -→ prado

    eliminar animal(m, p) modifica destrutivamente o prado m eliminando o animal da posição p deixando-a livre.
    Devolve o próprio prado.
    """

    i = 0
    for pos in m[3]:
        if posicoes_iguais(pos, p):
            break
        i = i + 1
    del m[2][i]
    del m[3][i]
    return m


def mover_animal(m, p1, p2):
    """
    mover animal: prado × posicao × posicao -→ prado

    mover animal(m, p1, p2) modifica destrutivamente o prado m movimentando o animal da posição p1 para a nova
    posição p2, deixando livre a posição onde se encontrava. Devolve o próprio prado.
    """

    i = 0
    for pos in m[3]:
        if posicoes_iguais(pos, p1):
            break
        i = i + 1
    m[3][i] = p2
    return m


def inserir_animal(m, a, p):
    """
    inserir animal: prado × animal × posicao -→ prado

    inserir animal(m, a, p) modifica destrutivamente o prado m acrescentando na posição p do prado o animal a
    passado com argumento. Devolve o próprio prado.
    """

    m[2].append(a)
    m[3].append(p)
    return m


def eh_prado(arg):
    """
    eh prado: universal -→ booleano

    eh prado(arg) devolve True caso o seu argumento seja um TAD prado e False caso contrário.
    """

    try:
        val = True

        if isinstance(arg, list) and isinstance(arg[1], tuple) and isinstance(arg[2], list)\
                and isinstance(arg[3], list) and eh_posicao(arg[0]) and 0 < len(arg[2]) == len(arg[3]):

            for ani in arg[2]:
                if not eh_animal(ani):
                    val = False

            for roc in arg[1]:
                if not eh_posicao(roc) or not 0 < obter_pos_x(roc) < obter_tamanho_x(arg) - 1 or not \
                        0 < obter_pos_y(roc) < obter_tamanho_y(arg) - 1 or arg[1].count(roc) > 1:
                    val = False

            for pos in arg[3]:
                if not eh_posicao(pos) or not 0 < obter_pos_x(pos) < obter_tamanho_x(arg) - 1 or not \
                        0 < obter_pos_y(pos) < obter_tamanho_y(arg) - 1 or eh_posicao_obstaculo(arg, pos) or \
                        arg[3].count(pos) > 1 or any([posicoes_iguais(pos, roc) for roc in arg[1]]):
                    val = False

        else:
            val = False

        return val

    except:
        return False


def eh_posicao_animal(m, p):
    """
    eh posicao animal: prado × posicao -→ booleano

    eh posicao animal(m, p) devolve True apenas no caso da posição p do prado estar ocupada por um animal.
    """

    val = False
    for pos in m[3]:
        if posicoes_iguais(pos, p):
            val = True
    return val


def eh_posicao_obstaculo(m, p):
    """
    eh posicao obstaculo: prado × posicao -→ booleano

    eh posicao obstaculo(m, p) devolve True apenas no caso da posição p do prado corresponder a uma montanha ou rochedo.
    """

    val = False
    for pos in m[1]:
        if posicoes_iguais(pos, p):
            val = True

    return val or obter_pos_x(p) == 0 or obter_pos_y(p) == 0 or obter_pos_x(p) == obter_tamanho_x(m) - 1 \
        or obter_pos_y(p) == obter_tamanho_y(m) - 1


def eh_posicao_livre(m, p):
    """
    eh posicao livre: prado × posicao -→ booleano

    eh posicao livre(m, p) devolve True apenas no caso da posição p do prado corresponder a um espaço livre
    (sem animais, nem obsáaculos).
    """

    return not eh_posicao_animal(m, p) and not eh_posicao_obstaculo(m, p) \
        and 0 < obter_pos_x(p) < obter_tamanho_x(m) - 1 and 0 < obter_pos_y(p) < obter_tamanho_y(m) - 1


def prados_iguais(m1, m2):
    """
    prados iguais: prado × prado -→ booleano

    prados iguais(m1, m2) devolve True apenas se m1 e m2 forem prados e forem iguais.
    """

    return eh_prado(m1) and eh_prado(m2) and m1[0] == m2[0] and m1[1] == m2[1] and m1[2] == m2[2] and m1[3] == m2[3]


def prado_para_str(m):
    """
    prado para str : prado -→ str

    prado para str(m) devolve uma cadeia de caracteres que representa o prado.
    """

    st = ""
    for y in range(0, obter_tamanho_y(m)):
        for x in range(0, obter_tamanho_x(m) + 1):
            if (x, y) == (0, 0) or (x, y) == (0, obter_tamanho_y(m) - 1) or (x, y) == (obter_tamanho_x(m) - 1, 0) or \
                    (x, y) == (obter_tamanho_x(m) - 1, obter_tamanho_y(m) - 1):
                st = st + "+"
            elif x == obter_tamanho_x(m) and y != obter_tamanho_y(m) - 1:
                st = st + "\n"
            elif (y == 0 or y == obter_tamanho_y(m) - 1) and x < obter_tamanho_x(m) - 1:
                st = st + "-"
            elif x == 0 or x == obter_tamanho_x(m) - 1:
                st = st + "|"
            elif eh_posicao_animal(m, cria_posicao(x, y)):
                st = st + animal_para_char(obter_animal(m, cria_posicao(x, y)))
            elif eh_posicao_obstaculo(m, cria_posicao(x, y)) and x < obter_tamanho_x(m) - 1:
                st = st + "@"
            elif x < obter_tamanho_x(m) - 1:
                st = st + "."
    return st


def obter_valor_numerico(m, p):
    """
    obter valor numerico: prado × posicao -→ int

    obter valor numerico(m, p) devolve o valor numérico da posição p correspondente à ordem de leitura no prado m.
    """

    return obter_tamanho_x(m) * obter_pos_y(p) + obter_pos_x(p)


def obter_movimento(m, p):
    """
    obter movimento: prado × posicao -→ posicao

    obter movimento(m, p) devolve a posição seguinte do animal na posição p dentro do prado m de acordo com
    as regras de movimento dos animais no prado.
    """

    if eh_presa(obter_animal(m, p)):

        # Obtem as posições livres das adjacentes
        opt = list(filter(lambda x: eh_posicao_livre(m, x), obter_posicoes_adjacentes(p)))

        if not opt:
            return p
        else:
            return opt[obter_valor_numerico(m, p) % len(opt)]

    elif eh_predador(obter_animal(m, p)):
        presas = []

        # Obtem as posições livres ou sem obstáculos das adjacentes
        opt = list(filter(lambda x: not eh_posicao_obstaculo(m, x), obter_posicoes_adjacentes(p)))

        for pos in opt:
            if eh_posicao_animal(m, pos):
                if eh_presa(obter_animal(m, pos)):
                    # Cria uma lista apenas com as posições adjacentes de presas
                    presas = presas + [pos, ]

        livres = list(filter(lambda x: eh_posicao_livre(m, x), obter_posicoes_adjacentes(p)))

        if len(livres) == 0 and len(presas) == 0:
            return p

        else:
            # Se não houver presas adjacentes:
            if len(presas) == 0:
                return livres[obter_valor_numerico(m, p) % len(livres)]
            else:
                return presas[obter_valor_numerico(m, p) % len(presas)]


#################
# 2.2.1 geração #
#################


def geracao(m):
    """
    geracao: prado -→ prado

    geracao(m) é a função auxiliar que modifica o prado m fornecido como argumento de acordo com a evolução
    correspondente a uma geração completa, e devolve o próprio prado. Isto é, seguindo a ordem de leitura do prado,
    cada animal (vivo) realiza o seu turno de ação de acordo com as regras descritas.
    """

    comidos = []
    for pos in obter_posicao_animais(m):

        if eh_posicao_animal(m, pos) and not any([posicoes_iguais(pos, morto) for morto in comidos]):

            aumenta_fome(obter_animal(m, pos))
            aumenta_idade(obter_animal(m, pos))
            nova = obter_movimento(m, pos)

            # Comer presas
            if eh_posicao_animal(m, nova) and eh_predador(obter_animal(m, pos)) and not posicoes_iguais(pos, nova):
                comidos = comidos + [nova, ]
                eliminar_animal(m, nova)
                reset_fome(obter_animal(m, pos))

            # Movimentação com reprodução (posição nova é diferente da atual)
            if not posicoes_iguais(pos, nova) and eh_animal_fertil(obter_animal(m, pos)):
                mover_animal(m, pos, nova)
                inserir_animal(m, reproduz_animal(obter_animal(m, nova)), pos)

            # Movimentação sem reprodução
            else:
                mover_animal(m, pos, nova)

            # Morte de famintos
            if eh_animal_faminto(obter_animal(m, nova)):
                eliminar_animal(m, nova)
    return m


############################
# 2.2.2 simula_ecossistema #
############################


def simula_ecossistema(f, g, v):
    """
    simula ecossistema: str × int × booleano -→ tuplo

    simula ecossitema(f, g, v) é a função principal que permite simular o ecossistema de um prado. A função recebe
    uma cadeia de caracteres f, um valor inteiro g e um valor booleano v e devolve o tuplo de dois elementos
    correspondentes ao número de predadores e presas no prado no fim da simulação. A cadeia de caracteres f passada
    por argumento corresponde ao nome do ficheiro de configuração da simulação. O valor inteiro g corresponde ao
    número de gerações a simular. O argumento booleano v ativa o modo verboso (True) ou o modo quiet (False).
    No modo quiet mostra-se pela saída standard o prado, o número de animais e o número de geração no início da
    simulação e após a última geração. No modo verboso, após cada geração, mostra-se também o prado, o número de
    animais e o número de geração, apenas se o número de animais predadores ou presas se tiver alterado.
    """

    with open(f, "r") as f1:
        lines = f1.readlines()

    a, p, r = (), (), ()

    for roc in eval(lines[1]):
        r = r + (cria_posicao(roc[0], roc[1]),)

    for ani in lines[2:]:
        ani = eval(ani)
        a = a + (cria_animal(ani[0], ani[1], ani[2]),)
        p = p + (cria_posicao(ani[3][0], ani[3][1]),)

    pos = cria_posicao(eval(lines[0])[0], eval(lines[0])[1])

    prado = cria_prado(pos, r, a, p)

    print("Predadores:", obter_numero_predadores(prado), "vs", "Presas:", obter_numero_presas(prado), "(Gen. 0)")
    print(prado_para_str(prado))

    if v:
        i = 1
        while i <= g:
            a = obter_numero_predadores(prado)
            b = obter_numero_presas(prado)
            geracao(prado)
            if a != obter_numero_predadores(prado) or b != obter_numero_presas(prado):
                print("Predadores:", obter_numero_predadores(prado), "vs", "Presas:", obter_numero_presas(prado),
                      "(Gen.", str(i) + ")")
                print(prado_para_str(prado))
            i += 1

    else:
        for ger in range(g):
            geracao(prado)
        print("Predadores:", obter_numero_predadores(prado), "vs", "Presas:", obter_numero_presas(prado),
              "(Gen.", str(g) + ")")
        print(prado_para_str(prado))

    return obter_numero_predadores(prado), obter_numero_presas(prado)
