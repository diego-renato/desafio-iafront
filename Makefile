data_inicial='01/06/2020'
data_final='01/08/2020'
pedidos='D:/dataset-desafio-ia-front/pedidos'
visitas='D:/dataset-desafio-ia-front/visitas'
produtos='D:/dataset-desafio-ia-front/produtos.csv'
departamento='agro_industria_e_comercio,automotivo,brinquedos,casa_conforto,eletrodomesticos,eletronicos,fashion_calcados,informatica_acessorios,telefonia'
saida='.\saida'
saida_data='.\saida\merge_visitas_pedidos'
saida_conversao='.\saida\conversao'
saida_graphics='.\saida\graphics\'
x_axis='latitude'
y_axis='longitude'
x_axis_hist='preco'


run_all: make_directory get_data standard_data standard_scatter standard_hist bayesian_mg scatter_after_cluster confidence_interval get_conversao confidential_line_time

make_directory:
	echo 'Making directory'
	mkdir saida
	mkdir saida/merge_visitas_pedidos
	mkdir saida/graphics
	mkdir saida/conversao

get_data:
	echo '+-+-+-+Extracting the data+-+-+-+'
	prepare_pedidos \
		  --pedidos $(pedidos) \
		  --visitas $(visitas) \
		  --produtos $(produtos) \
		  --saida $(saida_data) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final)

standard_data:
	echo 'Scaler: Standard scaler'
	standard_scaler \
			--visitas-com-conversao $(saida_data)\
			--saida $(saida)\
			--data-inicial $(data_inicial)\
			--data-final $(data_final)\
			--departamentos $(departamento)

standard_scatter:
	echo 'Graph 2: Plotting scatter from Standard scaler data'
	plot \
			--dataframe-path ${saida}'\standard_scaler' \
			--saida $(saida_graphics) \
 	       	--x_axis $(x_axis) \
 	       	--y_axis $(y_axis) \
 	       	--data-inicial $(data_inicial)\
 	       	--data-final $(data_final) \
			--name_to_save 'scatter_standard_scaler'

standard_hist:
	echo 'Hist : Plotting scatter from Standard scaler data'
	plot \
 			--dataframe-path ${saida}'\standard_scaler'\
  			--saida $(saida_graphics)\
   			--x_axis $(x_axis_hist)\
    		--y_axis $(y_axis)\
     		--data-inicial $(data_inicial)\
      		--data-final $(data_final)\
       		--type 'hist'\
       		--name_to_save 'preco_hist_standard_scaler'

bayesian_mg:
	echo "Clustering: Bayessian mixture gaussian"
	bayesian_gaussian_mixture \
		  --dataset ${saida}'\standard_scaler' \
		  --number_of_cluster 6 \
		  --saida $(saida) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final)

scatter_after_cluster:
	echo "Scatter of longitude and latitude by cluster"
	scatter_plot \
		  --dataframe-path ${saida}'\bayesian_gaussian_mixture\by_data_hora' \
 	      --x_axis $(x_axis) \
 	      --y_axis $(y_axis) \
 	      --cluster_label 'cluster_label' \
		  --saida $(saida_graphics) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final) \
		  --name_to_save 'scatter_bayesian_gaussian_standard'


confidence_interval:
	echo "Confidence interval plot of convertido"
	confidential_intervals_plot\
		  --dataframe-path ${saida}'\bayesian_gaussian_mixture\by_data_hora' \
		  --y_axis 'convertido' \
		  --saida $(saida_graphics) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final) \
		  --name_to_save 'conversao_confidence_interval'

get_conversao:
	echo 'Obtaining Conversao'
	prepare_conversao\
 			--dataframe-path ${saida}'\bayesian_gaussian_mixture\by_data_hora' \
  			--saida $(saida_conversao)\
     		--data-inicial $(data_inicial)\
      		--data-final $(data_final) \
      		--type 'hora'

confidential_line_time:
	echo "Confidential interval plot"
	time_series_plot \
		  --dataframe-path $(saida_conversao) \
		  --saida $(saida_graphics) \
		  --data-inicial $(data_inicial) \
		  --data-final $(data_final) \
		  --name_to_save 'time_series_line_day'