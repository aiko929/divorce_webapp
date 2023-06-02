import pickle
import gradio as gr
import pandas as pd
import numpy as np

df = pd.read_csv("reference.tsv", sep="|")
df = df["description"]

with open("model.pickle", "rb") as file:
    model = pickle.load(file)

sliders = []

for i, inf in enumerate(df):
    sliders.append(
        gr.Radio(
            choices=[
                "Never",
                "Seldom",
                "Averagely",
                "Frequently",
                "Always"
            ],
            value="Never",
            info=inf,
            label=f"Question {i}:"
        )
    )


def predict_divorce(*args):
    array = []
    value_map = {"Never": 0,
                 "Seldom": 1,
                 "Averagely": 2,
                 "Frequently": 3,
                 "Always": 4}
    for arg in args:
        array.append(value_map[arg])

    array = np.array(array).reshape(1, -1)
    result = model.predict(array)[0]

    data = {"Divorce": float(result[0]),
            "Stayed Married": 1 - float(result[0])}
    print(data)
    return data


demo = gr.Interface(
    fn=predict_divorce,
    inputs=sliders,
    outputs=gr.Label(),
    title="Divorce Prediction",
    description="Questions are based on: Divorce Predictors Scale variables (DPS)"
                " on the basis of Gottman couples therapy. Model trained on a "
                "dataset of Turkey couples that are divorced or happily married."

)

demo.launch(server_name="0.0.0.0", share=True)

# %%
