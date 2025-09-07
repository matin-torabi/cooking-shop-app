# from django.core.management.base import BaseCommand


# from authentication.core.path import SETTING_DIR , Setting
# from django.conf import settings





# def make_dir_in_proj_path():
#     setting = Setting()
#     path = setting.path().create_setting()
#     print(path)
#     return path



# class Command(BaseCommand):
#     def add_arguments(self, parser):
#         parser.add_argument("--jwt", action='store_true', help="set jwt tokens")
        
#     def handle(self, *args, **options):
#         jwt = options.get("jwt")
        
        
#         if jwt:
#             with open(SETTING_DIR / 'settings' / 'jwt.txt', 'r') as f:
#                 jwt_setting = f.read()
#             path = make_dir_in_proj_path()
#             self.stdout.write(self.style.SUCCESS(f"settings directory created"))
#             with open(path / "jwt.py", 'w', encoding='utf-8') as f:
#                 f.write(jwt_setting)
#             self.stdout.write(self.style.SUCCESS(f"jwt.py created inside settings directory"))
            
            
            
            
