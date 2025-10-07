class GeradorRelatorio:
    def gerar(self,titulo=0, corpo=0, rodape=0, paragrafo=0, multi=0, metadados={}):
        while True:
            
                if titulo == '':
                    print('')
                else:
                    print(titulo)
                    break
            
                    
                if not corpo :
                    print('')
                else:
                    if multi ==1:
                        for paragrafo in corpo:
                            print(corpo)
                    else:
                        print(paragrafo)
            
                if rodape == '':
                    print("rodape")
