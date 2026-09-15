# cores no python

# ======================

# style : 

# 0 para nenhum estilo
# 1 para negrito
# 4 para para sublinhar
# 7 para inverter as cores


# =======================

# texto : 

# de 30 a 37 (cada um representa uma cor)

# 30 (branco)
# 31 (vermelho)
# 32 (verde)
# 33 (amarelo)
# 34 (azul)
# 35 (magenta)
# 36 (ciano)
# 37 (cinza)


# =======================

# back (cores de fundo)

# de 40 a 47

# 40 (branco)
# 41 (vermelho)
# 42 (verde)
# 43 (amarelo)
# 44 (azul)
# 45 (magenta)
# 46 (ciano)
# 47 (cinza)

# =================

# modo de escrita

# (\033[0;33;44m)
# 

# ==========================

# print('\033[4;31;42mteste\033')
 
nome = 'fulano'

cores = {
    'branco' : '\033[30m' , 
    'verrmelho' : '\033[31m' ,
    'verde' : '\033[32m' ,
    'amarelo' : '\033[33m' ,
    'azul' : '\033[34m' ,
    'pretoebranco' : '\033[7;30m'
}

print(f"olá prazer em te conhecer {cores['pretoebranco']}{nome}{'\033[m'}")
