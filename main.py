from playlist import Playlist


def main():
    playlist = Playlist()

    while True:
        print('\nPlaylist - Estrutura de Dados')
        print('==============================')
        print('1. Adicionar música')
        print('2. Remover música')
        print('3. Avançar')
        print('4. Retroceder')
        print('5. Exibir playlist')
        print('6. Salvar playlist (Desafio extra)')
        print('7. Carregar playlist (Desafio extra)')
        print('0. Sair')

        opcao = input('Escolha uma opção: ')

        match opcao:
            case '1':
                titulo = input('Título: ')
                artista = input('Artista: ')
                print(playlist.adicionar_musica(titulo, artista))
            case '2':
                titulo = input('Título da música a remover: ')
                print(playlist.remover_musica(titulo))
            case '3':
                print(playlist.avancar())
            case '4':
                print(playlist.retroceder())
            case '5':
                print('\nPlaylist Atual:')
                print(playlist.exibir_playlist())
            case '6':
                print(playlist.salvar_em_json())
            case '7':
                print(playlist.carregar_de_json())
            case '0':
                print('Saindo...')
                break
            case _:
                print('Opção inválida. Tente novamente.')


if __name__ == '__main__':
    main()
