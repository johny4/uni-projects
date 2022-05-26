% Joao Trocado ist1103333

:- [codigo_comum].


% ---------------------------------------------------------------------------------------
% 2.1: extrai_ilhas_linha(N_L, Linha, Ilhas)
% Ilhas e a lista ordenada das ilhas existentes na linha N_L do puzzle
% ---------------------------------------------------------------------------------------

extrai_ilhas_linha(N_L, Linha, Ilhas) :- extrai_ilhas_linha(N_L, Linha, [], 1, Ilhas).

extrai_ilhas_linha(_, [], Ilhas, _, Ilhas).

extrai_ilhas_linha(N_L, [Cab|Resto], Res, Count1, Ilhas) :- 
	Cab == 0,
	NovoCount1 is Count1 + 1,
	extrai_ilhas_linha(N_L, Resto, Res, NovoCount1, Ilhas).

extrai_ilhas_linha(N_L, [Cab|Resto], Res, Count1, Ilhas) :-
	\+ Cab == 0, 
	append(Res, [ilha(Cab, (N_L, Count1))], NovoRes),
	NovoCount1 is Count1 + 1,
	extrai_ilhas_linha(N_L, Resto, NovoRes, NovoCount1, Ilhas).	 


% ---------------------------------------------------------------------------------------
% 2.2: ilhas(Puz, Ilhas)
% Ilhas e a lista ordenada das ilhas de Puz na linha N_L do puzzle
% ---------------------------------------------------------------------------------------
ilhas(Puz, Ilhas) :- ilhas(Puz, [], 1, Ilhas).

ilhas([], Ilhas, _, Ilhas).

ilhas([Cab|Resto], Res, Count2, Ilhas) :-
	extrai_ilhas_linha(Count2, Cab, IlhasAnteriores),
	append(Res, IlhasAnteriores, NovoRes),
	NovoCount2 is Count2 + 1,
	ilhas(Resto, NovoRes, NovoCount2, Ilhas).



% ---------------------------------------------------------------------------------------
% 2.3: vizinhas(Ilhas, Ilhas, Vizinhas)
% Vizinhas e a lista ordenada das ilhas vizinhas de Ilha
% ---------------------------------------------------------------------------------------

vizinhas(Ilhas, ilha(_, (X, Y)), Vizinhas) :-

	% Todas as ilhas com o mesmo X da Ilha
	findall(ilha(P, (X1, Y1)), (member(ilha(P, (X1, Y1)), Ilhas), X == X1), ListaX), 

	% Todas as ilhas com o mesmo Y da Ilha
	findall(ilha(P, (X1, Y1)), (member(ilha(P, (X1, Y1)), Ilhas), Y == Y1), ListaY), 	


	% Apenas as ilhas acima da Ilha
	findall(ilha(P, (X1, Y1)), (member(ilha(P, (X1, Y1)), ListaX), Y > Y1), Cima),	

	% Apenas as ilhas a esquerda da Ilha		
	findall(ilha(P, (X1, Y1)), (member(ilha(P, (X1, Y1)), ListaY), X > X1), Esquerda),

	% Apenas as ilhas a direita da Ilha	
	findall(ilha(P, (X1, Y1)), (member(ilha(P, (X1, Y1)), ListaY), X < X1), Direita),

	% Apenas as ilhas abaixo da Ilha		
	findall(ilha(P, (X1, Y1)), (member(ilha(P, (X1, Y1)), ListaX), Y < Y1), Baixo),		



	vizinhas_aux(Cima, IlhaCima),
	vizinhas_aux(Esquerda, IlhaEsquerda),	

	% Inverte a lista, para depois usar o auxiliar com o predicado last
	reverse(Direita, DireitaRev),
	reverse(Baixo, BaixoRev),	

	vizinhas_aux(DireitaRev, IlhaDireita),
	vizinhas_aux(BaixoRev, IlhaBaixo),

	% Junta as 4 possiveis ilhas vizinhas numa lista
	append([[IlhaEsquerda], [IlhaCima], [IlhaBaixo], [IlhaDireita]], PreVizinhas),

	% Remove as listas vazias possiveis oriundas do auxiliar
	flatten(PreVizinhas, Vizinhas).


% Predicaco auxiliar que "devolve" a ultima Ilha da lista ou [] se a Lista for vazia
vizinhas_aux(Lista, Res) :- Lista = [] -> Res = []; last(Lista, Res).
	

