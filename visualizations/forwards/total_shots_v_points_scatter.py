__author__ = 'gj'

from bokeh.plotting import figure, output_file, show

from utils.read_data import get_plot_data

data = get_plot_data('forwards', 'total_shots', 'points')
output_file("total_shots_v_points_scatter.html")
p = figure(plot_width=600, plot_height=600)
p.circle(data['total_shots'], data['points'], size=20, color="navy", alpha=0.5)
show(p)
