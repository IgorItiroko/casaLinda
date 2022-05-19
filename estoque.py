import json
from tokenize import String
class Estoque:
    def incluirProduto(self, nome, desc, preco, qtde):
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        list = {"Nome": nome, "Desc": desc, "Preco": preco, "Cod": len(dataEstoque["Produtos"]) + 1,"Qtde": qtde}
        dataEstoque["Produtos"].append(list)
        with open("estoque.json","w") as file2:
            json.dump(dataEstoque, file2, indent=4)

    def excluirProduto(self, codProd):
        encontrado = 0
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Cod"] == codProd:
                encontrado = 1
                dataEstoque["Produtos"].pop(index)
                break 
        if encontrado == 1:
            with open("estoque.json","w") as file2:
                json.dump(dataEstoque, file2, indent=4)
            return True
        return False
        
    
    def pesquisarProdutoPorNome(self, nome):
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Nome"] == nome:
                list.append(dataEstoque["Produtos"][index])
        return list
        
    def pesquisarPorPrecoMax(self, precMax):
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] < precMax:
                list.append(dataEstoque["Produtos"][index])
        return list

    def pesquisarPorPrecoMin(self, precMin):
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] > precMin:
                list.append(dataEstoque["Produtos"][index])
        return list

    def faltaDeEstoque(self):
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] == 0:
                list.append(dataEstoque["Produtos"][index])
        return list

    def estoqueBaixo(self):
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] < 2:
                list.append(dataEstoque["Produtos"][index])
        return list

    def editarProduto(self, state, codProd, novoNome, novaDesc, novoPreco):
        encontrado = 0
        with open("estoque.json") as file:
            dataEstoque = json.load(file)
        with open("logs.json") as file2:
            dataLogs = json.load(file2)
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Cod"] == codProd:
                encontrado = 1
                dataEstoque["Produtos"][index]["Nome"] = novoNome
                dataEstoque["Produtos"][index]["Desc"] = novaDesc
                dataEstoque["Produtos"][index]["Preco"] = novoPreco
        newLog = {"Cod": codProd, "Novo_Nome": novoNome, "Nova_Desc": novaDesc, "Novo_Preco": novoPreco, "Autor_Alteracao": state}
        dataLogs["Alteracoes"].append(newLog)
        if encontrado == 1:
            with open("estoque.json","w") as file3:
                json.dump(dataEstoque, file3, indent=4)
            with open("logs.json","w") as file4:
                json.dump(dataLogs, file4, indent=4)
            return True
        return False




    

