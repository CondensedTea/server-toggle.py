from hcloud import Client
from hcloud.images.domain import Image
from hcloud.servers.domain import Server
from hcloud.server_types.domain import ServerType
from hcloud.locations.domain import Location
from hcloud.networks.domain import Network
import json
import click


@click.group()
def cli():
    pass


@click.command(help="Creates server from snapshot and writes its ID to file")
def create():
    with open("data.json", "r") as file:
        data = json.load(file)

    client = Client(token=data["token"])
    response = client.servers.create(
        "win10-OCR",
        server_type=ServerType(name="cx41"),
        image=Image(id=22859215),
        networks=[Network(id=135205)],
        location=Location(id=2)
    )
    server = response.server
    data["server_id"] = f"{server.id}"

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


@click.command(help="Deletes server by ID")
def delete():
    with open("data.json", "r") as file:
        data = json.load(file)

    client = Client(token=data["token"])
    response = client.servers.delete(
        server=Server(id=data["server_id"]),
    )

    data["server_id"] = "SERVER-IS-DOWN"

    with open("data.json", "w") as file:
        json.dump(data, file, indent=4)


cli.add_command(create)
cli.add_command(delete)

if __name__ == '__main__':
    cli()