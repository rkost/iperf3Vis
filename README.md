# iperf3 Visualization Tool

This is a very basic tool for visualizing one or more [iperf3](https://iperf.fr/) log files using [seaborn](https://seaborn.pydata.org/index.html).

## Example

Each box plot represents one iperf log file (60 seconds of measurement per file) measured every 10ish minutes over a time period of roughly 24 hours.

![boxPlot1](https://rkost.org/iperf3Vis/examples/boxPlot_beta.png)


## Usage

### Data collection

Collect data using iperf3 and save it to any directory. Example: `iperf3 -c server --json --logfile /path/to/data/file.json`. 
If you experience high deviation during the measurement, run iperf3 longer using `-t SECS`.

### Requirements

Install the python requirements by `pip install --upgrade -r pythonRequirements.txt`.
Do yourself a favor and use a [virtual environment](https://docs.python.org/3/library/venv.html) for that.

### Visualize

Run `run.py` with arguments:

- `--data-directory /path/to/data/`
- `--output /path/to/output/plot.png` (optional)

Note that this tool will skip all json files that contain the "error" key.


## Contributing

Feel free to create issues or create pull requests. Clean-up, new features, bug fixes/reports welcome.
