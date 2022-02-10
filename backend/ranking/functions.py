from .models import Circuit
import pandas as pd


def loadCircuitsFromDataFile(path):
    # TODO: no validation :o
    df_circuits = pd.read_csv(path)
    for _, row in df_circuits.iterrows():
        circuit = Circuit(row["circuitId"], row["circuitRef"], row["name"], row["location"],
                          row["country"], row["lat"], row["lng"], row["alt"], row["url"])
        circuit.save()
