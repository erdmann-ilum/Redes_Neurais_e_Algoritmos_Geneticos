import random
from numpy import inf
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib import rcParams
rcParams['figure.dpi'] = 300


###############################################################################
#                               Caixas binárias                               #
###############################################################################


def gene_cb():
    """Sorteia um valor para uma caixa no problema das caixas binárias"""
    valores_possiveis = [0, 1]
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato_cb(n):
    """Cria uma lista com n valores zero ou um.

    Args:
      n: inteiro que representa o número de caixas.

    """
    candidato = []
    for _ in range(n):
        gene = gene_cb()
        candidato.append(gene)
    return candidato


def populacao_cb(tamanho, n):
    """Cria uma população para o problema das caixas binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_cb(n))
    return populacao


def funcao_objetivo_cb(candidato):
    """Computa a função objetivo no problema das caixas binárias

    Args:
      candidato: uma lista contendo os valores das caixas binárias do problema

    """
    return sum(candidato)


def funcao_objetivo_pop_cb(populacao):
    """Computa a função objetivo para uma população no problema das caixas binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_cb(individuo))
    return fitness


###############################################################################
#                             Caixas não-binárias                             #
###############################################################################


def gene_cnb(valor_max):
    """Sorteia um valor para uma caixa no problema das caixas não-binárias"""
    valores_possiveis = range(valor_max + 1)
    gene = random.choice(valores_possiveis)
    return gene


def cria_candidato_cnb(n, valor_max):
    """Cria uma lista com n valores entre zero e valor_max.

    Args:
      n: inteiro que representa o número de caixas.
      valor_max: inteiro represtando o valor máximo das caixas
    """
    candidato = []
    for _ in range(n):
        gene = gene_cnb(valor_max)
        candidato.append(gene)
    return candidato


def populacao_cnb(tamanho, n, valor_max):
    """Cria uma população para o problema das caixas não-binárias.

    Args:
      tamanho: tamanho da população
      n: inteiro que representa o número de caixas de cada indivíduo.
      valor_max: inteiro represtando o valor máximo das caixas

    """
    populacao = []
    for _ in range(tamanho):
        populacao.append(cria_candidato_cnb(n, valor_max))
    return populacao


def funcao_objetivo_cnb(candidato):
    """Computa a função objetivo no problema das caixas não-binárias

    Args:
      candidato: uma lista contendo os valores das caixas não-binárias do problema

    """
    return sum(candidato)


def funcao_objetivo_pop_cnb(populacao):
    """Computa a função objetivo para uma população no problema das caixas não-binárias

    Args:
      populacao: lista contendo os individuos do problema

    """
    fitness = []
    for individuo in populacao:
        fitness.append(funcao_objetivo_cnb(individuo))
    return fitness


###############################################################################
#                                    Senha                                    #
###############################################################################


def gene_senha(letras_possiveis):
    """Sorteia uma letra.

    Args:
      letras: letras possíveis de serem sorteadas.

    """
    letra = random.choice(letras_possiveis)
    return letra


def cria_candidato_senha(tamanho_senha, letras_possiveis):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_senha: inteiro representando o tamanho da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    candidato = []

    for _ in range(tamanho_senha):
        candidato.append(gene_senha(letras_possiveis))

    return candidato


def populacao_senha(tamanho_populacao, tamanho_senha, letras_possiveis):
    """Cria população inicial no problema da senha

    Args
      tamanho_populacao: tamanho da população.
      tamanho_senha: inteiro representando o tamanho da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_senha(tamanho_senha, letras_possiveis))

    return populacao


def funcao_objetivo_senha(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia = 0

    for letra_candidato, letra_senha in zip(candidato, senha_verdadeira):
        num_letra_candidato = ord(letra_candidato)
        num_letra_senha = ord(letra_senha)
        distancia += abs(num_letra_candidato - num_letra_senha)

    return distancia


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return fitness

###############################################################################
#                          Senha de tamanho variável                          #
###############################################################################


def cria_candidato_senha_variavel(tamanho_min_senha:int, tamanho_max_senha:int, letras_possiveis):
    """Cria um candidato para o problema da senha

    Args:
      tamanho_min_senha: inteiro representando o tamanho mínimo da senha.
      tamanho_max_senha: inteiro representando o tamanho máximo da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    candidato = []

    tamanho_senha = random.choice(range(tamanho_min_senha, tamanho_max_senha+1))
    for _ in range(tamanho_senha):
        candidato.append(gene_senha(letras_possiveis))

    return candidato

