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

    parser.add_argument(
        "--box-plot",
        help="Plots data as box plot(s) instead of a ribbon plot",
        action="store_const",
        const=True
    )

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    data = logReader.get_data_from_directory(args.data_directory)
    if args.box_plot:
        visualizer.plot_box_plot(data, "H", args.output)
    else:
        visualizer.plot_ribbon_plot(data, "H", args.output)
