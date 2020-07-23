import argparse
import os

import logReader
import visualizer


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
        "--time-interval",
        help="The time interval to floor data points to (see pandas timeseries-offset-aliases).",
        default="H"
    )

    parser.add_argument(
        "--img-width",
        type=int,
        help="The width of the image to output. (Default: 1500)",
        default=1500
    )

    parser.add_argument(
        "--img-height",
        type=int,
        help="The height of the image to output. (Default: 500)",
        default=500
    )

    parser.add_argument(
        "--display",
        help="Displays the resulting plot in the default browser in addition to saving it as png",
        action="store_const",
        const=True
    )

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
        visualizer.plot_box_plot(data, args.time_interval, args.output, args.img_width, args.img_height)
    else:
        visualizer.plot_ribbon_plot(data, args.time_interval, args.output, args.img_width, args.img_height, args.display)
