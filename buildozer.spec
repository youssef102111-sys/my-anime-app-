[app]

# اسم التطبيق
title = Emperor Anime

# اسم الباكدج (من غير مسافات)
package.name = emperoranime
package.domain = org.emperor

# مكان الكود
source.dir = .
source.include_exts = py,png,jpg,jpeg,kv
source.exclude_exts = spec

# النسخة
version = 1.0

# المتطلبات (شيلنا plyer)
requirements = python3,kivy

# الاتجاه
orientation = portrait

# أذونات
android.permissions = INTERNET

# نسخة أندرويد
android.api = 33
android.minapi = 21

# المعمارية (مهم عشان يشتغل على موبايلك)
android.archs = armeabi-v7a, arm64-v8a

# عدم ملء الشاشة
fullscreen = 0


[buildozer]

log_level = 2
warn_on_root = 1
