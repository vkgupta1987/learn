"""TODO(vivekgu): DO NOT SUBMIT without one-line documentation for a.

TODO(vivekgu): DO NOT SUBMIT without a detailed description of a.
"""

from typing import Sequence

from absl import app

#Line 2
#Line 3
#Line 4
#Line 4.5
def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')


if __name__ == '__main__':
  app.run(main)
