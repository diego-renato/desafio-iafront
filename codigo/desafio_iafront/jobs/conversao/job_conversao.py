import click
import pandas as pd
from functools import partial

from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date
from desafio_iafront.data.saving import save_partitioned

@click.command()
@click.option('--dataframe-path', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--type', default="dia")
def main(dataframe_path: str, saida: str, data_inicial, data_final, type):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(dataframe_path, filter_function=filter_function)
    if type.lower() == "hora":
        dataframe = dataframe.groupby(["data", "hora", "cluster_label"]).convertido.mean().reset_index()
        save_partitioned(dataframe, saida, ['data', 'hora', 'cluster_label'])
    else:
        dataframe = dataframe.groupby(["data", "cluster_label"]).convertido.mean().reset_index()
        save_partitioned(dataframe, saida, ['data', 'cluster_label'])

if __name__ == '__main__':
    main()