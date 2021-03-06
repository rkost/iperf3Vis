import json
import os
import pandas as pd

from datetime import timezone


def get_data_from_directory(path_to_logs):
    data_frames = []
    # iterate over all files in given directory
    for filename in os.listdir(path_to_logs):
        if filename.endswith(".json"):
            try:
                # try to extract log data from json file
                with open(os.path.join(path_to_logs, filename)) as iperf3FileLog:
                    data_frames.append(get_data_frame_from_file(iperf3FileLog, filename))
            except json.decoder.JSONDecodeError:
                print("Skipped malformed file", filename)

    # Merge all frames into a big one containing all intervals of all iperf3 logs.
    # Intervals of the same log file will now have the same timestamp.
    return pd.concat(data_frames)


def get_data_frame_from_file(logData, filename):
    iperf3_data = json.load(logData)
    data_frames = []
    if "error" in iperf3_data:
        # Ignore any file that contains errors
        print("File \"", filename, "\" contains error: \"", iperf3_data["error"], "\". Skipping...")
        return
    else:
        # Generate a pandas data frame for each interval with a datetime as index
        start_time = iperf3_data["start"]["timestamp"]["timesecs"]
        for interval in iperf3_data["intervals"]:
            ptime = pd.to_datetime(start_time + interval["sum"]["start"], unit='s', utc=False)
            speed = interval["sum"]["bits_per_second"] / 1024 / 1024

            data_frames.append(pd.DataFrame({"Upload Speed (MBit/s)": [speed]},
                                            index=[ptime]))

    # Merge all frames into a big one containing all intervals of an iperf3 log.
    return pd.concat(data_frames)
