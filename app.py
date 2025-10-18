import streamlit as st
import json
from playlist import Playlist

# Configuração da página
st.set_page_config(page_title="Playlist FATEC Rio Claro", page_icon="🎵", layout="wide")

# Inicializar a playlist no session_state
if "playlist" not in st.session_state:
    st.session_state.playlist = Playlist()

playlist = st.session_state.playlist

# Título principal
st.title("🎵 Playlist FATEC Rio Claro")
st.markdown("---")

# Layout em colunas
col1, col2 = st.columns([2, 3])

with col1:
    st.header("⚙️ Operações")

    # Adicionar música
    with st.expander("➕ Adicionar Música", expanded=True):
        titulo_add = st.text_input("Título da música:", key="titulo_add")
        artista_add = st.text_input("Artista ou banda:", key="artista_add")
        if st.button("Adicionar", type="primary", use_container_width=True):
            if titulo_add and artista_add:
                resultado = playlist.adicionar_musica(titulo_add, artista_add)
                st.success(resultado)
                st.rerun()
            else:
                st.error("Por favor, preencha todos os campos!")

    # Remover música
    with st.expander("❌ Remover Música"):
        titulo_rem = st.text_input("Título da música a remover:", key="titulo_rem")
        if st.button("Remover", type="secondary", use_container_width=True):
            if titulo_rem:
                resultado = playlist.remover_musica(titulo_rem)
                st.info(resultado)
                st.rerun()
            else:
                st.error("Por favor, informe o título da música!")

    # Navegação
    st.subheader("🎮 Controles de Navegação")
    col_nav1, col_nav2 = st.columns(2)
    with col_nav1:
        if st.button("⏮️ Retroceder", use_container_width=True):
            resultado = playlist.retroceder()
            st.info(resultado)
    with col_nav2:
        if st.button("⏭️ Avançar", use_container_width=True):
            resultado = playlist.avancar()
            st.info(resultado)

    # Desafio Extra: JSON
    st.subheader("💾 Persistência (Desafio Extra)")
    col_json1, col_json2 = st.columns(2)
    with col_json1:
        if st.button("💾 Salvar JSON", use_container_width=True):
            resultado = playlist.salvar_em_json()
            st.success(resultado)
    with col_json2:
        if st.button("📂 Carregar JSON", use_container_width=True):
            resultado = playlist.carregar_de_json()
            st.success(resultado)
            st.rerun()

with col2:
    st.header("📋 Playlist Atual")

    # Exibir música atual
    if playlist.atual:
        st.markdown(
            f"""
        <div style="background-color: #1e3a8a; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
            <h3 style="color: white; margin: 0;">🎵 Tocando Agora:</h3>
            <h2 style="color: #60a5fa; margin: 10px 0 5px 0;">{playlist.atual.titulo}</h2>
            <h4 style="color: #93c5fd; margin: 0;">🎤 {playlist.atual.artista}</h4>
        </div>
        """,
            unsafe_allow_html=True,
        )
    else:
        st.info("Nenhuma música tocando no momento.")

    # Exibir todas as músicas
    st.subheader("🎼 Todas as Músicas")

    if playlist.inicio is None:
        st.warning("A playlist está vazia. Adicione algumas músicas!")
    else:
        no_atual = playlist.inicio
        contador = 1
        while no_atual:
            # Destacar a música atual
            if no_atual == playlist.atual:
                st.markdown(
                    f"""
                <div style="background-color: #065f46; padding: 15px; border-radius: 8px; margin-bottom: 10px; border-left: 5px solid #10b981;">
                    <strong style="color: #10b981;">▶️ {contador}. {no_atual.titulo}</strong><br>
                    <span style="color: #6ee7b7;">🎤 {no_atual.artista}</span>
                </div>
                """,
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"""
                <div style="background-color: #1f2937; padding: 15px; border-radius: 8px; margin-bottom: 10px;">
                    <strong style="color: white;">{contador}. {no_atual.titulo}</strong><br>
                    <span style="color: #9ca3af;">🎤 {no_atual.artista}</span>
                </div>
                """,
                    unsafe_allow_html=True,
                )

            no_atual = no_atual.proximo
            contador += 1

# Rodapé
st.markdown("---")
st.markdown(
    """
<div style="text-align: center; color: #6b7280;">
    <p>Desenvolvido para FATEC Rio Claro - Estrutura de Dados</p>
    <p>Lista Duplamente Ligada com Interface Streamlit</p>
</div>
""",
    unsafe_allow_html=True,
)
