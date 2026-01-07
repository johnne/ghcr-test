# SPDX-FileCopyrightText: 2026-present John Sundh <john.sundh@scilifelab.se>
#
# SPDX-License-Identifier: MIT

from pathlib import Path

from snk_cli import CLI

my_example_workflow = CLI(Path(__file__).parent.parent)