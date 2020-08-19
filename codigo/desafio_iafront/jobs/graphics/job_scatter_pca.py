import click

from bokeh.io import output_file, save, show
from functools import partial

from desafio_iafront.jobs.graphics.utils import plot, get_pca
from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date


@click.command()
@click.option('--dataframe-path', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--cluster_label', default="null")
@click.option('--components', default=2)
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--name_to_save')
def main(dataframe_path: str, saida: str, cluster_label: str, components, data_inicial, data_final, name_to_save):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(dataframe_path, filter_function=filter_function)

    principalDf = get_pca(dataframe, cluster_label)

    output_file(saida+str(name_to_save)+".html")
    figura = plot(principalDf, 'principal component 1', 'principal component 2', cluster_label)
    save(figura)



if __name__ == '__main__':
    main()