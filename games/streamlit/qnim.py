import streamlit as st
import pandas as pd
import datetime
import io
import requests
import plotly.graph_objects as go


def app():
    st.write("# Quantum Nim game")
    rules = st.expander("Rules", expanded=False)
    rules_view = """
    This game is inspiring from the [Nim game](https://en.wikipedia.org/wiki/Nim). You are 2 players face to face, you have 11 sticks in front of you :
    <pre>
              \o/
               |
              / \\
    #######################
     | | | | | | | | | | | 
    #######################
              \ /
               |
              /o\\
    </pre>
    The goal is **NOT** take the last stick !!
    Originally, this game can be automatize by classical computer to always loose again a computer or against someone knowing [the strategy](https://en.wikipedia.org/wiki/Modular_arithmetic#Congruence).
    But what happens if we implement quantum rules ?

    Like the original game each player can take 1 to 3 sticks each turn but this time, they can say if they want to take the stick normally, put it in superposition or creating an entanglement between this stick and the sticks previously on the board (played before) :
    <table>
    	<thead>
    		<tr>
    			<th align="center">Symbols table</th>
    			<th align="center">name</th>
    			<th align="center">means</th>
    			<th align="center">action possible ?</th>
    		</tr>
    	</thead>
    	<tbody>
    		<tr>
    			<td align="center">|</td>
    			<td align="center">stick left</td>
    			<td align="center">a simple sticks</td>
    			<td align="center">any action</td>
    		</tr>
    		<tr>
    			<td align="center">/</td>
    			<td align="center">superposition stick</td>
    			<td align="center">sticks in states : |0> + |1></td>
    			<td align="center">no action (only here for info)</td>
    		</tr>
    		<tr>
    			<td align="center">¬</td>
    			<td align="center">entangle stick</td>
    			<td align="center">the faith of this stick depends of the previous one</td>
    			<td align="center">no action (only here for info)</td>
    		</tr>
    		<tr>
    			<td align="center">[ ]</td>
    			<td align="center">blank space</td>
    			<td align="center">the previous stick has been fully taken</td>
    			<td align="center">an cx action can be done with if it's not the first turn of the circuit generation</td>
    		</tr>
    	</tbody>
    </table>

    Here each stick correspond to a qubit at the `|0>` state.

    Example of a game :
    11 sticks in board : `| | | | | | | | | | |`  
    1st turn :  
    Robin choose 2 sticks
      - Robin apply an x gate the 11th stick
      - Robin apply an h gate to the 10th stick

    9 sticks in board : `| | | | | | | | | /`  
    Batman choose 3 sticks  
      - Batman apply a cx to the 9th stick (now the 9th stick is automatically link with the 10th)
      - Batman apply a x gate to the 8th stick
      - Batman apply a x gate to the 7th stick

    6 sticks in board : `| | | | | |`

    etc ...

    2 sticks left : `| | ¬`  
    Robin choose 1 sticks
      - Robin apply an x gate to the 2nd stick

    1 sticks left : `|`  
    Batman choose 1 sticks
      - Batman apply an x gate to the last stick

    When it doesn't have a stick anymore we run the circuit we create with the gates and get the result, for each qubit still at the state `|0>` we had 1 stick left.
    Then we continue wit the sticks remaning until we don't have stick at all after running the circuit.

    ### Modes
    #### 2 players
    A 2 players mode is available is you want to play with a friend or with your cat
    #### 1 player
    A 1 player is available and you'll fight against a quantum ia made with Grover with inside the modulo 4 classical algorythm.

    --> **Explanation coming soon !**

    <pre>
    q0|0>  ---------------------------------

    q1|0>  ---------------------------------

    q2|0>  ---------------------------------

    q3|0>  ---------------------------------

    psi|+> ---------------------------------
    </pre>
        """
    rules.write(rules_view, unsafe_allow_html=True)
    qnim = st.expander("Game", expanded=True)
    qnim_view = """
        <iframe
            title="Quantum Nim Game"
            width="100%"
            height="510"
            src="https://qnim-game.xtraorbitals.xyz">
        </iframe>
        """
    qnim.write(qnim_view, unsafe_allow_html=True)
    st.write("<h3>See on <a href='https://qnim-game.xtraorbitals.xyz'><b>QNim game page</b></a></h3>", unsafe_allow_html=True)
    badge = """
    [![GitHub release (latest by date)](https://img.shields.io/github/v/release/Quantronauts/quantum_Nim-game)](https://github.com/Quantronauts/quantum_Nim-game/releases)
    """
    st.markdown(badge)

    #############################################################
    # Graph
    r = requests.get('https://raw.githubusercontent.com/mickahell/robots-data/main/games/stats/qnim_results.csv')
    file_csv = io.StringIO(r.text)

    robot_csv = []
    human_csv = []
    robot_evo_csv = []
    human_evo_csv = []
    date_csv = []

    csv_file = pd.read_csv(filepath_or_buffer=file_csv, header=None)

    for i in range(len(csv_file[0])):
        robot_csv.append(csv_file[0][i])
        human_csv.append(csv_file[1][i])
        robot_evo_csv.append(csv_file[0][i] / (csv_file[1][i] + csv_file[0][i]) * 100)
        human_evo_csv.append(csv_file[1][i] / (csv_file[1][i] + csv_file[0][i]) * 100)
        date_csv.append(datetime.datetime.strptime(csv_file[2][i], '%m-%Y').date())

    left_column, right_column = st.columns(2)

    fig_bar = go.Figure([go.Bar(x=['Robot', 'Human'], y=[sum(robot_csv), sum(human_csv)])])
    fig_bar.update_layout(title_text='Robot VS Human')
    left_column.plotly_chart(fig_bar, use_container_width=True)

    fig_series = go.Figure([go.Scatter(x=date_csv, y=robot_evo_csv, mode='lines+markers', marker=dict(color="aqua"))])
    fig_series.update_layout(title_text='Robot evolution', xaxis_title="Months", yaxis_title="% of victory")
    right_column.plotly_chart(fig_series, use_container_width=True)
