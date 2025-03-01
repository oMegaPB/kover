import asyncio

from kover import Kover, AuthCredentials
from kover.gridfs import GridFS


async def main():
    credentials = AuthCredentials.from_environ()
    kover = await Kover.make_client(credentials=credentials)

    database = kover.get_database("files")
    fs = await GridFS(database).indexed()

    # can be bytes, any type of IO str or path
    file_id = await fs.put(b"Hello World!")

    file, binary = await fs.get_by_file_id(file_id)
    print(file, binary.read())

    files = await fs.list()
    print(f"total files: {len(files)}")

    deleted = await fs.delete(file_id)
    print("is file deleted?", deleted)

if __name__ == "__main__":
    asyncio.run(main())
