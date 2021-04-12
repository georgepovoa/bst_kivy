from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.popup import Popup

from tika import parser # pip install tika
import os
import sys

from kivy.core.clipboard import Clipboard

from kivy.uix.popup import Popup

class ModernApp(App):
    def build(self):
        
        
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

            lista_de_campos = ["valor", 'data','vencimento','repeticao','descricao','contato','observacoes']
            # adicionar dinamicamente label e input 
            for i in lista_de_campos:
                
                financeiro_view.add_widget(Label(text=str(i)))
                globals()[str(i)] = TextInput(multiline=False)
                financeiro_view.add_widget(globals()[str(i)])

            
            financeiro_view.add_widget(Label(text = "Conta"))
            conta = Button()
            financeiro_view.add_widget(conta)

            financeiro_view.add_widget(Label(text = "Categoria"))
            categoria = Button()
            financeiro_view.add_widget(categoria)

            financeiro_view.add_widget(Label(text = "Forma de pagamento"))
            forma_de_pagamento = Button()
            financeiro_view.add_widget(forma_de_pagamento)

            
            
            btt_teste = Button(text="btt test")
            btt_teste.bind(on_release = btt_test_func)
            financeiro_view.add_widget(btt_teste)




            parte_conteudo.add_widget(financeiro_view)
            
            
        def btt_test_func(instance):
            def adicionar_receita(instance):
                valor_value = valor.text
                data_value = data.text
                vencimento_value = vencimento.text
                repeticao_value = repeticao.text
                descricao_value = descricao.text
                contato_value = contato.text
                observacoes_value = observacoes.text
                db_list = [valor_value,data_value,vencimento_value,repeticao_value,descricao_value,contato_value]

                print("RECEITA")
                print(db_list)

            def adicionar_despesa(intance):
                valor_value = valor.text
                data_value = data.text
                vencimento_value = vencimento.text
                repeticao_value = repeticao.text
                descricao_value = descricao.text
                contato_value = contato.text
                observacoes_value = observacoes.text
                if vencimento.text != '' :
                    
                
                    try:
                        db_list = [float(valor_value)*-1,data_value,vencimento_value,repeticao_value,descricao_value,contato_value]

                        print("DESPESA")
                        print(db_list)
                    except Exception as e:
                        print(e)
                else :
                    print('Valores necessários estão vazios')


            valor_value = valor.text
            data_value = data.text
            vencimento_value = vencimento.text
            repeticao_value = repeticao.text
            descricao_value = descricao.text
            contato_value = contato.text
            observacoes_value = observacoes.text
            db_list = [valor_value,data_value,vencimento_value,repeticao_value,descricao_value,contato_value]
            tela_escolha = GridLayout(cols=2)

            tela_escolha_receita_btt = Button(text="receita")
            tela_escolha_receita_btt.bind(on_release = adicionar_receita)
            tela_escolha_despesa_btt = Button(text = "despesa")
            tela_escolha_despesa_btt.bind(on_release = adicionar_despesa)
            tela_escolha.add_widget(tela_escolha_receita_btt)
            tela_escolha.add_widget(tela_escolha_despesa_btt)
            

            tela_escolher_popup = Popup(title = "ENTRADA / SAIDA",content = tela_escolha)
            tela_escolher_popup.open()

            

        layout = GridLayout(cols=2)
        parte_conteudo = GridLayout(cols=1)
    

        menu = GridLayout(rows = 4)
        btt_financeiro_menu = Button(text= "Financeiro_view")
        btt_financeiro_menu.bind(on_release = financeiro_view)
        menu.add_widget(btt_financeiro_menu)
        
        cadastros_btt = Button(text="Cadastros ")
        # o que precisa cadastrar
        # conta
        # categoria
        # forma de pagamento
        # caso a forma de pagamento seja cartão crédito, e for receita, descontar valor do cartão
        
        menu.add_widget(cadastros_btt)

        menu.add_widget(Button(text="Resumo "))
        menu.add_widget(Button(text="Arquivos "))
        

        layout.add_widget(menu)
        layout.add_widget(parte_conteudo)
        
        # adicionar dinamicamente label e input 


        return layout
if __name__ == '__main__':
    ModernApp().run()
