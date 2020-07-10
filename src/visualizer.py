import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_series(data, output_file):
    fig = plt.figure(figsize=(24, 9))
    sns.set(style="ticks")
    sns.boxplot(data.index, data["Upload Speed (MBit/s)"])
    plt.show()

    fig = plt.figure(figsize=(24, 9))
    sns.set(style="darkgrid")
    ax = sns.lineplot(data.index, data["Upload Speed (MBit/s)"], ci="sd")
    ax.set(xlabel="Time (UTC)", ylabel="Measured Upload Speed in Mbit/s")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%y-%m-%d %H:%M"))
    ax.tick_params(axis="x", rotation=45)
    plt.show()
    # plt.savefig(output_file)

