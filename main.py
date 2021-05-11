import os
import sqlite3
import subprocess
import sys
from datetime import date
from datetime import timedelta

import pandas as pd
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.scrollview import ScrollView



conn = sqlite3.connect("bst_db.db")
cursor = conn.cursor()

hoje = date.today()
ano_hoje = str(hoje).split("-")[0]
mes_hoje = str(hoje).split("-")[1]
dia_hoje = str(hoje).split("-")[2]
print("hoje's date:", hoje)

futuro_range = hoje + pd.Timedelta("7 day")
print(futuro_range)



try:
    conn.execute("""CREATE TABLE contas(
id_contas INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome_titular TEXT NOT NULL,
num_conta TEXT NOT NULL,
tipo_conta TEXT NOT NULL,
agencia TEXT NOT NULL,
banco TEXT NOT NULL,
saldo TEXT NOT NULL
)
""")
except Exception as e:
    print(e)


try:
        conn.execute("""CREATE TABLE clientes(
    id_cliente INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome_cliente TEXT NOT NULL,
    telefone_cliente TEXT NOT NULL,
    email_cliente TEXT NOT NULL,
    endereco_cliente TEXT NOT NULL,
    bairro_cliente TEXT NOT NULL
    )
    """)
except Exception as e:
    print(e)

try:
        conn.execute("""CREATE TABLE fornecedores(
    id_fornecedor INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    nome_fornecedor TEXT NOT NULL,
    telefone_fornecedor TEXT NOT NULL,
    email_fornecedor TEXT NOT NULL,
    endereco_fornecedor TEXT NOT NULL,
    bairro_fornecedor TEXT NOT NULL
    )
    """)
except Exception as e:
    print(e)



try:
    conn.execute("""CREATE TABLE fluxo(
id_fluxo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
id_conta TEXT NOT NULL,
num_conta TEXT NOT NULL,
banco TEXT NOT NULL,
tipo_conta TEXT NOT NULL,
valor REAL NOT NULL,
data TEXT NOT NULL,
categoria TEXT NOT NULL,
descricao TEXT NOT NULL,
observacao TEXT ,
contato TEXT,
forma_de_pagamento TEXT,
saldo_da_conta REAL

)
""")
except Exception as e:
    print(e)




try:
    conn.execute("""CREATE TABLE categorias(
id_categorias INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome_categoria TEXT NOT NULL
)
""")
except Exception as e:
    print(e)




try:
    conn.execute("""CREATE TABLE formas_pagamento(
id_formas_pagamento INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome_forma_pagamento TEXT NOT NULL
)
""")
except Exception as e:
    print(e)

try:
    conn.execute("""CREATE TABLE futuro(
id_futuro INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
id_conta TEXT NOT NULL,
num_conta TEXT NOT NULL,
banco NOT NULL,
tipo_conta TEXT NOT NULL,
valor REAL NOT NULL,
data TEXT NOT NULL,
categoria TEXT NOT NULL,
descricao TEXT NOT NULL,
observacao TEXT ,
contato TEXT,
forma_de_pagamento TEXT
)
""")
except Exception as e:
    print(e)



def adicionar_conta_db(nome_titular,num_conta,tipo_conta,agencia,banco):
    try:
        list_db = [nome_titular,num_conta,tipo_conta,agencia,banco]
        conn.execute("INSERT INTO contas(nome_titular,num_conta,tipo_conta,agencia,banco,saldo) VALUES(?,?,?,?,?,0)",list_db)
        print(list_db," inserido no bd")
    except Exception as e:
        print(e)

def adicionar_cliente_db(nome_cliente,telefone_cliente,email_cliente,endereco_cliente,bairro_cliente):
    try:
        list_db = [nome_cliente,telefone_cliente,email_cliente,endereco_cliente,bairro_cliente]
        conn.execute("INSERT INTO clientes(nome_cliente,telefone_cliente,email_cliente,endereco_cliente,bairro_cliente) VALUES(?,?,?,?,?)",list_db)
        print(list_db," inserido no bd")
    except Exception as e:
        print(e)

def adicionar_fornecedor_db(nome_fornecedor,telefone_fornecedor,email_fornecedor,endereco_fornecedor,bairro_fornecedor):
    try:
        list_db = [nome_fornecedor,telefone_fornecedor,email_fornecedor,endereco_fornecedor,bairro_fornecedor]
        conn.execute("INSERT INTO fornecedores(nome_fornecedor,telefone_fornecedor,email_fornecedor,endereco_fornecedor,bairro_fornecedor) VALUES(?,?,?,?,?)",list_db)
        print(list_db," inserido no bd")
    except Exception as e:
        print(e)




def adicionar_categoria_db(nome_cadastro):
    try:
        list_db = [nome_cadastro]
        conn.execute("INSERT INTO categorias(nome_categoria) VALUES(?)",list_db)
        print(list_db," inserido no bd cadastro")
    except Exception as e:
        print(e)



def adicionar_forma_pagamento_db(nome_forma_pagamento):
    try:
        list_db = [nome_forma_pagamento]
        conn.execute("INSERT INTO formas_pagamento(nome_forma_pagamento) VALUES(?)",list_db)
        print(list_db," inserido no bd formas_pagamento")
    except Exception as e:
        print(e)




def adicionar_fluxo_db(id_conta,num_conta,banco,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento,saldo_da_conta):
    try:
        list_db = [id_conta,num_conta,banco,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento,saldo_da_conta]
        conn.execute("INSERT INTO fluxo(id_conta,num_conta,banco,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento,saldo_da_conta) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)",list_db)
        print(list_db," inserido no db")
    except Exception as e:
        print(e)


def adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento):
    try:
        list_db = [id_conta,num_conta,banco,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento]
        conn.execute("INSERT INTO futuro(id_conta,num_conta,banco,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento) VALUES(?,?,?,?,?,?,?,?,?,?,?)",list_db)
        print(list_db," inserido no db")
    except Exception as e:
        print(e)