def populacao_senha_variavel(tamanho_populacao:int, tamanho_min_senha:int, tamanho_max_senha:int, letras_possiveis):
    """Cria população inicial no problema da senha

    Args
      tamanho_populacao: tamanho da população.
      tamanho_min_senha: inteiro representando o tamanho mínimo da senha.
      tamanho_max_senha: inteiro representando o tamanho máximo da senha.
      letras_possiveis: letras possíveis de serem sorteadas.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_senha_variavel(tamanho_min_senha, tamanho_max_senha, letras_possiveis))

    return populacao

def funcao_objetivo_senha_variavel(candidato, senha_verdadeira):
    """Computa a funcao objetivo de um candidato no problema da senha com número variável de dígitos.

    Args:
      candidato: um palpite para a senha que você quer descobrir
      senha_verdadeira: a senha que você está tentando descobrir

    """
    distancia_letras = 0

    # checa se as letras estão corretas para o menor candidato
    for letra_candidato, letra_senha in zip(candidato, senha_verdadeira):
        num_letra_candidato = ord(letra_candidato)
        num_letra_senha = ord(letra_senha)
        distancia_letras += abs(num_letra_candidato - num_letra_senha)

    distancia_digitos = abs(len(candidato) - len(senha_verdadeira))

    return distancia_letras, distancia_digitos

def funcao_objetivo_pop_senha_variavel(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha com número variável de dígitos.

    Args:
      populacao: lista contendo os individuos do problema
      senha_verdadeira: a senha que você está tentando descobrir

    """
    fitness = []

    for individuo in populacao:
        fitness.append(sum(funcao_objetivo_senha_variavel(individuo, senha_verdadeira)))

    return fitness


###############################################################################
#                                   Caixeiro                                  #
###############################################################################


def cria_cidades(n:int, xy_minimo=0.0, xy_maximo=300.0):
    """Cria um dicionário aleatório de cidades com suas posições (x,y).

    Args:
      n: Número de cidades que serão visitadas pelo caixeiro.
      xy_minimo: Valor mínimo possível das coordenadas x e y.
      xy_maximo: Valor máximo possível das coordenadas x e y.

    """
    cidades = {}
    num_digitos = len(str(abs(n)))

    for i in range(n):
        cidades[f"Cidade {i:0>{num_digitos}}"] = (
            random.randint(xy_minimo, xy_maximo),
            random.randint(xy_minimo, xy_maximo),
        )

    return cidades


