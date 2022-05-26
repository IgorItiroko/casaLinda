from ast import Str
import json
from tokenize import String
class Estoque:
    """
        *----------------------------------------*

        Funcoes para manipulacao do arquivo JSON

        *----------------------------------------*
    """
    def abrirJson(self, arquivo):
        with open(arquivo) as file:
            return json.load(file)

    def fecharJson(self, arquivo, dados):
        with open(arquivo,"w") as file:
            json.dump(dados, file, indent=4)

    """
        *----------------------------------------*

        Monta tuplas, referenciando o arquivo Json
        como parametro preenche uma tupla para ser
        usada no KivyMD

        *----------------------------------------*
    """

    def montaTupla(self, data, index):
        produto = (
                            data["Produtos"][index]["Cod"],
                            data["Produtos"][index]["Nome"],
                            data["Produtos"][index]["Desc"],
                            data["Produtos"][index]["Preco"],
                            data["Produtos"][index]["Qtde"]
                        )
        return produto
        
    def validarInclusao(self, nome, desc, preco):
        if isinstance(nome, str) and isinstance(desc, str):
            if isinstance(preco, (int, float)):
                if nome != "" and desc != "":
                    return True
        return False
        
    def incluirProduto(self, nome, desc, preco):
        if not self.validarInclusao(nome, desc, preco):
            return False
        verifElemento=0
        dataEstoque = self.abrirJson("estoque.json")
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Nome"].upper() == nome.upper():
                if dataEstoque["Produtos"][index]["Desc"].upper() == desc.upper():
                    verifElemento=1
                    break
        if verifElemento == 0:
            list = {"Cod": dataEstoque["Produtos"][len(dataEstoque["Produtos"]) - 1]["Cod"] + 1, "Nome": nome, "Desc": desc, "Preco": preco, "Qtde": 0, "Vendas": 0}
            dataEstoque["Produtos"].append(list)
            self.fecharJson("estoque.json",dataEstoque)
        else:
            print("Elemento já adicionado")

    def excluirProduto(self, codProd):
        encontrado = 0
        dataEstoque = self.abrirJson("estoque.json")
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Cod"] == codProd:
                encontrado = 1
                dataEstoque["Produtos"].pop(index)
                break 
        if encontrado == 1:
            self.fecharJson("estoque.json", dataEstoque)
            return True
        return False
        
    
    def pesquisarProdutoPorNome(self, nome):
        if not isinstance(nome,str):
            return False
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Nome"].upper() == nome.upper():
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list
        
    def pesquisarPorPrecoMax(self, precMax):
        if not isinstance(precMax, (int, float)):
            return False
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] <= precMax:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list

    def pesquisarPorPrecoMin(self, precMin):
        if not isinstance(precMin, (int, float)):
            return False
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] >= precMin:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list

    def pesquisarPorNomePrecoMinMax(self, nome, precMin, precMax):
        if not (isinstance(precMax, (int, float)) and isinstance(precMin, (int, float)) and isinstance(nome, str)):
            return (False, "parametro passado errado")
        if precMin > precMax:
            return (False, "valor minimo maior que o maximo")
            
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] >= precMin and dataEstoque["Produtos"][index]["Nome"] == nome and dataEstoque["Produtos"][index]["Preco"] <= precMax:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list

    def pesquisarPorNomePrecoMin(self, nome, precMin):
        if not (isinstance(precMin, (int, float)) and isinstance(nome, str)):
            return False
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] >= precMin and dataEstoque["Produtos"][index]["Nome"] == nome:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list

    def pesquisarPorNomePrecoMax(self, nome, precMax):
        if not (isinstance(precMax, (int, float)) and  isinstance(nome, str)):
            return False
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] <= precMax and dataEstoque["Produtos"][index]["Nome"] == nome:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list
    
    def pesquisarPorPrecoMinMax(self, precMin, precMax):
        if not (isinstance(precMax, (int, float)) and isinstance(precMin, (int, float))):
            return False
        if precMin > precMax:
            return (False, "valor minimo maior que o maximo")
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] >= precMin and dataEstoque["Produtos"][index]["Preco"] <= precMax:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list

    def estoqueBaixo(self):
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] <= 2:
                list.append(self.montaTupla(dataEstoque, index))
        if not list:
            return (False,"Sem resultados para a pesquisa")
        return list

    def editarProduto(self, estado, codProd, novoNome, novaDesc, novoPreco):
        if not self.validarInclusao(novoNome, novaDesc, novoPreco):
            return False
        encontrado = 0
        dataEstoque = self.abrirJson("estoque.json")
        dataLogs = self.abrirJson("logs.json")
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Cod"] == codProd:
                encontrado = 1
                dataEstoque["Produtos"][index]["Nome"] = novoNome
                dataEstoque["Produtos"][index]["Desc"] = novaDesc
                dataEstoque["Produtos"][index]["Preco"] = novoPreco
        novoLog = {"Cod_Produto": codProd, "Novo_Nome": novoNome, "Nova_Desc": novaDesc, "Novo_Preco": novoPreco, "Autor_Alteracao": estado}
        dataLogs["Alteracoes"].append(novoLog)
        if encontrado == 1:
            self.fecharJson("estoque.json",dataEstoque)
            self.fecharJson("logs.json", dataLogs)
            return True
        return False





    

