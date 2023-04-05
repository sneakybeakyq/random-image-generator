import uuid
import argparse
import requests 


def create_uuid_string(length: int) -> str:
    return str(uuid.uuid4()).replace("-","")[:length]


def create_random_picture(
    x: int,
    y: int
):
    with open(f'pics/{create_uuid_string(8)}.jpg', "wb") as f:
        f.write(requests.get(f"https://picsum.photos/{x}/{y}").content)


def main():
    parser = argparse.ArgumentParser(description='Simple CLI for generating images by API calls')
    parser.add_argument('--x', type=int, help='x size', required=True)
    parser.add_argument('--y', type=int, help='y size', required=True)
    args = parser.parse_args()
    create_random_picture(
        args.x,
        args.y
    )


if __name__ == '__main__':
    main()
