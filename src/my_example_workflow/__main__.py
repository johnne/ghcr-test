# SPDX-FileCopyrightText: 2026-present John Sundh <john.sundh@scilifelab.se>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == "__main__":
    from my_example_workflow.cli import my_example_workflow

    sys.exit(my_example_workflow())
