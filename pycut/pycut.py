import argparse
import sys


def get_options():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawTextHelpFormatter, description=\
"""
pycut is similar to the Unix cut tool. There are several differences:
1) It implements a small subset of cut's functionality. It only supports
   the -f and -d arguments.
2) The delimiter (-d) argument supports strings longer than a single character.
3) The fields (-f) argument uses the ':' symbol, and not the '-' symbol to to signify ranges. This is because...
4) The fields (-f) argument supports negative numbers to refer to 2nd/3rd/nth from last field.

Examples:
* echo "some_file.ini.json.00000" | pycut -f :-1 -d ".json"  # Print all fields before the json substring
> some_file.ini
""")

    parser.add_argument('-f', '--fields', required=True, help=\
"""Select only these fields. For example:
-f 1      The first field
-f 2,3    The second and third fields
-f 1:4    Fields 1 through 4
-f 2:     Fields 2 to the end
-f :5     Fields 1 to 5
-f :-1    Fields 1 to second from last
-f 1,5:-2 Fields 1 and 5 to third from last""")

    parser.add_argument('-d', '--delimiter', default='\t', help=\
"""Delimiter. Defaults to tab. Can be a single character or string.""")

    parser.add_argument('files', nargs='*', type=argparse.FileType('r'), default=sys.stdin, help='Files or standard input')
    return parser.parse_args()


def get_segments(fields):
    return fields.split(',')


def get_fields(fields):
    if ':' not in fields:
        fields = int(fields) - 1
        return fields, fields

    result = fields.split(':')
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
    result = []
    segments = get_segments(fields)
    for segment in segments:
        fields = get_fields(segment)
        segment_result = value.split(delimiter)
        if fields[0] is not None and fields[1] is not None:
            segment_result = segment_result[fields[0]:fields[1] + 1]
        elif fields[0] is None:
            segment_result = segment_result[:fields[1] + 1]
        elif fields[1] is None:
            segment_result = segment_result[fields[0]:]
        result += segment_result
    return delimiter.join(result).rstrip('\n')


def main():
    cli_options = get_options()
    for file in cli_options.files:
        value = file  # files need to be read while stdin is already in strin form
        try:
            value = file.read()
        except Exception:
            pass
        result = cut(value, cli_options.fields, cli_options.delimiter)
        print(result)
    return 0
