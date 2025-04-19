# Stay

**S**imple **T**yped **A**rgparse, **Y**es

[![ruff-action](https://github.com/drkspace/stay/actions/workflows/ruff_action.yml/badge.svg?branch=main)](https://github.com/drkspace/stay/actions/workflows/ruff_action.yml)

Add typing to your argparse CLIs.

Example:

```python
from stay import Stayspace, StayParser

class ArgSpace(Stayspace):
    foo: int
    bar: str

parser = StayParser(namespace_cls=ArgSpace)

parser.add_argument("--foo", type=int)
parser.add_argument("--bar", type=float)

args = parser.parse_args()

reveal_type(args.foo) # int
reveal_type(args.bar) # float
reveal_type(args.invalid) # Type Error
```

## Install

To install from PyPi:

```bash
pip install -U TODO
```

To install the most recent dev version

```bash
git clone TODO
cd stay
pip install .
```

## Why not other typed argparse libraries?

There are two other typed argparse libraries, [tap](https://github.com/swansonk14/typed-argument-parser) and [typed-argparse](https://github.com/typed-argparse/typed-argparse).
Their main deficiencies are that they can not replicate all of argparse's features, like argument groups and mutually exclusive groups.
Stay, on the other hand, will always support 100% of argparse's features as the parsing class, ``StayParser``, is a subclass of ``argparse.ArgumentParser``.

However, Stay cannot generate a parser from a ``Namespace`` or other data structure.
If you require that functionality, please use [tap](https://github.com/swansonk14/typed-argument-parser) or [typed-argparse](https://github.com/typed-argparse/typed-argparse).
No Hard feelings.

## Examples

TODO