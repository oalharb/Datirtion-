

import plotly.graph_objects as go

def nut_plot(data, x):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][7],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Sugars", 'font': {'size': 20}},
        delta = {'reference': 150, 'increasing': {'color': "gray"}},
        gauge = {
            'axis': {'range': [None, 150], 'tickwidth': 2},
            'bar': {'color': "black"},
            'bgcolor': "white",
            'borderwidth': 1,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': 'green'},
                {'range': [30, 80], 'color': 'orange'},
                {'range': [80, 150], 'color': 'red'}],
           'threshold': {
                 'line': {'color': "white", 'width': 10},
                 'thickness': 0.25,
                 'value': 150}}))

    fig.show()
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][9],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Sodium", 'font': {'size': 24}},
        delta = {'reference': 150, 'increasing': {'color': "gray"}},
        gauge = {
            'axis': {'range': [None, 150], 'tickwidth': 1},
            'bar': {'color': "black"},
            #'bgcolor': "white",
            #'borderwidth': 1,
            #'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': 'green'},
                {'range': [50, 100], 'color': 'orange'},
                {'range': [100, 150], 'color': 'red'}],
             'threshold': {
                 'line': {'color': "white", 'width': 10},
                 'thickness': 0.25,
                 'value': 150}}))

#fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

    fig.show()
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][4],
        domain = {'x': [0, 1], 'y': [1, 0]},
        title = {'text': "Saturated Fat", 'font': {'size': 24}},
        delta = {'reference': 15, 'increasing': {'color': "gray"}},
        gauge = {
            'axis': {'range': [None, 15], 'tickwidth': 1},
            'bar': {'color': "black"},
            #'bgcolor': "white",
            #'borderwidth': 1,
            #'bordercolor': "black",
            'steps': [
                {'range': [0, 5], 'color': 'green'},
                {'range': [5, 10], 'color': 'orange'},
                {'range': [10, 15], 'color': 'red'}],
             'threshold': {
                 #'line': {'color': "white", 'width': 10},
                 #'thickness': 0.25,
                 'value': 15}}))

#fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

    fig.show()
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][12],
        domain = {'x': [0, 1], 'y': [1, 0]},
        title = {'text': "Cholesterol", 'font': {'size': 24}},
        delta = {'reference': 150, 'increasing': {'color': "gray"}},
        gauge = {
            'axis': {'range': [None, 150], 'tickwidth': 1},
            'bar': {'color': "black"},
            #'bgcolor': "white",
            #'borderwidth': 1,
            #'bordercolor': "gray",
            'steps': [
                {'range': [0, 50], 'color': 'green'},
                {'range': [50, 100], 'color': 'orange'},
                {'range': [100, 150], 'color': 'red'}],
             'threshold': {
                 #'line': {'color': "white", 'width': 10},
                 #'thickness': 0.25,
                 'value': 150}}))

#fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

    fig.show()

