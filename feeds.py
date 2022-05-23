import json

class Feed:
    def exibirMaisVendidos(self, qtde):
        with open("estoque.json") as fileEstoque: 
            dataEstoque = json.load(fileEstoque)
        list = []
        max = 0
        if len(dataEstoque["Produtos"]) >= qtde:
            for _ in range(0, qtde):
                for index in range(0, len(dataEstoque["Produtos"])):
                    if dataEstoque["Produtos"][index]["Vendas"] >= max:
                        max = dataEstoque["Produtos"][index]["Vendas"]
                        maxid = index
                max = 0
                list.append(dataEstoque["Produtos"][maxid])
                dataEstoque["Produtos"].pop(maxid)  
            return list
        fraseErro = "Quantidade de produtos em exib. menor do que " + str(qtde)
        return (False, fraseErro)
        
    def faltaDeEstoque(self):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] == 0:
                list.append(dataEstoque["Produtos"][index])
        return list
bob = Feed()
print(bob.exibirMaisVendidos(8))