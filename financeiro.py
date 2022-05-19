import json
class Financeiro:
    def adicionarFinanceiro(self, cod_Produto, tipo, qtde, valor):
        with open("financeiro.json") as fileFinanceiro:
            dataFinanceiro = json.load(fileFinanceiro)
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = {"Cod Compra": len(dataFinanceiro["Registros"]) + 1, "Cod Produto": cod_Produto, "CompraVenda": tipo,"Qtde": qtde, "Valor Uni": valor}
        dataFinanceiro["Registros"].append(list)
        for index in range(0, len(dataEstoque["Produtos"])):
            if(dataEstoque["Produtos"][index]["Cod"] == cod_Produto):
                    if(tipo == "C"):
                        dataEstoque["Produtos"][index]["Qtde"] += qtde
                    else:
                        dataEstoque["Produtos"][index]["Qtde"] -= qtde
        with open("estoque.json","w") as file3:
            json.dump(dataEstoque, file3, indent=4)
        with open("financeiro.json","w") as file2:
            json.dump(dataFinanceiro, file2, indent=4)
    

bob = Financeiro()
bob.adicionarFinanceiro(44,"C",443,444.3)



    

