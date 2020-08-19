## Table of contents
- [1. The problem](#1-the-problem)
- [2. The data](#2-the-data)
- [3. Comparing different scaler functions](#3-comparing-different-scaler-functions)
    - [3.1. Data transformation: scatter and hist (01-06-2020 to 07-06-2020)](#scatter-plots)
    - [3.2. Data transformation: scatter and hist (24-06-2020 to 30-06-2020)](#scatter-plots)
- [4. The optimal number of clusters](#4-the-optimal-number-of-clusters)
- [5. The optimal cluster algorithm](#5-the-optimal-cluster-algorithm)
- [6. Evaluating the *conversão total* in each cluster](#6-evaluating-the-*conversão-total*-in-each-cluster)
- [7. Answering the questions](#7-answering-the-questions)

# 1. The problem
B2W wants to know more about its customers, in the sense that B2W wants to know what is important to them, for this the B2W 
data scientists propose to study the behavior of the total conversion through cluster formations. The total conversion is 
the number of orders in relation  to the number of visits. Our objective in this challenge is to create a cluster to then be able
 to analyze the main variable and make decisions. 
# 2. The data
The dataset contains variables about the products, customer location and the time. The variables selected for this analyses are :
* preço
* prazo 
* frete  
* latitude 
* longitude 

The considered period is from 01/06/2020 to 31/07/2020. The departaments selected are: 'agro_industria_e_comercio,automotivo,brinquedos,casa_conforto,eletrodomesticos,eletronicos,fashion_calcados,informatica_acessorios,telefonia'


# 3. Comparing different scaler functions
After scaling the data, is important to see the behavior of the scaled or transformed data.
In this section I compared the different scaler jobs from the considered in this project for the week 01-06-2020 - 07-06-2020 and
the week 24/07/2020 - 30/08/2020 by scatter plots and histograms. The variables selected are <b>longitude</b>, <b>latitude</b> and <b>preço</b> because are variables
to be considered to obtain clusters in the next section.  

* I considered in the scatter plot the variables <b>longitude</b> and <b>latitude</b>, because this variables generate a the distribution of the customer in Brazil.
* I considered <b>preço</b> for the histogram.

#### Data transformation: scatter and hist (01-06-2020 to 07-06-2020)

##### Scatter plots
<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/before_scatter_semana1.png" />
    <p>Figure 1.1: Longitude vs latitude of the customers before transformation.</p>
</div>
<br>
<br>
<br>

Normalization              |  Standard scaler          | Max abs scaler
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/after_normalization_scatter_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/aftet_scatter_standard_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/after_scatter_max_abs_semana1.png" />

Min max scaler             |  Power transformer        | Robust scaler 
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/after_min_max_scatter_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/after_scatter_power-transformer_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/after_scatter_robust_scaler_semana1.png" />

<p>Figure 1.2: Longitude vs latitude of the customers after transformation.</p>

##### Histograms plot
<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/preco_before_semana1.png" />
    <p>Figure 1.1: Frequency histogram of preço of the considered products from customers before transformation.</p>
</div>
<br>
<br>
<br>

Normalization              |  Standard scaler          | Max abs scaler
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/normalization_after_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/standard_after_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/max_abs_after_semana1.png" />

Min max scaler             |  Power transformer        | Robust scaler 
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/min_max_after_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/powerTransformer_after_semana1.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana1/robust_scaler_after_semana1.png" />

<p>Figure 2.2: Frequency histogram of preço of the considered products from customers after transformation.</p>

#### Data transformation: scatter and hist (24-06-2020 to 30-06-2020)

##### Scatter plots
<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/scatter_before_semana2.png" />
    <p>Figure 3.1: Longitude vs latitude of the customers before transformation.</p>
</div>
<br>
<br>
<br>

Normalization              |  Standard scaler          | Max abs scaler
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/after_scatter_normalziation_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/after_scatter_standard_scaler_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/after_scatter_max_abs_semana2.png" />

Min max scaler             |  Power transformer        | Robust scaler 
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/after_scatter_min_max_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/after_scatter_power_transformer_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/after_scatter_robust_scaler_semana2.png" />

<p>Figure 1.2: Longitude vs latitude of the customers after transformation.</p>

##### Histograms plot
<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/preco_before_semana2.png" />
    <p>Figure 3.1: Frequency histogram of preço of the considered products from customers before transformation.</p>
</div>
<br>
<br>
<br>

Normalization              |  Standard scaler          | Max abs scaler
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/normalization_after_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/standard_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/max_abs_after_semana2.png" />

Min max scaler             |  Power transformer        | Robust scaler 
:-------------------------:|:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/min_max_after_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/powerTransformer_after_semana2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/semana2/robust_scaler_semana2.png" />

<p>Figure 3.2: Frequency histogram of preço of the considered products from customers after transformation.</p>

Some observation for this section:
* The standard, min-max, max abs and robust scalers have the best results in the sense that the variables have the same behaviour.
* The power transformer and normalization modify the distribution of variables (not good for our case).
* The standard, min-max and max abs scalers(in this order) have the best results because they don't modify the distributions of the points and also have similar statistics(mean and variance).
* The methods selected are standard, min-max and max abs scalers.
* The distribution are not affected by the time as we can see in the graphics. 
* The variable price is continuous uniform distributed(all points have the same weight).
# 4. The optimal number of clusters
<b>OBS.</b> Because the distribution of the variables considered for clustering are not affected by the time, I decided to make decisions(optimal *K* and best clustering method) taking a sample like 1 week.
 
The number of cluster is considered a hyperparameter, in the literature there are different ways to find the optimal number of cluster. 
For example from short datasets the hierarchical clustering is a good option(not in our case), the elbow method(graphics method) or 
the GAP statistic(ca be used in any clustering method), but there is another and powered method using a distribution probability actually a 
finite mixture distribution and computing some information criterion like AIC or BIC, it is the finite gaussian mixture. The gaussian mixture 
is a parametric probability distribution from *K* gaussian or normal random variables. For short explanation let see the equation above
 
<img src=https://wikimedia.org/api/rest_v1/media/math/render/svg/2f13843df7f69545e27b06c4b59f1d8fe9690ce1>

The *N(.)* denote a multivariate normal distribution with a vector of means and matrix of covariance, the 
phi denote the probability for a *latent variable* belong a one population, the *latent variable* is actually the cluster and
the number *K* is the number of cluster or populations. Please see [gaussian mixture](http://leap.ee.iisc.ac.in/sriram/teaching/MLSP_16/refs/GMM_Tutorial_Reynolds.pdf)
if you want to see more details. One limitation is that the data can't be 5 normal multivariate distributed. 

<b>OBS.</b> The individual distribution of the variables doesn't say anything about if it is normal multivariate distributed.

The benefit of using the gaussian mixture is that the dataset belows a multivariate distribution, they don´t need to be scaled
 and the log likelihood can be computed and also be compared for different k values (clusters). And also, we can predict the cluster from a given
 vector of observation with their respective probability.
 
So, for our case, it is considered a grid of values, *K = 2,3,...,10* ,to compute the BIC (Bayesian information criterion) using train-test split. Then,
the optimal number of cluster is the value of *K* that minimize the BIC in the train data and test data(30% of original data). This is important because we can evaluate in a
unobserved dataset(Observation: The BIC penalizes the -2 log likelihood by the number of parameters *log(n)). The following graph shows the results obtained.

<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/otimo_number_of%20cluster/optimal_cluster_bgm.jpg" />
    <p>Figure 4: BIC values from validation set using finite gaussian mixture .</p>
</div>
<br>
<br>
<br>

Also, I tried the GAP statistic using k-means. The GAP statistic, (see the original paper[GAP](https://statweb.stanford.edu/~gwalther/gap)), is obtained by taking the expected value
 of the mean for every distance pairwase for each cluster minus the logarithm of this mean. The optimal number of *K* is that maximize the GAP statistic.
In the next graph we can see different values of *K* with the respective GAP value.
 
 <div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/otimo_number_of%20cluster/optimal_GAP.jpg" />
    <p>Figure 5: GAP statistic from k-means .</p>
</div>
<br>
<br>
<br>

The decision is to use *K*=6, as we can see in the Figure 4, the BIC decrease as the number of cluster increases but for number of cluster greater than 6 the BIC increases.
The GAP statistic indicate that the optimal value is 8, so clearly we can see that the optimal number of cluster is between 6 and 8. Using these two references I decided to take *K*=6 and then evaluate if this make sense. 
 
# 5. The optimal cluster algorithm

In this section, the three selected method for scaling data and three algorithms: kmeans, gaussian mixture and bayesian mixture are evaluated and compared one to one.
I decided to plot the scatter plot from the section 3, and some other plot taking the confidence intervals. 

<b>OBS.</b> The bayesian gaussian mixture is not the same from gaussian mixture, actually, it's a generalization of the gaussian mixture but not at all. The main difference is that the parameters of the bayesian model have a stochastic behavior,
in other words, they are not constant. 

In the next graphics, different scatter plots are presented from the three types of algorithms and scaler functions.

Scaling method             | Kmeans                    |  gaussian mixture         | bayesian gaussian mixture
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Standard scaler            |<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_kmeans_standard.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_gaussian_mixture_standard.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_bayesian_gaussian_mixture_standard.png" />
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Min max scaler             |<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_kmeans_min_max.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_gaussian_mixture_min_max.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_bayesian_gaussian_mixture_min_max.png" />
:-------------------------:|:-------------------------:|:-------------------------:|:-------------------------:
Max abs scaler             |<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_kmeans_max_abs.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_gaussian_mixture_max_abs.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/scatter_bayesian_gaussian_mixture_max_abs.png" />

<p>Figure 6: Longitude vs latitude of the customers of B2W: three types of clustering and scaling methods.</p>

As we can see, the best results are from the standard scaler and from the kmeans and bayesian gaussian mixture. The main reason why the standard scaler is the best is because:

* The standard scaler doesn't modify the distribution of the points and also the mean and variance are 0 and 1 respectively, in other words, the variables are centered and have the same scaling (the same weight.)
* Outliers are good in clustering, because in clustering we want to identify subpopulations different from others subpopulations. 

Next, to take a decision between kmeans and bayesian gaussian mixture, the following graphic shows the confidential intervals from the five variables included in the clustering analysis.


Variable                   | kmeans                     | bayesian gaussian mixture
:-------------------------:|:-------------------------:|:-------------------------:
Preço                      | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/preco_confidence_interval_cluster_kmeans.jpg" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/preco_confidence_interval_cluster_BGM.jpg" />
:-------------------------:|:-------------------------:|:-------------------------:
Frete                      | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/frete_confidence_interval_cluster_kmeans.jpg" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/frete_confidence_interval_cluster_BGM.jpg" />
:-------------------------:|:-------------------------:|:-------------------------:
Prazo                      | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/prazo_confidence_interval_cluster_kmeans.jpg" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/prazo_confidence_interval_cluster_BGM.jpg" />
:-------------------------:|:-------------------------:|:-------------------------:
Longitude                  | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/longitude_confidence_interval_cluster_kmeans.jpg" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/longitude_confidence_interval_cluster_BGM.jpg" />
:-------------------------:|:-------------------------:|:-------------------------:
Latitude                   | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/latitude_confidence_interval_cluster_kmeans.jpg" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/cluster_scatter_evaluation/latitude_confidence_interval_cluster_BGM.jpg" />

<p>Figure 7: Kmeans and bayesian gaussian mixture: comparing the differences in each variable.</p>


The red, blue and green dots are the respective means, upper limit and lower limit of each variable. Statistically with 95% confidence(or 5% significance), there are non-significant clusters for example in kmeans and prazo variable, there is not enough evidence
that the cluster 0 and 2 are different,  is the same from cluster 1 and 4, cluster 3 and 5.

The chosen clustering method is bayesian gaussian mixture by vote of greater significant differences between clusters in the variables.

# 6. Evaluating the *conversão total* in each cluster

Before clustering the dataset in the period 01/06/2020 - 31/07/2020, we are interested in the main objective: evaluate the main variables in each cluster.
The conversão total is obtained taking the ratio of number of purchases to number of visits in such period. The next graphic shows the confidence interval of the main variable *conversão*.

<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/conversao/conversao_confidence_interval.jpg" />
    <p>Figure 8: Differences in *conversão total* with their respective confidential intervals for each cluster.</p>
</div>
<br>
<br>
<br>

<div align="center">
    <img width="450" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/conversao/time_series_line.jpg" />
    <p>Figure 9: Time series(days) *conversão* by cluster.</p>
</div>
<br>
<br>
<br>

In the Figure 8, we can see the confidential intervals of *conversão total* from 01/06/2020 to 31/07/2020 by cluster. 
There is not enough evidence that the cluster 0, 1 ,2 and 3 are different with 5% of significance, but comparing the cluster 4 with 
the 0, 1, 2 and 3 there is enough evidence to not reject that there are differences between clusters. In other words, at the end, 
the worst clusters are 0, 1, 2 and 3 with respect to the behaviour of *conversão total* variable. Next, in the Figure 9 shows the behaviour of *conversão* 
through time, the cluster 2 is unstable through time (see also the Figure 8 - width of confidence intervals). The cluster 5 have is the cluster with the 
better behavior.

The next graphics present the *conversão* through time with bootstrap conficencial intervals. The bootstrap conficencial intervals use sampling with replacement to obtain the quantile in the position 2.5% and 97.5%. 

Clusters                   |           Cluster
:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/conversao/cluster_by_day_0_2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/conversao/cluster_by_day_3_5.png" /> 

<p>Figure 10: Time series(days) *conversão* by cluster and boostrap confidencial intervals at 95%.</p>

Cluster                    |           Cluster
:-------------------------:|:-------------------------:
<img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/conversao/cluster_by_hora_0_2.png" /> | <img width="750" src="https://github.com/diego-renato/desafio-iafront/blob/branch-edit/resultados_gr%C3%A1ficos/conversao/cluster_by_hora_3_5.png" /> 

<p>Figure 11: Time series(hours) *conversão* by cluster and boostrap confidencial intervals at 95%.</p>

# 7. Answering the questions

* Usando uma semana de dados como entrada e vendo os gráficos, o que você pode dizer sobre cada uma das transformações?
 As transformações como normalization e power transformer mudam a distribuição dos pontos, por exemplo a transformação de power
 transformer utiliza uma variante do método Box Cox e o Box Cox utiliza a função logaritmica para ele correguir a falta de normalidade.
 Os métodos como standard, min max, max abs e robust scaler não mudam a distribuição dos pontos, estes tentam uniformizar as variáveis, porém
 o metodo standard scaler foi uns dos melhores. 
* Use uma semana diferente, o que você viu mudando?
A distribuição dos pontos das variáveis não são afeitados através do tempo.
* Quais colunas escolheu para gerar suas análises, e por quê?
As variáveis escolhidas foram: preço, latitude e longitude. As variáveis latitude e longitude geram um mapa da poblação alvo.
A variável preço por ser muito interessante, este está uniformemente distribuida assim como o frete. 
* Quais colunas sofreram maiores efeitos e quai sofretam menos?
As variáveis que mais sofreram efeitos nos métodos de transformação como normalization e power transformer foram as variáveis que tem 
um comportamente muito distante da normal por exemplo a variável preço, frete.

* Quais clusters têm problemas para serem analisados?
Os clusters 0,1,2 e 3 são os que tem maiores problemas no periodo total porque com un nível de significancia ao 5%, não tem-se suficiente evidência para estes sejam 
diferentes.
* Quais clusters têm uma evolução ruim ao longo do tempo, e quais têm uma evolução boa.
O cluster 2 tem muita variabilidade através do tempo, esto quer dizer que ele é inestável como pode-se ver na Figura 9.
O cluster 5 é o contrario, ele é mais estável e tem uma *conversão total* maior que os outros.
* Quais clusters você considera que precisam de mais investimento para ampliar a conversão?
Se tomamos como referência no periodo total, os cluster 0, 1, 2 e 3 porque eles são considerados como um só. Se tomamos como referência o 
comportamento através do tempo o cluster 2 sería uma ótima opção, já que ele tem muita variabilidade, assim intentar estudar o porque dessa 
variabilidade para ser reduzida.
* Você consegue identificar algum fenômeno temporal que gere destaque a um ou mais clusters? 

O cluster 2 tem heterocedasticidade(variação não constante ao longo do tempo). Nas Figuras 10 e 11, pode-se apreciar as cartas de control, assim, pontos
fora da linha inferior e superior indicam pontos anormais.  