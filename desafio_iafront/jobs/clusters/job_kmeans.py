from functools import partial

import click
import numpy as np
import os

from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.clusters.clusters import kmeans
from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date


@click.command()
@click.option('--dataset', type=click.Path(exists=True))
@click.option('--number_of_cluster', type=click.INT)
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
def main(dataset: str, number_of_cluster: int, saida: str, data_inicial, data_final):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)

    dataset = read_partitioned_json(file_path=dataset, filter_function=filter_function)
    vector = np.asarray(list(dataset['features'].to_numpy()))
    coordinates, labels = kmeans(vector, number_of_cluster)

    dataset['cluster_coordinate'] = list(coordinates)

    dataset['cluster_label'] = list(labels)

    saida = os.path.join(saida, "kmeans")
    os.mkdir(saida)

    by_cluster_data_hora = os.path.join(saida, "by_cluster_data_hora")
    os.mkdir(by_cluster_data_hora)

    by_data_hora_cluster = os.path.join(saida, "by_data_hora_cluster")
    os.mkdir(by_data_hora_cluster)

    by_data_hora = os.path.join(saida, "by_data_hora")
    os.mkdir(by_data_hora)
    print("Directory successfully created")

    save_partitioned(dataset, by_cluster_data_hora, ['cluster_label', 'data', 'hora'])
    save_partitioned(dataset, by_data_hora_cluster, ['data', 'hora', 'cluster_label'])
    save_partitioned(dataset, by_data_hora, ['data', 'hora'])

if __name__ == '__main__':
    main()
