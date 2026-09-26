"""lens-observe — The Lens observe module: signals over activity.

Read CHARTER.md first. This package holds the launcher that computes signals
(active / orphaned / degrading / blind) over activity and exposes them, against an
injected database. It is the module both observatory types borrow. The shared
schema it reads is defined in lens-core.
"""

__version__ = "0.0.1"
