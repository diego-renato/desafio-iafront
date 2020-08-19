import click

from bokeh.io import output_file, save
from functools import partial

from desafio_iafront.jobs.graphics.utils import line_confidence_intervals
from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date

@click.command()
@click.option('--dataframe-path', type=click.Path(exists=True), help="Path of data that contains clusters")
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--y_axis')
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--name_to_save')
def main(dataframe_path: str, saida: str, y_axis, data_inicial, data_final, name_to_save):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(dataframe_path, filter_function=filter_function)

    output_file(saida+str(name_to_save)+".html")
    figura = line_confidence_intervals(dataframe=dataframe, y_axis=y_axis)
    save(figura)


if __name__ == '__main__':
    main()
