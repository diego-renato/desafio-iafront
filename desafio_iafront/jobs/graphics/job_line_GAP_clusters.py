import click
import numpy as np

from bokeh.io import output_file, save, show
from functools import partial


from desafio_iafront.jobs.graphics.utils import line_cluster_GAP, optimalK
from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date

@click.command()
@click.option('--dataframe-path', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--number-of-cluster', type=click.INT)
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--name_to_save')
def main(dataframe_path: str, saida, number_of_cluster: int, data_inicial, data_final, name_to_save):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)

    dataset = read_partitioned_json(file_path=dataframe_path, filter_function=filter_function)
    vector = np.asarray(list(dataset['features'].to_numpy()))
    k, gapdf = optimalK(data=vector, maxClusters=number_of_cluster+1)

    output_file(saida + str(name_to_save) + ".html")
    figura = line_cluster_GAP(gapdf)

    save(figura)


if __name__ == '__main__':
    main()