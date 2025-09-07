# تست ها

این فایل درباره مستندات تست های اپ های جنگو هست.

هر اپ جنگو به صورت مجزا تست های خودش را دارد.



<font color="cyan">در ادامه توضیح داده شده که چظوری همه تست های یک اپ را اجرا کنید یا به صورت مجزا برای یک endpiont خاص تست را اجرا کنید
</font>

##

# دستورات اجرای تست ها


```bash
python manage.py test <APP_NAME.tests>
```
```bash
pipenv run python manage.py test <APP_NAME.tests>
```
```bash
docker compose exec django python manage.py test <APP_NAME.tests> توصیه شده
```

#  اپ ها
همانطور که توضیح داده شد اپ ها به صورت ماژولار نوشته شده و شما میتوانید به صورت تکی یا همه تست های یک اپ تست کنید .


برای مثال با این دستور تست های اپ احراز هویت اجرا میشود:
```bash
docker compose exec django python manage.py test authentication.tests
```
<font color="green">داخل هر اپ پوشه بنام tests هست که تمام تست های آن اپ در آنجا هست با اجرای این پوشه میتوان تمام تستهای آن اپ را اجرا کرد</font>

## 
در ادامه اپ ها لیست شده اند تا برای تست شما آماده باشند:

- `authentication`:

test_register

##
برای اجرای مجزا هر تست مثلا شما میتوانبد به این شکل عمل کنید:
```bash
docker compose exec django python manage.py test authentication.tests.test_register
```
