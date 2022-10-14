#-variaveis-#
colunas = 9
linhas = 9
dadosdosudoku =list ()
dictsudoku=dict()
cont = 0
#-----------#

#--lendo sudokou-#
file = open('sudoku_input.txt','r',encoding='utf-8')
for dados in file:
    dados = dados [:-1]
    dados = dados.split(';')
    for unidades  in dados :
        dadosdosudoku.append(unidades)
tamanho_matriz = len(dados)
    #dadosdosudoku = dadosdosudoku.split(',')#
#----------------#

#print(dadosdosudoku)

#--- sudoku in matriz ----#
for l in range(1,linhas+1):
    for c in range(1,colunas+1):
        dictsudoku['a'+str(l)+str(c)] = dadosdosudoku[cont]
        cont += 1
#-------------------------#
sub_matriz= list()
sub_matriz_vertical =list()
sub_matriz_horizontal =list()
sub_sudoku3x3 = list()
coluna = 0
linha = 0
respostaspossiveis = dict()
#----- colnetando colunas --------#
lista_elementos = dictsudoku.keys()        
for elemento in  dictsudoku:
    #print(elemento)
    sub_matriz.append(dictsudoku[elemento])
    if len(sub_matriz) == 9:
        tamanho= len(sub_matriz)
        for zero in dictsudoku:
            #print(zero,dictsudoku[zero])
           
            if dictsudoku[zero] == '0':
                #print('passando por 0')
                
                linha = str(zero[1])
                coluna = str(zero[2])
                #print('linha '+linha,' coluna '+coluna,zero)
                ###input()

                #!!!! mexer apenas daqui pra frente
                for resposta in range(1,tamanho_matriz+1):
                    resposta = str(resposta)
                    print(resposta)
                    
                    if not resposta in sub_matriz  :
                        #criar uma uma lista com todas respotas possiveis.


                        
                        #print(resposta,'resposta')
                        for horizontal_coluna in range(1,tamanho_matriz+1):
                            sub_elemento = 'a'+str(linha)+str(horizontal_coluna)
                            #print(sub_elemento,type(dictsudoku[sub_elemento]))
                            sub_matriz_horizontal.append(str(dictsudoku[sub_elemento]))

                        for vertical_linha  in range(1,tamanho+1):
                            sub_elemento = 'a'+str(vertical_linha)+str(coluna)
                            #print(sub_elemento,type(dictsudoku[sub_elemento]))
                            sub_matriz_vertical.append(str(dictsudoku[sub_elemento]))
                        #print(zero,type(zero),resposta)
                        #print(sub_matriz_horizontal,'horizontal')
                        #print(sub_matriz_vertical,'vertical')
                        #input('sa')
                        
                        if not resposta in sub_matriz_vertical and not resposta in sub_matriz_horizontal:
                            #print(zero+'passado') 
                            coluna = int(coluna)
                            linha = int(linha)
                            if coluna<=3:
                                iniciocoluna = 1
                                finalcoluna = 3
                            elif coluna>3 and coluna<=6:
                                iniciocoluna = 4
                                finalcoluna = 6
                            elif coluna >6:
                                iniciocoluna = 7
                                finalcoluna = 9
                            if linha <=3:
                                iniciolinha = 1
                                finallinha = 3
                            elif linha >3 and coluna <=6:
                                iniciolinha = 4
                                finallinha = 6
                            elif linha >6:
                                iniciolinha = 7
                                finallinha = 9
                            
                            for coluna_sub_sudoku in range(iniciocoluna,finalcoluna+1):
                                for linha_sub_sudoku in range(iniciolinha,finallinha+1):
                                    a = 'a'+str(linha_sub_sudoku)+str(coluna_sub_sudoku)
                                    sub_sudoku3x3.append(dictsudoku[a])
                                    #print(a)
                                    #input()
                                    ###input('sub')
                            if not resposta in sub_sudoku3x3:                                
                                print(zero,resposta,type(resposta))
                                print(sub_matriz_horizontal,'horizontal')
                                print(sub_matriz_vertical,'vertical')
                                print(sub_sudoku3x3,'3x3')
                                print('hi registrando resposta')
                                # registrar respostas
    
                                
                                
                                dictsudoku[zero] = str(resposta)
                                print(dictsudoku[zero],zero)
                                input()

                            #respostaspossiveis[fr'a{linha}{coluna}'] = fr'a{linha}{coluna}'.append(resposta)
                            #print(respostaspossiveis)
                            #auxiliar para para o for resposta#
                            
                    
                            sub_sudoku3x3 = list()
                        sub_matriz_horizontal = list()
                        sub_matriz_vertical = list()
                
        sub_matriz = list()

            
print(dictsudoku)
file = open('resultado.txt','w')
file.write(str(dictsudoku))
file.close()
input('i')
#passr linha depois colocar resposta
