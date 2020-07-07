import os
import json

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_series(path):
    dataFrames = []
    for filename in os.listdir(path):
        if filename.endswith(".json"):
            try:
                with open(os.path.join(path, filename)) as iperf3FileLog:
                    iperf3Data = json.load(iperf3FileLog)
                    if "error" in iperf3Data:
                        print("File \"", filename, "\" contains error: \"", iperf3Data["error"], "\". Skipping...")
                    else:
                        for interval in iperf3Data["intervals"]:
                            time = iperf3Data["start"]["timestamp"]["timesecs"]
                            speed = interval["sum"]["bits_per_second"]/1024/1024
                            dataFrames.append(pd.DataFrame({"timepoint": [time],
                                                            "Upload Speed": [speed]}))
            except json.decoder.JSONDecodeError:
                print("Skipped file", filename)

    totalDataFrame = pd.concat(dataFrames)

    plt.show()

    fig = plt.figure(figsize=(24, 9))
    sns.set(style="ticks")
    sns.boxplot(x="timepoint", y="Upload Speed", data=totalDataFrame)
    plt.show()


if __name__ == "__main__":
    plot_series("/home/rkost/speedtests")
