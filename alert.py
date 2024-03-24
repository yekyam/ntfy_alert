import subprocess
import sys
import os
import requests
import time

def main():
    env_var_for_topic = "PY_NTFY_ALERT_TOPIC"

    if len(sys.argv) < 3:
        print("""usage: alert type command [args...]
    type - the type of alert to send out. `completion` sends an unconditional alert when the command is completed. `success` has different alerts depending on the error code.
    command - the command to run
    args - optional list of arguments to pass to the command""")
        exit(1)

    if not sys.argv[1] in ['completion', 'success']:
        print("error; invalid alert type", file=sys.stderr)
        exit(1)

    ntfy_topic = os.getenv(env_var_for_topic)
    if ntfy_topic is None:
        print(f"error; env variable `{env_var_for_topic}` isn't set", file=sys.stderr)
        exit(1)

    start_time = time.time() 
    info = subprocess.run(" ".join(sys.argv[2:]), shell=True)
    total_time = time.time() - start_time
    total_time = round(total_time, 2)

    alert_type = sys.argv[1]
    
    topic_url = f"https://ntfy.sh/{ntfy_topic}"
    command = sys.argv[2]
    completion_message = f"Your command `{command}` has completed! ({total_time}s)"
    success_message = f"Your command `{command}` was succesful! ({total_time}s)"
    error_message = f"Your command `{command}` failed. ({total_time}s)"


    if alert_type == "completion":
        requests.post(topic_url, data=completion_message, headers={"Title": "Done!", "Tags": "+1"})
        exit(0)

    if alert_type == "success":
        if info.returncode == 0:
            requests.post(topic_url, data=success_message, headers={"Title": "Success!", "Tags": "tada"})
            exit(0)
        if info.returncode == 1:
            requests.post(topic_url, data=error_message, headers={"Title": "Error!", "Tags": "rotating_light"})
            exit(info.returncode)


main()
