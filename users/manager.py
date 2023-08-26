from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, name, email, phone, password=None, **extra_fields):
        if not phone:
            raise ValueError('Phone is required!')
        
        extra_fields['email'] = self.normalize_email(email)
        user = self.model(phone = phone, name=name, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user


    def create_superuser(self, name, email, phone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(name, email, phone, password, **extra_fields)