% ---------------------------------------------------------------------------------------
% 2.4: estado(Ilhas, Estado)
% Estado e a lista ordenada cujas elementos sao entradas de cada uma das Ilhas
% ---------------------------------------------------------------------------------------

estado(Ilhas, Estado) :- estado(Ilhas, Ilhas, [], Estado).

estado([], _, Res, Res).

estado([Cab|Resto], Ilhas, Res, Estado) :-
	vizinhas(Ilhas, Cab, Vizinhas),
	append(Res, [[Cab, Vizinhas, []]], NovoRes),
	estado(Resto, Ilhas, NovoRes, Estado).	


% ---------------------------------------------------------------------------------------
% 2.5: posicoes_entre(Pos1, Pos2, Posicoes)
% Lista ordenada de posicoes entre Pos1 e Pos2 (excluindo Pos1 e Pos2)
% ---------------------------------------------------------------------------------------

posicoes_entre((X1, Y1), (X2, Y2), Posicoes) :-
	X1 == X2,
	Y2 >= Y1,
	Y1F is Y1 + 1,
	Y2F is Y2 - 1,
	findall((X1, Y), between(Y1F, Y2F, Y), Posicoes).

posicoes_entre((X1, Y1), (X2, Y2), Posicoes) :-
	Y1 == Y2,
	X2 >= X1,
	X1F is X1 + 1,
	X2F is X2 - 1,
	findall((X, Y1), between(X1F, X2F, X), Posicoes).

posicoes_entre((X1, Y1), (X2, Y2), Posicoes) :-
	X1 == X2,
	Y1 >= Y2,
	Y2F is Y2 + 1,
	Y1F is Y1 - 1,
	findall((X1, Y), between(Y2F, Y1F, Y), Posicoes).

posicoes_entre((X1, Y1), (X2, Y2), Posicoes) :-
	Y1 == Y2,
	X1 >= X2,
	X2F is X2 + 1,
	X1F is X1 - 1,
	findall((X, Y1), between(X2F, X1F, X), Posicoes).


% ---------------------------------------------------------------------------------------
% 2.6 cria_ponte(Pos1, Pos2, Ponte)
% Cria uma ponte entre as duas poiscoes (ordenadas)
% ---------------------------------------------------------------------------------------

cria_ponte((X1, Y1), (X2, Y2), Ponte) :-
	X1 >= X2, Y1 >= Y2,
	Ponte = ponte((X2, Y2), (X1, Y1)).

cria_ponte((X1, Y1), (X2, Y2), Ponte) :-
	X1 =< X2, Y1 =< Y2,
	Ponte = ponte((X1, Y1), (X2, Y2)).

cria_ponte((X1, Y1), (X2, Y2), Ponte) :-
	X1 >= X2, Y1 =< Y2,
	Ponte = ponte((X2, Y1), (X1, Y2)).

cria_ponte((X1, Y1), (X2, Y2), Ponte) :-
	X1 =< X2, Y1 >= Y2,
	Ponte = ponte((X1, Y2), (X2, Y1)).



% ---------------------------------------------------------------------------------------
% 2.7: caminho_livre(Pos1, Pos2, Posicoes, I, Vz)
% Verifica se a adicao de uma ponte Pos1-Pos2 anula a vizinhanca de I e Vz
% ---------------------------------------------------------------------------------------

caminho_livre((X3, Y3), (X4, Y4), Posicoes, ilha(_, (X1, Y1)), ilha(_, (X2, Y2))) :-
	
	% Condicao em que Pos1 e Pos 2 sao I e Vz, onde e forcado um true pelo uso do 2==2
	(X3==X1, Y3==Y1, X4==X2, Y4==Y2); (X3==X2, Y3==Y2, X4==X1, Y4==Y1) -> 2==2;

	posicoes_entre((X1, Y1), (X2,Y2), Posicoes2),
	intersection(Posicoes, Posicoes2, Res),
	length(Res, Comp),
	Comp == 0.


% ---------------------------------------------------------------------------------------
% 2.8: actualiza_vizinhas_entrada(Pos1, Pos2, Posicoes, Entrada, Nova_Entrada)
% Remove as ilhas vizinhas da Entrada que o deixam de ser depois de ser criada uma ponte 
% ---------------------------------------------------------------------------------------

