from __future__ import annotations

import sys

from resources.lib.router import dispatch


def main(argv: list[str] | None = None) -> None:
    args = list(sys.argv if argv is None else argv)
    dispatch(args)


if __name__ == "__main__":
    main()
