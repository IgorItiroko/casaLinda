import json
from tokenize import String
class Estoque:
    def incluirProduto(self, nome, desc, preco, qtde):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = {"Nome": nome, "Desc": desc, "Preco": preco, "Cod": len(dataEstoque["Produtos"]) + 1,"Qtde": qtde, "Vendas": 0}
        dataEstoque["Produtos"].append(list)
        with open("estoque.json","w") as fileOutEstoque:
            json.dump(dataEstoque, fileOutEstoque, indent=4)

    def excluirProduto(self, codProd):
        encontrado = 0
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Cod"] == codProd:
                encontrado = 1
                dataEstoque["Produtos"].pop(index)
                break 
        if encontrado == 1:
            with open("estoque.json","w") as fileOutEstoque:
                json.dump(dataEstoque, fileOutEstoque, indent=4)
            return True
        return False
        
    
    def pesquisarProdutoPorNome(self, nome):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Nome"] == nome:
                list.append(dataEstoque["Produtos"][index])
        return list
        
    def pesquisarPorPrecoMax(self, precMax):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] < precMax:
                list.append(dataEstoque["Produtos"][index])
        return list

    def pesquisarPorPrecoMin(self, precMin):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] > precMin:
                list.append(dataEstoque["Produtos"][index])
        return list

    def estoqueBaixo(self):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] < 2:
                list.append(dataEstoque["Produtos"][index])
        return list

    def editarProduto(self, estado, codProd, novoNome, novaDesc, novoPreco):
        encontrado = 0
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        with open("logs.json") as fileLogs:
            dataLogs = json.load(fileLogs)
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Cod"] == codProd:
                encontrado = 1
                dataEstoque["Produtos"][index]["Nome"] = novoNome
                dataEstoque["Produtos"][index]["Desc"] = novaDesc
                dataEstoque["Produtos"][index]["Preco"] = novoPreco
        novoLog = {"Cod_Produto": codProd, "Novo_Nome": novoNome, "Nova_Desc": novaDesc, "Novo_Preco": novoPreco, "Autor_Alteracao": estado}
        dataLogs["Alteracoes"].append(novoLog)
        if encontrado == 1:
            with open("estoque.json","w") as fileOutEstoque:
                json.dump(dataEstoque, fileOutEstoque, indent=4)
            with open("logs.json","w") as fileOutLogs:
                json.dump(dataLogs, fileOutLogs, indent=4)
            return True
        return False
bob = Estoque()
bob.incluirProduto("Mesa","Mesa da sala", 20, 145.99)





    

