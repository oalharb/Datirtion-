

import plotly.graph_objects as go

def nut_plot(data, x):
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][4],
        domain = {'x': [0, 1], 'y': [1, 0]},
        title = {'text': "Sugars g", 'font': {'size': 20}},
        delta = {'reference': 0, 'decreasing': {'color': "green"}
            ,'reference': 15, 'increasing': {'color': "red"}},
        gauge = {
            'axis': {'range': [None, 20], 'tickwidth': 1},
            'bar': {'color': "black"},
#             'bgcolor': "white",
#             'borderwidth': 1,
#             'bordercolor': "gray",
            'steps': [
                {'range': [0, 5], 'color': 'green'},
                {'range': [5, 15], 'color': 'orange'},
                {'range': [15, 20], 'color': 'red'}],
           'threshold': {
                  'line': {'color': "white", 'width': 10},
                  'thickness': 0.25,
                 'value': 20}}))
    fig.show()
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][7],
        domain = {'x': [0, 1], 'y': [1, 0]},
        title = {'text': "Saturated Fat g", 'font': {'size': 20}},
        delta = {'reference': 0, 'decreasing': {'color': "green"}
            ,'reference': 5, 'increasing': {'color': "red"}},
        gauge = {
            'axis': {'range': [None, 15], 'tickwidth': 1},
            'bar': {'color': "black"},
            #'bgcolor': "white",
            #'borderwidth': 1,
            #'bordercolor': "black",
            'steps': [
                {'range': [0, 1.5], 'color': 'green'},
                {'range': [1.5, 5], 'color': 'orange'},
                {'range': [5, 15], 'color': 'red'}],
             'threshold': {
                 'line': {'color': "white", 'width': 10},
                 'thickness': 0.25,
                 'value': 15}}))

#fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

    fig.show()

    
    

    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][8],
        domain = {'x': [0, 1], 'y': [1, 0]},
        title = {'text': "Trans Fat g", 'font': {'size': 20}},
        delta = {'reference': 0, 'decreasing': {'color': "green"}
            ,'reference': 20, 'increasing': {'color': "red"}},
        gauge = {
            'axis': {'range': [None, 25], 'tickwidth': 1},
            'bar': {'color': "black"},
            #'bgcolor': "white",
            #'borderwidth': 1,
            #'bordercolor': "gray",
            'steps': [
                {'range': [0, 3], 'color': 'green'},
                {'range': [3, 20], 'color': 'orange'},
                {'range': [20, 25], 'color': 'red'}],
             'threshold': {
                 'line': {'color': "white", 'width': 10},
                 'thickness': 0.25,
                 'value': 25}}))
    fig.show()
#fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})

  
    fig = go.Figure(go.Indicator(
        mode = "gauge+number+delta",
        value = data.iloc[x][10],
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Sodium mg", 'font': {'size': 20}},
        delta = {'reference': 0, 'decreasing': {'color': "green"}
            ,'reference': 150, 'increasing': {'color': "red"}},
        gauge = {
            'axis': {'range': [None, 200], 'tickwidth': 1},
            'bar': {'color': "black"},
            #'bgcolor': "white",
            #'borderwidth': 1,
            #'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': 'green'},
                {'range': [30, 150], 'color': 'orange'},
                {'range': [150, 200], 'color': 'red'}],
             'threshold': {
                 'line': {'color': "white", 'width': 10},
                 'thickness': 0.25,
                 'value': 200}}))

#fig.update_layout(paper_bgcolor = "lavender", font = {'color': "darkblue", 'family': "Arial"})


    fig.show()
