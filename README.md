#  Mini Projeto FATEC Playlist

Este projeto foi desenvolvido como parte do curso de Estrutura de Dados da FATEC Rio Claro. Ele simula um sistema de gerenciamento de playlists musicais com duas interfaces: uma web via Streamlit e outra via terminal (CLI). O objetivo é aplicar conceitos como listas duplamente ligadas, persistência com JSON e separação de responsabilidades.

---

##  Estrutura do Projeto

```
Mini_Projeto_FATEC_Playlist/
├── app.py                 # Interface web com Streamlit
├── main.py                # Interface de linha de comando (CLI)
├── playlist.py            # Lógica principal da playlist (classe Playlist e classe No)
├── playlist.json          # Armazena playlists criadas pelo usuário
├── musicas.json           # Catálogo estático de músicas
├── requirements.txt       # Dependências do projeto
└── README.md              # Documentação do projeto
```

---

##  Arquitetura em Camadas

- **Camada de Apresentação**  
  - `app.py`: Interface web com botões e inputs via Streamlit  
  - `main.py`: Interface CLI com menu interativo e entrada via terminal

- **Lógica de Negócio**  
  - `playlist.py`: Classe `Playlist` com métodos para adicionar, remover, navegar e salvar músicas

- **Estrutura de Dados**  
  - Classe `No`: Implementa a lista duplamente ligada com ponteiros `anterior` e `proximo`

- **Persistência**  
  - `playlist.json`: Playlist do usuário  
  - `musicas.json`: Catálogo de músicas disponíveis

---

##  Fluxo de Interação

```plaintext
Usuário → app.py ou main.py → Playlist() → No nodes → playlist.json
```

##  Requisitos

- Python 3.10+
- Bibliotecas externas:
  - `streamlit==1.50.0`
  - `tabulate==0.9.0`

Instale com:

```bash
pip install -r requirements.txt
```

---

##  Como Executar

### Interface Web

```bash
streamlit run app.py
```

Acesse via navegador em `http://localhost:8501`

### Interface Terminal

```bash
python main.py
```
