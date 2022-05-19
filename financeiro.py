import json
class Financeiro:
    def adicionarFinanceiro(self, cod_Produto, tipo, qtde, valor):
        with open("financeiro.json") as file:
            data = json.load(file)
        list = {"Cod Compra": len(data["Registros"]) + 1, "Cod Produto": cod_Produto, "CompraVenda": tipo,"Qtde": qtde, "Valor Uni": valor}
        data["Registros"].append(list)
        with open("financeiro.json","w") as file2:
            json.dump(data, file2, indent=4)
    

bob = Financeiro()
bob.adicionarFinanceiro(44,"C",443,444.3)



    

