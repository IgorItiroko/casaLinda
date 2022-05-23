import json

class Feed:
    def exibir5MaisVendidos(self):
        with open("estoque.json") as fileEstoque: 
            dataEstoque = json.load(fileEstoque)
        list = []
        max = 0
        if len(dataEstoque["Produtos"]) >= 5:
            for _ in range(0, 5):
                for index in range(0, len(dataEstoque["Produtos"])):
                    if dataEstoque["Produtos"][index]["Vendas"] >= max:
                        max = dataEstoque["Produtos"][index]["Vendas"]
                        maxid = index
                max = 0
                list.append(dataEstoque["Produtos"][maxid])
                dataEstoque["Produtos"].pop(maxid)  
            return list
        return (False, "Menos de 5 elementos")
        
    def faltaDeEstoque(self):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] == 0:
                list.append(dataEstoque["Produtos"][index])
        return list
bob = Feed()
print(bob.exibir5MaisVendidos())