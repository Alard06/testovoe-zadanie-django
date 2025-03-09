import httpx
import asyncio
import json


async def get_yandex_files(public_key: str) -> list:
    """
    Получает список файлов из Яндекс.Диска
    :param public_key: str - публичный ключ
    :return: list - список файлов
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://cloud-api.yandex.net/v1/disk/resources/files",
            headers={"Authorization": f"OAuth {public_key}"},
        )
        if response.status_code == 200:
            return response.json()
        else:
            return {}
    
# async def main():
#     data = await get_yandex_files("")
#     with open("data.json", "w") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
#     print(data)

# if __name__ == "__main__":
#     asyncio.run(main())