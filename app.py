import plotly.graph_objects as go
import streamlit as st
import pandas as pd


def grafico_estudantes(IES, CURSO, GRAFICOS, dados1):

  if(len(GRAFICOS) == 0):
    st.subheader('')
    st.error('É necessária a escolha de pelo menos uma opção de gráfico. Por favor, tente novamente.')
  else:
    if(len(GRAFICOS) == 1):
      titulo = st.header('Gerando o Gráfico...')  
    if(len(GRAFICOS) > 1):
      titulo = st.header('Gerando os Gráficos...')

    if('Situações' in GRAFICOS):

        y_masculino1 = []
        y_feminino1 = []

        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1)]['TP_SEXO'].count())
        y_masculino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2)]['TP_SEXO'].count())
        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
        y_masculino1.append( dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())
        y_feminino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_SITUACAO'] == 7)]['TP_SITUACAO'].count())
        y_masculino1.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_SITUACAO'] == 7)]['TP_SITUACAO'].count())

        maiorcount = 0
        if(max(y_masculino1) > maiorcount):
          maiorcount = max(y_masculino1)
          if(max(y_feminino1) > max(y_masculino1)):
            maiorcount = max(y_feminino1)

        situacoes = ['Total', 'Cursando', 'Matricula<br>Trancada', 'Desvinculados', 'Transferidos', 'Formados', 'Falecidos']

        fig1 = go.Figure(data=[go.Bar(name = 'Homens', x = situacoes, y = y_masculino1, text = y_masculino1, marker_pattern_shape="/"), go.Bar(name = 'Mulheres', x = situacoes, y= y_feminino1, text = y_feminino1, marker_pattern_shape="x", marker_color='#f63366')])

        fig1.update_xaxes(tickfont_size=11)
        fig1.update_yaxes(range = [0, maiorcount+50], tickfont_size=11, showgrid = False)
        fig1.update_traces(textposition = 'outside', textfont_size=11)
        fig1.update_layout(title_text = f'Quantidade de Estudantes entre Homens e Mulheres por Situações no Curso de<br>{CURSO} da {IES} no Ano de 2019', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if('Cor/Raça' in GRAFICOS):

      y_masculino2 = []
      y_feminino2 = []

      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_feminino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())
      y_masculino2.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())

      maiorcount = 0
      if(max(y_masculino2) > maiorcount):
        maiorcount = max(y_masculino2)
        if(max(y_feminino2) > max(y_masculino2)):
          maiorcount = max(y_feminino2)

      cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Quis<br>Declarar', 'Não Informado']

      fig2 = go.Figure(data=[go.Bar(name = 'Homens', x = cor_raca, y = y_masculino2, text = y_masculino2, marker_pattern_shape="/"), go.Bar(name = 'Mulheres', x = cor_raca, y= y_feminino2, text = y_feminino2, marker_pattern_shape="x", marker_color='#f63366')])

      fig2.update_xaxes(tickfont_size=11)
      fig2.update_yaxes(range = [0, maiorcount+50], tickfont_size=11, showgrid = False)
      fig2.update_traces(textposition = 'outside', textfont_size=11)
      fig2.update_layout(title_text = f'Quantidade de Estudantes entre Homens e Mulheres por Cor/Raça no Curso de<br>{CURSO} da {IES} no Ano de 2019', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if('Idades' in GRAFICOS):

      y_masculino3 = []
      y_feminino3 = []

      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] <= 20)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] <= 20)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 21) & (dados1['NU_IDADE'] <= 24)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 21) & (dados1['NU_IDADE'] <= 24)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 25) & (dados1['NU_IDADE'] <= 28)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 25) & (dados1['NU_IDADE'] <= 28)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 29) & (dados1['NU_IDADE'] <= 32)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 29) & (dados1['NU_IDADE'] <= 32)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 33) & (dados1['NU_IDADE'] <= 36)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 33) & (dados1['NU_IDADE'] <= 36)]['TP_SEXO'].count())
      y_feminino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 1) & (dados1['NU_IDADE'] >= 37)]['TP_SEXO'].count())
      y_masculino3.append(dados1[(dados1['SG_IES'] == IES) & (dados1['NO_CURSO'] == CURSO) & (dados1['TP_SEXO'] == 2) & (dados1['NU_IDADE'] >= 37)]['TP_SEXO'].count())

      maiorcount = 0
      if(max(y_masculino3) > maiorcount):
        maiorcount = max(y_masculino3)
        if(max(y_feminino3) > max(y_masculino3)):
          maiorcount = max(y_feminino3)

      idades = ['Total', 'Até 20', '21 até 24', '25 até 28', '29 até 32', '33 até 36', 'Mais que 36']

      fig3 = go.Figure(data=[go.Bar(name = 'Homens', x = idades, y = y_masculino3, text = y_masculino3, marker_pattern_shape="/"), go.Bar(name = 'Mulheres', x = idades, y= y_feminino3, text = y_feminino3, marker_pattern_shape="x", marker_color='#f63366')])

      fig3.update_xaxes(title_text = 'Idades', tickfont_size=11)
      fig3.update_yaxes(title_text = 'Estudantes', range = [0, maiorcount+50], tickfont_size=11, showgrid = False)
      fig3.update_traces(textposition = 'outside', textfont_size=11)
      fig3.update_layout(title_text = f'Quantidade de Estudantes entre Homens e Mulheres por Idades no Curso de<br>{CURSO} da {IES} no Ano de 2019', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
      
    titulo.empty()
    if(len(GRAFICOS) == 1):
      st.header('Gráfico (Estudantes):') 
      st.subheader('')
    if(len(GRAFICOS) > 1):
      st.header('Gráficos (Estudantes):')
      st.subheader('')
    if('Situações' in GRAFICOS):
      st.plotly_chart(fig1, use_container_width=True)
    if('Cor/Raça' in GRAFICOS):
      st.plotly_chart(fig2, use_container_width=True)
    if('Idades' in GRAFICOS):
      st.plotly_chart(fig3, use_container_width=True)
    st.subheader('')
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
        pagina_inicial()

def grafico_professores(IES, GRAFICOS, dados2):

  if(len(GRAFICOS) == 0):
    st.subheader('')
    st.error('É necessária a escolha de pelo menos uma opção de gráfico. Por favor, tente novamente.')
  else:
    if('Situações' in GRAFICOS):

      y_masculino1 = []
      y_feminino1 = []

      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 1)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 1)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 2)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 3)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 4)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 5)]['TP_SITUACAO'].count())
      y_feminino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())
      y_masculino1.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_SITUACAO'] == 6)]['TP_SITUACAO'].count())

      maiorcount = 0
      if(max(y_masculino1) > maiorcount):
        maiorcount = max(y_masculino1)
        if(max(y_feminino1) > max(y_masculino1)):
          maiorcount = max(y_feminino1)

      situacoes = ['Total', 'Em Exercício', 'Em Qualificação', 'Em Outra<br>Entidade', 'Afastados<br>(Saúde)', 'Afastados<br>(Outros)', 'Falecidos']

      fig1 = go.Figure(data=[go.Bar(name = 'Homens', x = situacoes, y = y_masculino1, text = y_masculino1, marker_pattern_shape="/"), go.Bar(name = 'Mulheres', x = situacoes, y= y_feminino1, text = y_feminino1, marker_pattern_shape="x", marker_color='#f63366')])

      fig1.update_xaxes(tickfont_size=11)
      fig1.update_yaxes(range = [0, maiorcount+100], tickfont_size=11, showgrid = False)
      fig1.update_traces(textposition = 'outside', textfont_size=11)
      fig1.update_layout(title_text = f'Quantidade de Professores entre Homens e Mulheres por Situações<br>da {IES} no Ano de 2019', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if('Cor/Raça' in GRAFICOS):

      y_masculino2 = []
      y_feminino2 = []

      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 1)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 2)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 3)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 4)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 5)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 0)]['TP_COR_RACA'].count())
      y_feminino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())
      y_masculino2.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['TP_COR_RACA'] == 9)]['TP_COR_RACA'].count())

      maiorcount = 0
      if(max(y_masculino2) > maiorcount):
        maiorcount = max(y_masculino2)
        if(max(y_feminino2) > max(y_masculino2)):
          maiorcount = max(y_feminino2)

      cor_raca = ['Total', 'Brancos', 'Pretos', 'Pardos', 'Amarelos', 'Indígenas', 'Não Quis<br>Declarar', 'Não Informado']

      fig2 = go.Figure(data=[go.Bar(name = 'Homens', x = cor_raca, y = y_masculino2, text = y_masculino2, marker_pattern_shape="/"), go.Bar(name = 'Mulheres', x = cor_raca, y= y_feminino2, text = y_feminino2, marker_pattern_shape="x", marker_color='#f63366')])

      fig2.update_xaxes(tickfont_size=11)
      fig2.update_yaxes(range = [0, maiorcount+100], tickfont_size=11, showgrid = False)
      fig2.update_traces(textposition = 'outside', textfont_size=11)
      fig2.update_layout(title_text = f'Quantidade de Professores entre Homens e Mulheres por Cor/Raça<br>da {IES} no Ano de 2019', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))

    if('Idades' in GRAFICOS):

      y_masculino3 = []
      y_feminino3 = []

      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] <= 30)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] <= 30)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 31) & (dados2['NU_IDADE'] <= 34)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 31) & (dados2['NU_IDADE'] <= 34)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 35) & (dados2['NU_IDADE'] <= 38)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 35) & (dados2['NU_IDADE'] <= 38)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 39) & (dados2['NU_IDADE'] <= 42)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 39) & (dados2['NU_IDADE'] <= 42)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 43) & (dados2['NU_IDADE'] <= 46)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 43) & (dados2['NU_IDADE'] <= 46)]['TP_SEXO'].count())
      y_feminino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 1) & (dados2['NU_IDADE'] >= 47)]['TP_SEXO'].count())
      y_masculino3.append(dados2[(dados2['SG_IES'] == IES) & (dados2['TP_SEXO'] == 2) & (dados2['NU_IDADE'] >= 47)]['TP_SEXO'].count())

      maiorcount = 0
      if(max(y_masculino3) > maiorcount):
        maiorcount = max(y_masculino3)
        if(max(y_feminino3) > max(y_masculino3)):
          maiorcount = max(y_feminino3)

      idades = ['Total', 'Até 30', '31 até 34', '35 até 38', '39 até 42', '43 até 46', 'Mais que 46']

      fig3 = go.Figure(data=[go.Bar(name = 'Homens', x = idades, y = y_masculino3, text = y_masculino3, marker_pattern_shape="/"), go.Bar(name = 'Mulheres', x = idades, y= y_feminino3, text = y_feminino3, marker_pattern_shape="x", marker_color='#f63366')])

      fig3.update_xaxes(title_text = 'Idades', tickfont_size=11)
      fig3.update_yaxes(title_text = 'Professores', range = [0, maiorcount+100], tickfont_size=11, showgrid = False)
      fig3.update_traces(textposition = 'outside', textfont_size=11)
      fig3.update_layout(title_text = f'Quantidade de Professores entre Homens e Mulheres por Idades<br>da {IES} no Ano de 2019', legend=dict(yanchor = 'top', y = 1, xanchor = 'right', x = 1))
       
    if(len(GRAFICOS) == 1):
      st.header('Gráfico (Professores):') 
      st.subheader('')
    if(len(GRAFICOS) > 1):
      st.header('Gráficos (Professores):')
      st.subheader('')
    if('Situações' in GRAFICOS):
      st.plotly_chart(fig1, use_container_width=True)
    if('Cor/Raça' in GRAFICOS):
      st.plotly_chart(fig2, use_container_width=True)
    if('Idades' in GRAFICOS):
      st.plotly_chart(fig3, use_container_width=True)
    st.subheader('')
    button_pagina_incical = st.button('Página Inicial')
    if(button_pagina_incical):
        pagina_inicial()