actualiza_vizinhas_entrada((X1, Y1), (X2, Y2), Posicoes, [ilha(N_L, (X3, Y3)), Vizinhas, Pontes], Nova_Entrada) :-

	% Este findall usa o predicado 2.6 para encontrar todas as ilhas vizinhas que ainda o sao depois de ser criada a ponte
	findall(X, (member(X, Vizinhas), caminho_livre((X1, Y1), (X2, Y2), Posicoes, ilha(_, (X3, Y3)), X)), NovasVizinhas),

	Nova_Entrada = [ilha(N_L, (X3, Y3)), NovasVizinhas, Pontes].



% ---------------------------------------------------------------------------------------------------
% 2.9: actualiza_vizinhas_apos_pontes(Estado, Pos1, Pos2, Novo_estado)
% Remove as ilhas vizinhas das entradas do Estado que o deixam de ser depois de ser criada uma ponte 
% ---------------------------------------------------------------------------------------------------

actualiza_vizinhas_apos_pontes(Estado, (X1, Y1), (X2, Y2), Novo_estado) :- actualiza_vizinhas_apos_pontes(Estado, (X1, Y1), (X2, Y2), [], Novo_estado).

actualiza_vizinhas_apos_pontes([], (_, _), (_, _), Novo_estado, Novo_estado).

actualiza_vizinhas_apos_pontes([Cab|Resto], (X1, Y1), (X2, Y2), Res, Novo_estado) :-
	posicoes_entre((X1, Y1), (X2, Y2), Posicoes),
	actualiza_vizinhas_entrada((X1, Y1), (X2, Y2), Posicoes, Cab, Nova_Entrada),
	append(Res, [Nova_Entrada], NovoRes),
	actualiza_vizinhas_apos_pontes(Resto, (X1, Y1), (X2, Y2), NovoRes, Novo_estado).



% ---------------------------------------------------------------------------------------------------
% 2.10: ilhas_terminadas(Estado, Ilhas_term)
% Remove as ilhas vizinhas das entradas do Estado que o deixam de ser depois de ser criada uma ponte 
% ---------------------------------------------------------------------------------------------------

ilhas_terminadas(Estado, Ilhas_term) :- ilhas_terminadas(Estado, [], Ilhas_term).

ilhas_terminadas([], Ilhas_term, Ilhas_term).

ilhas_terminadas([Cab|Resto], Res, Ilhas_term) :-
	[ilha(N_L, (X1, Y1)), _, X] = Cab,
	length(X, Comp),
	Comp == N_L, !,
	append(Res, [ilha(N_L, (X1, Y1))], NovoRes),
	ilhas_terminadas(Resto, NovoRes, Ilhas_term).

ilhas_terminadas([Cab|Resto], Res, Ilhas_term) :-
	[ilha(N_L, _), _, X] = Cab,
	length(X, Comp),
	Comp \== N_L, !,
	ilhas_terminadas(Resto, Res, Ilhas_term).


% ---------------------------------------------------------------------------------------------------
% 2.11: tira_ilhas_terminadas_entrada(Ilhas_term, Entrada, Nova_entrada)
% Remove as ilhas terminadas (Ilhas_term e uma lista delas) da lista de vizinhas na Entrada 
% ---------------------------------------------------------------------------------------------------

tira_ilhas_terminadas_entrada(Ilhas_term, [Ilha, Vizinhas, Vazia], Nova_entrada) :- 
	findall(X, (member(X, Vizinhas), \+ member(X, Ilhas_term)), NovasVizinhas),
	Nova_entrada = [Ilha, NovasVizinhas, Vazia]. 


% ---------------------------------------------------------------------------------------------------
% 2.12: tira_ilhas_terminadas(Estado, Ilhas_term, Novo_estado)
% Aplica o predicado anterior a cada uma das entradas do Estado
% ---------------------------------------------------------------------------------------------------

tira_ilhas_terminadas(Estado, Ilhas_term, Novo_estado) :-
	maplist(tira_ilhas_terminadas_entrada(Ilhas_term), Estado, Novo_estado).


% ---------------------------------------------------------------------------------------------------
% 2.13: marca_ilhas_terminadas_entrada(Ilhas_term, Entrada, Nova_entrada)
% Substitui N_L por 'X' se a ilha da Entrada pertencer a Ilhas_term
% ---------------------------------------------------------------------------------------------------

