class GeradorRelatorio:
    def gerar(self, titulo=None, *corpo, rodape=None, **metadados):
        if len(titulo) > 0:
            print(f"{titulo}\n")

        if len(corpo) > 0:
            for paragrafo in corpo:
                print(paragrafo)
            print()

        if rodape:
            print(f"{rodape}\n")
            print()

        if metadados:
            print("Metadados:")
            for chave, valor in metadados.items():
                print(f"{chave}: {valor}")
                print()
            print()

