# این مستند درباره دستورات اپ احراز هویت هست
در ادامه توضیح داده شده که چطوری از این دستورات استفاده کنیم:
--
## group
- `python manage.py group --add <GROUP_NAME>` ساخت یک گروه جدید
- `python manage.py group --delete <GROUP_NAME>` حذف گروه فعلی
- `python manage.py group --list <GROUP_NAME>`لیست کاربران در گروه تایین شده
- `python manage.py group --username <USERNAME> --group <GROUP_NAME>`اضافه کردن کاربر به گروه فعلی
- `python manage.py group --username <USERNAME> --group <GROUP_NAME> --removeuser` حذف کاربر از گروه تایین شده

---
## jwt