class Bst_sistemaApp(App):
    def build(self):
        def fin_btt_func(instance):
            try:
                menu_direita.clear_widgets()
            except Exception as e:
                print(e)

            def selecionar_conta(instance):
                def escolha_conta(text):
                    while "'" in text :
                        text = text.replace("'",'')
                    text = text.replace("(",'')
                    text = text.split(",")

                    print(text)



                    conta.text = "{}\n{}\n{}\n{}\n{}".format(text[0],text[1],text[3],text[2],text[5])
                    selecionar_conta_view_popup.dismiss()

                selecionar_conta_view = GridLayout(cols=3)

                cursor.execute("SELECT * FROM contas")
                result_contas = cursor.fetchall()

                for i in result_contas:
                    btn = Button(text = str(i))
                    selecionar_conta_view.add_widget(btn)
                    btn.bind(on_release=lambda btn: escolha_conta(btn.text))

                selecionar_conta_view_popup = Popup(title="SELECIONAR CONTA",content = selecionar_conta_view)
                selecionar_conta_view_popup.open()

            def selecionar_categoria(instance):
                def escolha_categoria(text):
                    while "'" in text:
                        text = text.replace("'",'')
                    text = text.replace("(",'')
                    text = text.replace(")",'')
                    text = text.split(',')
                    categoria.text = text[1]
                    selecionar_categoria_view_popup.dismiss()

                selecionar_categoria_view = GridLayout(cols=2)

                cursor.execute("SELECT * FROM categorias")
                result_categorias = cursor.fetchall()

                for i in result_categorias:
                    btn = Button(text=str(i))
                    selecionar_categoria_view.add_widget(btn)
                    btn.bind(on_release=lambda btn: escolha_categoria(btn.text))

                selecionar_categoria_view_popup = Popup(title="SELECIONAR CONTA", content=selecionar_categoria_view)
                selecionar_categoria_view_popup.open()

            def selecionar_forma_pagamento(instance):
                def escolha_forma_pagamento(text):
                    while "'" in text :
                        text = text.replace("'",'')
                    text = text.replace(')','')
                    text = text.split(',')
                    forma_de_pagamento.text = text[1]
                    selecionar_forma_pagamento_view_popup.dismiss()

                selecionar_forma_pagamento_view = GridLayout(cols=2)

                cursor.execute("SELECT * FROM formas_pagamento")
                result_formas_pagamento = cursor.fetchall()

                for i in result_formas_pagamento:
                    btn = Button(text=str(i))
                    selecionar_forma_pagamento_view.add_widget(btn)
                    btn.bind(on_release=lambda btn: escolha_forma_pagamento(btn.text))

                selecionar_forma_pagamento_view_popup = Popup(title="SELECIONAR FORMA DE PAGAMENTO",content = selecionar_forma_pagamento_view)
                selecionar_forma_pagamento_view_popup.open()
            

            def financeiro_view(instance):
                def btt_test_func(instance):
                    def adicionar_receita(instance):
                        valor_value = valor.text
                        descricao_value = descricao.text
                        contato_value = contato.text
                        observacoes_value = observacoes.text

                        print("RECEITA")
                        id_conta = conta.text.split('\n')[0].strip()
                        num_conta = conta.text.split('\n')[3].strip()
                        tipo_conta =conta.text.split('\n')[2].strip()
                        banco = conta.text.split('\n')[4].strip()

                        data_value = "{}-{}-{}".format(ano.text,mes.text,dia.text)

                        if pd.Timestamp(data_value) > pd.Timestamp(str(hoje)):
                            if int(quantidade.text) <=1: 
                                adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip())
                            else:
                                for i in range(int(quantidade.text)):
                                    format_dias = "{} day".format(i*int(frequencia.text))
                                    data_value_rep = str(pd.Timestamp(data_value) + pd.Timedelta(format_dias)).split(' ')[0]
                                    print(data_value)
                                    adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value_rep,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip())
                                    


                        else:
                            if int(quantidade.text) <=1:
                                print("VAI PARA FLUXO")

                                cursor.execute("SELECT * FROM contas WHERE id_contas = ?",list(id_conta))
                                conta_atual = cursor.fetchone()
                                print(conta_atual)
                                saldo_atual = conta_atual[6]
                                saldo_novo = [float(saldo_atual) + float(valor_value)]
                                update_saldo = [saldo_novo[0],id_conta]


                                conn.execute("UPDATE contas SET saldo = ? WHERE id_contas = ?",update_saldo)
                            

                                print(tipo_conta)
                                adicionar_fluxo_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip(),float(saldo_novo[0]))
                                
                            else:
                                for i in range(int(quantidade.text)):
                                    format_dias = "{} day".format(i*int(frequencia.text))
                                    data_value_rep = str(pd.Timestamp(data_value) + pd.Timedelta(format_dias)).split(' ')[0]
                                    print(data_value)
                                    adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value_rep,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip())
                        tela_escolher_popup.dismiss()        




                    def adicionar_despesa(intance):
                        valor_value = float(valor.text)*-1
                        descricao_value = descricao.text
                        contato_value = contato.text
                        observacoes_value = observacoes.text
                        print("DESPESA")
                        id_conta = conta.text.split('\n')[0].strip()
                        num_conta = conta.text.split('\n')[3].strip()
                        tipo_conta =conta.text.split('\n')[2].strip()
                        banco = conta.text.split('\n')[4].strip()

                        data_value = "{}-{}-{}".format(ano.text,mes.text,dia.text)

                        if pd.Timestamp(data_value) > pd.Timestamp(str(hoje)):
                            if int(quantidade.text) <=1: 
                                print("VAI PARA FUTURO")

                                adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip())
                            else:
                                for i in range(int(quantidade.text)):
                                    format_dias = "{} day".format(i*int(frequencia.text))
                                    data_value_rep = str(pd.Timestamp(data_value) + pd.Timedelta(format_dias)).split(' ')[0]
                                    print(data_value)
                                    adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value_rep,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip())
                            
                                    


                        else:
                            if int(quantidade.text) <=1:
                                print("VAI PARA FLUXO")
                            
                            

                                cursor.execute("SELECT * FROM contas WHERE id_contas = ?",list(id_conta))
                                conta_atual = cursor.fetchone()
                                print(conta_atual)
                                saldo_atual = conta_atual[6]
                                saldo_novo = [float(saldo_atual) + float(valor_value)]
                                update_saldo = [saldo_novo[0],id_conta]



                                conn.execute("UPDATE contas SET saldo = ? WHERE id_contas = ?",update_saldo)
                            

                                print(tipo_conta)
                                adicionar_fluxo_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip(),float(saldo_novo[0]))
                            
                            else:
                                for i in range(int(quantidade.text)):
                                    format_dias = "{} day".format(i*int(frequencia.text))
                                    data_value_rep = str(pd.Timestamp(data_value) + pd.Timedelta(format_dias)).split(' ')[0]
                                    print(data_value)
                                    adicionar_futuro_db(id_conta,num_conta,banco,tipo_conta,valor_value,data_value_rep,categoria.text.strip(),descricao.text.strip(),observacoes_value,contato.text,forma_de_pagamento.text.strip())
                        tela_escolher_popup.dismiss()   




                    valor_value = valor.text
                    descricao_value = descricao.text
                    contato_value = contato.text
                    observacoes_value = observacoes.text
                    
                    tela_escolha = GridLayout(cols=2)

                    tela_escolha_receita_btt = Button(text="receita")
                    tela_escolha_receita_btt.bind(on_release=adicionar_receita)
                    tela_escolha_despesa_btt = Button(text="despesa")
                    tela_escolha_despesa_btt.bind(on_release=adicionar_despesa)
                    tela_escolha.add_widget(tela_escolha_receita_btt)
                    tela_escolha.add_widget(tela_escolha_despesa_btt)

                    tela_escolher_popup = Popup(title="ENTRADA / SAIDA", content=tela_escolha)
                    tela_escolher_popup.open()

                
                financeiro_view = GridLayout(cols=2)

                # valor
                # data
                # vencimento
                # repeticao
                # descrição
                # conta
                # categoria
                # contato
                # forma de pagamento
                # observações

                lista_de_campos = ["valor", 'descricao','contato', 'observacoes']

                financeiro_view.add_widget(Label(text = "valor"))
                valor = TextInput(multiline=False, write_tab=False)
                financeiro_view.add_widget(valor)

                financeiro_view.add_widget(Label(text = "descricao"))
                descricao = TextInput(multiline=False, write_tab=False)
                financeiro_view.add_widget(descricao)

                financeiro_view.add_widget(Label(text = "contato"))
                contato = TextInput(multiline=False, write_tab=False)
                financeiro_view.add_widget(contato)

                financeiro_view.add_widget(Label(text = "observacoes"))
                observacoes = TextInput(multiline=False, write_tab=False)
                financeiro_view.add_widget(observacoes)
                
                financeiro_view.add_widget(Label(text="data"))
                data_campo_input = GridLayout(cols=3)
                
                global ano,mes,dia
                ano = TextInput(text = str(ano_hoje),multiline=False, write_tab=False)
                mes = TextInput(text = str(mes_hoje),multiline=False, write_tab=False)
                dia = TextInput(text = str(dia_hoje),multiline=False, write_tab=False)
                data_campo_input.add_widget(dia)
                data_campo_input.add_widget(mes)
                data_campo_input.add_widget(ano)
                financeiro_view.add_widget(data_campo_input)
                financeiro_view.add_widget(Label(text="Repetição"))
                repeticao_campo_input = GridLayout(cols=4)
                global frequencia,quantidade
                
                
                frequencia = TextInput(text = '0',multiline=False, write_tab=False)
                quantidade= TextInput(text = '0',multiline=False, write_tab=False)
                repeticao_campo_input.add_widget(Label(text = "Frequencia"))
                repeticao_campo_input.add_widget(frequencia)

                repeticao_campo_input.add_widget(Label(text = "Quantidade"))
                repeticao_campo_input.add_widget(quantidade)
                financeiro_view.add_widget(repeticao_campo_input)


                

                

                financeiro_view.add_widget(Label(text="Conta"))
                global conta
                conta = Button(text = "Selecionar Conta")
                conta.bind(on_release =selecionar_conta )
                financeiro_view.add_widget(conta)

                financeiro_view.add_widget(Label(text="Categoria"))
                global categoria
                categoria = Button(text = "Selecionar Categorias")
                categoria.bind(on_release = selecionar_categoria)
                financeiro_view.add_widget(categoria)

                financeiro_view.add_widget(Label(text="Forma de pagamento"))
                global forma_de_pagamento
                forma_de_pagamento = Button(text = "Selecionar forma de pagamento")
                forma_de_pagamento.bind(on_release = selecionar_forma_pagamento)
                financeiro_view.add_widget(forma_de_pagamento)
                

                btt_teste = Button(text="Enviar para financeiro")
                btt_teste.bind(on_release=btt_test_func)
                financeiro_view.add_widget(btt_teste)

                financeiro_view_popup =Popup(title = "Fin view", content = financeiro_view)
                financeiro_view_popup.open()
                

            def cadastro_view(instance):
                def cadastrar_contas_view(instance):
                    def enviar_cadastro_conta_btt_func(instance):
                        lista_para_db_conta = [nome_titular.text,num_conta.text,tipo_conta.text,agencia.text,banco.text]
                        adicionar_conta_db(nome_titular.text,num_conta.text,tipo_conta.text,agencia.text,banco.text)
                    
                    cadastro_layout_tela_2 = GridLayout(cols = 4)
                    #nome_titular
                    #num_conta
                    #tipo_conta
                    #agencia
                    global lista_de_campos
                    lista_de_campos = ['nome_titular','num_conta','tipo_conta','agencia','banco']
                    cadastro_layout_tela_2.add_widget(Label(text = "Nome do Titular"))
                    nome_titular=TextInput(multiline=False, write_tab=False)
                    cadastro_layout_tela_2.add_widget(nome_titular)

                    cadastro_layout_tela_2.add_widget(Label(text = "Numero de conta"))
                    num_conta=TextInput(multiline=False, write_tab=False)
                    cadastro_layout_tela_2.add_widget(num_conta)

                    cadastro_layout_tela_2.add_widget(Label(text = "Tipo de conta"))
                    tipo_conta=TextInput(multiline=False, write_tab=False)
                    cadastro_layout_tela_2.add_widget(tipo_conta)

                    cadastro_layout_tela_2.add_widget(Label(text = "Agencia"))
                    agencia=TextInput(multiline=False, write_tab=False)
                    cadastro_layout_tela_2.add_widget(agencia)

                    cadastro_layout_tela_2.add_widget(Label(text = "Banco"))
                    banco=TextInput(multiline=False, write_tab=False)
                    cadastro_layout_tela_2.add_widget(banco)

                    
                    enviar_cadastro_conta_btt = Button(text="Enviar")
                    enviar_cadastro_conta_btt.bind(on_release = enviar_cadastro_conta_btt_func)
                    cadastro_layout_tela_2.add_widget(enviar_cadastro_conta_btt)
                    cadastro_contas_popup = Popup(title= "CONTAS", content = cadastro_layout_tela_2)
                    cadastro_contas_popup.open()
                    

                def cadastrar_categorias_view(instance):
                    def enviar_cadastro_categoria(instance):
                        lista_para_db_conta = [categoria_nome_cadastro.text]
                        adicionar_categoria_db(categoria_nome_cadastro.text)

                    
                    cadastrar_categorias_layout = GridLayout(cols =2)
                    cadastrar_categorias_layout.add_widget(Label(text = "Nome :"))
                    categoria_nome_cadastro = TextInput(multiline=False, write_tab=False)
                    cadastrar_categorias_layout.add_widget(categoria_nome_cadastro)
                    categoria_nome_cadastro_btt = Button(text = "Enviar")
                    categoria_nome_cadastro_btt.bind(on_release = enviar_cadastro_categoria)
                    cadastrar_categorias_layout.add_widget(categoria_nome_cadastro_btt)

                    cadastro_categoria_popup = Popup(title = "CONTAS",content = cadastrar_categorias_layout)
                    cadastro_categoria_popup.open()

                    

                def cadastrar_forma_pagamento_view(instance):
                    def enviar_cadastro_forma_pagamento(instance):
                        lista_para_db_conta = [forma_pagamento_nome_cadastro.text]
                        adicionar_forma_pagamento_db(forma_pagamento_nome_cadastro.text)
                    
                    cadastrar_forma_pagamento_layout = GridLayout(cols=2)
                    cadastrar_forma_pagamento_layout.add_widget(Label(text="Nome :"))
                    forma_pagamento_nome_cadastro = TextInput(multiline=False, write_tab=False)
                    cadastrar_forma_pagamento_layout.add_widget(forma_pagamento_nome_cadastro)
                    forma_pagamento_nome_cadastro_btt = Button(text="Enviar")
                    forma_pagamento_nome_cadastro_btt.bind(on_release=enviar_cadastro_forma_pagamento)
                    cadastrar_forma_pagamento_layout.add_widget(forma_pagamento_nome_cadastro_btt)

                    cadastro_forma_pag_popup = Popup(title = "Formas de Pagamento", content =cadastrar_forma_pagamento_layout )
                    cadastro_forma_pag_popup.open()


                def cadastrar_cliente_view(instance):
                    def enviar_cliente_db(instance):
                        nome_cliente = nome.text
                        telefone_cliente = telefone.text
                        email_cliente = email.text
                        endereco_cliente = endereco.text
                        bairro_cliente = bairro.text

                        list_bd = [nome_cliente,telefone_cliente,email_cliente,endereco_cliente,bairro_cliente]

                        adicionar_cliente_db(nome_cliente,telefone_cliente,email_cliente,endereco_cliente,bairro_cliente)
                        
                    cadastrar_cliente_layout = GridLayout(cols = 4)
                    lista_de_campos = ["nome", 'telefone', 'email', 'endereco','bairro']

                    cadastrar_cliente_layout.add_widget(Label(text = "nome"))
                    nome= TextInput(multiline=False, write_tab=False)
                    cadastrar_cliente_layout.add_widget(nome)

                    cadastrar_cliente_layout.add_widget(Label(text = "telefone"))
                    telefone= TextInput(multiline=False, write_tab=False)
                    cadastrar_cliente_layout.add_widget(telefone)

                    cadastrar_cliente_layout.add_widget(Label(text = "email"))
                    email= TextInput(multiline=False, write_tab=False)
                    cadastrar_cliente_layout.add_widget(email)

                    cadastrar_cliente_layout.add_widget(Label(text = "endereco"))
                    endereco= TextInput(multiline=False, write_tab=False)
                    cadastrar_cliente_layout.add_widget(endereco)

                    cadastrar_cliente_layout.add_widget(Label(text = "bairro"))
                    bairro= TextInput(multiline=False, write_tab=False)
                    cadastrar_cliente_layout.add_widget(bairro)


                    enviar_cliente_btt = Button(text = "Enviar")
                    enviar_cliente_btt.bind(on_release = enviar_cliente_db)
                    cadastrar_cliente_layout.add_widget(enviar_cliente_btt)

                    cadastrar_cliente_popup = Popup(title = "CLIENTES",content = cadastrar_cliente_layout)
                    cadastrar_cliente_popup.open()


                def cadastrar_fornecedor_view(instance):
                    def enviar_fornecedor_db(instance):
                        nome_fornecedor = nome.text
                        telefone_fornecedor = telefone.text
                        email_fornecedor = email.text
                        endereco_fornecedor = endereco.text
                        bairro_fornecedor = bairro.text

                        list_bd = [nome_fornecedor,telefone_fornecedor,email_fornecedor,endereco_fornecedor,bairro_fornecedor]

                        adicionar_fornecedor_db(nome_fornecedor,telefone_fornecedor,email_fornecedor,endereco_fornecedor,bairro_fornecedor)
                        
                    cadastrar_fornecedor_layout = GridLayout(cols = 4)
                    cadastrar_fornecedor_layout.add_widget(Label(text = "nome"))
                    nome= TextInput(multiline=False, write_tab=False)
                    cadastrar_fornecedor_layout.add_widget(nome)

                    cadastrar_fornecedor_layout.add_widget(Label(text = "telefone"))
                    telefone= TextInput(multiline=False, write_tab=False)
                    cadastrar_fornecedor_layout.add_widget(telefone)

                    cadastrar_fornecedor_layout.add_widget(Label(text = "email"))
                    email= TextInput(multiline=False, write_tab=False)
                    cadastrar_fornecedor_layout.add_widget(email)

                    cadastrar_fornecedor_layout.add_widget(Label(text = "endereco"))
                    endereco= TextInput(multiline=False, write_tab=False)
                    cadastrar_fornecedor_layout.add_widget(endereco)

                    cadastrar_fornecedor_layout.add_widget(Label(text = "bairro"))
                    bairro= TextInput(multiline=False, write_tab=False)
                    cadastrar_fornecedor_layout.add_widget(bairro)

                    enviar_fornecedor_btt = Button(text = "Enviar")
                    enviar_fornecedor_btt.bind(on_release = enviar_fornecedor_db)
                    cadastrar_fornecedor_layout.add_widget(enviar_fornecedor_btt)

                    cadastrar_fornecedores_popup = Popup(title = "fornecedores_",content = cadastrar_fornecedor_layout)
                    cadastrar_fornecedores_popup.open()





                

                cadastro_layout_tela_1 = GridLayout(rows=3,spacing = 25)

                cadastrar_conta_btt = Button(text = "cadastrar Contas")
                cadastrar_conta_btt.bind(on_press = cadastrar_contas_view)

                cadastrar_categorias_btt = Button(text="Cadastrar Categorias")
                cadastrar_categorias_btt.bind(on_press = cadastrar_categorias_view)

                cadastrar_forma_pagamento_btt = Button(text="Cadastrar Formas de pagamento")
                cadastrar_forma_pagamento_btt.bind(on_press = cadastrar_forma_pagamento_view)

                cadastrar_cliente = Button(text = "Cadastrar cliente")
                cadastrar_cliente.bind(on_release = cadastrar_cliente_view)



                cadastrar_fornecedor = Button(text = "Cadastrar fornecedor")
                cadastrar_fornecedor.bind(on_release = cadastrar_fornecedor_view)





                
                cadastro_layout_tela_1.add_widget(cadastrar_conta_btt)
                cadastro_layout_tela_1.add_widget(cadastrar_categorias_btt)
                cadastro_layout_tela_1.add_widget(cadastrar_forma_pagamento_btt)
                cadastro_layout_tela_1.add_widget(cadastrar_cliente)
                cadastro_layout_tela_1.add_widget(cadastrar_fornecedor)

                cadastro_popup = Popup(title = "CADASTROS",content = cadastro_layout_tela_1)
                cadastro_popup.open()
                

            def filtrar_func(instance):
                tb = next( (t for t in ToggleButton.get_widgets('filtro') if t.state=='down'), None)
                test = tb.text if tb else ''
                print(test)
                comeco_format_date = "{}-{}-{}".format(filtro_comeco_ano.text,filtro_comeco_mes.text,filtro_comeco_dia.text)
                fim_format_date = "{}-{}-{}".format(filtro_fim_ano.text,filtro_fim_mes.text,filtro_fim_dia.text)
                data_range_filter = pd.date_range(pd.Timestamp(comeco_format_date),pd.Timestamp(fim_format_date)-timedelta(days=1),freq='d')
                
                futuros_layout.clear_widgets()
                cursor.execute("SELECT * FROM futuro")
                futuros_result = cursor.fetchall()
                for i in futuros_result:
                    if test == "Contas a pagar":
                        if i[6] in data_range_filter and i[5]<0 :
                        
                        
                            i = str(i)
                            i=i.replace('(','')
                            i=i.replace(')','')
                            while "'" in i:
                                i=i.replace("'",'')
                            

                            split_i = i.split(",")

                            id = split_i[0]
                            banco = split_i[3]
                            tipo  = split_i[4]
                            valor = split_i[5]
                            data = split_i[6]
                            


                            
                            #futuros_btt_text = "{}".format()
                            #id,conta, tipo,valor
                            btn = Button(text="{} | {} | {} | {} | {} ".format(id,banco,tipo,valor,data), size_hint_y=None, height=40)
                            btn.bind(on_release=lambda btn: escolha_futuro(btn.text))
                            futuros_layout.add_widget(btn)
                        
                        else:
                            pass
                    if test == "Contas a receber":
                        if i[6] in data_range_filter and i[5]>0 :
                        
                        
                            i = str(i)
                            i=i.replace('(','')
                            i=i.replace(')','')
                            while "'" in i:
                                i=i.replace("'",'')
                            

                            split_i = i.split(",")

                            id = split_i[0]
                            banco = split_i[3]
                            tipo  = split_i[4]
                            valor = split_i[5]
                            data = split_i[6]
                            


                            
                            #futuros_btt_text = "{}".format()
                            #id,conta, tipo,valor
                            btn = Button(text="{} | {} | {} | {} | {} ".format(id,banco,tipo,valor,data), size_hint_y=None, height=40)
                            btn.bind(on_release=lambda btn: escolha_futuro(btn.text))
                            futuros_layout.add_widget(btn)
                        
                        else:
                            pass
                    if test != 'Contas a receber' and test != 'Contas a pagar' :
                        if i[6] in data_range_filter :
                    
                    
                            i = str(i)
                            i=i.replace('(','')
                            i=i.replace(')','')
                            while "'" in i:
                                i=i.replace("'",'')
                            

                            split_i = i.split(",")

                            id = split_i[0]
                            banco = split_i[3]
                            tipo  = split_i[4]
                            valor = split_i[5]
                            data = split_i[6]
                            


                            
                            #futuros_btt_text = "{}".format()
                            #id,conta, tipo,valor
                            btn = Button(text="{} | {} | {} | {} | {} ".format(id,banco,tipo,valor,data), size_hint_y=None, height=40)
                            btn.bind(on_release=lambda btn: escolha_futuro(btn.text))
                            futuros_layout.add_widget(btn)
                            
                        
                        else:
                            pass
                        


            def futuros_view_func(instance):
                    
                def escolha_futuro(text_futuros):
                    
                    def modificar_func(instance):
                        def enviar_mod_db(instance):
                            print(valor_modificar.text,data_modificar.text,categoria_modificar.text,descricao_modificar.text,observacao_modificar.text,forma_de_pagamento_modificar.text)
                        print(text_futuros)
                        print("Modificar func")
                        modificar_func_layout = GridLayout(cols=4)
                        lista_de_campos = ['valor_modificar','data_modificar','categoria_modificar','descricao_modificar','observacao_modificar','forma_de_pagamento_modificar']
                        for i in lista_de_campos:
                            modificar_func_layout.add_widget(Label(text=str(i)))
                            globals()[str(i)] = TextInput(multiline=False, write_tab=False)
                            modificar_func_layout.add_widget(globals()[str(i)])

                        enviar_modificacao_btt = Button(text = "Enviar modificação")
                        enviar_modificacao_btt.bind(on_release = enviar_mod_db)
                        modificar_func_layout.add_widget(enviar_modificacao_btt)
                        modificar_func_popup = Popup(title = "Modificar",content =modificar_func_layout )
                        modificar_func_popup.open()
                        

                    def cancelar_func(instance):
                        print(text_futuros)
                        print("cancelar func")
                        conn.execute("DELETE FROM futuro WHERE id_futuro = {}".format(text_futuros.split('|')[0]))
                    
                    def resolver_func(instance):
                        print(text_futuros)
                        print("resolver func")
                        
                        
                        id_conta_resolver = item_result_splited[1].strip()
                        num_conta_resolver = item_result_splited[2].strip()
                        banco_resolver = item_result_splited[3].strip()
                        tipo_conta_resolver = item_result_splited[4].strip()
                        valor_resolver = item_result_splited[5].strip()
                        data_resolver = item_result_splited[6].strip()
                        categoria_resolver = item_result_splited[7].strip()
                        descricao_resolver = item_result_splited[8].strip()
                        observacao_resolver = item_result_splited[9].strip()
                        contato_resolver = item_result_splited[10].strip()
                        forma_de_pagamento_resolver = item_result_splited[11].strip()
                        cursor.execute("SELECT * FROM contas WHERE id_contas = ?",list(id_conta_resolver))
                        conta_atual = cursor.fetchone()
                        saldo_atual = conta_atual[6]
                        saldo_novo = [float(saldo_atual) + float(valor_resolver)]
                        update_saldo = [saldo_novo[0],id_conta_resolver]

                        print(id_conta_resolver,num_conta_resolver,banco_resolver,tipo_conta_resolver,valor_resolver,data_resolver,categoria_resolver,descricao_resolver,observacao_resolver,contato_resolver,forma_de_pagamento_resolver,saldo_novo[0])
                        conn.execute("UPDATE contas SET saldo = ? WHERE id_contas = ?",update_saldo)
                        adicionar_fluxo_db(id_conta_resolver,num_conta_resolver,banco_resolver,tipo_conta_resolver,valor_resolver,data_resolver,categoria_resolver,descricao_resolver,observacao_resolver,contato_resolver,forma_de_pagamento_resolver,saldo_novo[0])
                        conn.execute("DELETE FROM futuro WHERE id_futuro = {}".format(text_futuros.split('|')[0]))
                        escolha_futuro_layout_popup.dismiss()

                    
                        
                    
                    
                    item = cursor.execute("SELECT * FROM futuro WHERE id_futuro = {}".format(text_futuros.split('|')[0]))
                    item_result =str( cursor.fetchone())
                    while "'" in item_result : 
                        item_result = item_result.replace("'",'')
                    
                    item_result_splited = item_result.split(',')
                    

                    escolha_futuro_layout = GridLayout(rows=4)
                    escolha_futuro_layout.add_widget(Label (text = str(item_result)))
                    modificar_futuros_btt = Button(text="Modificar")
                    modificar_futuros_btt.bind(on_release = modificar_func)
                    escolha_futuro_layout.add_widget(modificar_futuros_btt)

                    cancelar_futuro_btt = Button(text="Cancelar")
                    cancelar_futuro_btt.bind(on_release = cancelar_func)

                    escolha_futuro_layout.add_widget(cancelar_futuro_btt)

                    resolver_futuro_btt = Button(text = "Resolver")
                    resolver_futuro_btt.bind(on_release = resolver_func)
                    escolha_futuro_layout.add_widget(resolver_futuro_btt)

                    escolha_futuro_layout_popup = Popup(title=text_futuros.split(",")[0],content = escolha_futuro_layout)
                    escolha_futuro_layout_popup.open()
                

                futuros_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
                futuros_layout.bind(minimum_height=futuros_layout.setter('height'))



                filtro_view = GridLayout(cols = 8,size_hint_y = None,row_default_height=15)
                global filtro_comeco_ano,filtro_comeco_dia,filtro_comeco_mes,filtro_fim_dia,filtro_fim_mes,filtro_fim_ano
                filtro_view_linha_2 = GridLayout(cols =3,size_hint_y = None,row_default_height=15,spacing = 20)
                filtro_comeco_dia = TextInput()
                filtro_comeco_mes = TextInput()
                filtro_comeco_ano = TextInput()
                filtro_fim_dia = TextInput()
                filtro_fim_mes = TextInput()
                filtro_fim_ano = TextInput()
                

                filtro_view.add_widget(Label(text = "DE "))
                filtro_view.add_widget(filtro_comeco_dia)
                filtro_view.add_widget(filtro_comeco_mes)
                filtro_view.add_widget(filtro_comeco_ano)
                filtro_view.add_widget(Label(text = "ATE "))
                filtro_view.add_widget(filtro_fim_dia)
                filtro_view.add_widget(filtro_fim_mes)
                filtro_view.add_widget(filtro_fim_ano)


                contas_a_pagar = ToggleButton(text = "Contas a pagar",group = 'filtro')

                contas_a_receber = ToggleButton(text = "Contas a receber", group = "filtro")
                filtro_view_linha_2.add_widget(contas_a_pagar)
                filtro_view_linha_2.add_widget(contas_a_receber)

                filtro_view_btt = Button(text = "filtrar")
                

                filtro_view_btt.bind(on_release = filtrar_func)
                filtro_view_linha_2.add_widget(filtro_view_btt)


                futuros_layout.add_widget(filtro_view)
                futuros_layout.add_widget(filtro_view_linha_2)



                cursor.execute("SELECT * FROM futuro")
                futuros_result = cursor.fetchall()
                for i in futuros_result:
                    
                    
                    i = str(i)
                    i=i.replace('(','')
                    i=i.replace(')','')
                    while "'" in i:
                        i=i.replace("'",'')
                    

                    split_i = i.split(",")

                    id = split_i[0]
                    banco = split_i[3]
                    tipo  = split_i[4]
                    valor = split_i[5]
                    data = split_i[6]
                    


                    
                    #futuros_btt_text = "{}".format()
                    #id,conta, tipo,valor
                    btn = Button(text="{} | {} | {} | {} | {} ".format(id,banco,tipo,valor,data), size_hint_y=None, height=40)
                    btn.bind(on_release=lambda btn: escolha_futuro(btn.text))
                    futuros_layout.add_widget(btn)
                root = ScrollView(size_hint=(1, 1))
                root.add_widget(futuros_layout)

                futuros_layout_popup = Popup(content = root)
                futuros_layout_popup.open()
            
                
            
            def arquivos_view(instance):
                try:
                    df = pd.read_sql_query("SELECT * from fluxo", conn)

                    df.to_excel(r'fluxo.xlsx', index=False)

                    df_futuro = pd.read_sql_query("SELECT * from futuro", conn)
                    df_futuro.to_excel(r'futuro.xlsx', index=False)

                    df_contas = pd.read_sql_query("SELECT * from contas", conn)
                    df_contas.to_excel(r'contas.xlsx', index=False)

                    df_clientes = pd.read_sql_query("SELECT * from clientes", conn)
                    df_clientes.to_excel(r'clientes.xlsx', index=False)

                    df_fornecedores = pd.read_sql_query("SELECT * from fornecedores", conn)
                    df_fornecedores.to_excel(r'fornecedores.xlsx', index=False)


                    #if sys.platform == "win32":
                    #    os.startfile('fluxo.xlsx')
                    #else:
                    #    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    #    subprocess.call([opener, 'fluxo.xlsx'])
                except Exception as e:
                    print(e)
                
            def excluir_repeticao_view_func(instance):
                def excluir_rep_db(intance):
                    list_db_exc = [excluir_repeticao_input.text]

                    conn.execute("DELETE FROM futuro WHERE descricao = ?",list_db_exc)

                excluir_repeticao_layout= GridLayout(cols=2)
                excluir_repeticao_layout.add_widget(Label(text= "Qual a descrição da repetição ?"))
                global excluir_repeticao_input
                excluir_repeticao_input = TextInput()
                excluir_repeticao_btt = Button(text = "Excluir repetição")
                excluir_repeticao_btt.bind(on_release = excluir_rep_db)

                excluir_repeticao_layout.add_widget(excluir_repeticao_input)
                excluir_repeticao_layout.add_widget(excluir_repeticao_btt)

                excluir_repeticao_layout_popup = Popup(title = "ASLKJDJLASÇ", content = excluir_repeticao_layout)
                excluir_repeticao_layout_popup.open()
            
            def funcionarios_view_func(instance):
                def gerenciar_funcionarios_func(instance):
                    gerenciar_funcionarios_layout = GridLayout(cols = 4)
                    adicionar_funcionario_btt = Button(text = "Adicionar funcionário")
                    remover_funcionario_btt = Button(text = "Remover funcionário")
                    ajustar_funcionario_btt = Button(text = "Ajustar funcionário")
                    gerenciar_funcionarios_layout.add_widget(adicionar_funcionario_btt)
                    gerenciar_funcionarios_layout.add_widget(remover_funcionario_btt)
                    gerenciar_funcionarios_layout.add_widget(ajustar_funcionario_btt)

                    gerenciar_funcionarios_popup = Popup(title = "Gerenciar",content = gerenciar_funcionarios_layout)
                    gerenciar_funcionarios_popup.open()

                funcionarios_layout =GridLayout(rows=3,spacing = 25)
                gerenciar_funcionarios = Button(text= "Gerenciar funcionários")
                gerenciar_funcionarios.bind(on_release = gerenciar_funcionarios_func)
                resumo_de_funcionarios = Button(text= "Resumo de funcionários")
                alterar_cobrança = Button(text = "Alterar cobrança")

                funcionarios_layout.add_widget(gerenciar_funcionarios)
                funcionarios_layout.add_widget(resumo_de_funcionarios)
                funcionarios_layout.add_widget(alterar_cobrança)

            



                

            


            menu_financeiro = GridLayout(rows=6)
            
            btt_financeiro_menu_financeiro = Button(text="Financeiro_view")
            btt_financeiro_menu_financeiro.bind(on_release=financeiro_view)
            menu_financeiro.add_widget(btt_financeiro_menu_financeiro)

            cadastros_btt = Button(text="Cadastros ")
            cadastros_btt.bind(on_release = cadastro_view)
            # o que precisa cadastrar
            # conta
            # categoria
            # forma de pagamento
            # caso a forma de pagamento seja cartão crédito, e for receita, descontar valor do cartão

            menu_financeiro.add_widget(cadastros_btt)

            menu_financeiro.add_widget(Button(text="Resumo "))
            
            futuro_view_btt = Button(text="Futuros")
            futuro_view_btt.bind(on_release=futuros_view_func)
            menu_financeiro.add_widget(futuro_view_btt)
            
            arquivos_btt = Button(text="Arquivos ")
            arquivos_btt.bind(on_release = arquivos_view)
            menu_financeiro.add_widget(arquivos_btt)

            excluir_repeticao_view = Button(text="Excluir repetição")
            excluir_repeticao_view.bind(on_release = excluir_repeticao_view_func)
            menu_financeiro.add_widget(excluir_repeticao_view)

            funcionarios_view = Button(text="funcionário")
            funcionarios_view.bind(on_release = funcionarios_view_func)
            menu_financeiro.add_widget(funcionarios_view)

            menu_direita.add_widget(menu_financeiro)
            

        def estoque_btt_func(instance):
            try:
                def gerenciar_estoque_func(instance):
                    def adicionar_estoque_func(instance):
                        print(instance.text)

                    def pesquisar_estoque_func(instance):
                        print(instance.text)
                        
                    def remover_estoque_func(instance):
                        print(instance.text)
                        
                    def alterar_estoque_func(instance):
                        print(instance.text)
                    

                    gerenciar_estoque_layout = GridLayout(rows=2,spacing=25,padding=10)

                    
                    adicionar_estoque_btt = Button(text= "Adicionar")
                    adicionar_estoque_btt.bind(on_release = adicionar_estoque_func)

                    pesquisar_estoque_btt = Button(text= "Pesquisar")
                    pesquisar_estoque_btt.bind(on_release =pesquisar_estoque_func)

                    remover_estoque_btt = Button(text= "Remover")
                    remover_estoque_btt.bind(on_release = remover_estoque_func)
                    
                    alterar_estoque_btt = Button(text= "Alterar")
                    alterar_estoque_btt.bind(on_release = alterar_estoque_func)
                    
                    _estoque_btt = Button(text= "xxx")

                    _2_estoque_btt = Button(text= "xxx")

                    gerenciar_estoque_layout.add_widget(adicionar_estoque_btt)

                    gerenciar_estoque_layout.add_widget(pesquisar_estoque_btt)

                    gerenciar_estoque_layout.add_widget(remover_estoque_btt)

                    gerenciar_estoque_layout.add_widget(alterar_estoque_btt)

                    gerenciar_estoque_layout.add_widget(_estoque_btt)

                    gerenciar_estoque_layout.add_widget(_2_estoque_btt)

                    gerenciar_estoque_popup = Popup(title= "Gerenciar Estoque",content = gerenciar_estoque_layout)
                    gerenciar_estoque_popup.open()

                    




                    
                    


                    
                def ver_estoque_func(instance):

                    def ver_categoria_func(instance):
                        print(instance.text)
                        
                    def proximos_fim_func(instance):
                        print(instance.text)

                    def pesquisar_produto_func(instance):
                        print(instance.text)
                    ver_estoque_layout = GridLayout(rows = 2,spacing=25,padding=10)

                    ver_categoria_btt = Button(text = "Ver por categoria")
                    ver_categoria_btt.bind(on_release =ver_categoria_func)
                    ver_estoque_layout.add_widget(ver_categoria_btt)

                    proximos_do_fim_btt = Button(text = "Ver próximos de acabar")
                    proximos_do_fim_btt.bind(on_release =proximos_fim_func)
                    ver_estoque_layout.add_widget(proximos_do_fim_btt)
                    
                    pesquisar_produto_btt = Button(text = "Informações de produto")
                    pesquisar_produto_btt.bind(on_release =pesquisar_produto_func)
                    ver_estoque_layout.add_widget(pesquisar_produto_btt)

                    ver_estoque_popup = Popup(title = "VER ESTOQUE",content = ver_estoque_layout)
                    ver_estoque_popup.open()
                    

                    
                def etiquetas_func(instance):
                    def pelo_id_func(instance):
                        print(instance)
                        
                    def por_categoria_func(instance):
                        print(instance)
                        
                    def por_produto_func(instance):
                        print(instance)
                        
                    etiquetas_layout = GridLayout(rows = 2,spacing=25,padding=10)


                    pelo_id_btt = Button(text = "Imprimir pelo ID")
                    pelo_id_btt.bind(on_press = pelo_id_func)
                    etiquetas_layout.add_widget(pelo_id_btt)

                    por_categoria_btt = Button(text = "Pesquisar por categoria")
                    por_categoria_btt.bind(on_press =por_categoria_func )
                    etiquetas_layout.add_widget(por_categoria_btt)

                    por_produto_btt = Button(text = "Pesquisar por produto")
                    por_produto_btt.bind(on_press = por_produto_func)
                    etiquetas_layout.add_widget(por_produto_btt)

                    etiquetas_popup = Popup(title = "Etiquetas",content = etiquetas_layout)
                    etiquetas_popup.open()

                    

                    
                def cadastrar_estoque_func(instance):
                    def cadastrar_categoria_func(insntace):
                        print(instance)
                    def cadastrar_produto_func(insntace):
                        print(instance)
                    def cadastrar_fornecedor_func(insntace):
                        print(instance)
                    def cadastrar_unidade_func(insntace):
                        print(instance)
                    cadastrar_layout = GridLayout(rows = 2,spacing=25,padding=10)

                    cadastrar_categoria_btt = Button(text = "Categoria")
                    cadastrar_categoria_btt.bind(on_release=cadastrar_categoria_func)
                    cadastrar_layout.add_widget(cadastrar_categoria_btt)
                    
                    cadastrar_produto_btt = Button(text = "Produto")
                    cadastrar_produto_btt.bind(on_release=cadastrar_produto_func)
                    cadastrar_layout.add_widget(cadastrar_produto_btt)
                    
                    cadastrar_fornecedor_btt = Button(text = "Fornecedor")
                    cadastrar_fornecedor_btt.bind(on_release=cadastrar_fornecedor_func)
                    cadastrar_layout.add_widget(cadastrar_fornecedor_btt)
                    
                    cadastrar_unidade_btt = Button(text = "Unidade de Medida")
                    cadastrar_unidade_btt.bind(on_release=cadastrar_unidade_func)
                    cadastrar_layout.add_widget(cadastrar_unidade_btt)

                    cadastrar_popup = Popup(title = "Cadastrar",content =cadastrar_layout )
                    cadastrar_popup.open()

                    
                menu_direita.clear_widgets()
                estoque_layout = GridLayout(cols =3,spacing=45,padding=100)

                gerenciar_estoque_btt = Button(text = "Gerenciar estoque")
                gerenciar_estoque_btt.bind(on_release = gerenciar_estoque_func)
                estoque_layout.add_widget(gerenciar_estoque_btt)


                ver_estoque_btt = Button(text = "Ver estoque")
                ver_estoque_btt.bind(on_release = ver_estoque_func)
                estoque_layout.add_widget(ver_estoque_btt)

                etiquetas_btt = Button(text ="Etiquetas")
                etiquetas_btt.bind(on_press = etiquetas_func)
                estoque_layout.add_widget(etiquetas_btt)


                cadastro_estoque_btt = Button(text ="Cadastrar")
                cadastro_estoque_btt.bind(on_press = cadastrar_estoque_func)
                estoque_layout.add_widget(cadastro_estoque_btt)

                
                menu_direita.add_widget(estoque_layout)

                
                
                
            except Exception as e:
                print(e)

        def prod_btt_func(instance):
            try:
                menu_direita.clear_widgets()
            except Exception as e:
                print(e)

        def arquivos_btt_func(instance):
            try:
                menu_direita.clear_widgets()
            except Exception as e:
                print(e)
        
        layout_float = FloatLayout(size=(Window.width,Window.height))
        layout_grid = GridLayout(cols=2)

        layout_float.add_widget(layout_grid)

        side_menu = GridLayout(rows = 6,size_hint_x=None, width=150,spacing = 25)

        fin_btt = ToggleButton(text = "Financeiro", group = "menu_lateral")
        fin_btt.bind(on_release = fin_btt_func)
        side_menu.add_widget(fin_btt)

        estoque_btt = ToggleButton(text= "Estoque", group = "menu_lateral")
        estoque_btt.bind(on_release = estoque_btt_func)
        side_menu.add_widget(estoque_btt)
        

        prod_btt = ToggleButton(text= "Produção", group = "menu_lateral")
        prod_btt.bind(on_release = prod_btt_func)
        side_menu.add_widget(prod_btt)

        arquivos_btt = ToggleButton(text= "Arquivos", group = "menu_lateral")
        arquivos_btt.bind(on_release = arquivos_btt_func )
        side_menu.add_widget(arquivos_btt)

        menu_direita = GridLayout(cols = 3)

        layout_grid.add_widget(side_menu)
        layout_grid.add_widget(menu_direita)



        return layout_float
    
if __name__ == '__main__':
    Window.maximize()
    Bst_sistemaApp().run()

conn.commit()