def plota_cidades(cidades:dict):
    """Plota as cidades do problema do caixeiro viajante

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue", marker="s")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()

def plota_trajeto(cidades:dict, trajeto:list):
    """Plota o trajeto do caixeiro

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      trajeto: lista contendo a ordem das cidades que foram visitadas

    """
    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue", marker="s")

    # nomes das cidades
    for cidade, (x, y) in cidades.items():
        plt.annotate(
            cidade,
            (x, y),
            textcoords="offset points",
            xytext=(0, 10),
            ha="center",
        )

    # plotando os trajetos
    for i in range(len(trajeto) - 1):
        cidade1 = trajeto[i]
        cidade2 = trajeto[i + 1]
        plt.annotate(
            '', xy=(cidades[cidade2][0], cidades[cidade2][1]), xytext=(cidades[cidade1][0], cidades[cidade1][1]),
            arrowprops=dict(arrowstyle="->", color='red', lw=2)
        )

    # trajeto de volta à cidade inicial
    cidade1 = trajeto[-1]
    cidade2 = trajeto[0]
    plt.annotate(
        '', xy=(cidades[cidade2][0], cidades[cidade2][1]), xytext=(cidades[cidade1][0], cidades[cidade1][1]),
        arrowprops=dict(arrowstyle="->", color='red', lw=2)
    )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()

def plota_trajeto_multiplos_caixeiros(cidades:dict, trajeto:list, n:int, nomes=True):
    """Plota o trajeto dos múltiplos caixeiros

    Nota: código de base criado pelo Google Gemini e modificado aqui.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      trajeto: lista contendo a ordem das cidades que foram visitadas
      n: número inteiro de caixeiros viajantes.

    """
    cores = list(mcolors.CSS4_COLORS.keys())

    for cor in ['white','whitesmoke','snow', 'mistyrose','seashell','linen','antiquewhite','oldlace','floralwhite','ivory', 'beige','lightyellow','lightgoldenrodyellow', 'cornsilk', 'lemonchiffon', 'honeydew', 'mintcream','azure','lightcyan','aliceblue','ghostwhite','lavender','lavenderblush']:
        cores.remove(cor)

    cores = random.sample(cores, k=n)

    x = [cidades[cidade][0] for cidade in cidades]
    y = [cidades[cidade][1] for cidade in cidades]

    # plotando as cidades
    plt.scatter(x, y, color="blue", marker="s")

    # nomes das cidades
    if nomes:
        for cidade, (x, y) in cidades.items():
            plt.annotate(
                cidade,
                (x, y),
                textcoords="offset points",
                xytext=(0, 10),
                ha="center",
            )

    # plotando os trajetos
    for v in range(n):
        for i in range(len(trajeto[v::n])):
            cidade1 = trajeto[v::n][i - 1]
            cidade2 = trajeto[v::n][i]
            plt.annotate(
                '', xy=(cidades[cidade2][0], cidades[cidade2][1]), xytext=(cidades[cidade1][0], cidades[cidade1][1]),
                arrowprops=dict(arrowstyle="->", color=cores[v], lw=2)
            )

    plt.xlabel("Coordenada x")
    plt.ylabel("Coordenada y")
    plt.show()

def dist_euclidiana(coord1:float|int, coord2:float|int):
    """Computa a distância Euclidiana entre dois pontos em R^2

    Args:
      coord1: lista contendo as coordenadas x e y de um ponto.
      coord2: lista contendo as coordenadas x e y do outro ponto.

    """
    x1 = coord1[0]
    x2 = coord2[0]
    y1 = coord1[1]
    y2 = coord2[1]

    distancia = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1 / 2)

    return distancia


def cria_candidato_caixeiro(cidades:dict):
    """Sorteia um caminho possível no problema do caixeiro viajante

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    nomes_cidades = list(cidades.keys())
    caminho = random.sample(nomes_cidades, k=len(nomes_cidades))
    return caminho


def populacao_caixeiro(tamanho_populacao:int, cidades:dict):
    """Cria uma população no problema do caixeiro viajante

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiro(cidades))

    return populacao


def funcao_objetivo_caixeiro(candidato:list, cidades:dict):
    """Funcao objetivo de um candidato no problema do caixeiro viajante

    Args:
      candidato: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    distancia = 0

    for pos in range(len(candidato) - 1):
        coord_cidade_partida = cidades[candidato[pos]]
        coord_cidade_chegada = cidades[candidato[pos + 1]]
        distancia += dist_euclidiana(
            coord_cidade_partida, coord_cidade_chegada
        )

    # distância para retornar à cidade inicial
    coord_cidade_final = cidades[candidato[-1]]
    coord_cidade_inicial = cidades[candidato[0]]
    distancia += dist_euclidiana(coord_cidade_final, coord_cidade_inicial)

    return distancia


def funcao_objetivo_pop_caixeiro(populacao:list, cidades:dict):
    """Funcao objetivo de uma populacao no problema do caixeiro viajante

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_caixeiro(individuo, cidades))

    return fitness

def cria_candidato_caixeiro_impar(cidades:dict):
    """Sorteia um caminho possível no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    nomes_cidades = list(cidades.keys())
    nomes_cidades_pares = nomes_cidades[2::2]
    nomes_cidades_impares = nomes_cidades[1::2]
    caminho = [nomes_cidades[0]]
    caminho += random.sample(nomes_cidades_impares, k=len(nomes_cidades_impares))
    caminho += random.sample(nomes_cidades_pares, k=len(nomes_cidades_pares))
    return caminho


