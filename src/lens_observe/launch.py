"""`lens-observe` launcher (stub).

The Lens — observe: computes signals over activity (active / orphaned / degrading /
blind) and exposes them. The module both observatory types borrow. Stdlib-only so
`lens-observe --help` works the moment pip install completes. The database is
INJECTED via LENS_DB_URL — never hardcoded.

This is a scaffold: it validates inputs and prints the plan. Real signal
computation lands in follow-up commits.
"""
from __future__ import annotations

import argparse
import os
import sys

SIGNALS = ["active", "orphaned", "degrading", "blind"]


def _cmd_observe(args: argparse.Namespace) -> int:
    db = args.db_url or os.environ.get("LENS_DB_URL")
    if not db:
        print("error: no database. Set LENS_DB_URL or pass --db-url "
              "(the connection is injected, never hardcoded).", file=sys.stderr)
        return 1
    print("==> lens-observe: computing signals over activity")
    print(f"    database:  {db.split('@')[-1] if '@' in db else '(set)'}")
    print(f"    signals:   {', '.join(SIGNALS)}")
    print()
    print("STUB: signal computation not implemented yet.")
    print("      Next commit computes signals over activity and serves them.")
    return 0


def _cmd_version(_args: argparse.Namespace) -> int:
    from lens_observe import __version__
    print(f"lens-observe {__version__}")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="lens-observe", description="The Lens — observe: compute signals (active/orphaned/degrading/blind) over activity.")
    subs = p.add_subparsers(dest="command", metavar="<command>")

    obs = subs.add_parser("observe", help="Compute signals over activity and expose them.")
    obs.add_argument("--db-url", default=None, help="Database URL (default: LENS_DB_URL env).")
    obs.set_defaults(func=_cmd_observe)

    subs.add_parser("version", help="Print version.").set_defaults(func=_cmd_version)

    args = p.parse_args(argv)
    if not getattr(args, "func", None):
        p.print_help()
        return 0
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
