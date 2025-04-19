#!/usr/bin/env python
# ruff: noqa: T201
from stay import StayParser, Stayspace


class CLIInput(Stayspace):
    name: str
    age: int

def main() -> None:

    parser = StayParser(namespace_cls=CLIInput)

    parser.add_argument("--name", type=str)
    parser.add_argument("--age", type=int)

    args = parser.parse_args()

    print(f"Hello {args.name}. You are {args.age} years old")

if __name__ == "__main__":
    main()