import numpy as np
import plotly.graph_objects as go
import os

def plot_parabola_plotly(a=1, output_file='index.html'):
    # Generate x values from 0 to 2a for the parabola
    x = np.linspace(0, 2 * a, 200)
    y_positive = np.sqrt(4 * a * x)  # Upper branch
    y_negative = -np.sqrt(4 * a * x)  # Lower branch
    
    # Create figure
    fig = go.Figure()
    
    # Plot the parabola
    fig.add_trace(go.Scatter(x=x, y=y_positive, mode='lines', name='$y^2 = 4ax$', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=x, y=y_negative, mode='lines', showlegend=False, line=dict(color='blue')))
    
    # Plot the focus
    fig.add_trace(go.Scatter(x=[a], y=[0], mode='markers', marker=dict(color='red', size=10), name='Focus ($a,0$)'))
    
    # Plot the latus rectum
    latus_rectum_y = [2 * a, -2 * a]
    latus_rectum_x = [a, a]
    fig.add_trace(go.Scatter(x=latus_rectum_x, y=latus_rectum_y, mode='markers+lines', marker=dict(color='green', size=8), name='Latus Rectum'))
    
    # Labels and layout
    fig.update_layout(
        title='Parabola $y^2 = 4ax$ and Latus Rectum',
        xaxis_title='x',
        yaxis_title='y',
        xaxis=dict(zeroline=True, showgrid=True),
        yaxis=dict(zeroline=True, showgrid=True),
        showlegend=True
    )
    
    # Save as HTML
    fig.write_html(output_file)
    print(f"Plot saved as {output_file}")

# Run the function to generate HTML
a = 1  # You can change 'a' as needed
plot_parabola_plotly(a)

os.system("start index.html")  # Open the HTML file in the default browser