def populacao_caixeiro_impar(tamanho_populacao:int, cidades:dict):
    """Cria uma população no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      tamanho_populacao: tamanho da população.
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    populacao = []

    for _ in range(tamanho_populacao):
        populacao.append(cria_candidato_caixeiro_impar(cidades))

    return populacao

def funcao_objetivo_caixeiro_impar(candidato:list, cidades:dict):
    """Funcao objetivo de um candidato no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      candidato: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    distancia = 0

    nomes_cidades = list(cidades.keys())
    nomes_cidades_pares = nomes_cidades[2::2]
    nomes_cidades_impares = nomes_cidades[1::2]

    if candidato[0] != nomes_cidades[0]:
        distancia = inf
        return distancia
    
    for pos in range(len(candidato) - 1):
        coord_cidade_partida = cidades[candidato[pos]]
        coord_cidade_chegada = cidades[candidato[pos + 1]]

        if (candidato[pos] in nomes_cidades_pares) and (candidato[pos + 1] in nomes_cidades_impares):
            distancia = inf
            return distancia

        distancia += dist_euclidiana(
            coord_cidade_partida, coord_cidade_chegada
        )

    # distância para retornar à cidade inicial
    coord_cidade_final = cidades[candidato[-1]]
    coord_cidade_inicial = cidades[candidato[0]]
    distancia += dist_euclidiana(coord_cidade_final, coord_cidade_inicial)

    return distancia


