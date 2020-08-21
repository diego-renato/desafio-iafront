import click
from bokeh.io import output_file, save, show
from functools import partial


from desafio_iafront.jobs.graphics.utils import line_cluster_BIC, get_bic_dataframe
from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date


@click.command()
@click.option('--dataframe-path', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--number-of-cluster', type=click.INT, help='A number of k to be computed')
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--name_to_save')
def main(dataframe_path: str, saida: str,  number_of_cluster: int, data_inicial, data_final, name_to_save):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(dataframe_path, filter_function=filter_function)

    vector_cluster = list(range(2, int(number_of_cluster)+1))
    dataframe = get_bic_dataframe(dataframe, vector_cluster)
    output_file(saida+str(name_to_save)+".html")
    figura = line_cluster_BIC(dataframe)

    save(figura)


if __name__ == '__main__':
    main()