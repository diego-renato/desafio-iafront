import pandas as pd
import numpy as np

from bokeh.models import ColumnDataSource, Whisker
from bokeh.plotting import figure
from bokeh.layouts import row
from desafio_iafront.jobs.clusters.clusters import gaussian_mixture
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans

def plot(dataframe: pd.DataFrame, x_axis, y_axis, cluster_label, title="", toolbar_location=None, tools="",):
    clusters = [label for label in dataframe[cluster_label]]

    colors = [set_color(_) for _ in clusters]

    p = figure(title=title, x_axis_label=x_axis, y_axis_label=y_axis)

    p.scatter(dataframe[x_axis].tolist(), dataframe[y_axis].tolist(), fill_color=colors)

    return p
def plot_scatter(dataframe: pd.DataFrame, x_axis, y_axis, title=""):
    x_axis_scaled_position = get_position(x_axis)
    y_axis_scaled_position = get_position(y_axis)

    x_scaled = list(zip(*dataframe.features))[x_axis_scaled_position]
    y_scaled = list(zip(*dataframe.features))[y_axis_scaled_position]

    mean_x_before, var_x_before, mean_y_before, var_y_before = get_statistics(dataframe[x_axis],dataframe[y_axis])

    x_axis_label_before = x_axis + "  mean:%f" % mean_x_before + "  variance:%f" % var_x_before
    y_axis_label_before = y_axis + "  mean:%f" % mean_y_before + "  variance:%f" % var_y_before

    s1 = figure(title="Before scaled ", x_axis_label=x_axis_label_before, y_axis_label=y_axis_label_before)
    s1.scatter(dataframe[x_axis].tolist(), dataframe[y_axis].tolist())

    mean_x_after, var_x_after, mean_y_after, var_y_after = get_statistics(x_scaled, y_scaled)

    x_axis_label_after = x_axis + "  mean:%f" % mean_x_after + "  variance:%f" % var_x_after
    y_axis_label_after = y_axis + "  mean:%f" % mean_y_after + "  variance:%f" % var_y_after
    s2 = figure(title="After scaled ", x_axis_label=x_axis_label_after, y_axis_label=y_axis_label_after)
    s2.scatter(x_scaled, y_scaled)

    p = row(s1, s2)
    return p


def plot_hist(dataframe: pd.DataFrame, x_axis, title=""):
    x_axis_scaled_position = get_position(x_axis)

    x_scaled = list(zip(*dataframe.features))[x_axis_scaled_position]

    x_mean_before, x_var_before, x_mean_after, x_var_after = get_statistics(dataframe[x_axis],x_scaled)

    h1 = figure(title=x_axis + " before scaled mean: " + str(x_mean_before) + "  variance: " + str(x_var_before),
                 y_axis_label="Frequenty")
    hist, edges = np.histogram(dataframe[x_axis].tolist())
    h1.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])

    h2 = figure(title=x_axis + " after scaled  mean: " + str(x_mean_after) + "  variance: " + str(x_var_after),
                y_axis_label="Frequenty")
    hist, edges = np.histogram(x_scaled)
    h2.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:])

    p = row(h1, h2)
    return p

def line_cluster_BIC(dataframe: pd.DataFrame):

    n_cluster = list(dataframe.number_of_cluster)
    BIC_validation = list(dataframe.BIC_validation)
    BIC_train = list(dataframe.BIC_train)

    title = "Optimal number of cluster by gaussian mixture"
    p = figure(title=title,
               toolbar_location=None, tools="", x_axis_label="Number of clusters", y_axis_label="BIC")

    p.line(n_cluster, BIC_validation, line_width=3, line_color="blue", legend="validation")
    p.circle(n_cluster, BIC_validation, fill_color="white", size=8)

    return p

def line_cluster_GAP(dataframe: pd.DataFrame):

    n_cluster = list(dataframe.clusterCount)
    GAP = list(dataframe.gap)

    title = "Optimal number of cluster by GAP statistic"
    p = figure(title=title,
               toolbar_location=None, tools="", x_axis_label="Number of clusters", y_axis_label="GAP")

    p.line(n_cluster, GAP, line_width=2)
    p.circle(n_cluster, GAP, fill_color="white", size=8)

    return p

