

from django.contrib.auth.base_user import BaseUserManager

class ShopUserManager(BaseUserManager):
    """creating the user"""
    def create_user(self, first_name,last_name, username,email, password=None):
        if not email:
            raise ValueError('user most have a email')
        if not username:
            raise ValueError('user most have a username')
        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            username = username,


        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self,first_name,last_name, username,email,password):
        user = self.create_user(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            password= password,
            username = username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.is_superadmin = True    
        user.save(using=self._db)
        return user