def pagina_inicial(dados1, dados2):

  titulo = st.title('Analisador Gráfico do Censo da Educação Superior de 2019')
  espaco1 = st.subheader('')
  sobre = st.header('Sobre:')
  descricao1 = st.subheader('O site realiza análises gráficas dos dados do Censo da Educação Superior de 2019, comparando a quantidade de estudantes e professores entre homens e mulheres presentes nos cursos e instituições de ensino superior do Brasil.')
  descricao2 = st.subheader('Desenvolvido por Guilherme Tomaselli Borchardt, junto ao grupo de Iniciação Científica sobre Evasão Escolar, orientado pela professora Isabela Gasparini e pertencente à Universidade do Estado de Santa Catarina (CCT).')
  st.sidebar.title('Opções:')
  escolha = st.sidebar.selectbox('O que deseja analisar:', ('Estudantes', 'Professores'))
  if(escolha == 'Estudantes'):
    estudantes(titulo, espaco1, sobre, descricao1, descricao2, dados1)
  if(escolha == 'Professores'):
    professores(titulo, espaco1, sobre, descricao1, descricao2, dados2)

def estudantes(titulo, espaco1, sobre, descricao1, descricao2, dados1):

  escolha_ESTADO = st.sidebar.selectbox('Escolha um estado:', ('Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul','Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'))
  if(escolha_ESTADO == 'Rondônia'):
    escolha_ESTADO = 11
  if(escolha_ESTADO == 'Acre'):
    escolha_ESTADO = 12
  if(escolha_ESTADO == 'Amazonas'):
    escolha_ESTADO = 13  
  if(escolha_ESTADO == 'Roraima'):
    escolha_ESTADO = 14
  if(escolha_ESTADO == 'Pará'):
    escolha_ESTADO = 15 
  if(escolha_ESTADO == 'Amapá'):
    escolha_ESTADO = 16
  if(escolha_ESTADO == 'Tocantins'):
    escolha_ESTADO = 17 
  if(escolha_ESTADO == 'Maranhão'):
    escolha_ESTADO = 21
  if(escolha_ESTADO == 'Piauí'):
    escolha_ESTADO = 22
  if(escolha_ESTADO == 'Ceará'):
    escolha_ESTADO = 23
  if(escolha_ESTADO == 'Rio Grande do Norte'):
    escolha_ESTADO = 24
  if(escolha_ESTADO == 'Paraíba'):
    escolha_ESTADO = 25
  if(escolha_ESTADO == 'Pernambuco'):
    escolha_ESTADO = 26
  if(escolha_ESTADO == 'Alagoas'):
    escolha_ESTADO = 27
  if(escolha_ESTADO == 'Sergipe'):
    escolha_ESTADO = 28
  if(escolha_ESTADO == 'Bahia'):
    escolha_ESTADO = 29
  if(escolha_ESTADO == 'Minas Gerais'):
    escolha_ESTADO = 31
  if(escolha_ESTADO == 'Espírito Santo'):
    escolha_ESTADO = 32
  if(escolha_ESTADO == 'Rio de Janeiro'):
    escolha_ESTADO = 33
  if(escolha_ESTADO == 'São Paulo'):
    escolha_ESTADO = 35
  if(escolha_ESTADO == 'Paraná'):
    escolha_ESTADO = 41
  if(escolha_ESTADO == 'Rio Grande do Sul'):
    escolha_ESTADO = 43
  if(escolha_ESTADO == 'Santa Catarina'):
    escolha_ESTADO = 42
  if(escolha_ESTADO == 'Mato Grosso do Sul'):
    escolha_ESTADO = 50
  if(escolha_ESTADO == 'Mato Grosso'):
    escolha_ESTADO = 51
  if(escolha_ESTADO == 'Goiás'):
    escolha_ESTADO = 52
  if(escolha_ESTADO == 'Distrito Federal'):
    escolha_ESTADO = 43
  escolha_IES = st.sidebar.selectbox('Escolha uma IES:', (dados1[dados1['CO_UF'] == escolha_ESTADO]['SG_IES'].drop_duplicates().sort_values().dropna()))
  escolha_CURSO = st.sidebar.selectbox('Escolha um curso:', (dados1[(dados1['CO_UF'] == escolha_ESTADO) & (dados1['SG_IES'] == escolha_IES)]['NO_CURSO'].drop_duplicates().sort_values().dropna()))
  escolha_GRAFICOS = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
  button_gerar_grafico = st.sidebar.button('Gerar Gráfico')
  if(button_gerar_grafico):
    titulo.empty()
    espaco1.empty()
    sobre.empty()
    descricao1.empty()
    descricao2.empty()
    grafico_estudantes(escolha_IES, escolha_CURSO, escolha_GRAFICOS, dados1)