def funcao_objetivo_pop_caixeiro_impar(populacao:list, cidades:dict):
    """Funcao objetivo de uma populacao no problema do caixeiro viajante que prefere cidades ímpares.

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_caixeiro_impar(individuo, cidades))

    return fitness

def funcao_objetivo_multiplos_caixeiros(candidato:list, cidades:dict, n:int):
    """Funcao objetivo de um candidato no problema dos múltiplos caixeiros viajantes, que não podem visitar uma cidade já visitada por um caixeiro.

    Args:
      candidato: uma lista contendo o caminho percorrido
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      n: número inteiro de caixeiros viajantes.

    """
    distancia = 0
    posicoes = range(len(candidato))
    caixeiros = range(n)

    for v in caixeiros:
        for pos in posicoes[v::n]:
            if (pos + n) < len(candidato):
                coord_cidade_partida = cidades[candidato[pos]]
                coord_cidade_chegada = cidades[candidato[pos + n]]
                distancia += dist_euclidiana(
                    coord_cidade_partida, coord_cidade_chegada
                )
            else:
                coord_cidade_partida = cidades[candidato[pos]]
                coord_cidade_chegada = cidades[candidato[v]]
                distancia += dist_euclidiana(
                    coord_cidade_partida, coord_cidade_chegada
                )

    return distancia


def funcao_objetivo_pop_multiplos_caixeiros(populacao:list, cidades:dict, n:int):
    """Funcao objetivo de uma populacao no problema dos múltiplos caixeiros viajantes.

    Args:
      populacao: lista contendo os individuos do problema
      cidades:
        Dicionário contendo o nome das cidades como chaves e a coordenada no
        plano cartesiano das cidades como valores.
      n: número inteiro de caixeiros viajantes.

    """
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_multiplos_caixeiros(individuo, cidades,n))

    return fitness


###############################################################################
#                             Problema da mochila                             #
###############################################################################


def calcula_mochila(candidato, itens, ordem_dos_itens):
    """Computa o peso e o valor total de uma mochila

    Args:
      candidato: lista representando quais itens estão na mochila
      itens: dicionário com os pesos e valores dos itens
      ordem_dos_itens: ordem dos itens da lista `candidato`

    """
    peso = 0
    valor = 0
    for pegou_item_ou_nao, nome_item in zip(candidato, ordem_dos_itens):
        if pegou_item_ou_nao == 1:
            peso += itens[nome_item]["peso"]
            valor += itens[nome_item]["valor"]
    return peso, valor


def funcao_objetivo_mochila(candidato, itens, ordem_dos_itens, limite):
    """Computa a funcao objetivo de um candidato no problema da mochila

    Args:
      candidato: lista representando quais itens estão na mochila
      itens: dicionário com os pesos e valores dos itens
      ordem_dos_itens: ordem dos itens da lista `candidato`
      limite: valor representando o limite de peso da mochila

    """
    peso, valor = calcula_mochila(candidato, itens, ordem_dos_itens)

    if peso <= limite:
        return valor
    else:
        return 0.01


def funcao_objetivo_pop_mochila(populacao, itens, ordem_dos_itens, limite):
    """Computa a fun. objetivo de uma populacao no problema da mochila

    Args:
      populacao: lista contendo os individuos do problema
      itens: dicionário com os pesos e valores dos itens
      ordem_dos_itens: ordem dos itens da lista `candidato`
      limite: valor representando o limite de peso da mochila

    """
    fitness = []

    for individuo in populacao:
        fitness.append(
            funcao_objetivo_mochila(individuo, itens, ordem_dos_itens, limite)
        )

    return fitness

###############################################################################
#                                Liga ternária                                #
###############################################################################

def cria_candidato_liga(elementos:dict, k=3) -> dict:

    dicionario = dict()
    selecao = random.sample(list(elementos.keys()), k=k)

    massas = [random.uniform(5,100-5*(k-1))]

    for j in range(k-1):
        if j == k-2:
            massas.append(100-sum(massas))
        else:
            massas.append(random.uniform(5,100-sum(massas)-5*(k-2-j)))

    for i in range(k):
        dicionario[selecao[i]] = massas[i]
    
    return dicionario

def populacao_liga(tamanho_populacao:int, elementos:dict, k=3) -> list:

    candidatos = list()

    for _ in range(tamanho_populacao):
        candidatos.append(cria_candidato_liga(elementos, k))

    return candidatos

def funcao_objetivo_liga(candidato:dict, tabela:dict) -> float:
    """Função objetivo do problema da liga ternária mais cara: calcula o custo da liga.

    Args:
      candidato: dicionário contendo um indivíduo do problema (par elemento: massa em g)
      tabela: dicionário contendo os elementos e seus respectivos preços por quilo

    """

    custo = 0

    for elemento in candidato.keys():
        custo += candidato[elemento]*tabela[elemento]/1000

    return custo 

def funcao_objetivo_pop_liga(populacao:list, tabela:dict) -> list:
    """Função objetivo de população do problema da liga ternária mais cara: calcula o custo de cada liga.

    Args:
      populacao: lista contendo os indivíduo do problema (sendo esses indivíduos dicionários com os pares elemento: massa em g)
      tabela: dicionário contendo os elementos e seus respectivos preços por quilo

    """

    fitness = list()

    for i in range(len(populacao)):
        fitness.append(funcao_objetivo_liga(populacao[i], tabela))

    return fitness

def funcao_objetivo_liga_leve(candidato:dict, precos:dict, peso_atomico:dict) -> float:
    """Função objetivo do problema da liga ternária mais cara: calcula o custo da liga.

    Args:
      candidato: dicionário contendo um indivíduo do problema (par elemento: massa em g)
      tabela: dicionário contendo os elementos e seus respectivos preços por quilo

    """

    custo = 0
    peso_molar = 0

    maior_preco = max(precos.values())
    maior_massa = max(peso_atomico.values())

    for elemento in candidato.keys():
        # massa do elemento em kg * preco do elemento por kg
        custo += candidato[elemento]*precos[elemento]/1000
        # fracao massica do elemento * seu peso atomico
        peso_molar += candidato[elemento]*peso_atomico[elemento]/100

    # normalização absmax
    custo /= maior_preco*100/1000
    peso_molar /= maior_massa

    return custo/peso_molar 

def funcao_objetivo_pop_liga_leve(populacao:list, precos:dict, peso_atomico:dict) -> list:
    """Função objetivo de população do problema da liga ternária mais cara: calcula o custo de cada liga.

    Args:
      populacao: lista contendo os indivíduo do problema (sendo esses indivíduos dicionários com os pares elemento: massa em g)
      tabela: dicionário contendo os elementos e seus respectivos preços por quilo

    """

    fitness = list()

    for i in range(len(populacao)):
        fitness.append(funcao_objetivo_liga_leve(populacao[i], precos, peso_atomico))

    return fitness

def cruzamento_ponto_simples_liga(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples no problema da liga ternária mais cara do mundo

  Args:
    pai: lista representando um individuo
    mae: lista representando um individuo
    chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte = random.randint(1, len(list(mae.keys())) - 1)
        keys_filho1 = list(pai.keys())[:corte] + list(mae.keys())[corte:]
        keys_filho2 = list(mae.keys())[:corte] + list(pai.keys())[corte:]
            
        # avaliação para garantir que um filho não está com duas vezes o mesmo elemento
        genes_vistos_1 = set()
        genes_vistos_2 = set()
        for g1, g2 in zip(keys_filho1,keys_filho2):
            if g1 in genes_vistos_1:
                return pai, mae
            elif g2 in genes_vistos_2:
                return pai, mae
            else:
                genes_vistos_1.add(g1)
                genes_vistos_2.add(g2)

        filho1 = dict()
        filho2 = dict()

        for i in range(len(keys_filho1)):
            filho1[keys_filho1[i]] = pai[list(pai.keys())[i]]
            filho2[keys_filho2[i]] = mae[list(mae.keys())[i]]

        return filho1, filho2
  
    else:
        return pai, mae

def mutacao_troca_liga(populacao:list, chance_de_mutacao:float):
    """Aplica mutacao de troca nos elementos de indivíduos do problema da liga ternária mais cara do mundo

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1, gene2 = random.sample(list(individuo.keys()), k=2)

            while individuo[gene1] == individuo[gene2]:
                gene1, gene2 = random.sample(list(individuo.keys()), k=2)

            individuo[gene1], individuo[gene2] = (
                individuo[gene2],
                individuo[gene1],
            )

