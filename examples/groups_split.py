#!/usr/bin/env python
# ruff: noqa: T201

from typing_extensions import TypeIs

from stay import StayParser, Stayspace


class CLIInput1(Stayspace):
    foo: int


class CLIInput2(Stayspace):
    bar: str


class CLICombined(CLIInput1, CLIInput2): ...


def is_inp_1(inp: CLIInput1 | CLIInput2) -> TypeIs[CLIInput1]:
    return "foo" in inp


def main() -> None:
    parser = StayParser[CLIInput1 | CLIInput2](namespace_cls=CLICombined)

    meg = parser.add_mutually_exclusive_group(required=True)
    meg.add_argument("--foo", type=int)
    meg.add_argument("--bar", type=str)

    args = parser.parse_args()

    if is_inp_1(args):
        print(f"You inputted foo with a value of {args.foo}")
    else:
        print(f"You inputted bar with a value of {args.bar}")


if __name__ == "__main__":
    main()
