import json
import time
class Financeiro:
    """
        *----------------------------------------*

        Funcoes de validacao de entrada de dados

        *----------------------------------------*
    """  
    def validaAdd(self, cod, tipo, qtde, valor):
        if tipo == "V" or tipo == "C":
            if isinstance(cod, int) and isinstance(qtde, int) and isinstance(valor,(int,float)):
                return True
            else:
                print("Valores fornecidos não são números")
        else:
            print("Tipo de transacao incompativel com compra ou venda")
        return False
    """
        *----------------------------------------*

        Funcao de adicionar operacoes na tabela
        do financeiro

        *----------------------------------------*
    """  
    def adicionarFinanceiro(self, codProd, tipo, qtde, valor):
        if not self.validaAdd(codProd, tipo, qtde, valor):
            return False
        encontrado = 0
        with open("financeiro.json") as fileFinanceiro:
            dataFinanceiro = json.load(fileFinanceiro)
        with open("estoque.json") as fileEstoque:
            dataEstoque = json.load(fileEstoque)
        try:
            list = {"Cod_Compra": dataFinanceiro["Registros"][len(dataFinanceiro["Registros"]) - 1]["Cod_Compra"] + 1, "Cod_Produto": codProd, "CompraVenda": tipo,"Qtde": qtde, "Valor_Uni": valor, "Data": str(time.localtime(). tm_mday) + "/" + str(time.localtime(). tm_mon) + "/" + str(time.localtime(). tm_year)}
            dataFinanceiro["Registros"].append(list)
        except:
            list = {"Cod_Compra": 1, "Cod_Produto": codProd, "CompraVenda": tipo,"Qtde": qtde, "Valor_Uni": valor, "Data": str(time.localtime(). tm_mday) + "/" + str(time.localtime(). tm_mon) + "/" + str(time.localtime(). tm_year)}
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
                        return False
        if(encontrado == 1):
            with open("estoque.json","w") as fileOutEstoque:
                json.dump(dataEstoque, fileOutEstoque, indent=4)
            with open("financeiro.json","w") as fileOutFinanceiro:
                json.dump(dataFinanceiro, fileOutFinanceiro, indent=4)
            return True
        else: 
            return False