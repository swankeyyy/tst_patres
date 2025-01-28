import asyncio
from app.src.models.db_config import db_config
from app.api.users.service import UserService

async def create_superuser(username: str, password: str):
    async for session in db_config.get_session():
        superuser_data = {
            "username": username,
            "password": password,
            "is_superuser": True
        }
        superuser = await UserService.create_user(**superuser_data, session=session)
        return superuser

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python create_superuser.py <username> <password>")
        sys.exit(1)
    
    username = sys.argv[1]
    password = sys.argv[2]

    asyncio.run(create_superuser(username, password))
    print(f"Superuser {username} created successfully.")