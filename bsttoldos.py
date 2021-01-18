from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.uix.checkbox import CheckBox
import calendar

import sqlite3
import math

dbcon_estoque = sqlite3.connect('estoque.db')
dbcon_cliente = sqlite3.connect('cliente.db')
dbcon_func = sqlite3.connect('func.db')
dbcon_fin = sqlite3.connect('fin.db')

c_estoque = dbcon_estoque.cursor()
c_cliente = dbcon_cliente.cursor()
c_func = dbcon_func.cursor()
c_fin = dbcon_fin.cursor()


class TutorialApp(App):
    def test_placeholder():
        pass
        # # ## ## ## ## ## ## ## ## ESTRUTURA DE MUDANÇA DE PAGINA # ## ## ## ## ## ## ## ## ##
        def orcamento(instance):
            try:
                layout.remove_widget(client_page) or layout.remove_widget(estoque_page) or layout.remove_widget(
                    clientes_page) or layout.remove_widget(func_page) or layout.remove_widget(
                    agenda_page) or layout.remove_widget(fin_page)
                layout.add_widget(orcpage)
            except:
                pass

        def estoque(instance):
            try:
                layout.remove_widget(client_page) or layout.remove_widget(orcpage) or layout.remove_widget(
                    clientes_page) or layout.remove_widget(func_page) or layout.remove_widget(
                    agenda_page) or layout.remove_widget(fin_page)
                layout.add_widget(estoque_page)
            except:
                pass

        def clientes(instance):
            try:
                layout.remove_widget(client_page) or layout.remove_widget(orcpage) or layout.remove_widget(
                    estoque_page) or layout.remove_widget(func_page) or layout.remove_widget(
                    agenda_page) or layout.remove_widget(fin_page)
                layout.add_widget(clientes_page)
            except:
                pass

        def func(instance):
            try:
                layout.remove_widget(client_page) or layout.remove_widget(orcpage) or layout.remove_widget(
                    estoque_page) or layout.remove_widget(clientes_page) or layout.remove_widget(
                    agenda_page) or layout.remove_widget(fin_page)
                layout.add_widget(func_page)
            except:
                pass

        def agenda(instance):
            try:
                layout.remove_widget(client_page) or layout.remove_widget(orcpage) or layout.remove_widget(
                    estoque_page) or layout.remove_widget(clientes_page) or layout.remove_widget(
                    func_page) or layout.remove_widget(fin_page)
                layout.add_widget(agenda_page)
            except:
                pass

        def fin(instance):
            try:
                layout.remove_widget(client_page) or layout.remove_widget(orcpage) or layout.remove_widget(
                    estoque_page) or layout.remove_widget(clientes_page) or layout.remove_widget(
                    func_page) or layout.remove_widget(agenda_page)
                layout.add_widget(fin_page)
            except:
                pass

        def on_checkbox_active(checkbox, value):
            if value:
                print('The checkbox', checkbox, 'is active')
            else:
                print('The checkbox', checkbox, 'is inactive')

        checkbox = CheckBox()
        checkbox.bind(active=on_checkbox_active)

        # # ## ## ## ## ## ## ## ## ESTRUTURA DE MUDANÇA DE PAGINA # ## ## ## ## ## ## ## ## ##

        # # ## ## ## ## ## # FRONT PAGE # ## ## ## ## ## ##
        layout = GridLayout(cols=2)

        menulayout = GridLayout(cols=1, spacing=[25, 25])

        # # ## ## ## ## ## ## ## ## button config # ## ## ## ## ## ## ## #
        b_orc = Button(text="Orçamento ", size_hint_x=None, width=350, background_color='white')
        b_orc.bind(on_press=orcamento)

        b_estoq = Button(text="Estoque", size_hint_x=None, width=350, background_color='white')
        b_estoq.bind(on_press=estoque)

        b_clientes = Button(text="Clientes", size_hint_x=None, width=350, background_color='white')
        b_clientes.bind(on_press=clientes)
        b_func = Button(text="Funcionários", size_hint_x=None, width=350, background_color='white')
        b_func.bind(on_press=func)
        b_agenda = Button(text="Agenda", size_hint_x=None, width=350, background_color='white')
        b_agenda.bind(on_press=agenda)
        b_fin = Button(text="Financeiro", size_hint_x=None, width=350, background_color='white')
        b_fin.bind(on_press=fin)

        # # ## ## ## ## ## ## ## ## button config # ## ## ## ## ## ## ## #

        # # ## ## ## ## ## ## ## ## Add Buttons # ## ## ## ## ## ## ## #

        menulayout.add_widget(b_orc)
        menulayout.add_widget(b_estoq)
        menulayout.add_widget(b_clientes)
        menulayout.add_widget(b_func)
        menulayout.add_widget(b_agenda)
        menulayout.add_widget(b_fin)
        # # ## ## ## ## ## ## ## ## Add Buttons # ## ## ## ## ## ## ## #

        # # ## ## ## ## ## ## ## ## # set 1st page # ## ## ## ## ## ## #
        layout.add_widget(menulayout)
        client_page = GridLayout(cols=1)
        client_page.add_widget(Label(text="info empresa"))
        layout.add_widget(client_page)

        # ## ## ## ## ## ## ## ## ## set 1st page # ## ## ## ## ## ## #

        # ## ## ## ## ## ## ## ## FRONT PAGE# ## ## ## ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## ORC PAGE# ## ## ## ## ## ## ## ## ## ## ## #
        def sumar(instance):
            global qnt_lona, sobra, total_lona, qnt_sarrafo, tam_sarrafo
            altura = float(altura_input.text)
            largura = float(largura_input.text)
            # metragem para lona
            for i in range(30):
                if i * 1.4 < altura:
                    pass
                else:
                    qnt_lona = i
                    sobra = round((i * 1.4) - altura, 2)
                    total_lona = round(largura * qnt_lona, 1)
                    print('quantas lonas: ' + str(qnt_lona))
                    print('quanto sobra por lona: ' + str(sobra))
                    print('metragem para o pedido de lona: ' + str(total_lona))
                    break
            # metragem para a vulcanização
            v_lar = round((largura * 4) + ((qnt_lona - 1) * largura), 2)
            v_alt = round(altura * 2, 2)
            v_total = round(v_alt + v_lar, 2)
            print('vulcanização necessária na vertical: ' + str(v_alt))
            print('vulcanização necessária na horizonta: ' + str(v_lar))
            print('vulcanização total: ' + str(v_total))
            #
            # # tubo e sarrafo
            # # preciso da metragem e quantidade
            #
            for i in range(3, 7):

                # menor que 6 metros
                if largura < 6 and i >= largura:
                    qnt_sarrafo = 1
                    tam_sarrafo = i
                    tam_sarrafo_conta = i
                    break
                elif largura > 6 and largura - 6 - i <= 0 and largura < 12:
                    qnt_sarrafo = 2
                    tam_sarrafo = [6, math.ceil(largura - 6)]
                    tam_sarrafo_conta = tam_sarrafo[0] + tam_sarrafo[1]
                    break
                elif largura > 12 and largura < 18 and largura - 12 - i <= 0:
                    qnt_sarrafo = 3
                    tam_sarrafo = [6, 6, math.ceil(largura - 12)]
                    tam_sarrafo_conta = tam_sarrafo[0] + tam_sarrafo[1] + tam_sarrafo[2]
                    break

            popup_orc = GridLayout(cols=2)
            popup_orc.add_widget(Label(text='quantas lonas: ' + str(qnt_lona)))
            popup_orc.add_widget(Label(text='quantas lonas: ' + str(qnt_lona)))
            popup_orc.add_widget(Label(text='quanto sobra por lona: ' + str(sobra)))
            popup_orc.add_widget(Label(text='metragem para o pedido de lona: ' + str(total_lona)))
            popup_orc.add_widget(Label(text='vulcanização necessária na vertical: ' + str(v_alt)))
            popup_orc.add_widget(Label(text='vulcanização necessária na horizonta: ' + str(v_lar)))
            popup_orc.add_widget(Label(text='vulcanização total: ' + str(v_total)))
            popup_orc.add_widget(Label(text='quantidade de sarrafos: ' + str(qnt_sarrafo)))

            popup_orc.add_widget(Label(text='quantidade de tubos: ' + str(qnt_sarrafo)))
            popup_orc.add_widget(Label(text='tamanho do tubos: ' + str(tam_sarrafo)))
            popup_orc.add_widget(
                Label(text='Preço Total: ' + str(round(altura * largura * float(preco_metro_input.text), 2)),
                      font_size=40))
            popup_orc.add_widget((Button(text="CONFIRMAR ORÇAMENTO")))
            popup_orc.add_widget((Button(text="EXCLUIR ORÇAMENTO")))
            popup_orc.add_widget((Button(text="ARQUIVAR ORÇAMENTO")))

            popup_window = Popup(title="Popup Window", content=popup_orc)

            popup_window.open()

        def refresh_list():
            clientes_page_content.clear_widgets()
            c_cliente.execute("SELECT * FROM clientes ORDER BY nome")
            cliente_db = c_cliente.fetchall()
            for i in cliente_db:
                for j in i:
                    clientes_page_content.add_widget(Label(text=str(j)))
            dbcon_cliente.commit()

        def refresh_list_estoque():
            estoque_tabela_content.clear_widgets()
            c_estoque.execute("SELECT * FROM estoque ORDER BY nome")
            estoque_db = c_estoque.fetchall()
            for i in estoque_db:
                for j in i:
                    estoque_tabela_content.add_widget(Label(text=str(j)))
            dbcon_estoque.commit()

        def refresh_list_func():
            func_page_content.clear_widgets()
            c_func.execute("SELECT * FROM func ORDER BY nome")
            func_db = c_func.fetchall()
            for i in func_db:
                for j in i:
                    func_page_content.add_widget(Label(text=str(j)))
            dbcon_func.commit()

        def refresh_list_fin():
            fin_page_content.clear_widgets()
            c_fin.execute("SELECT * FROM fin ORDER BY nome")
            fin_db = c_fin.fetchall()
            for i in fin_db:
                for j in i:
                    fin_page_content.add_widget(Label(text=str(j)))
                fin_page_content.add_widget(CheckBox())
            dbcon_fin.commit()

        def adicionar_popup_cliente(instance):
            def adicionar_cliente_adicionar(instance):
                adicionar_cliente_lista = [adicionar_nome_input.text, adicionar_telefone_input.text,
                                           adicionar_endereco_input.text, adicionar_email_input.text]
                print(adicionar_cliente_lista)
                c_cliente.execute("INSERT INTO clientes VALUES(?,?,?,?)", adicionar_cliente_lista)
                dbcon_cliente.commit()

                # c_cliente.execute("SELECT * FROM clientes")
                # print(c_cliente.fetchall())
                refresh_list()

            popup_adicionar_cliente = GridLayout(cols=4)

            popup_adicionar_cliente.add_widget(Label(text="NOME"))
            adicionar_nome_input = TextInput(multiline=False)
            popup_adicionar_cliente.add_widget(Label(text="TELEFONE"))
            adicionar_telefone_input = TextInput()
            popup_adicionar_cliente.add_widget(Label(text="ENDEREÇO"))
            adicionar_endereco_input = TextInput(multiline=False)
            popup_adicionar_cliente.add_widget(Label(text="EMAIL"))
            adicionar_email_input = TextInput()
            popup_adicionar_cliente.add_widget(adicionar_nome_input)
            popup_adicionar_cliente.add_widget(adicionar_telefone_input)
            popup_adicionar_cliente.add_widget(adicionar_endereco_input)
            popup_adicionar_cliente.add_widget(adicionar_email_input)
            adicionar_cliente = Button(text="adicionar")
            popup_adicionar_cliente.add_widget(adicionar_cliente)

            adicionar_cliente.bind(on_press=adicionar_cliente_adicionar)

            popup_adicionar_cliente_window = Popup(title="ADICIONAR_CLIENTE", content=popup_adicionar_cliente,size_hint=(None,None),size = (750,200))
            popup_adicionar_cliente_window.open()

        def adicionar_popup_estoque(instance):

            def adicionar_estoque(instance):
                adicionar_estoque_lista = [adicionar_nome_input_estoque.text, adicionar_quantidade_input_estoque.text,
                                           adicionar_preco_input_estoque.text, adicionar_obs_input_estoque.text]
                print(adicionar_estoque_lista)
                c_estoque.execute("INSERT INTO estoque VALUES(?,?,?,?)", adicionar_estoque_lista)
                dbcon_estoque.commit()
                refresh_list_estoque()

            popup_adicionar_estoque = GridLayout(cols=4)

            popup_adicionar_estoque.add_widget(Label(text="NOME"))
            adicionar_nome_input_estoque = TextInput()
            popup_adicionar_estoque.add_widget(Label(text="QUANTIDADE"))
            adicionar_quantidade_input_estoque = TextInput(multiline=False)
            popup_adicionar_estoque.add_widget(Label(text="PREÇO"))
            adicionar_preco_input_estoque = TextInput(multiline=False)
            popup_adicionar_estoque.add_widget(Label(text="OBSERVAÇÃO"))
            adicionar_obs_input_estoque = TextInput()

            popup_adicionar_estoque.add_widget(adicionar_nome_input_estoque)
            popup_adicionar_estoque.add_widget(adicionar_quantidade_input_estoque)
            popup_adicionar_estoque.add_widget(adicionar_preco_input_estoque)
            popup_adicionar_estoque.add_widget(adicionar_obs_input_estoque)

            adicionar_estoque_button = Button(text='adicionar')
            popup_adicionar_estoque.add_widget(adicionar_estoque_button)

            adicionar_estoque_button.bind(on_press=adicionar_estoque)

            popup_adicionar_estoque_window = Popup(title='adicionar_estoque', content=popup_adicionar_estoque,size_hint=(None,None),size = (750,200))
            popup_adicionar_estoque_window.open()

        def adicionar_popup_func(instance):
            def add_func(instance):
                add_func_list = [adicionar_func_input_nome.text, adicionar_func_input_funcao.text,
                                 adicionar_func_input_salario.text, adicionar_func_input_imposto.text,
                                 adicionar_func_input_comissao.text]

                c_func.execute("INSERT INTO func VALUES(?,?,?,?,?)", add_func_list)
                dbcon_func.commit()
                refresh_list_func()
                link_func_fin()

            popup_adicionar_func = GridLayout(cols=5)

            popup_adicionar_func.add_widget(Label(text="NOME"))
            adicionar_func_input_nome = TextInput(multiline=False)
            popup_adicionar_func.add_widget(Label(text="FUNÇÃO"))
            adicionar_func_input_funcao = TextInput()
            popup_adicionar_func.add_widget(Label(text="SALÁRIO"))
            adicionar_func_input_salario = TextInput(multiline=False)
            popup_adicionar_func.add_widget(Label(text="IMPOSTO"))
            adicionar_func_input_imposto = TextInput(multiline=False)
            popup_adicionar_func.add_widget(Label(text="COMISSÃO"))
            adicionar_func_input_comissao = TextInput(multiline=False)

            popup_adicionar_func.add_widget(adicionar_func_input_nome)
            popup_adicionar_func.add_widget(adicionar_func_input_funcao)
            popup_adicionar_func.add_widget(adicionar_func_input_salario)
            popup_adicionar_func.add_widget(adicionar_func_input_imposto)
            popup_adicionar_func.add_widget(adicionar_func_input_comissao)

            add_estoque_button = Button(text='ADICIONAR')
            popup_adicionar_func.add_widget(add_estoque_button)
            add_estoque_button.bind(on_press=add_func)

            popup_adicionar_func_window = Popup(title="ADICIONAR_FUNCIONARIO", content=popup_adicionar_func,size_hint=(None,None),size = (750,200))
            popup_adicionar_func_window.open()

        def adicionar_popup_fin(instance):
            def adicionar_fin(instance):
                add_fin_list = [adicionar_fin_input_nome.text, adicionar_fin_input_valor.text,
                                adicionar_fin_input_validade.text]

                c_fin.execute("INSERT INTO fin VALUES(?,?,?)", add_fin_list)
                dbcon_fin.commit()
                refresh_list_fin()
                link_func_fin()

            popup_adicionar_fin = GridLayout(cols=3)

            popup_adicionar_fin.add_widget(Label(text='NOME'))
            adicionar_fin_input_nome = TextInput(multiline=False)
            popup_adicionar_fin.add_widget(Label(text='VALOR'))
            adicionar_fin_input_valor = TextInput(multiline=False)
            popup_adicionar_fin.add_widget(Label(text='VALIDADE'))
            adicionar_fin_input_validade = TextInput(multiline=False)

            popup_adicionar_fin.add_widget(adicionar_fin_input_nome)
            popup_adicionar_fin.add_widget(adicionar_fin_input_valor)
            popup_adicionar_fin.add_widget(adicionar_fin_input_validade)

            popup_adicionar_fin_add_button = Button(text="ADICIONAR")
            popup_adicionar_fin_add_button.bind(on_press=adicionar_fin)
            popup_adicionar_fin.add_widget(popup_adicionar_fin_add_button)

            popup_adicionar_fin_window = Popup(title='ADICIONAR_FIN', content=popup_adicionar_fin,size_hint=(None,None),size = (750,200))
            popup_adicionar_fin_window.open()

        def estoque_excluir_popup(instance):
            def excluir_estoque(instance):
                excluir_nome_estoque = (estoque_excluir_popup_page_input.text)
                print(excluir_nome_estoque)
                c_estoque.execute("DELETE FROM estoque WHERE nome = ? ",[excluir_nome_estoque])
                dbcon_estoque.commit()
                refresh_list_estoque()

            estoque_excluir_popup_page = GridLayout(cols=3)

            estoque_excluir_popup_page.add_widget(Label(text="Nome"))
            estoque_excluir_popup_page_input = TextInput(multiline=False)
            estoque_excluir_popup_page_button = Button(text="Excluir")
            estoque_excluir_popup_page_button.bind(on_press=excluir_estoque)

            estoque_excluir_popup_page.add_widget(estoque_excluir_popup_page_input)
            estoque_excluir_popup_page.add_widget(estoque_excluir_popup_page_button)

            popup_estoque_excluir = Popup(title="excluir_estoque", content=estoque_excluir_popup_page,size_hint=(None,None),size=(500,100))
            popup_estoque_excluir.open()

        def cliente_excluir_popup(instance):
            def excluir_cliente(instance):
                excluir_nome_clientes = (cliente_excluir_popup_page_input.text)
                print(excluir_nome_clientes)
                c_cliente.execute("DELETE FROM clientes WHERE nome = ? ", [excluir_nome_clientes])
                dbcon_cliente.commit()
                refresh_list()

            cliente_excluir_popup_page = GridLayout(cols=3)

            cliente_excluir_popup_page.add_widget(Label(text="Nome"))
            cliente_excluir_popup_page_input = TextInput(multiline=False)
            cliente_excluir_popup_page_button = Button(text="Excluir")
            cliente_excluir_popup_page_button.bind(on_press=excluir_cliente)

            cliente_excluir_popup_page.add_widget(cliente_excluir_popup_page_input)
            cliente_excluir_popup_page.add_widget(cliente_excluir_popup_page_button)

            popup_cliente_excluir = Popup(title="excluir_cliente", content=cliente_excluir_popup_page,
                                              size_hint=(None, None), size=(500, 100))
            popup_cliente_excluir.open()
        def func_excluir_popup(instance):
            def excluir_func(instance):
                excluir_nome_func = str(func_excluir_popup_page_input.text)
                print(excluir_nome_func)
                c_func.execute("DELETE FROM func WHERE nome = ? ", [str(excluir_nome_func)])
                dbcon_func.commit()
                refresh_list_func()
                link_func_fin()

            func_excluir_popup_page = GridLayout(cols=3)

            func_excluir_popup_page.add_widget(Label(text="Nome"))
            func_excluir_popup_page_input = TextInput(multiline=False)
            func_excluir_popup_page_button = Button(text="Excluir")
            func_excluir_popup_page_button.bind(on_press=excluir_func)

            func_excluir_popup_page.add_widget(func_excluir_popup_page_input)
            func_excluir_popup_page.add_widget(func_excluir_popup_page_button)

            popup_func_excluir = Popup(title="excluir_func", content=func_excluir_popup_page,
                                              size_hint=(None, None), size=(500, 100))
            popup_func_excluir.open()

        def fin_excluir_popup(instance):
            def excluir_fin(instance):
                excluir_nome_fin = str(fin_excluir_popup_page_input.text)
                print(excluir_nome_fin)
                c_fin.execute("DELETE FROM fin WHERE nome = ? ", [str(excluir_nome_fin)])
                dbcon_fin.commit()
                refresh_list_fin()
                link_func_fin()

            fin_excluir_popup_page = GridLayout(cols=3)

            fin_excluir_popup_page.add_widget(Label(text="Nome"))
            fin_excluir_popup_page_input = TextInput(multiline=False)
            fin_excluir_popup_page_button = Button(text="Excluir")
            fin_excluir_popup_page_button.bind(on_press=excluir_fin)

            fin_excluir_popup_page.add_widget(fin_excluir_popup_page_input)
            fin_excluir_popup_page.add_widget(fin_excluir_popup_page_button)

            popup_fin_excluir = Popup(title="excluir_fin", content=fin_excluir_popup_page,
                                              size_hint=(None, None), size=(500, 100))
            popup_fin_excluir.open()
        def link_func_fin():
            fin_page_content.clear_widgets()
            c_fin.execute("SELECT * FROM fin ORDER BY nome")
            c_func.execute("SELECT * FROM func ORDER BY nome")
            fin_db = c_fin.fetchall()
            func_db = c_func.fetchall()
            for i in fin_db:
                for j in i:
                    fin_page_content.add_widget(Label(text=str(j)))
                fin_page_content.add_widget(CheckBox())
            for x in func_db:
                fin_page_content.add_widget(Label(text=str(x[0])))
                fin_page_content.add_widget(Label(text=str(x[2])))
                fin_page_content.add_widget(Label(text="Dia 12"))
                fin_page_content.add_widget(CheckBox())

            dbcon_fin.commit()
            dbcon_func.commit()

        def procurar_estoque(instance):
            def procurar_popup_resultado(instance):

                procurar_popup_resultado_page = GridLayout(cols=4)
                pesquisar_nome_estoque = [procurar_popup_estoque_input_nome.text]
                procurar_popup_resultado_page.add_widget(Label(text="nome"))
                procurar_popup_resultado_page.add_widget(Label(text="quantidade"))
                procurar_popup_resultado_page.add_widget(Label(text="preço"))
                procurar_popup_resultado_page.add_widget(Label(text="obs"))
                c_estoque.execute("SELECT * FROM estoque WHERE nome = ?",pesquisar_nome_estoque)
                pesquisa_estoque = c_estoque.fetchall()
                for i in pesquisa_estoque:
                    for j in i:
                        procurar_popup_resultado_page.add_widget(Label(text=str(j)))


                popup_procurar_resultado_page_window = Popup(title='Resultado',content =procurar_popup_resultado_page )
                popup_procurar_resultado_page_window.open()

            procurar_popup_estoque = GridLayout(cols = 4)

            procurar_popup_estoque.add_widget(Label(text="nome"))
            procurar_popup_estoque_input_nome = TextInput(multiline=False)
            procurar_popup_estoque.add_widget(procurar_popup_estoque_input_nome)

            procurar_popup_estoque_button = Button(text='procurar')
            procurar_popup_estoque_button.bind(on_press = procurar_popup_resultado)

            procurar_popup_estoque.add_widget(procurar_popup_estoque_button)
            popup_procurar_window = Popup(title='Pesquisa_estoque',content = procurar_popup_estoque)
            popup_procurar_window.open()

        def procurar_cliente(instance):
            def procurar_popup_resultado(instance):

                procurar_popup_resultado_page = GridLayout(cols=4)
                pesquisar_nome_cliente = [procurar_popup_cliente_input_nome.text]
                procurar_popup_resultado_page.add_widget(Label(text="nome"))
                procurar_popup_resultado_page.add_widget(Label(text="telefone"))
                procurar_popup_resultado_page.add_widget(Label(text="endereço"))
                procurar_popup_resultado_page.add_widget(Label(text="email"))
                c_cliente.execute("SELECT * FROM clientes WHERE nome = ?",pesquisar_nome_cliente)
                pesquisa_cliente = c_cliente.fetchall()
                for i in pesquisa_cliente:
                    for j in i:
                        procurar_popup_resultado_page.add_widget(Label(text=str(j)))


                popup_procurar_resultado_page_window = Popup(title='Resultado',content =procurar_popup_resultado_page )
                popup_procurar_resultado_page_window.open()

            procurar_popup_cliente = GridLayout(cols = 4)

            procurar_popup_cliente.add_widget(Label(text="nome"))
            procurar_popup_cliente_input_nome = TextInput(multiline=False)
            procurar_popup_cliente.add_widget(procurar_popup_cliente_input_nome)

            procurar_popup_cliente_button = Button(text='procurar')
            procurar_popup_cliente_button.bind(on_press = procurar_popup_resultado)

            procurar_popup_cliente.add_widget(procurar_popup_cliente_button)
            popup_procurar_window = Popup(title='Pesquisa_cliente',content = procurar_popup_cliente)
            popup_procurar_window.open()

        def procurar_func(instance):
            def procurar_popup_resultado(instance):

                procurar_popup_resultado_page = GridLayout(cols=5)
                pesquisar_nome_func = [procurar_popup_func_input_nome.text]
                procurar_popup_resultado_page.add_widget(Label(text="nome"))
                procurar_popup_resultado_page.add_widget(Label(text="função"))
                procurar_popup_resultado_page.add_widget(Label(text="salário"))
                procurar_popup_resultado_page.add_widget(Label(text="imposto"))
                procurar_popup_resultado_page.add_widget(Label(text="comissão"))
                c_func.execute("SELECT * FROM func WHERE nome = ?", pesquisar_nome_func)
                pesquisa_func = c_func.fetchall()
                for i in pesquisa_func:
                    for j in i:
                        procurar_popup_resultado_page.add_widget(Label(text=str(j)))

                popup_procurar_resultado_page_window = Popup(title='Resultado', content=procurar_popup_resultado_page)
                popup_procurar_resultado_page_window.open()

            procurar_popup_func = GridLayout(cols=4)

            procurar_popup_func.add_widget(Label(text="nome"))
            procurar_popup_func_input_nome = TextInput(multiline=False)
            procurar_popup_func.add_widget(procurar_popup_func_input_nome)

            procurar_popup_func_button = Button(text='procurar')
            procurar_popup_func_button.bind(on_press=procurar_popup_resultado)

            procurar_popup_func.add_widget(procurar_popup_func_button)
            popup_procurar_window = Popup(title='Pesquisa_func', content=procurar_popup_func)
            popup_procurar_window.open()

        def procurar_fin(instance):
            def procurar_popup_resultado(instance):

                procurar_popup_resultado_page = GridLayout(cols=3)
                pesquisar_nome_fin = [procurar_popup_fin_input_nome.text]
                procurar_popup_resultado_page.add_widget(Label(text="nome"))
                procurar_popup_resultado_page.add_widget(Label(text="valor"))
                procurar_popup_resultado_page.add_widget(Label(text="venciemnto"))

                c_fin.execute("SELECT * FROM fin WHERE nome = ?", pesquisar_nome_fin)
                pesquisa_fin = c_fin.fetchall()
                for i in pesquisa_fin:
                    for j in i:
                        procurar_popup_resultado_page.add_widget(Label(text=str(j)))

                popup_procurar_resultado_page_window = Popup(title='Resultado', content=procurar_popup_resultado_page)
                popup_procurar_resultado_page_window.open()

            procurar_popup_fin = GridLayout(cols=4)

            procurar_popup_fin.add_widget(Label(text="nome"))
            procurar_popup_fin_input_nome = TextInput(multiline=False)
            procurar_popup_fin.add_widget(procurar_popup_fin_input_nome)

            procurar_popup_fin_button = Button(text='procurar')
            procurar_popup_fin_button.bind(on_press=procurar_popup_resultado)

            procurar_popup_fin.add_widget(procurar_popup_fin_button)
            popup_procurar_window = Popup(title='Pesquisa_fin', content=procurar_popup_fin)
            popup_procurar_window.open()




        orcpage = GridLayout(cols=2)
        orcpage.add_widget(Label(text="altura"))
        altura_input = TextInput(multiline=False)
        orcpage.add_widget(altura_input)
        orcpage.add_widget(Label(text="Largura"))
        largura_input = TextInput(multiline=False)
        orcpage.add_widget(largura_input)
        orcpage.add_widget(Label(text="Cor"))
        color_input = TextInput(multiline=False)
        orcpage.add_widget(color_input)
        orcpage.add_widget(Label(text="preço por metro"))
        preco_metro_input = TextInput(multiline=False)
        orcpage.add_widget(preco_metro_input)
        butaudeorcamento = Button(text="fazer orçamento")
        butaudeorcamento.bind(on_press=sumar)
        orcpage.add_widget(butaudeorcamento)
        print_orc = Button(text="print orçamento")
        print_orc.bind(on_press=sumar)
        orcpage.add_widget(print_orc)
        orcpage.add_widget(Button(text="Abrir calculadora"))
        orcpage.add_widget(Button(text="alterar valores base(valor de compra, de lucro, etc)"))

        # ## ## ## ## ## ## ## ## ## ## ## ORC PAGE # ## ## ## ## ## ## ## ## ## ## ## #

        # ## ## ## ## ## ## ## ## ## ## ## ESTOQUE_PAGE # ## ## ## ## ## ## ## ## ## ##
        estoque_page = GridLayout(rows=3, size_hint_x=None, width=800)

        estoque_page_buttons = GridLayout(cols=1, spacing=30)
        estoque_page.add_widget(estoque_page_buttons)

        estoque_page_body = GridLayout(cols=4, )
        estoque_page.add_widget(estoque_page_body)

        estoque_page_content = GridLayout(cols=1)
        estoque_page.add_widget(estoque_page_content)

        # ## ## ## ## ## ## ## ## ## ## ## # WIDGET estoque_page # ## ## ## ## ## ## ## ## ## ## #
        adicionar_item_buton = Button(text="ADICIONAR ")
        adicionar_item_buton.bind(on_press=adicionar_popup_estoque)
        estoque_page_buttons.add_widget(adicionar_item_buton)

        remover_item_buton = Button(text="EXCLUIR")
        remover_item_buton.bind(on_press=estoque_excluir_popup)

        estoque_page_buttons.add_widget(remover_item_buton)

        procurar_item_buton = Button(text="PROCURAR ITEM")
        procurar_item_buton.bind(on_press= procurar_estoque)
        estoque_page_buttons.add_widget(procurar_item_buton)

        estoque_page_body.add_widget(Label(text="NOME"))
        estoque_page_body.add_widget(Label(text="QNT"))
        estoque_page_body.add_widget(Label(text="PREÇO"))
        estoque_page_body.add_widget(Label(text="OBS"))

        estoque_tabela = ScrollView(size_hint=(1, None), height=100)
        estoque_page_content.add_widget(estoque_tabela)
        estoque_tabela_content = GridLayout(cols=4, size_hint_y=None, height=300, spacing=[0, 0], padding=[10,10])
        estoque_tabela.add_widget(estoque_tabela_content)
        c_estoque.execute("SELECT * FROM estoque ORDER BY nome")
        estoque_db = c_estoque.fetchall()
        for i in estoque_db:
            for j in i:
                estoque_tabela_content.add_widget(Label(text=str(j)))
        dbcon_estoque.commit()
        # ## ## ## ## ## ## ## ## ## ## ## # WIDGET estoque_page # ## ## ## ## ## ## ## ## ## ## #

        # ## ## ## ## ## ## ## ## ## ## ## ESTOQUE_PAGE # ## ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - GRIDS # ## ## ## ## ## ## ## ## ##
        clientes_page = GridLayout(rows=3, size_hint_x=None, width=800)
        clientes_page_buttons = GridLayout(cols=1, spacing=30)
        clientes_page_body = GridLayout(cols=4)
        clientes_page_content = GridLayout(cols=4, size_hint_y=None, height=300, spacing=[0, 45], padding=25)
        clientes_tabela = ScrollView(size_hint=(1, None), width=850, height=150)
        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - GRIDS # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - BUTTONS # ## ## ## ## ## ## ## ## ##

        clientes_page.add_widget(clientes_page_buttons)

        adicionar_CLIENTE_buton = Button(text="ADICIONAR")
        adicionar_CLIENTE_buton.bind(on_press=adicionar_popup_cliente)
        clientes_page_buttons.add_widget(adicionar_CLIENTE_buton)

        remover_CLIENTE_buton = Button(text="EXCLUIR")
        remover_CLIENTE_buton.bind(on_press=cliente_excluir_popup)
        clientes_page_buttons.add_widget(remover_CLIENTE_buton)

        procurar_CLIENTE_buton = Button(text="PROCURAR")
        procurar_CLIENTE_buton.bind(on_press=procurar_cliente)
        clientes_page_buttons.add_widget(procurar_CLIENTE_buton)

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - BUTTONS # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - BODY # ## ## ## ## ## ## ## ## ##
        clientes_page.add_widget(clientes_page_body)

        clientes_page_body.add_widget(Label(text="NOME"))
        clientes_page_body.add_widget(Label(text="TELEFONE"))
        clientes_page_body.add_widget(Label(text="ENDEREÇO"))
        clientes_page_body.add_widget(Label(text="EMAIL"))

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - BODY # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - CONTENT # ## ## ## ## ## ## ## ## ##
        clientes_tabela.add_widget(clientes_page_content)
        clientes_page.add_widget(clientes_tabela)
        c_cliente.execute("SELECT * FROM clientes ORDER BY nome")
        cliente_db = c_cliente.fetchall()
        for i in cliente_db:
            for j in i:
                clientes_page_content.add_widget(Label(text=str(j)))
        dbcon_cliente.commit()

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE - CONTENT # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # CLIENTES_PAGE # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE  GRID # ## ## ## ## ## ## ## ## ##
        func_page = GridLayout(rows=3, size_hint_x=None, width=800)
        func_page_bunttons = GridLayout(cols=1, spacing=30)
        func_page_body = GridLayout(cols=5)
        func_page_content = GridLayout(cols=5, size_hint_y=None, height=500, spacing=10)
        func_tabela = ScrollView(size_hint=(1, None), height=150)

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE  GRID # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE  BUTTONS # ## ## ## ## ## ## ## ## ##
        func_page.add_widget(func_page_bunttons)
        func_page_add_button = Button(text="ADICIONAR")
        func_page_add_button.bind(on_press=adicionar_popup_func)
        func_page_bunttons.add_widget(func_page_add_button)

        func_page_remove_button = Button(text="EXCLUIR")
        func_page_remove_button.bind(on_press=func_excluir_popup)
        func_page_bunttons.add_widget(func_page_remove_button)

        func_page_srch_button = Button(text="PROCURAR")
        func_page_srch_button.bind(on_press=procurar_func)
        func_page_bunttons.add_widget(func_page_srch_button)

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE BODY # ## ## ## ## ## ## ## ## ##

        func_page.add_widget(func_page_body)

        func_page_body.add_widget(Label(text="NOME"))
        func_page_body.add_widget(Label(text="FUNÇÃO"))
        func_page_body.add_widget(Label(text="SALÁRIO"))
        func_page_body.add_widget(Label(text="IMPOSTO"))
        func_page_body.add_widget(Label(text="COMISSÃO"))
        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE BODY # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE CONTENT # ## ## ## ## ## ## ## ## ##
        func_tabela.add_widget(func_page_content)
        func_page.add_widget(func_tabela)
        c_func.execute("SELECT * FROM func ORDER BY nome")
        func_db = c_func.fetchall()
        for i in func_db:
            for j in i:
                func_page_content.add_widget(Label(text=str(j)))

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE CONTENT # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FUNC_PAGE # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # ANGENDA_PAGE # ## ## ## ## ## ## ## ## ##
        agenda_page = GridLayout(rows=1)
        send_button = Button(text="Enviar agendamentos")
        agenda_page.add_widget(send_button)



        # ## ## ## ## ## ## ## ## ## ## ## # ANGENDA_PAGE # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE # ## ## ## ## ## ## ## ## ##
        fin_page = GridLayout(rows=3, size_hint_x=None, width=800)
        fin_page_bunttons = GridLayout(cols=1, spacing=30)
        fin_page_body = GridLayout(cols=4)
        fin_page_content = GridLayout(cols=4, size_hint_y=None, height=300, spacing=10)
        fin_tabela = ScrollView(size_hint=(1, None), height=150)
        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE BUTTONS # ## ## ## ## ## ## ## ## ##

        fin_page.add_widget(fin_page_bunttons)
        fin_page_add_button = Button(text="ADICIONAR")
        fin_page_add_button.bind(on_press=adicionar_popup_fin)
        fin_page_bunttons.add_widget(fin_page_add_button)

        fin_page_remove_button = Button(text="EXCLUIR")
        fin_page_remove_button.bind(on_press=fin_excluir_popup)
        fin_page_bunttons.add_widget(fin_page_remove_button)

        fin_page_srch_button = Button(text="PROCURAR")
        fin_page_srch_button.bind(on_press = procurar_fin)
        fin_page_bunttons.add_widget(fin_page_srch_button)

    # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE BUTTONS # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE BODY # ## ## ## ## ## ## ## ## ##

        fin_page.add_widget(fin_page_body)

        fin_page_body.add_widget(Label(text="NOME"))
        fin_page_body.add_widget(Label(text="VALOR"))
        fin_page_body.add_widget(Label(text="VALIDADE"))
        fin_page_body.add_widget(Label(text="PAGO"))

        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE BODY # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE CONTENT # ## ## ## ## ## ## ## ## ##

        fin_tabela.add_widget(fin_page_content)
        fin_page.add_widget(fin_tabela)
        c_fin.execute("SELECT * FROM fin ORDER BY nome")
        c_func.execute("SELECT * FROM func ORDER BY nome")
        fin_db = c_fin.fetchall()
        func_db = c_func.fetchall()
        for i in fin_db:
            for j in i:
                fin_page_content.add_widget(Label(text=str(j)))
            fin_page_content.add_widget(CheckBox())
        for x in func_db:
            fin_page_content.add_widget(Label(text=str(x[0])))
            fin_page_content.add_widget(Label(text=str(x[2])))
            fin_page_content.add_widget(Label(text="Dia 12"))
            fin_page_content.add_widget(CheckBox())

        dbcon_fin.commit()
        dbcon_func.commit()


        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE CONTENT # ## ## ## ## ## ## ## ## ##

        # ## ## ## ## ## ## ## ## ## ## ## # FIN_PAGE # ## ## ## ## ## ## ## ## ##

        return layout


if __name__ == "__main__":
    Window.size = (1200, 500)
    TutorialApp().run()
