from tabulate import tabulate


class No:
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista
        self.anterior = None
        self.proximo = None


class Playlist:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.atual = None

    def adicionar_musica(self, titulo, artista):
        novo_no = No(titulo, artista)
        if self.inicio is None:
            self.inicio = novo_no
            self.fim = novo_no
            self.atual = novo_no
        else:
            self.fim.proximo = novo_no
            novo_no.anterior = self.fim
            self.fim = novo_no
        return f'Música "{titulo}" adicionada.'

    def remover_musica(self, titulo):
        if self.inicio is None:
            return 'Playlist vazia. Nenhuma música para remover.'

        no_atual = self.inicio
        while no_atual:
            if no_atual.titulo == titulo:
                if no_atual.anterior:
                    no_atual.anterior.proximo = no_atual.proximo
                else:
                    self.inicio = no_atual.proximo

                if no_atual.proximo:
                    no_atual.proximo.anterior = no_atual.anterior
                else:
                    self.fim = no_atual.anterior

                if self.atual == no_atual:
                    if no_atual.proximo:
                        self.atual = no_atual.proximo
                    elif no_atual.anterior:
                        self.atual = no_atual.anterior
                    else:
                        self.atual = None
                return f'Música "{titulo}" removida.'
            no_atual = no_atual.proximo
        return f'Música "{titulo}" não encontrada na playlist.'

    def avancar(self):
        if self.atual and self.atual.proximo:
            self.atual = self.atual.proximo
            return f'Tocando agora: {self.atual.titulo} - {self.atual.artista}'
        elif self.atual:
            return (
                f'Já está na última música: {self.atual.titulo} - {self.atual.artista}'
            )
        else:
            return 'Playlist vazia.'

    def retroceder(self):
        if self.atual and self.atual.anterior:
            self.atual = self.atual.anterior
            return f'Tocando agora: {self.atual.titulo} - {self.atual.artista}'
        elif self.atual:
            return f'Já está na primeira música: {self.atual.titulo} - {self.atual.artista}'
        else:
            return 'Playlist vazia.'

    def exibir_playlist(self):
        if self.inicio is None:
            return 'Playlist vazia.'

        headers = ['Título', 'Artista']
        table_data = []
        no_atual = self.inicio
        while no_atual:
            table_data.append([no_atual.titulo, no_atual.artista])
            no_atual = no_atual.proximo
        return tabulate(table_data, headers=headers, tablefmt='fancy_grid')

    def salvar_em_json(self, nome_arquivo='playlist.json'):
        import json

        if self.inicio is None:
            return 'Playlist vazia. Nada para salvar.'

        data = []
        no_atual = self.inicio
        while no_atual:
            data.append({'titulo': no_atual.titulo, 'artista': no_atual.artista})
            no_atual = no_atual.proximo

        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        return f'Playlist salva em {nome_arquivo}'

    def carregar_de_json(self, nome_arquivo='playlist.json'):
        import json

        try:
            with open(nome_arquivo, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.inicio = None
            self.fim = None
            self.atual = None

            for item in data:
                self.adicionar_musica(item['titulo'], item['artista'])
            return f'Playlist carregada de {nome_arquivo}'
        except FileNotFoundError:
            return f'Arquivo {nome_arquivo} não encontrado.'
        except json.JSONDecodeError:
            return f'Erro ao decodificar JSON do arquivo {nome_arquivo}.'
