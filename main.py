[app]
title = Emperor Anime
package.name = emperoranime
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# إضافة plyer للإشعارات و pillow للصور
requirements = python3,kivy==2.2.1,pillow,requests,urllib3,certifi,chardet,idna,plyer

icon.filename = %(source.dir)s/icon.png
orientation = portrait

# صلاحيات الإنترنت والاهتزاز للإشعارات
android.permissions = INTERNET, VIBRATE, RECEIVE_BOOT_COMPLETED

android.api = 34
android.minapi = 21
android.ndk = 25c
android.sdk = 34
android.archs = arm64-v8a
android.build_mode = debug

[buildozer]
log_level = 2
warn_on_root = 1
