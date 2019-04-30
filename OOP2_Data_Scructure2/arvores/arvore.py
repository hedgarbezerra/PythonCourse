

#       R     -- Raiz
#     E    D  -- Nós
#         E D -- Folhas
#
#
#       10      -- Raiz
#     5   15   -- Nós
#   4        16 -- Folha
# X 5 X 10 X 15 X 16 X
# 4 5 10 15 16

class Arvore():
    def __init__(self, raiz=None):
        self.__raiz = raiz

    @property
    def raiz(self):
        return self.__raiz

    # 9
    def inserir_elemento(self, no):
        no.no_direito = None
        no.no_esquerdo = None
        if(self.__raiz == None):
            self.__raiz = no
        else:
            self.__inserir(self.__raiz, no)


    #   7
    #       10
    #    9     12
    def __inserir(self, referencia, novo_no):
        if referencia.peso() < novo_no.peso():
            if referencia.no_direito == None:
                referencia.no_direito = novo_no
            else:
                self.__inserir(referencia.no_direito, novo_no)
        else:
            if referencia.no_esquerdo == None:
                referencia.no_esquerdo = novo_no
            else:
                self.__inserir(referencia.no_esquerdo, novo_no)

    def buscar(self, no_busca):
        return self.__buscar(self.__raiz, no_busca)

    def __buscar(self, referencia, no_busca):
        if referencia.valor == no_busca.valor:
            return referencia
        else:
            # Direita do nó
            if referencia.peso() < no_busca.peso():
                if referencia.no_direito == None:
                    raise ValueError("Elemento não encontrado")
                else:
                    print("Navegando pela direita do nó", referencia.valor.__str__())
                    return self.__buscar(referencia.no_direito, no_busca)
            else:
                # Esquerda do nó
                if referencia.no_esquerdo == None:
                    raise ValueError("Elemento não encontrado")
                else:
                    print("Navegando pela esquerda do nó", referencia.valor.__str__())
                    return self.__buscar(referencia.no_esquerdo, no_busca)

    def em_ordem(self):
        #ERD
        self.__em_ordem(self.__raiz)

    #       7
    #   6         10
    # 4       9      12
    #   5
    def __em_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__em_ordem(referencia.no_esquerdo)
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)
        else:
            print(referencia.valor.__str__())
            if referencia.no_direito != None:
                self.__em_ordem(referencia.no_direito)

    def pre_ordem(self):
        #RED
        self.__pre_ordem(self.__raiz)

    def __pre_ordem(self, referencia):
        print(referencia.valor.__str__())
        if referencia.no_esquerdo != None:
            self.__pre_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)
        else:
            if referencia.no_direito != None:
                self.__pre_ordem(referencia.no_direito)


    #       7
    #   6         10
    # 4       9      12
    #   5
    def pos_ordem(self):
        #EDR
        self.__pos_ordem(self.__raiz)

    def __pos_ordem(self, referencia):
        if referencia.no_esquerdo != None:
            self.__pos_ordem(referencia.no_esquerdo)
            if referencia.no_direito != None:
                self.__pos_ordem(referencia.no_direito)
            print(referencia.valor.__str__())
        else:
            if referencia.no_direito != None:
                self.__pos_ordem(referencia.no_direito)
                print(referencia.valor.__str__())
            else:
                print(referencia.valor.__str__())


    #       7
    #   6 h = 1         10
    # 4  h = 2     9      12
    #   5 h = 3

    def altura(self):
        return self.__altura(self.__raiz)

    def __altura(self, referencia):
        if referencia == None:
            return -1
        altura_esquerda = self.__altura(referencia.no_esquerdo)
        altura_direita = self.__altura(referencia.no_direito)
        return (altura_esquerda + 1) if altura_esquerda > altura_direita else (altura_direita + 1)

    def __str__(self):
        return "[(X)]" if self.__raiz == None else self.__raiz.__str__()
