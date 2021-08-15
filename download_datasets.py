import kaggle

kaggle.api.authenticate()
kaggle.api.dataset_download_files('arefrazavi/fasttext-dataset', path='datasets', unzip=True)

