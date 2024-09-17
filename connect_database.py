import psycopg2
import os
from dotenv import load_dotenv
from contrato import Imovel

load_dotenv()

class PostgreClient():
    def __init__(self):
        self._envs = {
                "database": os.getenv("DATABASE"),
                "user": os.getenv("USERNAME"),
                "password": os.getenv("PASSWORD"), 
                "host": os.getenv("HOSTNAME"),
                "port": os.getenv("PORT")
            }
        print(self._envs["port"])

    def conect_database(self):
        
        self.connection = psycopg2.connect(database= self._envs["database"], user=self._envs["user"], 
                                    password=self._envs["password"], host= self._envs["host"], port= self._envs["port"])
        self.cursor = self.connection.cursor()
    
    def creat_table(self, database_table, columns: Imovel):
        self.conect_database()
        try:
            sql_create = f'''
                CREATE TABLE IF NOT EXISTS {database_table} (
                id SERIAL PRIMARY KEY, 
                {columns.preco} NUMERIC NOT NULL
                {columns.metragem} NUMERIC NOT NULL,
                {columns.quartos} VARCHAR(255) NOT NULL,
                {columns.bairro} VARCHAR(255) NOT NULL);
            '''
            self.cursor.execute(sql_create)
            print(f'Tabela {database_table} criada com sucesso')
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
        
    def insert_table(self, dataset_table, data: Imovel):
        try:
            insert_query = f'''INSERT INTO {dataset_table} (email, preco, metragem, quartos, bairro) VALUES (%s, %s, %s, %s, %s)'''
            self.cursor.execute(insert_query, (
                data.email,
                data.preco,
                data.metragem,
                data.quartos,
                data.bairro
            ))
            print('Dados inseridos com sucesso')
        except Exception as e:
            print(f'Erro ao salvar dados no banco {e}')

a = PostgreClient()
a.insert_table('buscas')