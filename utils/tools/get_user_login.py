"""take user login module"""
import getpass
from core.types.user_login_type import UserName


async def take_user_login() -> UserName:
    """Returns user login with UserName type"""
    return UserName(getpass.getuser())
