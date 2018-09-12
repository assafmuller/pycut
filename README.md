pycut is similar to the Unix cut tool. There are several differences:

1. It implements a small subset of cut's functionality. It only supports
   the -f and -d arguments.
2. The delimiter (-d) argument supports strings longer than a single character.
3. The fields (-f) argument uses the ':' symbol, and not the '-' symbol to to signify ranges. This is because...
4. The fields (-f) argument supports negative numbers to refer to 2nd/3rd/nth from last field.

Examples:

Print all fields before the json substring

```
echo "some_file.ini.json.00000" | pycut -f :-1 -d ".json"
> some_file.ini
```
