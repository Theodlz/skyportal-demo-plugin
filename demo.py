import requests
import time

from baselayer.app.env import load_env
from baselayer.log import make_log

env, cfg = load_env()
log = make_log('plugin/demo')

REQUEST_TIMEOUT_SECONDS = cfg['health_monitor.request_timeout_seconds']

host = f'{cfg["server.protocol"]}://{cfg["server.host"]}' + (
    f':{cfg["server.port"]}' if cfg['server.port'] not in [80, 443] else ''
)

PLUGIN_CFG = cfg['plugins'].get('demo', {})


def is_loaded():
    try:
        r = requests.get(f'{host}/api/sysinfo', timeout=REQUEST_TIMEOUT_SECONDS)
    except:  # noqa: E722
        status_code = 0
    else:
        status_code = r.status_code

    if status_code == 200:
        return True
    else:
        return False

def service():
    text = PLUGIN_CFG.get("params", {}).get("demo_param", "Missing demo parameter")
    while True:
        if is_loaded():
            try:
                log(text)
                time.sleep(30)
            except Exception as e:
                log(e)
        else:
            log("Server not loaded yet. Waiting...")
            time.sleep(15)


if __name__ == "__main__":
    service()

