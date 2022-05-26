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
                produto = (
                            dataEstoque["Produtos"][maxid]["Cod"],
                            dataEstoque["Produtos"][maxid]["Nome"],
                            dataEstoque["Produtos"][maxid]["Desc"],
                            dataEstoque["Produtos"][maxid]["Preco"],
                            dataEstoque["Produtos"][maxid]["Qtde"],
                            dataEstoque["Produtos"][maxid]["Vendas"]
                        )
                list.append(produto)

                dataEstoque["Produtos"].pop(maxid)  
            return list
        return (False, "Quantidade de produtos registrados menor do que " + str(qtde))
    def faltaDeEstoque(self):
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = []
        for index in range(0, len(dataEstoque["Produtos"])):
            if dataEstoque["Produtos"][index]["Qtde"] == 0:
                list.append(dataEstoque["Produtos"][index])
        return list
bob = Feed()
print(bob.exibirMaisVendidos(20))