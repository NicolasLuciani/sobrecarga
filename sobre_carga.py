class GeradorRelatorio:
    def gerar(self, titulo=None, *corpo, rodape=None, **metadados):
        if titulo:
            print(f"{titulo}\n")

        if corpo:
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

relatorio = GeradorRelatorio()

relatorio.gerar("Filme-titulo\n-----------------------------------------------------------")

relatorio.gerar("Parágrafo 1\n-----------------------------------------------------------", "Parágrafo 2\n-----------------------------------------------------------", "Parágrao 3\n-----------------------------------------------------------", rodape="Se inscreva\n-----------------------------------------------------------")

relatorio.gerar(autor="Irmão", data="07/10/2025\n-----------------------------------------------------------")