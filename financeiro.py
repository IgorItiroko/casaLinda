import json
class Financeiro:
    def validaAdd(self, cod, tipo, qtde, valor):
        if tipo == "V" or tipo == "C":
            if isinstance(cod, int) and isinstance(qtde, int):
                if isinstance(valor,int) or isinstance(valor,float):
                    return True
        return False

    def adicionarFinanceiro(self, codProd, tipo, qtde, valor):
        if not self.validaAdd(codProd, tipo, qtde, valor):
            return False
        encontrado = 0
        with open("financeiro.json") as fileFinanceiro:
            dataFinanceiro = json.load(fileFinanceiro)
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        list = {"Cod_Compra": dataFinanceiro["Registros"][len(dataFinanceiro["Registros"]) - 1]["Cod_Compra"] + 1, "codProd": codProd, "CompraVenda": tipo,"Qtde": qtde, "Valor Uni": valor}
        dataFinanceiro["Registros"].append(list)
        for index in range(0, len(dataEstoque["Produtos"])):
            if(dataEstoque["Produtos"][index]["Cod"] == codProd):
                encontrado = 1
                if(tipo == "C"):
                    dataEstoque["Produtos"][index]["Qtde"] += qtde
                else:
                    if (dataEstoque["Produtos"][index]["Qtde"] - qtde) > 0:
                        dataEstoque["Produtos"][index]["Qtde"] -= qtde
                        dataEstoque["Produtos"][index]["Vendas"] += qtde
                    else:
                        return (False,"Sem estoque")
        if(encontrado == 1):
            with open("estoque.json","w") as fileOutEstoque:
                json.dump(dataEstoque, fileOutEstoque, indent=4)
            with open("financeiro.json","w") as fileOutFinanceiro:
                json.dump(dataFinanceiro, fileOutFinanceiro, indent=4)
            return True
        else: 
            return (False,"Codigo invalido")
    

bob = Financeiro()
print(bob.adicionarFinanceiro(2,"V",3,145.00))

    

