import seaborn as sns
import matplotlib.pyplot as plt


def plot_series(data, output_file):
    fig = plt.figure(figsize=(24, 9))
    sns.set(style="ticks")
    sns.boxplot(x="timepoint", y="Upload Speed (MBit/s)", data=data)
    plt.show()

    # fig = plt.figure(figsize=(24, 9))
    # sns.set(style="darkgrid")
    # sns.lineplot(x="timepoint", y="Upload Speed (MBit/s)", data=data, ci="sd")
    # plt.show()

