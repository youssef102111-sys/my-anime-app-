[app]

# اسم التطبيق
title = Emperor Anime

# اسم الباكدج (من غير مسافات)
package.name = emperoranime
package.domain = org.emperor

# مكان الكود
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv

# استبعد ملفات غير مهمة
source.exclude_exts = spec

# النسخة
version = 1.0

# المتطلبات
requirements = python3,kivy,plyer

# الاتجاه
orientation = portrait




# شاشة بداية (اختياري لو عندك صورة)
# android.presplash.filename = presplash.png

# أذونات
android.permissions = INTERNET

# نسخة أندرويد
android.api = 33
android.minapi = 21

# المعمارية (مناسبة لموبايلك A20s)
android.archs = arm64-v8a

# تسريع build
android.gradle_dependencies =

# عدم استخدام fullscreen
fullscreen = 0


[buildozer]

# مستوى اللوج
log_level = 2

# تحذير لو شغال root
warn_on_root = 1
