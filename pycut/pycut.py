#!/usr/bin/env python3

import argparse
import sys


def get_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--fields', help='Select only these fields', required=True)
    parser.add_argument('-d', '--delimiter', help='Delimiter. Defaults to tab', default='\t')
    parser.add_argument('files', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help='Files or standard input')
    return parser.parse_args()


def get_fields(fields):
    if '-' not in fields:
        fields = int(fields) - 1
        return fields, fields

    result = fields.split('-')
    if result[0] == '':
        result[0] = None
    else:
        result[0] = int(result[0]) - 1
    if result[1] == '':
        result[1] = None
    else:
        result[1] = int(result[1]) - 1

    return result[0], result[1]


def cut(value, fields, delimiter):
    fields = get_fields(fields)
    result = value.split(delimiter)
    if fields[0] is not None and fields[1] is not None:
        result = result[fields[0]:fields[1] + 1]
    elif fields[0] is None:
        result = result[:fields[1] + 1]
    elif fields[1] is None:
        result = result[fields[0]:]
    return delimiter.join(result)


def main():
    cli_options = get_options()
    for file in cli_options.files:
        value = file
        break
    print(cut(value, cli_options.fields, cli_options.delimiter), end='')
    return 0


if __name__ == "__main__":
    main()
