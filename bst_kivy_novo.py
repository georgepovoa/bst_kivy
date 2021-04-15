
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup
import sqlite3
from kivy.core.window import Window
import pandas as pd
import sys
import os
import subprocess



from kivy.uix.popup import Popup

conn = sqlite3.connect("bst_db.db")
cursor = conn.cursor()



try:
    conn.execute("""CREATE TABLE contas(
id_contas INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
nome_titular TEXT NOT NULL,
num_conta TEXT NOT NULL,
tipo_conta TEXT NOT NULL,
agencia TEXT NOT NULL,
saldo TEXT NOT NULL
)
""")
except Exception as e:
    print(e)



try:
    conn.execute("""CREATE TABLE fluxo(
id_fluxo INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
num_conta TEXT NOT NULL,
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



def adicionar_conta_db(nome_titular,num_conta,tipo_conta,agencia):
    try:
        list_db = [nome_titular,num_conta,tipo_conta,agencia]
        conn.execute("INSERT INTO contas(nome_titular,num_conta,tipo_conta,agencia,saldo) VALUES(?,?,?,?,0)",list_db)
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




def adicionar_fluxo_db(num_conta,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento):
    try:
        list_db = [num_conta,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento]
        conn.execute("INSERT INTO fluxo(num_conta,tipo_conta,valor,data,categoria,descricao,observacao,contato,forma_de_pagamento) VALUES(?,?,?,?,?,?,?,?,?)",list_db)
        print(list_db," inserido no db")
    except Exception as e:
        print(e)



class ModernApp(App):
    def build(self):
        def selecionar_conta(instance):
            def escolha_conta(text):
                while "'" in text :
                    text = text.replace("'",'')
                text = text.split(",")

                print(text)



                conta.text = "{}\n{}\n{}".format(text[1],text[3],text[2])
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








        def arquivos_view(instance):
            try:
                df = pd.read_sql_query("SELECT * from fluxo", conn)

                df.to_excel(r'fluxo.xlsx', index=False)

                if sys.platform == "win32":
                    os.startfile('fluxo.xlsx')
                else:
                    opener = "open" if sys.platform == "darwin" else "xdg-open"
                    subprocess.call([opener, 'fluxo.xlsx'])
            except Exception as e:
                print(e)
        def cadastro_view(instance):
            def cadastrar_contas_view(instance):
                def enviar_cadastro_conta_btt_func(instance):
                    lista_para_db_conta = [nome_titular.text,num_conta.text,tipo_conta.text,agencia.text]
                    adicionar_conta_db(nome_titular.text,num_conta.text,tipo_conta.text,agencia.text)
                parte_conteudo.clear_widgets()
                cadastro_layout_tela_2 = GridLayout(cols = 4)
                #nome_titular
                #num_conta
                #tipo_conta
                #agencia
                lista_de_campos = ['nome_titular','num_conta','tipo_conta','agencia']
                for i in lista_de_campos:
                    cadastro_layout_tela_2.add_widget(Label(text=str(i)))
                    globals()[str(i)] = TextInput(multiline=False, write_tab=False)
                    cadastro_layout_tela_2.add_widget(globals()[str(i)])
                enviar_cadastro_conta_btt = Button(text="Enviar")
                enviar_cadastro_conta_btt.bind(on_release = enviar_cadastro_conta_btt_func)
                cadastro_layout_tela_2.add_widget(enviar_cadastro_conta_btt)
                parte_conteudo.add_widget(cadastro_layout_tela_2)

            def cadastrar_categorias_view(instance):
                def enviar_cadastro_categoria(instance):
                    lista_para_db_conta = [categoria_nome_cadastro.text]
                    adicionar_categoria_db(categoria_nome_cadastro.text)

                parte_conteudo.clear_widgets()
                cadastrar_categorias_layout = GridLayout(cols =2)
                cadastrar_categorias_layout.add_widget(Label(text = "Nome :"))
                categoria_nome_cadastro = TextInput(multiline=False, write_tab=False)
                cadastrar_categorias_layout.add_widget(categoria_nome_cadastro)
                categoria_nome_cadastro_btt = Button(text = "Enviar")
                categoria_nome_cadastro_btt.bind(on_release = enviar_cadastro_categoria)
                cadastrar_categorias_layout.add_widget(categoria_nome_cadastro_btt)

                parte_conteudo.add_widget(cadastrar_categorias_layout)

            def cadastrar_forma_pagamento_view(instance):
                def enviar_cadastro_forma_pagamento(instance):
                    lista_para_db_conta = [forma_pagamento_nome_cadastro.text]
                    adicionar_forma_pagamento_db(forma_pagamento_nome_cadastro.text)
                parte_conteudo.clear_widgets()
                cadastrar_forma_pagamento_layout = GridLayout(cols=2)
                cadastrar_forma_pagamento_layout.add_widget(Label(text="Nome :"))
                forma_pagamento_nome_cadastro = TextInput(multiline=False, write_tab=False)
                cadastrar_forma_pagamento_layout.add_widget(forma_pagamento_nome_cadastro)
                forma_pagamento_nome_cadastro_btt = Button(text="Enviar")
                forma_pagamento_nome_cadastro_btt.bind(on_release=enviar_cadastro_forma_pagamento)
                cadastrar_forma_pagamento_layout.add_widget(forma_pagamento_nome_cadastro_btt)

                parte_conteudo.add_widget(cadastrar_forma_pagamento_layout)




            parte_conteudo.clear_widgets()

            cadastro_layout_tela_1 = GridLayout(rows=3,spacing = 25)
            cadastrar_conta_btt = Button(text = "cadastrar Contas")
            cadastrar_conta_btt.bind(on_press = cadastrar_contas_view)

            cadastrar_categorias_btt = Button(text="Cadastrar Categorias")
            cadastrar_categorias_btt.bind(on_press = cadastrar_categorias_view)

            cadastrar_forma_pagamento_btt = Button(text="Cadastrar Formas de pagamento")
            cadastrar_forma_pagamento_btt.bind(on_press = cadastrar_forma_pagamento_view)



            cadastro_layout_tela_1.add_widget(cadastrar_conta_btt)
            cadastro_layout_tela_1.add_widget(cadastrar_categorias_btt)
            cadastro_layout_tela_1.add_widget(cadastrar_forma_pagamento_btt)

            parte_conteudo.add_widget(cadastro_layout_tela_1)


        def financeiro_view(instance):

            parte_conteudo.clear_widgets()
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

            lista_de_campos = ["valor", 'data', 'repeticao', 'descricao', 'contato', 'observacoes']
            # adicionar dinamicamente label e input
            for i in lista_de_campos:
                financeiro_view.add_widget(Label(text=str(i)))
                globals()[str(i)] = TextInput(multiline=False, write_tab=False)
                financeiro_view.add_widget(globals()[str(i)])

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
            valor.input_filter='float'

            parte_conteudo.add_widget(financeiro_view)

        def btt_test_func(instance):
            def adicionar_receita(instance):
                valor_value = valor.text
                data_value = data.text
                repeticao_value = repeticao.text
                descricao_value = descricao.text
                contato_value = contato.text
                observacoes_value = observacoes.text
                db_list = [valor_value, data_value, repeticao_value, descricao_value, contato_value,conta.text.split('\n')[1],categoria.text,forma_de_pagamento.text]

                print("RECEITA")



                adicionar_fluxo_db(conta.text.split('\n')[2].strip(),conta.text.split('\n')[1].strip(),valor_value,data_value,categoria.text,descricao.text,observacoes_value,contato.text,forma_de_pagamento.text)



            def adicionar_despesa(intance):
                valor_value = valor.text
                data_value = data.text
                repeticao_value = repeticao.text
                descricao_value = descricao.text
                contato_value = contato.text
                observacoes_value = observacoes.text

                try:
                    db_list = [float(valor_value) * -1, data_value, repeticao_value,
                                   descricao_value, contato_value,conta.text,categoria.text,forma_de_pagamento.text]

                    print("DESPESA")
                    print(db_list)
                except Exception as e:
                    print(e)


            valor_value = valor.text
            data_value = data.text

            repeticao_value = repeticao.text
            descricao_value = descricao.text
            contato_value = contato.text
            observacoes_value = observacoes.text
            db_list = [valor_value, data_value, repeticao_value, descricao_value, contato_value]
            tela_escolha = GridLayout(cols=2)

            tela_escolha_receita_btt = Button(text="receita")
            tela_escolha_receita_btt.bind(on_release=adicionar_receita)
            tela_escolha_despesa_btt = Button(text="despesa")
            tela_escolha_despesa_btt.bind(on_release=adicionar_despesa)
            tela_escolha.add_widget(tela_escolha_receita_btt)
            tela_escolha.add_widget(tela_escolha_despesa_btt)

            tela_escolher_popup = Popup(title="ENTRADA / SAIDA", content=tela_escolha)
            tela_escolher_popup.open()

        layout = GridLayout(cols=2,spacing=50)
        parte_conteudo = GridLayout(cols=1)

        menu = GridLayout(rows=4)
        btt_financeiro_menu = Button(text="Financeiro_view")
        btt_financeiro_menu.bind(on_release=financeiro_view)
        menu.add_widget(btt_financeiro_menu)

        cadastros_btt = Button(text="Cadastros ")
        cadastros_btt.bind(on_release = cadastro_view)
        # o que precisa cadastrar
        # conta
        # categoria
        # forma de pagamento
        # caso a forma de pagamento seja cartão crédito, e for receita, descontar valor do cartão

        menu.add_widget(cadastros_btt)

        menu.add_widget(Button(text="Resumo "))
        arquivos_btt = Button(text="Arquivos ")
        arquivos_btt.bind(on_release = arquivos_view)
        menu.add_widget(arquivos_btt)

        layout.add_widget(menu)
        layout.add_widget(parte_conteudo)

        # adicionar dinamicamente label e input

        return layout


if __name__ == '__main__':
    Window.maximize()
    ModernApp().run()


conn.commit()
conn.close()