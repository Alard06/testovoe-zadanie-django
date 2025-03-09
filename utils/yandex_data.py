import httpx
import asyncio
from typing import Dict, List, Any


async def get_yandex_files(public_key: str) -> List[Dict[str, Any]]:
    """
    Получает список файлов из Яндекс.Диска.

    :param public_key: Публичный ключ для авторизации.
    :return: Список файлов в формате JSON. В случае ошибки возвращает пустой словарь.
    """
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://cloud-api.yandex.net/v1/disk/resources/files",
            headers={"Authorization": f"OAuth {public_key}"},
        )
        if response.status_code == 200:
            return response.json()
        return {}
    
# async def main():
#     data = await get_yandex_files("")
#     with open("data.json", "w") as f:
#         json.dump(data, f, indent=4, ensure_ascii=False)
#     print(data)

# if __name__ == "__main__":
#     asyncio.run(main())