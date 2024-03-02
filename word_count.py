"""Taller evaluable"""

import glob

import pandas as pd


def load_input(input_directory):
    """Load text files in 'input_directory/'"""
    #
    # Lea los archivos de texto en la carpeta input/ y almacene el contenido en
    # un DataFrame de Pandas. Cada línea del archivo de texto debe ser una
    # entrada en el DataFrame.
    #
    filenames = glob.glob(f"{input_directory}/*.txt")
    
    #df =pd.read_csv(filenames[0], sep="\t", header=None, names=["text"])

    dataframes=[
        pd.read_csv(filename, sep="\t", header=None, names=["text"])
        for filename in filenames
    ]

    concatenated_df = pd.concat(dataframes, ignore_index=True)
    return concatenated_df

def clean_text(dataframe):
    """Text cleaning"""
    #
    # Elimine la puntuación y convierta el texto a minúsculas.
    #
    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.lower()

    # Remove punctuation
    dataframe["text"] = dataframe["text"].str.replace(r"[^\w\s]", "")
    #Este primero elimina todos los signos de puntuación y borra los caracteres especiales
    dataframe["text"] = dataframe["text"].str.replace(".","")
    dataframe["text"] = dataframe["text"].str.replace(",","")

    return dataframe

def count_words(dataframe):
    """Word count"""

    # dataframe = dataframe.copy()
    # dataframe["text"] = dataframe["text"].str.split()
    # dataframe = dataframe.explode("text")
    # dataframe['count'] = 1

    # dataframe=dataframe.groupby("text").agg(
    #     {"count":"sum"}
    # )

    dataframe = dataframe.copy()
    dataframe["text"] = dataframe["text"].str.split()
    dataframe = dataframe.explode("text")
    dataframe = dataframe['text'].value_counts()

    return dataframe




def save_output(dataframe, output_filename):
    """Save output to a file."""
    #
    # Guarde el conteo de palabras en un archivo de texto.
    #
    dataframe.to_csv(output_filename, sep="\t", index=True,header=False)

#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
    
# ctxt=clean_text(load_input("input"))
# wctxt=count_words(ctxt)
# save_output(wctxt,"output.txt")

def run(input_directory, output_filename):
    """Call all functions."""

    dataframe = load_input(input_directory)
    dataframe = clean_text(dataframe)
    dataframe = count_words(dataframe)
    save_output(dataframe, output_filename)


if __name__ == "__main__":
    run(
        "input",
        "output.txt",
    )
