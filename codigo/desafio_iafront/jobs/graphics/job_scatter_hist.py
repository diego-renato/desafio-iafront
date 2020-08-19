import click

from bokeh.io import output_file, save
from functools import partial

from desafio_iafront.jobs.graphics.utils import plot_hist, plot_scatter
from desafio_iafront.data.dataframe_utils import read_partitioned_json
from desafio_iafront.jobs.common import filter_date

@click.command()
@click.option('--dataframe-path', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--x_axis')
@click.option('--y_axis')
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--type', default="scatter")
@click.option('--name_to_save')
def main(dataframe_path: str, saida: str, x_axis, y_axis, data_inicial, data_final, type, name_to_save):
    filter_function = partial(filter_date, data_inicial=data_inicial, data_final=data_final)
    dataframe = read_partitioned_json(dataframe_path, filter_function=filter_function)

    output_file(saida+str(name_to_save)+".html")
    if type.lower() =="hist":
        figura = plot_hist(dataframe=dataframe, x_axis=x_axis)
    else:
        figura = plot_scatter(dataframe=dataframe, x_axis=x_axis, y_axis=y_axis)
    save(figura)


if __name__ == '__main__':
    main()
