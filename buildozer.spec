[app]

title = Emperor Anime
package.name = emperoranime
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# Android Settings (مستقر مع GitHub)
android.api = 33
android.minapi = 21
android.archs = arm64-v8a

# ⚠️ سيب الأيقونة فاضية دلوقتي
# icon.filename =
# android.presplash.filename =


[buildozer]

log_level = 2
warn_on_root = 1