def professores(titulo, espaco1, sobre, descricao1, descricao2, dados2):

  escolha_ESTADO = st.sidebar.selectbox('Escolha um estado:', ('Acre', 'Alagoas', 'Amapá', 'Amazonas', 'Bahia', 'Ceará', 'Distrito Federal', 'Espírito Santo', 'Goiás', 'Maranhão', 'Mato Grosso', 'Mato Grosso do Sul','Minas Gerais', 'Pará', 'Paraíba', 'Paraná', 'Pernambuco', 'Piauí', 'Rio de Janeiro', 'Rio Grande do Norte', 'Rio Grande do Sul', 'Rondônia', 'Roraima', 'Santa Catarina', 'São Paulo', 'Sergipe', 'Tocantins'))
  if(escolha_ESTADO == 'Rondônia'):
    escolha_ESTADO = 11
  if(escolha_ESTADO == 'Acre'):
    escolha_ESTADO = 12
  if(escolha_ESTADO == 'Amazonas'):
    escolha_ESTADO = 13  
  if(escolha_ESTADO == 'Roraima'):
    escolha_ESTADO = 14
  if(escolha_ESTADO == 'Pará'):
    escolha_ESTADO = 15 
  if(escolha_ESTADO == 'Amapá'):
    escolha_ESTADO = 16
  if(escolha_ESTADO == 'Tocantins'):
    escolha_ESTADO = 17 
  if(escolha_ESTADO == 'Maranhão'):
    escolha_ESTADO = 21
  if(escolha_ESTADO == 'Piauí'):
    escolha_ESTADO = 22
  if(escolha_ESTADO == 'Ceará'):
    escolha_ESTADO = 23
  if(escolha_ESTADO == 'Rio Grande do Norte'):
    escolha_ESTADO = 24
  if(escolha_ESTADO == 'Paraíba'):
    escolha_ESTADO = 25
  if(escolha_ESTADO == 'Pernambuco'):
    escolha_ESTADO = 26
  if(escolha_ESTADO == 'Alagoas'):
    escolha_ESTADO = 27
  if(escolha_ESTADO == 'Sergipe'):
    escolha_ESTADO = 28
  if(escolha_ESTADO == 'Bahia'):
    escolha_ESTADO = 29
  if(escolha_ESTADO == 'Minas Gerais'):
    escolha_ESTADO = 31
  if(escolha_ESTADO == 'Espírito Santo'):
    escolha_ESTADO = 32
  if(escolha_ESTADO == 'Rio de Janeiro'):
    escolha_ESTADO = 33
  if(escolha_ESTADO == 'São Paulo'):
    escolha_ESTADO = 35
  if(escolha_ESTADO == 'Paraná'):
    escolha_ESTADO = 41
  if(escolha_ESTADO == 'Rio Grande do Sul'):
    escolha_ESTADO = 43
  if(escolha_ESTADO == 'Santa Catarina'):
    escolha_ESTADO = 42
  if(escolha_ESTADO == 'Mato Grosso do Sul'):
    escolha_ESTADO = 50
  if(escolha_ESTADO == 'Mato Grosso'):
    escolha_ESTADO = 51
  if(escolha_ESTADO == 'Goiás'):
    escolha_ESTADO = 52
  if(escolha_ESTADO == 'Distrito Federal'):
    escolha_ESTADO = 43
  escolha_IES = st.sidebar.selectbox('Escolha uma IES:', (dados2[dados2['CO_UF'] == escolha_ESTADO]['SG_IES'].drop_duplicates().sort_values().dropna()))
  escolha_GRAFICOS = st.sidebar.multiselect('Escolha uma ou mais opções para analisar:', ['Cor/Raça', 'Idades', 'Situações'], default = ['Cor/Raça'])
  button_gerar_grafico = st.sidebar.button('Gerar Gráfico')
  if(button_gerar_grafico):
    titulo.empty()
    espaco1.empty()
    sobre.empty()
    descricao1.empty()
    descricao2.empty()
    grafico_professores(escolha_IES, escolha_GRAFICOS, dados2)

