from sobracarga import*
gerador = GeradorRelatorio()

titulo= input("Insira um titulo, caso n queira de um entrer: \n-->")
tupla=(titulo)
print(tupla)
corpo=input("Insira um paragrafo: \n--->")
multi=int(input("Deseja inserir mais paragrafos? \nDigite: \n1-SIM \n2-NÃO \n--->"))
rodape=input("Insira um rodape, caso n queira de um entrer: \n-->")
resp= int(input("Deseja inserir informaçoes como autor,data e versão? \nDigite: \n1-SIM \n2-NÃO \n--->"))

gerador.gerar(titulo, corpo, multi)