marca_ilhas_terminadas_entrada(Ilhas_term, [Ilha, Vizinhas, Pontes], Nova_entrada) :-
	Ilha = ilha(_, (X, Y)),
	member(Ilha, Ilhas_term),
	Nova_entrada = [ilha('X', (X, Y)), Vizinhas, Pontes].

marca_ilhas_terminadas_entrada(Ilhas_term, [Ilha, Vizinhas, Pontes], Nova_entrada) :-
	Ilha = ilha(N_L, (X, Y)),
	\+ member(Ilha, Ilhas_term),
	Nova_entrada = [ilha(N_L, (X, Y)), Vizinhas, Pontes].

% ---------------------------------------------------------------------------------------------------
% 2.14: marca_ilhas_terminadas(Estado, Ilhas_term, Novo_estado)
% Aplica o predicado anterior a cada uma das entradas do Estado
% ---------------------------------------------------------------------------------------------------

marca_ilhas_terminadas(Estado, Ilhas_term, Novo_estado) :-
	maplist(marca_ilhas_terminadas_entrada(Ilhas_term), Estado, Novo_estado).


% ---------------------------------------------------------------------------------------------------
% 2.15: trata_ilhas_terminadas(Estado, Novo_estado)
% Resultado de aplicar os predicados tira_ilhas_terminadas e marca_ilhas_terminadas ao Estado
% ---------------------------------------------------------------------------------------------------

trata_ilhas_terminadas(Estado, Novo_estado) :-

	% Uso do predicado 2.10 para saber quais as ilhas terminadas
	ilhas_terminadas(Estado, Ilhas_term),

	tira_ilhas_terminadas(Estado, Ilhas_term, PreNovoEstado),
	marca_ilhas_terminadas(PreNovoEstado, Ilhas_term, Novo_estado).


% ---------------------------------------------------------------------------------------------------
% 2.16: junta_pontes(Estado, Num_pontes, Ilha1, Ilha2, Novo_estado)
% Resultado de aplicar os predicados tira_ilhas_terminadas e marca_ilhas_terminadas ao Estado
% ---------------------------------------------------------------------------------------------------

junta_pontes(Estado, Num_pontes, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Novo_estado) :-
	cria_ponte((X1, Y1), (X2, Y2), Ponte),

	% Duplica a ponte do cria_ponte caso o Num_pontes seja 2
	(Num_pontes == 2 -> Pontes = [Ponte, Ponte]; Pontes = [Ponte]),

	% Utiliza o auxiliar abaixo para adicionar as pontes
	adiciona_pontes(Estado, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, EstadoComPontes),


	actualiza_vizinhas_apos_pontes(EstadoComPontes, (X1, Y1), (X2, Y2), QuaseNovoEstado),


	trata_ilhas_terminadas(QuaseNovoEstado, Novo_estado).



% Predicado auxiliar que adiciona a(s) ponte(s) as entradas da Ilha1 e Ilha2 no Estado

adiciona_pontes(Estado, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, NovoEstado) :- 
	adiciona_pontes(Estado, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, [], NovoEstado).

adiciona_pontes([], _, _, _, NovoEstado, NovoEstado).

adiciona_pontes([[ilha(N_L, (X, Y)), Vizinhas, _]|Resto], ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, Res, Novo_estado) :-
	N_L == N_L1,
	X == X1,
	Y == Y1,
	append(Res, [[ilha(N_L, (X, Y)), Vizinhas, Pontes]], NovoRes),
	adiciona_pontes(Resto, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, NovoRes, Novo_estado).


adiciona_pontes([[ilha(N_L, (X, Y)), Vizinhas, _]|Resto], ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, Res, Novo_estado) :-
	N_L == N_L2,
	X == X2,
	Y == Y2,
	append(Res, [[ilha(N_L, (X, Y)), Vizinhas, Pontes]], NovoRes),
	adiciona_pontes(Resto, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, NovoRes, Novo_estado).


adiciona_pontes([[ilha(N_L, (X, Y)), Vizinhas, Vazia]|Resto], ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, Res, Novo_estado) :-
	append(Res, [[ilha(N_L, (X, Y)), Vizinhas, Vazia]], NovoRes),
	adiciona_pontes(Resto, ilha(N_L1, (X1, Y1)), ilha(N_L2, (X2, Y2)), Pontes, NovoRes, Novo_estado).
