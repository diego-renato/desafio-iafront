from setuptools import setup, find_packages

setup(
    name='desafio_iafront',
    version='',
    packages=find_packages(),
    url='',
    license='',
    author='Time IA-FRONT',
    author_email='',
    description='',
    install_requires=[
        "scikit-learn==0.23.1",
        "click==7.1.2",
        "bokeh==2.1.1",
        "dataset-loader==1.6",
        'pandas==1.1.0',
        'numpy==1.19.1'
    ],
    entry_points={
        'console_scripts': [
            'prepare_pedidos=codigo.desafio_iafront.jobs.pedidos.job:main',
            'prepare_conversao=codigo.desafio_iafront.jobs.conversao.job_conversao:main',
            'standard_scaler=codigo.desafio_iafront.jobs.escala_pedidos.job_standard_scaler:main',
            'max_abs_scaler=codigo.desafio_iafront.jobs.escala_pedidos.job_max_abs_scaler:main',
            'min_max_scaler=codigo.desafio_iafront.jobs.escala_pedidos.job_min_max_scaler:main',
            'normalization_scaler=codigo.desafio_iafront.jobs.escala_pedidos.job_normalizacao_scaler:main',
            'power_transformer=codigo.desafio_iafront.jobs.escala_pedidos.job_power_transformer:main',
            'robust_scaler=codigo.desafio_iafront.jobs.escala_pedidos.job_robust_scaler:main',
            'kmeans=codigo.desafio_iafront.jobs.clusters.job_kmeans:main',
            'mini_batch_kmeans=codigo.desafio_iafront.jobs.clusters.job_mini_batch_kmeans:main',
            'birch=codigo.desafio_iafront.jobs.clusters.job_birch:main',
            'gaussian_mixture=codigo.desafio_iafront.jobs.clusters.job_gaussian_mixture:main',
            'bayesian_gaussian_mixture=codigo.desafio_iafront.jobs.clusters.job_bayesian_gaussian_mixture:main',
            'spectral_clustering=codigo.desafio_iafront.jobs.clusters.job_spectral_clustering:main',
            'BIC_decision_plot=codigo.desafio_iafront.jobs.graphics.job_line_BIC_clusters:main',
            'GAP_decision_plot=codigo.desafio_iafront.jobs.graphics.job_line_GAP_clusters:main',
            'scatter_plot=codigo.desafio_iafront.jobs.graphics.job_graphics:main',
            'plot=codigo.desafio_iafront.jobs.graphics.job_scatter_hist:main',
            'pca_plot=codigo.desafio_iafront.jobs.graphics.job_scatter_pca:main',
            'confidential_intervals_plot=codigo.desafio_iafront.jobs.graphics.job_pos_cluster_confidencial_interval:main',
            'time_series_plot=codigo.desafio_iafront.jobs.graphics.conversao_graphics.job_time_series_line:main'

        ]
    }
)
