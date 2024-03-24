# ntfy\_alert

## Purpose

Provides an easy wrapper around ntfy to monitor the result of a command.

## Usage

1. Create a topic on [https://ntfy.sh](https://ntfy.sh) and subscribe to it. 
2. Set the `$PY\_NTFY\_ALERT\_TOPIC` variable to the name of the topic
3. Run the `alert.py` using one of these two formats:

```python
python3 alert.py completion script script_arg1 ...
``` 

```python
python3 alert.py success script script_arg1 ...
```

Completion mode does not customize the ntfy message and title based off the command's exit code.

### TODO
- Create some sort of config for alerts in this type of format:
```
completion:
	title: "Done!"
	message: "Script compelted in {time} seconds with error_code {code}"
```
- Better docs