def line_confidence_intervals(dataframe: pd.DataFrame, y_axis):

    p = figure(title="Confidence interval by cluster",
               toolbar_location=None, tools="", x_axis_label="cluster", y_axis_label=y_axis)

    base, lower, upper, mean_by_cluster = [], [], [], []

    for i, cluster_label in enumerate(list(dataframe.cluster_label.unique())):
        variable_y = dataframe[dataframe["cluster_label"] == cluster_label][y_axis]
        sample_y = len(variable_y)
        mean = variable_y.mean()
        std = variable_y.std()
        lower.append(mean - 1.96*std/np.sqrt(sample_y))
        upper.append(mean + 1.96*std/np.sqrt(sample_y))
        base.append(variable_y)
        mean_by_cluster.append(mean)

    source_error = ColumnDataSource(data=dict(base=base, lower=lower, upper=upper))

    p.add_layout(
        Whisker(source=source_error, base="base", upper="upper", lower="lower")
    )

    x = dataframe["cluster_label"].unique()
    p.circle(x=x, y=lower, color="green", size=20)
    p.circle(x=x, y=upper, color="blue", size=20)
    p.circle(x=x, y=mean_by_cluster, color="red", size=20)
    p.segment(x, lower, x, upper, color="lightgrey", line_width=9)

    return p

def _unique(original):
    return list(set(original))


def set_color(color):
    COLORS = ["green", "blue", "red", "orange", "purple", "yellow", "grey", "lawngreen"]

    index = color % len(COLORS)

    return COLORS[index]

def get_position(axis):
    variables = np.array(['preco', 'prazo', 'frete', 'latitude', 'longitude'])
    position = np.where(variables == axis)
    position = int(np.array(position))
    return position

def get_statistics(variable1,variable2):
    mean1 = np.array(variable1).mean().round(4)
    var1 = np.array(variable1).var().round(4)
    mean2 = np.array(variable2).mean().round(4)
    var2 = np.array(variable2).var().round(4)
    return mean1, var1, mean2, var2

def get_bic_dataframe(dataframe, vector_cluster):
    times = 1

    np.random.seed(140597)
    vector = np.asarray(list(dataframe['features'].to_numpy()))
    mask = np.random.choice([False, True], len(vector), p=[0.98, 0.02])
    vector = vector[mask]
    result = np.zeros((len(vector_cluster), 3))
    sample = np.zeros((times, 1))
    sample_train = np.zeros((times, 1))
    for i, n_cluster_i in enumerate(vector_cluster):
        for time_i in range(times):
            BIC, BIC_train = gaussian_mixture(vector, n_cluster_i, BIC_calculate=True)
            sample[time_i] = BIC
            sample_train[time_i] = BIC_train
        BIC_validation = sample.mean()
        BIC_train = sample_train.mean()
        result[i] = [n_cluster_i, BIC_validation, BIC_train]

    result = pd.DataFrame(result, columns=["number_of_cluster", "BIC_validation", "BIC_train"])
    return result
def get_pca(dataframe, cluster_label: str):

    variable_to_standard = ['preco', 'prazo', 'frete', 'latitude', 'longitude']
    scaled_df = StandardScaler().fit_transform(dataframe[variable_to_standard])
    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(scaled_df)
    principalDf = pd.DataFrame(data=principalComponents
                               , columns=['principal component 1', 'principal component 2'])
    if cluster_label != "null":
        principalDf[cluster_label] = dataframe[cluster_label]
    else:
        principalDf[cluster_label] = 1
    return principalDf


def optimalK(data, maxClusters: int):
    nrefs = 1

    gaps = np.zeros((len(range(1, maxClusters)),))
    results_df = pd.DataFrame({'clusterCount': [], 'gap': []})
    for gap_index, k in enumerate(range(1, maxClusters)):

        refDisps = np.zeros(nrefs)

        for i in range(nrefs):

            randomReference = np.random.random_sample(size=data.shape)

            # Fit to it
            km = KMeans(k)
            km.fit(randomReference)

            refDisp = km.inertia_
            refDisps[i] = refDisp

        km = KMeans(k)
        km.fit(data)

        origDisp = km.inertia_

        gap = np.log(np.mean(refDisps)) - np.log(origDisp)

        gaps[gap_index] = gap

        results_df = results_df.append({'clusterCount': k, 'gap': gap}, ignore_index=True)

    return (gaps.argmax() + 1,
            results_df)


