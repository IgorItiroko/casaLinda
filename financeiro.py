import json
class Financeiro:
    def adicionarFinanceiro(self, cod_Produto, tipo, qtde, valor):
        encontrado = 0
        with open("financeiro.json") as fileFinanceiro:
            dataFinanceiro = json.load(fileFinanceiro)
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = {"Cod_Compra": len(dataFinanceiro["Registros"]) + 1, "Cod_Produto": cod_Produto, "CompraVenda": tipo,"Qtde": qtde, "Valor Uni": valor}
        dataFinanceiro["Registros"].append(list)
        for index in range(0, len(dataEstoque["Produtos"])):
            if(dataEstoque["Produtos"][index]["Cod"] == cod_Produto):
                encontrado = 1
                if(tipo == "C"):
                    dataEstoque["Produtos"][index]["Qtde"] += qtde
                else:
                    dataEstoque["Produtos"][index]["Qtde"] -= qtde
        if(encontrado == 1):
            with open("estoque.json","w") as file3:
                json.dump(dataEstoque, file3, indent=4)
            with open("financeiro.json","w") as file2:
                json.dump(dataFinanceiro, file2, indent=4)
            return True
        else: 
            return False
    

bob = Financeiro()
print(bob.adicionarFinanceiro(1,"C",10,444.3))



    