def mutacao_distribuicao_valores_liga(populacao:list, chance_de_mutacao:float):
    """Seleciona dois genes, soma suas massas e redistribui aleatoriamente nos indivíduos do problema da liga ternária mais cara do mundo

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1, gene2 = random.sample(list(individuo.keys()), k=2)

            pool = individuo[gene1]+individuo[gene2]

            individuo[gene1] = random.uniform(5,pool-5)
            individuo[gene2] = pool - individuo[gene1]

def mutacao_simples_liga(populacao:list, chance_de_mutacao:float, elementos:dict) -> None:
    """Troca um elemento, mantendo a massa, dos indivíduos do problema da liga ternária mais cara do mundo

    Args:
      populacao: lista contendo os indivíduos do problema
      elementos: dicionário contendo os elementos e seus respectivos preços por quilo
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.choice(list(individuo.keys()))
            valor = individuo[gene]

            possiveis = list(elementos.keys())
            for g in individuo.keys():
                possiveis.remove(g)

            escolha = random.choice(possiveis)
            individuo[escolha] = valor
            individuo.pop(gene)

###############################################################################
#                                 Palíndromo                                  #
###############################################################################

def funcao_objetivo_palindromo(individuo, vistos):
    loss = 0
    vogal = False
    palindromo = True

    for letra in ["A","E","I","O","U"]:
        if letra in list(individuo):
            vogal = True
            break    
    
    for i,j in zip(individuo[::],individuo[::-1]):
        if i != j:
            palindromo = False
            break

    if not vogal or not palindromo:
        loss = inf

    if str(individuo) in vistos:
        loss = 1
    else:
        vistos.add(str(individuo))

    return loss

def funcao_objetivo_pop_palindromo(populacao, vistos):
    fitness = []

    for individuo in populacao:
        fitness.append(funcao_objetivo_palindromo(individuo, vistos))

    return fitness

def cruzamento_ponto_duplo_palindromo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte1 = random.randint(1, int((len(mae)-1)/2))
        corte2 = -corte1
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    else:
        return pai, mae

def mutacao_troca_palindromo(populacao, chance_de_mutacao):
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            ultimo_dif = int((len(individuo)-1)/2-1)
            ponto = random.randint(0, ultimo_dif)
            possib = list(range(int((len(individuo)-1)/2)))
            possib.remove(ponto)
            troca = random.choice(possib)
            individuo[ponto],individuo[troca] = individuo[troca],individuo[ponto]
            individuo[-ponto-1],individuo[-troca-1] = individuo[-troca-1],individuo[-ponto-1]

