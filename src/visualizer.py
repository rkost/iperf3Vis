import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt


def plot_ribbon_plot(data, interval_string, output_file, width, height, display):
    data.index = data.index.floor(interval_string)

    # Generate data for mean and error bands
    interval_data = pd.concat([
        data.groupby(data.index).quantile(0.05).rename(columns={"Upload Speed (MBit/s)": "q05"}),
        data.groupby(data.index).quantile(0.10).rename(columns={"Upload Speed (MBit/s)": "q10"}),
        data.groupby(data.index).quantile(0.25).rename(columns={"Upload Speed (MBit/s)": "q25"}),
        data.groupby(data.index).quantile(0.50).rename(columns={"Upload Speed (MBit/s)": "q50"}),
        data.groupby(data.index).quantile(0.75).rename(columns={"Upload Speed (MBit/s)": "q75"}),
        data.groupby(data.index).quantile(0.90).rename(columns={"Upload Speed (MBit/s)": "q90"}),
        data.groupby(data.index).quantile(0.95).rename(columns={"Upload Speed (MBit/s)": "q95"}),
    ], axis=1)

    # Disclaimer: This was written by @rkost while he did not know anything about altair.
    # It basically is a giant hack (I guess). Suggestions welcome!
    # Plot: Mean, confidence (50, 80, 90) and scattered raw data
    alt.data_transformers.disable_max_rows()
    line = alt.Chart(interval_data.reset_index()).mark_line().encode(
        x=alt.X('index', axis=alt.Axis(title='Time (UTC)')),
        y=alt.Y('q50:Q', axis=alt.Axis(title='MBit/s: Mean'))
    ).properties(width=width/2, height=height/2)
    area50 = alt.Chart(interval_data.reset_index()).mark_area(opacity=0.2).encode(
        x='index',
        y=alt.Y('q75:Q', axis=alt.Axis(title='confidence 50')),
        y2='q25'
    )
    area80 = alt.Chart(interval_data.reset_index()).mark_area(opacity=0.2).encode(
        x='index',
        y=alt.Y('q90:Q', axis=alt.Axis(title='confidence 80')),
        y2='q10'
    )
    area90 = alt.Chart(interval_data.reset_index()).mark_area(opacity=0.2).encode(
        x='index',
        y=alt.Y('q95:Q', axis=alt.Axis(title='confidence 90')),
        y2='q05'
    )
    scatter = alt.Chart(data.reset_index()).mark_point(opacity=0.05, filled=True).encode(
        x='index',
        y='Upload Speed (MBit/s)'
    )

    # Combine plots, save, display
    plot = (line + area50 + area80 + area90 + scatter)
    plot.save(output_file, scale_factor=2.0)
    if display:
        plot.show()


def plot_box_plot(data, interval_string, output_file, width, height):
    data.index = data.index.floor(interval_string)
    fig = plt.figure(figsize=(24, 9))
    sns.set(style="ticks")
    sns.boxplot(x=data["Upload Speed (MBit/s)"])
    plt.savefig(output_file)
