import pandas as pd
import numpy as np

from bokeh.plotting import figure
from bokeh.models import DatetimeTickFormatter
from bokeh.layouts import column

def bar(dataframe: pd.DataFrame, data_inicial, data_final):
    cluster_label = ["cluster_" + str(cluster_label_i) for cluster_label_i in dataframe.cluster_label]
    conversao = list(dataframe.convertido)

    cluster = [label for label in dataframe["cluster_label"]]
    colors = [set_color(_) for _ in cluster]

    title = "Total Conversão by cluster in the period: " + str(data_inicial) + "-" + str(data_final)
    p = figure(x_range=cluster_label, title=title,
               toolbar_location=None, tools="")

    p.vbar(x=cluster_label, top=conversao, width=0.9, fill_color=colors)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    return p


def line_time(dataframe: pd.DataFrame, data_inicial, data_final):

    if ('hora' in dataframe.columns)==True:
        dataframe["data"] = pd.to_datetime(dataframe.data) + pd.to_timedelta(list(map(int, dataframe.hora)), unit='h')

    colors = set_color_unproportional(dataframe.cluster_label.unique())

    title = "Conversão time series plot in the period: " + str(data_inicial) + "-" + str(data_final)
    plots = []
    for cluster_label, color in zip(range(0, dataframe.cluster_label.nunique()), colors):
        p = figure(title="",
                   toolbar_location=None, tools="", x_axis_label="datatime", y_axis_label="Conversão", plot_width=1300)
        date = pd.to_datetime(dataframe.loc[dataframe["cluster_label"] == str(cluster_label)]['data'])
        convertido = dataframe.loc[dataframe["cluster_label"] == str(cluster_label)]['convertido']
        lengenda = "cluster " + str(cluster_label)
        sample_size = len(date[::1])
        limite_central, limite_superior, limite_inferior = get_bootstrap_confidencial_interval(convertido)

        p.line(date, convertido, line_color=color, line_width=2, legend=lengenda)
        p.circle(date[::1], np.repeat(limite_central, sample_size), size=3, fill_color="black", line_color="black")
        p.circle(date[::1], np.repeat(limite_inferior, sample_size), size=3, fill_color="black", line_color="black")
        p.circle(date[::1], np.repeat(limite_superior, sample_size), size=3, fill_color="black", line_color="black",
                 legend= "bootstrap confidential intervals")
        p.xaxis.formatter = DatetimeTickFormatter(
            hours=["%d %B %Y"],
            days=["%d %B %Y"],
            months=["%d %B %Y"],
            years=["%d %B %Y"],
        )
        p.xaxis.major_label_orientation = 3.1614 / 4
        plots.append(p)

    return column(plots)


def set_color_unproportional(label):
    COLORS = ["green", "blue", "red", "orange", "purple", "yellow", "grey", "lawngreen"]

    index = len(label)

    return COLORS[0:index]

def set_color(color):
    COLORS = ["green", "blue", "red", "orange", "purple", "yellow", "grey", "lawngreen"]

    index = color % len(COLORS)

    return COLORS[index]

def get_bootstrap_confidencial_interval(sample):
    sample = np.array(sample)
    sample = sample[~np.isnan(sample)]
    sample_size = len(sample)
    mean_bootstrap, limite_superior_bootstrap, limite_inferior_bootstrap = [], [], []
    for bootstrap_i in range(0, 1000):
        position = np.random.choice(sample_size, sample_size, replace =True)
        sample_bootstrap = sample[position]
        sample_mean = np.mean(sample_bootstrap)
        limite_superior = np.quantile(sample_bootstrap, 0.975)
        limite_inferior = np.quantile(sample_bootstrap, 0.025)
        mean_bootstrap.append(sample_mean)
        limite_superior_bootstrap.append(limite_superior)
        limite_inferior_bootstrap.append(limite_inferior)
    mean_bootstrap = np.mean(mean_bootstrap)
    limite_superior_bootstrap = np.mean(limite_superior_bootstrap)
    limite_inferior_bootstrap = np.mean(limite_inferior_bootstrap)
    return mean_bootstrap, limite_superior_bootstrap, limite_inferior_bootstrap