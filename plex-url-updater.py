#!/usr/bin/env python3
import sys
import urllib.parse
import urllib.request

from config import config


def ip_to_plex(ip: str) -> str:
    return ip.strip().replace(':', '-').replace('.', '-')


def main():
    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <NEW_IP>', file=sys.stderr)
        sys.exit(1)
    new_ip = ip_to_plex(sys.argv[1])

    custom_urls = [f"https://{new_ip}.{config['base_plex_direct']}:{config['port']}"]

    for entry in config['custom_ips']:
        custom_urls.append(f"https://{ip_to_plex(entry['ip'])}.{config['base_plex_direct']}:{entry['port']}")

    params = {
        'customConnections': ','.join(custom_urls),
        'X-Plex-Token': config['plex_token'],
    }
    query = urllib.parse.urlencode(params, safe=',:/')

    url = f"{config['plex_baseurl']}/:/prefs?{query}"
    req = urllib.request.Request(url, method='PUT', headers={'Accept': 'application/json'})

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            status = resp.status
            body = resp.read().decode('utf-8')
        if status == 200:
            print('✔ customConnections successfully set:', custom_urls)
            sys.exit(0)
        else:
            print(f'✖ Error {status}: {body}', file=sys.stderr)
            sys.exit(2)
    except Exception as e:
        print('✖ Exception:', e, file=sys.stderr)
        sys.exit(3)


if __name__ == "__main__":
    main()
