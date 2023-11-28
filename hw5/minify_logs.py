from tensorboard.backend.event_processing.event_accumulator import EventAccumulator
from tensorboardX import SummaryWriter
import os
import glob


def extract_tensorboard_log(input_dir, output_dir):
    print(f"Minifying {input_dir}...")
    log_file_in = glob.glob(os.path.join(input_dir, '*.tfevents*'))[0]

    # Initialize an EventAccumulator with the path to the log directory

    event_acc = EventAccumulator(log_file_in)
    event_acc.Reload()  # Load the events from disk

    # Extract the scalar summaries
    scalars = {}
    for tag in event_acc.Tags()["scalars"]:
        scalars_for_tag = event_acc.Scalars(tag)
        scalars[tag] = scalars_for_tag[-1000:]
    
    # print(f"Got max eval_return of {max(s.value for s in scalars['eval_return'])} for {input_dir}")

    # Write the scalar summaries to a new TensorBoard log
    writer = SummaryWriter(output_dir)
    for tag, events in scalars.items():
        for event in events:
            writer.add_scalar(tag, event.value, event.step)


if __name__ == "__main__":
    import argparse

    # Example usage
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir", "-i", type=str, required=True)
    parser.add_argument("--output_dir", "-o", type=str, required=True)
    args = parser.parse_args()

    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    def minify_dir(folder: str):
        in_dir = os.path.join(args.input_dir, folder)
        out_dir = os.path.join(args.output_dir, folder)

        if not os.path.isdir(in_dir):
            print(f"Skipping non-directory file {in_dir}")
            return
    
        if not os.path.exists(out_dir):
            os.makedirs(out_dir)

        extract_tensorboard_log(
            in_dir,
            out_dir,
        )

    dirs = os.listdir(args.input_dir)

    if len(dirs) > 3:
        print("*" * 80)
        warn_msg = [
            f"WARNING: Your data directory contains a lot {len(dirs)} of subdirectories.",
            "This may take a long time to minify. Consider moving",
            "log files you don't want to submit from the data/ directory.",
        ]
        for line in warn_msg:
            padding_size = (80 - len(line))
            padding_left = padding_size // 2 - 1
            padding_right = padding_size - padding_left - 1
            print(f"{'*' * padding_left} {line} {'*' * padding_right}")
        print("*" * 80)

    for folder in dirs:
        minify_dir(folder)