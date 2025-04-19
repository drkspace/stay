#!/usr/bin/env python
# ruff: noqa: T201

from stay import StayParser, Stayspace


class CLIInput(Stayspace):
    foo: int|None
    bar: str|None


def main() -> None:

    parser = StayParser(namespace_cls=CLIInput)

    meg = parser.add_mutually_exclusive_group()
    meg.add_argument("--foo", type=int, default=None)
    meg.add_argument("--bar", type=str, default=None)

    args = parser.parse_args()

    if args.foo is not None:
        print(f"You inputted foo with a value of {args.foo}")
    elif args.bar is not None:
        print(f"You inputted bar with a value of {args.bar}")
    else:
        print("You didn't provide anything")

if __name__ == "__main__":
    main()