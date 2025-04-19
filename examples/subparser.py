#!/usr/bin/env python
# ruff: noqa: T201, E501

from pathlib import Path

from typing_extensions import TypeIs

from stay import StayParser, Stayspace


class MainInputs(Stayspace):
    file: Path


class CSVOutput(MainInputs):
    delimiter: str


class JSONOutput(MainInputs):
    pretty: bool


class CLICombined(CSVOutput, JSONOutput): ...


def is_csv(inp: CSVOutput | JSONOutput) -> TypeIs[CSVOutput]:
    return "delimiter" in inp


def main() -> None:
    parser = StayParser[CSVOutput | JSONOutput](namespace_cls=CLICombined)

    parser.add_argument("file", type=Path)

    subparsers = parser.add_subparsers()
    csv_parser = subparsers.add_parser("csv", namespace_cls=CSVOutput)
    csv_parser.add_argument("--delimiter", type=str)

    csv_parser = subparsers.add_parser("json", namespace_cls=JSONOutput)
    csv_parser.add_argument("--pretty", action="store_true", default=False)

    args = parser.parse_args()

    if is_csv(args):
        print(f'Using a CSV file {args.file} with a delimiter of "{args.delimiter}"')
    else:
        print(
            f"USING a JSON file {args.file} that {'is' if args.pretty else 'is not'} pretty printed"
        )


if __name__ == "__main__":
    main()
