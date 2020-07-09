import argparse
import os

import src.logReader as logReader
import src.visualizer as visualizer


def parse_arguments():
    parser = argparse.ArgumentParser(description="iperf3 Visualization Tool")

    parser.add_argument(
        "--data-directory",
        required=True,
        help="Directory containing iperf3 logs",
        default=None)

    parser.add_argument(
        "--output",
        help="The file to store the plot to",
        default=os.path.dirname(__file__) + "/plot.png")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    data = logReader.get_data_from_directory(args.data_directory)
    data.index = data.index.floor('H')
    visualizer.plot_series(data, args.output)
