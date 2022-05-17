import json
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
    

bob = Estoque()
bob.excluirProduto(9)




    

