import click
import os
from sklearn.preprocessing import RobustScaler

from desafio_iafront.data.saving import save_partitioned
from desafio_iafront.jobs.common import prepare_dataframe, transform
from desafio_iafront.jobs.escala_pedidos.constants import get_departamentos_all

@click.command()
@click.option('--visitas-com-conversao', type=click.Path(exists=True))
@click.option('--saida', type=click.Path(exists=False, dir_okay=True, file_okay=False))
@click.option('--data-inicial', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--data-final', type=click.DateTime(formats=["%d/%m/%Y"]))
@click.option('--departamentos', type=str, help="Departamentos separados por virgula")
def main(visitas_com_conversao, saida, data_inicial, data_final, departamentos):
    if departamentos.lower() == "all":
        departamentos_lista = get_departamentos_all()
    else:
        departamentos_lista = [departamento.strip() for departamento in departamentos.split(",")]


    result = prepare_dataframe(departamentos_lista, visitas_com_conversao, data_inicial, data_final)

    # Faz a escala dos valores
    result = transform(result, RobustScaler())

    # salva resultado numa nova pasta
    saida = os.path.join(saida, "robust_scaler")
    os.mkdir(saida)
    save_partitioned(result, saida, ['data', 'hora'])


if __name__ == '__main__':
    main()