@st.cache(allow_output_mutation=True, show_spinner=False)
def load_data_alunos():

  dados1_alunos = pd.read_csv('SUP_ALUNO1.CSV', sep='|', encoding='utf8')
  dados2_alunos = pd.read_csv('SUP_ALUNO2.CSV', sep='|', encoding='utf8')
  dados3_alunos = pd.read_csv('SUP_ALUNO3.CSV', sep='|', encoding='utf8')
  dados4_alunos = pd.read_csv('SUP_ALUNO4.CSV', sep='|', encoding='utf8')
  dados5_alunos = pd.read_csv('SUP_ALUNO5.CSV', sep='|', encoding='utf8')
  dados6_alunos = pd.read_csv('SUP_ALUNO6.CSV', sep='|', encoding='utf8')
  dados7_alunos = pd.read_csv('SUP_ALUNO7.CSV', sep='|', encoding='utf8')
  dados8_alunos = pd.read_csv('SUP_ALUNO8.CSV', sep='|', encoding='utf8')
  dados9_alunos = pd.read_csv('SUP_ALUNO9.CSV', sep='|', encoding='utf8')
  dados10_alunos = pd.read_csv('SUP_ALUNO10.CSV', sep='|', encoding='utf8')
  dados11_alunos = pd.read_csv('SUP_ALUNO11.CSV', sep='|', encoding='utf8')
  dados12_alunos = pd.read_csv('SUP_ALUNO12.CSV', sep='|', encoding='utf8')
  dados13_alunos = pd.read_csv('SUP_ALUNO13.CSV', sep='|', encoding='utf8')
  dados_ALUNOS = pd.concat([dados1_alunos, dados2_alunos, dados3_alunos, dados4_alunos, dados5_alunos, dados11_alunos, dados12_alunos, dados13_alunos])
  dados_IES = pd.read_csv('SUP_IES_2019.CSV', sep='|', encoding='utf8')
  dados_CURSO = pd.read_csv('SUP_CURSO_2019.CSV', sep='|', encoding='utf8')
  dados = dados_ALUNOS.merge(dados_IES, how='outer').merge(dados_CURSO, how='outer')
  dados.sort_values(by=['SG_IES', 'NO_CURSO'], ignore_index=True, ascending=False)
  return dados

@st.cache(allow_output_mutation=True, show_spinner=False)
def load_data_professores():

  dados_PROFESSORES = pd.read_csv('SUP_DOCENTE_2019.CSV', sep='|', encoding='utf8')
  dados_IES = pd.read_csv('SUP_IES_2019.CSV', sep='|', encoding='utf8')
  dados = dados_PROFESSORES.merge(dados_IES, how='outer')
  dados.sort_values(by=['SG_IES'], ignore_index=True, ascending=False)
  return dados

if __name__ == '__main__':

  st.set_page_config(page_title='Analisador Educacional', page_icon='☁️')
  titulo_inicial = st.title('Realizando a Leitura dos Dados...')
  espaco_inicial = st.subheader('')
  descricao_inicial = st.subheader('Por favor aguarde um momento, a aplicação já irá iniciar.')
  dados1 = load_data_alunos()
  dados2 = load_data_professores()
  titulo_inicial.empty()
  espaco_inicial.empty()
  descricao_inicial.empty()
  pagina_inicial(dados1, dados2)
