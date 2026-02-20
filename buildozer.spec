[app]

# اسم التطبيق اللي يظهر على الموبايل
title = Emperor Anime

# اسم الباكدج
package.name = emperoranime
package.domain = org.test

# مكان السورس
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# الإصدار
version = 0.1

# المتطلبات (مهم جداً متزودش حاجة)
requirements = python3,kivy==2.2.1,pyjnius,plyer

# الأيقونة (لو مش عندك صورة امسح السطر ده)
# icon.filename = %(source.dir)s/icon.png

# اتجاه الشاشة
orientation = portrait

# الصلاحيات
android.permissions = INTERNET

# إعدادات أندرويد المستقرة على GitHub
android.api = 33
android.minapi = 21

# سيبهم فاضيين (مهم جداً)
android.ndk =
android.sdk =
android.ndk_path =

# المعمارية
android.archs = arm64-v8a

# وضع البناء
android.build_mode = debug


[buildozer]
log_level = 2
warn_on_root = 1
