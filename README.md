# Divorce prediction webapp

## Dataset:

The dataset can be found on kaggle (https://www.kaggle.com/datasets/andrewmvd/divorce-prediction)

## Data processing and Model creation:

The data processing, model creation and model training finds place in the divorce.ipynb.
After training i did some feature importance calculations and indeed some features doesnt seem to have an impact, so they could be removed.

## Webapp

To start the webapp created with gradio:

```
python gradio_app.py
```

Now you can visit the URL presented by you in the terminal and try out the divorce predictor.

![image](https://github.com/aiko929/divorce_webapp/assets/26790700/e6b44b01-89ca-492e-9502-2090112ad83a)

## Results of the feature importance:

![image](https://github.com/aiko929/divorce_webapp/assets/26790700/e9b8f7f1-8cc0-4941-a59e-8274bd91b756)