def mutacao_simples_palindromo(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação simples em palíndromo (de maneira simétrica).

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_sorteio = set(valores_possiveis) - set([valor_gene])
            valor_novo = random.choice(list(valores_sorteio))
            individuo[gene], individuo[-gene-1] = valor_novo, valor_novo


###############################################################################
#                                   Seleção                                   #
###############################################################################


def selecao_roleta_max(populacao, fitness):
    """Realiza seleção da população pela roleta

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo

    """
    selecionados = random.choices(populacao, fitness, k=len(populacao))
    return selecionados


def selecao_torneio_max(populacao:list, fitness:list, tamanho_torneio:int):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    maximização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de indivíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        max_fitness = max(fitness_sorteados)
        indice_max_fitness = fitness_sorteados.index(max_fitness)
        individuo_selecionado = sorteados[indice_max_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


def selecao_torneio_min(populacao:list, fitness:list, tamanho_torneio:int):
    """Faz a seleção de uma população usando torneio.

    Nota: da forma que está implementada, só funciona em problemas de
    minimização.

    Args:
      populacao: lista contendo os individuos do problema
      fitness: lista contendo os valores computados da funcao objetivo
      tamanho_torneio: quantidade de indivíduos que batalham entre si

    """
    selecionados = []

    for _ in range(len(populacao)):
        sorteados = random.sample(populacao, tamanho_torneio)

        fitness_sorteados = []
        for individuo in sorteados:
            indice_individuo = populacao.index(individuo)
            fitness_sorteados.append(fitness[indice_individuo])

        min_fitness = min(fitness_sorteados)
        indice_min_fitness = fitness_sorteados.index(min_fitness)
        individuo_selecionado = sorteados[indice_min_fitness]

        selecionados.append(individuo_selecionado)

    return selecionados


###############################################################################
#                                  Cruzamento                                 #
###############################################################################


def cruzamento_ponto_simples(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte = random.randint(1, len(mae) - 1)
        filho1 = pai[:corte] + mae[corte:]
        filho2 = mae[:corte] + pai[corte:]
        return filho1, filho2
    else:
        return pai, mae
    
def cruzamento_ponto_simples_variavel(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto simples com dois indivíduos de tamanho diferente.

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        ordem = sorted([pai, mae], key=len)
        if len(ordem[0]) == 1:
            corte = random.randint(0, len(ordem[1]) - 1)
            filho1 = list(ordem[1][corte])
            filho2 = ordem[1][:corte] + list(ordem[0][0]) + ordem[1][(corte+1):]
        else:
            corte = random.randint(1, len(ordem[0]))
            filho1 = pai[:corte] + mae[corte:]
            filho2 = mae[:corte] + pai[corte:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ponto_duplo(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento de ponto duplo

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        corte1 = random.randint(1, len(mae) - 2)
        corte2 = random.randint(corte1 + 1, len(mae) - 1)
        filho1 = pai[:corte1] + mae[corte1:corte2] + pai[corte2:]
        filho2 = mae[:corte1] + pai[corte1:corte2] + mae[corte2:]
        return filho1, filho2
    else:
        return pai, mae


def cruzamento_uniforme(pai, mae, chance_de_cruzamento):
    """Realiza cruzamento uniforme

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        filho1 = []
        filho2 = []

        for gene_pai, gene_mae in zip(pai, mae):
            if random.choice([True, False]):
                filho1.append(gene_pai)
                filho2.append(gene_mae)
            else:
                filho1.append(gene_mae)
                filho2.append(gene_pai)

        return filho1, filho2
    else:
        return pai, mae


def cruzamento_ordenado(pai:list, mae:list, chance_de_cruzamento:float):
    """Cruzamento ordenado entre dois individuos

    Args:
      pai: lista representando um individuo
      mae: lista representando um individuo
      chance_de_cruzamento: float entre 0 e 1 representando a chance de cruzamento

    """
    if random.random() < chance_de_cruzamento:
        tamanho_individuo = len(mae)

        # pontos de corte
        corte1 = random.randint(0, tamanho_individuo - 2)
        corte2 = random.randint(corte1 + 1, tamanho_individuo)

        # filho1
        filho1 = [None] * tamanho_individuo
        filho1[corte1:corte2] = mae[corte1:corte2]
        pai_ = pai[corte2:] + pai[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in pai_:
            if valor not in filho1:
                filho1[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        # filho2
        filho2 = [None] * tamanho_individuo
        filho2[corte1:corte2] = pai[corte1:corte2]
        mae_ = mae[corte2:] + mae[:corte2]
        posicao = corte2 % tamanho_individuo
        for valor in mae_:
            if valor not in filho2:
                filho2[posicao] = valor
                posicao += 1
                posicao %= tamanho_individuo

        return filho1, filho2
    else:
        return pai, mae


###############################################################################
#                                   Mutação                                   #
###############################################################################


def mutacao_simples(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação simples

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_sorteio = set(valores_possiveis) - set([valor_gene])
            individuo[gene] = random.choice(list(valores_sorteio))


def mutacao_salto(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de salto

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            indice_letra = valores_possiveis.index(valor_gene)
            indice_letra += random.choice([1, -1])
            indice_letra %= len(valores_possiveis)
            individuo[gene] = valores_possiveis[indice_letra]


def mutacao_troca(populacao:list, chance_de_mutacao:float):
    """Aplica mutação de troca em um indivíduo

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene1 = random.randint(0, len(individuo) - 1)
            gene2 = random.randint(0, len(individuo) - 1)

            while gene1 == gene2:
                gene1 = random.randint(0, len(individuo) - 1)
                gene2 = random.randint(0, len(individuo) - 1)

            individuo[gene1], individuo[gene2] = (
                individuo[gene2],
                individuo[gene1],
            )


def mutacao_simples_cb(populacao, chance_de_mutacao):
    """Realiza mutação simples no problema das caixas binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            individuo[gene] = 0 if individuo[gene] == 1 else 1


def mutacao_simples_cnb(populacao, chance_de_mutacao, valor_max):
    """Realiza mutação simples no problema das caixas não-binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valor_max: inteiro represtando o valor máximo das caixas

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            gene = random.randint(0, len(individuo) - 1)
            valor_gene = individuo[gene]
            valores_possiveis = list(range(valor_max + 1))
            valores_possiveis.remove(valor_gene)
            individuo[gene] = random.choice(valores_possiveis)


def mutacao_sucessiva_cb(populacao, chance_de_mutacao, chance_mutacao_gene):
    """Realiza mutação simples no problema das caixas binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    individuo[gene] = 0 if individuo[gene] == 1 else 1


def mutacao_sucessiva_cnb(
    populacao, chance_de_mutacao, chance_mutacao_gene, valor_max
):
    """Realiza mutação simples no problema das caixas não-binárias

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      chance_mutacao_gene: float entre 0 e 1 representando a chance de mutação de cada gene
      valor_max: inteiro represtando o valor máximo das caixas

    """
    for individuo in populacao:
        if random.random() < chance_de_mutacao:
            for gene in range(len(individuo)):
                if random.random() < chance_mutacao_gene:
                    valores_possiveis = list(range(valor_max + 1))
                    valor_gene = individuo[gene]
                    valores_possiveis.remove(valor_gene)
                    individuo[gene] = random.choice(valores_possiveis)

def mutacao_tamanho(populacao, chance_de_mutacao, valores_possiveis):
    """Realiza mutação de tamanho, adicionando ou diminuindo um dígito do indivíduo.

    Args:
      populacao: lista contendo os indivíduos do problema
      chance_de_mutacao: float entre 0 e 1 representando a chance de mutação
      valores_possiveis: lista com todos os valores possíveis dos genes

    """
    for indice in range(len(populacao)):
        if random.random() < chance_de_mutacao:
            mutacao = random.choice((-1,1))
            if mutacao == -1 and len(populacao[indice]) > 1:
                populacao[indice] = populacao[indice][0:len(populacao[indice])-1]
            else:
                populacao[indice].append(gene_senha(valores_possiveis))