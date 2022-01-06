import streamlit as st
import pandas as pd
import datetime
import io
import requests
import plotly.graph_objects as go


def info():
    page_name = "home"
    return page_name


def app():
    home_page = """
    <div align="center">
        Here is the online version of my <b>Quantum games</b>. Of course, all of these are free and <b>opensource</b>. <br>
        Every of these games are 100% coded by me, sometimes I've been inspired by pop-culture and something by <b>physics law</b>. <br>
        Some are part of <b>experiments</b> and others can be part of past <b>Hackaton</b> or a onenight stand idea... 
        I like created games and making then winnable by a machine. So here every of these games have a tough <b>robot as opponent !</b><br>
        Will you succeed to win each times ? Have fun and good luck !!! 
    </div>
    </br>
    """
    st.markdown(home_page, unsafe_allow_html=True)

    #############################################################
    # Graph

    robot_evo_csv = []
    human_evo_csv = []
    date_csv = []

    ## Qpokemon
    r = requests.get('https://raw.githubusercontent.com/mickahell/robots-data/main/games/stats/qpokemon_results.csv')
    file_csv = io.StringIO(r.text)
    csv_file = pd.read_csv(filepath_or_buffer=file_csv)

    robot_csv = csv_file["robot"].tolist()
    human_csv = csv_file["human"].tolist()
    date_csv_temp = csv_file["date"].tolist()

    for i in range(len(date_csv_temp)):
        date_csv.append(datetime.datetime.strptime(date_csv_temp[i], '%m-%Y').date())

    ## Qnim
    r = requests.get('https://raw.githubusercontent.com/mickahell/robots-data/main/games/stats/qnim_results.csv')
    file_csv = io.StringIO(r.text)
    csv_file = pd.read_csv(filepath_or_buffer=file_csv)

    qnim_robot_csv = csv_file["robot"].tolist()
    qnim_human_csv = csv_file["human"].tolist()
    qnim_date_csv_temp = csv_file["date"].tolist()
    qnim_date_csv = []

    for i in range(len(qnim_date_csv_temp)):
        qnim_date_csv.append(datetime.datetime.strptime(qnim_date_csv_temp[i], '%m-%Y').date())

    ## Fusion
    compteur = 0
    for i in qnim_date_csv:
        temp_date = i
        if temp_date in date_csv:
            compteur_bis = 0
            for u in date_csv:
                if u == temp_date:
                    robot_csv[compteur_bis] += qnim_robot_csv[compteur]
                    human_csv[compteur_bis] += qnim_human_csv[compteur]
                compteur_bis += 1
        else:
            robot_csv.append(qnim_robot_csv[compteur])
            human_csv.append(qnim_human_csv[compteur])

            date_csv.append(temp_date)
        compteur += 1

    for i in range(len(robot_csv)):
        robot_evo_csv.append(robot_csv[i] / (human_csv[i] + robot_csv[i]) * 100)
        human_evo_csv.append(human_csv[i] / (human_csv[i] + robot_csv[i]) * 100)

    graph = """
    ## Graph - Victory
    """
    st.markdown(graph)

    fig_bar = go.Figure([go.Bar(x=['Robot', 'Human'], y=[sum(robot_csv), sum(human_csv)])])
    fig_bar.update_layout(title_text='Robot VS Human')
    st.plotly_chart(fig_bar, use_container_width=True)

    left_column, right_column = st.columns([1, 5])

    graph_filter = left_column.radio("Filter", ("Robot", "Human"))
    if graph_filter == 'Human':
        graph_csv = human_evo_csv
    else:
        graph_csv = robot_evo_csv

    fig_series = go.Figure([go.Scatter(x=date_csv, y=graph_csv, mode='lines+markers', marker=dict(color="aqua"))])
    fig_series.update_layout(title_text='Robot evolution', xaxis_title="Months", yaxis_title="% of victory")
    right_column.plotly_chart(fig_series, use_container_width=True)



