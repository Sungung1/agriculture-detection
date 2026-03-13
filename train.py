import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Agriculture detection training entrypoint placeholder."
    )
    parser.add_argument(
        "--dataset",
        default="data/",
        help="Dataset directory for future crop-image training workflows.",
    )
    return parser


def main() -> None:
    build_parser().parse_args()
    print("Training pipeline is not versioned in this repository yet. Use this project as a deployable web prototype.")


if __name__ == "__main__":
    main()
