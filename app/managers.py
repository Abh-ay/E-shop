# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.hashers import make_password


# class UserManager(BaseUserManager):
#     use_in_migrations = True

#     def create_user(self, email, password=None, **extrafields):
#         if not email:
#             raise ValueError("Email is required")

#         email = self.normalize_email(email)
#         user = self.model(email=email, **extrafields)
#         user.password = make_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password, **extrafields):
#         extrafields.setdefault('is_staff', True)
#         extrafields.setdefault('is_superuser', True)
#         extrafields.setdefault('is_active', True)

#         return self.create_user(email, password, **extrafields)
