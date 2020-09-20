### server-toggle.py
Simple script for creating and deleting hetzner server using static snapshot.

You need to create `data.json` with your hcloud token in order to work with hcloud API. 

Example of cronjobs:
```
45 7 * * 1-5 /usr/bin/python3 /root/server-toggle.py/server-toggle.py create
15 21 * * 1-5 /usr/bin/python3 /root/server-toggle.py/server-toggle.py delete
```

Based on [click](https://click.palletsprojects.com/en/7.x/) and [hcloud-python](https://github.com/hetznercloud/hcloud-python).
