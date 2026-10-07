import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Calculadora",
    page_icon="🧮",
    layout="centered"
)

precos_itens = {
    "Arroz (5kg)": 25.90,
    "Feijão (1kg)": 8.50,
    "Picanha (1kg)": 90.00,
    "Morango (250g)": 12.00,
    "Batata (1kg)": 7.00,
}


def calcular_preco_total(itens_selecionados):
    total = sum(precos_itens[item] for item in itens_selecionados)
    return total


itens_selecionados = st.multiselect(
    label="Selecione os itens do supermercado:",
    options=list(precos_itens.keys())
)

total_compra = calcular_preco_total(itens_selecionados)


if itens_selecionados:
    st.subheader("Itens Selecionados:")

    for item in itens_selecionados:
        st.write(f"- {item}: R$ {precos_itens[item]:.2f}")

    st.divider()

    st.metric(
        label="Total da Compra",
        value=f"R$ {total_compra:.2f}"
    )
else:
    st.info(
        "Nenhum item selecionado. Marque os produtos acima para ver o valor total."
    )


dinheiro = st.number_input(
    label="Insira o valor em dinheiro:",
    min_value=0.0,    
)


if itens_selecionados and dinheiro > 0:
    if dinheiro >= total_compra:
        troco = dinheiro - total_compra

        st.success(
            f"Compra realizada com sucesso! 🎉\n\n"
            f"Troco: **R$ {troco:.2f}**"
        )
    else:
        falta = total_compra - dinheiro

        st.error(
            f"Dinheiro insuficiente! ❌\n\n"
            f"Faltam **R$ {falta:.2f}**."
        )

