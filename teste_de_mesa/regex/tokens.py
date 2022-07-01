# import tokenize

# with tokenize.open('regex/codigo.txt') as f:
#     tokens = tokenize.generate_tokens(f.readline)
    
#     for token in tokens:
#         print(f' idDadosTm:?  linha: {token[2][0]} variavel_o:? variavel_p: {token[1]}  dado_hexa:?  id_var:?  id_puso:?  id_cuso?   id_teste_mesa  cod_linha: {token[4]}')


import tokenize

from io import BytesIO

 

text = "teste = 1"

tokens = tokenize.tokenize(BytesIO(text.encode('utf-8')).readline)

for t in tokens:

    if t[0] == 63 or t[0] == 4 or t[0] == 0: continue
    else: print (t[1])