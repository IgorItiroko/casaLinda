import json
class Estoque:

    def incluirProduto(self, nome, desc, preco, qtde):
        with open("estoque.json") as file:
            data = json.load(file)
        list = [{"Nome": nome, "Desc": desc, "Preco": preco, "Cod": len(data) + 1,"Qtde": qtde}]
        data.append(list)
        with open("estoque.json","w") as file2:
            json.dump(data, file2, indent=4)
bob = Estoque()
bob.incluirProduto("Alho", "para comer", 10.0, 5)




    

