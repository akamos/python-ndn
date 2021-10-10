# -----------------------------------------------------------------------------
# Copyright (C) 2019-2021 The python-ndn authors
#
# This file is part of python-ndn.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# -----------------------------------------------------------------------------
import argparse
from . import cmd_get_status, cmd_get_face


CMD_LIST = '''
Available commands:
  Get-Status (status)
  Get-Face (face,gf)
  New-Face (nf)
  Remove-Face (rf)
  Get-Route (route,gr)
  New-Route (nr)
  Remove-Route (rr)
  Get-Strategy (strategy,gs)
  Set-Strategy (ss)
  Remove-Strategy (rs)

Try '%(prog)s COMMAND -h' for more information on each command
'''


def main():
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, epilog=CMD_LIST)
    subparsers = parser.add_subparsers(metavar='COMMAND', help='sub-command to execute')

    cmd_get_status.add_parser(subparsers)
    cmd_get_face.add_parser(subparsers)

    args = parser.parse_args()
    if 'executor' not in args:
        parser.print_help()
        exit(-1)

    return args.executor(args)
