import json
from tokenize import String
class Estoque:
    def incluirProduto(self, nome, desc, preco, qtde):
        with open("estoque.json") as file:
            data = json.load(file)
        list = {"Nome": nome, "Desc": desc, "Preco": preco, "Cod": len(data["Produtos"]) + 1,"Qtde": qtde}
        data["Produtos"].append(list)
        with open("estoque.json","w") as file2:
            json.dump(data, file2, indent=4)

    def excluirProduto(self, codProd):
        with open("estoque.json") as file:
            data = json.load(file)
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Cod"] == codProd:
                data["Produtos"].pop(index)
                break 
        with open("estoque.json","w") as file2:
            json.dump(data, file2, indent=4)
    
    def pesquisarProdutoPorNome(self, nome):
        with open("estoque.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Nome"] == nome:
                list.append(data["Produtos"][index])
        return list
        
    def pesquisarPorPrecoMax(self, precMax):
        with open("estoque.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Preco"] < precMax:
                list.append(data["Produtos"][index])
        return list

    def pesquisarPorPrecoMin(self, precMin):
        with open("estoque.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Preco"] > precMin:
                list.append(data["Produtos"][index])
        return list

    def faltaDeEstoque(self):
        with open("estoque.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Qtde"] == 0:
                list.append(data["Produtos"][index])
        return list

    def estoqueBaixo(self):
        with open("estoque.json") as file:
            data = json.load(file)
        list = []
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Qtde"] < 2:
                list.append(data["Produtos"][index])
        return list

    def editarProduto(self, codProd, novoNome, novaDesc, novoPreco):
        with open("estoque.json") as file:
            data = json.load(file)
        for index in range(0, len(data["Produtos"])):
            if data["Produtos"][index]["Cod"] == codProd:
                data["Produtos"][index]["Nome"] = novoNome
                data["Produtos"][index]["Desc"] = novaDesc
                data["Produtos"][index]["Preco"] = novoPreco
        with open("estoque.json","w") as file2:
            json.dump(data, file2, indent=4)




    

