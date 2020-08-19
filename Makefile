data_inicial='01/06/2020'
data_final='01/08/2020'
pedidos='./dataset-desafio-ia-front/pedidos'
visitas='./dataset-desafio-ia-front/visitas'
produtos='./dataset-desafio-ia-front/produtos.csv'
departamento='agro_industria_e_comercio,automotivo,brinquedos,casa_conforto,eletrodomesticos,eletronicos,fashion_calcados,informatica_acessorios,telefonia'
saida='.\saida'
saida_data='.\saida\merge_visitas_pedidos'
saida_conversao='D:\dataset-desafio-ia-front\saida\all_data\conversao'
saida_graphics='.\saida\graphics\'
x_axis='latitude'
y_axis='longitude'
x_axis_hist='preco'

install:


make_directory:
	echo 'Making directory'
	mkdir saida
	mkdir saida/merge_visitas_pedidos
	mkdir saida/graphics
	mkdir saida/conversao

getting_data:
	echo '+-+-+-+Extracting the data+-+-+-+'
	python ./codigo/desafio_iafront/jobs/pedidos/job.py \
		  --pedidos $(pedidos) \
		  --visitas $(visitas) \
		  --produtos $(produtos) \
		  --saida $(saida_data) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final)


standard_data:
	echo 'Scaler: Standard scaler'
	python ./codigo/desafio_iafront/jobs/escala_pedidos/job_standard_scaler.py \
			--visitas-com-conversao $(saida_data)\
			--saida $(saida)\
			--data-inicial $(data_inicial)\
			--data-final $(data_final)\
			--departamentos $(departamento)


standard_scatter:
	echo 'Graph 2: Plotting scatter from Standard scaler data'
	python ./codigo/desafio_iafront/jobs/graphics/job_scatter_hist.py \
			--dataframe-path '${saida}/standard_scaler' \
			--saida $(saida_graphics) \
 	       	--x_axis $(x_axis) \
 	       	--y_axis $(y_axis) \
 	       	--data-inicial $(data_inicial)\
 	       	--data-final $(data_final) \
			--name_to_save 'scatter_standard_scaler'


standard_hist:
	echo 'Hist 2: Plotting scatter from Standard scaler data'
	python ./codigo/desafio_iafront/jobs/graphics/job_scatter_hist.py\
 			--dataframe-path '${saida}/standard_scaler'\
  			--saida $(saida_graphics)\
   			--x_axis $(x_axis_hist)\
    		--y_axis $(y_axis)\
     		--data-inicial $(data_inicial)\
      		--data-final $(data_final)\
       		--type 'hist'\
       		--name_to_save 'preco_hist_standard_scaler'


Bayessian_mg:
	echo "Clustering 4: Bayessian mixture gaussian"
	python ./codigo/desafio_iafront/jobs/clusters/job_bayesian_gaussian_mixture.py \
		  --dataset '${saida}/standard_scaler' \
		  --number_of_cluster 6 \
		  --saida $(saida) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final)

scatter_after_cluster:
	echo "Confidence interval plot"
	python ./codigo/desafio_iafront/jobs/graphics/job_graphics.py\
		  --dataframe-path '${saida}/bayesian_gaussian_mixture/by_data_hora' \
 	      --x_axis $(x_axis) \
 	      --y_axis $(y_axis) \
 	      --cluster_label 'cluster_label' \
		  --saida $(saida_graphics) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final) \
		  --name_to_save 'scatter_bayesian_gaussian_standard'


Confidence_interval:
	echo "Confidence interval plot"
	python ./codigo/desafio_iafront/jobs/graphics/job_pos_cluster_confidencial_interval.py\
		  --dataframe-path '${saida}/bayesian_gaussian_mixture/by_data_hora' \
		  --y_axis 'convertido' \
		  --saida $(saida_graphics) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final) \
		  --name_to_save 'conversao_confidence_interval'

Conversao:
	echo 'Conversao by time'
	python ./codigo/desafio_iafront/jobs/conversao/job_conversao.py\
 			--dataframe-path '${saida}/bayesian_gaussian_mixture/by_data_hora'\
  			--saida $(saida_conversao)\
     		--data-inicial $(data_inicial)\
      		--data-final $(data_final) \
      		--type 'day'

Confidence_line_time:
	echo "Confidence interval plot"
	python ./codigo/desafio_iafront/jobs/graphics/conversao_graphics/job_time_series_line.py\
		  --dataframe-path $(saida_conversao) \
		  --saida $(saida_graphics) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final) \
		  --name_to_save 'time_series_line_day'