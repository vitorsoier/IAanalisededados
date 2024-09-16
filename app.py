import streamlit as st
from contrato import Imovel
from pydantic import ValidationError

def main():
    options = ['Castelo', 'Ouro Preto', 'Palmares', 'Cidade Nova', 'Sion']

    st.title("Crawler imoveis aluguel")

    email = st.text_input("Entre com seu e-mail")
    preco = st.number_input("Entre com o valor do imovel", min_value= 0, max_value= 100000)
    metragem = st.number_input("Entre com a metragem do imovel", min_value= 0, max_value= 100000)
    quartos = st.radio("Selecione a quantidade de quartos", ['1+', '2+', '3+', '4+'])
    bairro = st.multiselect('Escolha o seu bairro', options = options)
    
    
    if st.button('Realizar busca', ): 
        try:
            pesquisa = Imovel(email =  email,
                                preco =  preco,
                                metragem =  metragem,
                                quartos =  quartos,
                                bairro =  bairro)
            st.write(pesquisa)
        except ValidationError as e:
            st.error(e)
        
if __name__ == "__main__":
    main()