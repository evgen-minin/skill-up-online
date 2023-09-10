from rest_framework import permissions


class IsModerator(permissions.BasePermission):
    """
    Пользователи с разрешением "Модератор" могут только просматривать курсы,
    но не могут их создавать, обновлять или удалять.
    """

    def has_permission(self, request, view):
        """
         Проверяет, имеет ли пользователь разрешение на выполнение действия на уровне представления.
        """
        # Проверка, является ли пользователь модератором
        is_moderator = request.user.is_staff

        # Разрешить GET-запросы всем пользователям
        if request.method in permissions.SAFE_METHODS:
            return True

        # Разрешить редактирование объекта только владельцу или модератору
        return is_moderator

    def has_object_permission(self, request, view, obj):
        """
          Проверяет, имеет ли пользователь разрешение на выполнение действия на уровне объекта.
        """
        # Проверка, является ли пользователь владельцем объекта
        is_owner = obj.user == request.user

        # Проверка, является ли пользователь модератором
        is_moderator = request.user.is_staff

        # Разрешить доступ к объекту только владельцу или модератору
        return is_owner or is_moderator
