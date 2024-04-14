def http_400_username_details(username: str) -> str:
    return f"Имя пользователя {username} занято! Придумайте другое!"


def http_400_signup_credentials_details() -> str:
    return "Ошибка при регистрации! Проверьте введенные данные!"


def http_400_signin_credentials_details() -> str:
    return "Ошибка при попытке авторизации! Проверьте введенные данные!"


def http_401_unauthorized_details() -> str:
    return "Отказано в выполнении запроса из-за отсутствия действительной аутентификации!"


def http_403_forbidden_details() -> str:
    return "Доступ запрещен для запрашиваемых ресурсов!"


def http_404_id_details(id: int) -> str:
    return f"Либо учетная запись с идентификатором `{id}` не существует, была удалена, либо вы не авторизованы!"


def http_404_username_details(username: str) -> str:
    return f"Либо учетная запись с именем пользователя `{username}` не существует, была удалена, либо вы не авторизованы!"
