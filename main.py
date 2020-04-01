import pandas as pd
import os
from imageio import imread
import numpy as np
from matplotlib import pyplot as plt

file_headers = ["# Frame", " x(0-1024)", " y(0-1024)", " obj id", " bounding size(0-1024^2)",
                " sequence(may be normalized)", " num objects", " current_time", " current_milli"]

header = ["frame", "x", "y", "obj_id", "bounding_size",
          "sequence", "num_objects", "current_time", "current_milli"]
color_list = [[0, 0, 0], [255, 255, 255], [0, 255, 0], [255, 0, 0], [0, 0, 255], [0, 0, 0], [255, 255, 255],
              [0, 255, 0], [255, 0, 0], [0, 0, 255]]

def read_directory(path):
    for root, dirs, files in os.walk(path):
        files.sort()
        yield from files

def read_csv(file):
    with open(file, newline='') as csvfile:
        df = pd.read_csv(csvfile, header=3, usecols=file_headers)
        df.columns = header
        return df

if __name__ == "__main__":

    image = imread("base.png")
    directory = read_directory("oddetectData ")
    data = next(directory)
    df = read_csv("oddetectData/" + data)
    for index, row in df.iterrows():
        x = int(row["x"])
        y = int(row["y"])
        obj_id = int(row["obj_id"])
        obj_id = obj_id % 10
        image[x - 2:x + 2, y - 2:y + 2, 0:3] = color_list[obj_id]
    plt.imshow(image)
    plt.show()
