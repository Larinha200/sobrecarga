class GeradorRelatorio:
    def gerar(self,titulo=, corpo=0, rodape=0, *paragrafo, multi=0, metadados={}):
        while True:
            
                if titulo == '':
                    print('')
                else:
                    print(titulo)

                lista = []
                if not corpo :
                    print('')
                else:
                    if multi ==1:
                        lista.append(paragrafo)
                        print(lista)  
                        break
                    else:
                        print(paragrafo)
                        break
                if rodape == '':
                    print("rodape")
                else:
                    print(rodape)
                
                

           
                
