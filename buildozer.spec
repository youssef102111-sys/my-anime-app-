[app]

# (1) الاسم اللي هيظهر بره على الشاشة
title = Emperor Anime

# (2) اسم الحزمة (بدون مسافات)
package.name = emperoranime
package.domain = org.test

# سورس الكود والملفات المطلوبة
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# الإصدار
version = 0.1

# المتطلبات البرمجية (لضمان عمل الصور والقوائم)
requirements = python3,kivy==2.2.1,pillow,requests,urllib3,certifi,chardet,idna

# (3) الأيقونة (لو عندك صورة اسمها icon.png ارفعها بجانب الكود)
icon.filename = %(source.dir)s/icon.png

# اتجاه الشاشة
orientation = portrait

# (4) الصلاحيات (ضرورية جداً لتشغيل الحلقات والصور)
android.permissions = INTERNET

# (5) الإعدادات الذهبية اللي نجحت معانا (مهمة جداً)
android.api = 34
android.minapi = 21
android.ndk = 25c
android.ndk_path = 
android.sdk = 34

# المعمارية اللي اشتغلت في المحاولة 57
android.archs = arm64-v8a

# تفعيل الـ Android App Bundle (إيقافها للـ Debug)
android.build_mode = debug

[buildozer]
log_level = 2
warn_on_root = 1
