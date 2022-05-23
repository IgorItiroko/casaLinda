import json
from tokenize import String
class Estoque:
    def abrirJson(self, arquivo):
        with open(arquivo) as file:
            return json.load(file)

    def fecharJson(self, arquivo, dados):
        with open(arquivo,"w") as file:
            json.dump(dados, file, indent=4)

    def incluirProduto(self, nome, desc, preco):
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
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Nome"].upper() == nome.upper():
                list.append(dataEstoque["Produtos"][index])
        return list
        
    def pesquisarPorPrecoMax(self, precMax):
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] < precMax:
                list.append(dataEstoque["Produtos"][index])
        return list

    def pesquisarPorPrecoMin(self, precMin):
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Preco"] > precMin:
                list.append(dataEstoque["Produtos"][index])
        return list

    def estoqueBaixo(self):
        dataEstoque = self.abrirJson("estoque.json")
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] < 2:
                list.append(dataEstoque["Produtos"][index])
        return list

    def editarProduto(self, estado, codProd, novoNome, novaDesc, novoPreco):
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
bob = Estoque()
bob.incluirProduto("Caneta","bla",10)




    

