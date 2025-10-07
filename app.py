from sobracarga import*
gerador = GeradorRelatorio()

titulo= input("Insira um titulo, caso n queira de um entrer: \n-->")
corpo=input("Insira um paragrafo: \n--->")
multi=int(input("Deseja inserir mais paragrafos? \nDigite: \n1-SIM \n2-NÃO \n--->"))


gerador.gerar(titulo= titulo, corpo=corpo, multi=multi)

