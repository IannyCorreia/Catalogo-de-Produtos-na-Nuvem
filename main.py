import streamlit as st #biblioteca para desenhar componentes visuais (textos,botoes,caixas de upload etc)
from azure.storage.blob import BlobServiceClient
import os 
import pymssql #python microsoft sql, 
import uuid 
import json
from dotenv import load_dotenv 


load_dotenv()
blob_connection_string = os.getenv('BLOB_CONNECTION_STRING')
blob_container_name =  os.getenv('BLOB_CONTAINER_NAME')
blob_account_name = os.getenv('BLOB_ACCOUNT_NAME')

SQL_SERVER = os.getenv('SQL_SERVER')
SQL_DATABASE = os.getenv('SQL_DATABASE')    
SQL_USER = os.getenv('SQL_USER')
SQL_PASSWORD = os.getenv('SQL_PASSWORD')

#formulario de cadastro de produtos
st.title('Cadastro de Produtos')

product_name = st.text_input('Nome do Produto')
product_description = st.text_area('Descrição do Produto')
product_price = st.number_input('Preço do Produto', min_value=0.0, format="%.2f")
product_image = st.file_uploader('Imagem do Produto', type=['jpg', 'jpeg', 'png'])

def upload_blob(file):
    blob_service_client = BlobServiceClient.from_connection_string(blob_connection_string)
    container_client = blob_service_client.get_container_client(blob_container_name)
    blob_name = str(uuid.uuid4()) + file.name
    blob_client = container_client.get_blob_client(blob_name)
    blob_client.upload_blob(file.read(), overwrite=True)
    image_url = f"https://{blob_account_name}.blob.core.windows.net/{blob_container_name}/{blob_name}"
    return image_url

def insert_product(product_name, product_price, product_description, product_image):
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        comando_sql = "INSERT INTO Produtos (name, price, description, image_url) VALUES (%s, %d, %s, %s)"
        values=(product_name, product_price, product_description, product_image)
        cursor.execute(comando_sql, values)
        conn.commit()
        conn.close()
        return True
    
    except Exception as e:
        st.error(f"Erro ao inserir produto: {e}")
        return False

def list_products():
    try:
        conn = pymssql.connect(server=SQL_SERVER, user=SQL_USER, password=SQL_PASSWORD, database=SQL_DATABASE)
        cursor = conn.cursor()
        comando_sql = "SELECT name, price, description, image_url FROM Produtos"
        cursor.execute(comando_sql)
        products = cursor.fetchall()
        conn.close()
        return products
    
    except Exception as e:
        st.error(f"Erro ao listar produtos: {e}")
        return []

if st.button('Cadastrar Produto'):
    if product_name and product_price > 0 and product_image is not None:
        
        with st.spinner('Salvando produto...'):
            try:
                url_gerada = upload_blob(product_image)
                
                sucesso = insert_product(product_name, product_price, product_description, url_gerada)
                
                if sucesso:
                    st.toast('Produto cadastrado com sucesso!', icon='✅')
                    st.success('Tudo certo! Seu produto já está salvo.')
                else:
                    st.toast('Erro ao salvar no banco de dados.', icon='❌')
            
            except Exception as e:
                st.toast('Erro na comunicação com o Azure.', icon='⚠️')
                st.error(f"Detalhe do erro: {e}")
                
    else:
        st.toast('Atenção: Preencha todos os campos e anexe a imagem!', icon='⚠️')
        st.warning('Por favor, certifique-se de preencher o nome, preço e fazer o upload da imagem.')

st.divider() 
st.header('🛍️ Produtos Cadastrados (Vitrine)')

if st.button('Atualizar Vitrine'):
    produtos_salvos = list_products()
    
    if len(produtos_salvos) == 0:
        st.info("Nenhum produto cadastrado ainda. Seja o primeiro a cadastrar!")
    else:
        for produto in produtos_salvos:
            nome, preco, descricao, url_imagem = produto
            
            with st.container(border=True):
                col_foto, col_texto = st.columns([1, 2])
                
                with col_foto:
                    try:
                        st.image(url_imagem, use_container_width=True)
                    except:
                        st.error("Imagem indisponível")
                        
                with col_texto:
                    st.subheader(nome)
                    st.markdown(f"**Preço:** R$ {preco:,.2f}".replace(',', '_').replace('.', ',').replace('_', '.'))
                    st.write(descricao)