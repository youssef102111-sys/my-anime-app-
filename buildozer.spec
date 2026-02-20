[app]

# (str) Title of your application
title = My Anime App

# (str) Package name
package.name = myanimeapp

# (str) Package domain
package.domain = org.test

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements (مهم 👇 ضفنا pyjnius)
requirements = python3,kivy,pyjnius

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# ================= ANDROID =================

android.api = 34
android.minapi = 21
android.sdk = 34

# مهم جداً 👇
android.ndk = 25c

android.accept_sdk_license = True
android.permissions = INTERNET

# مهم علشان يحل مشكلة jnius 👇
android.archs = arm64-v8a


# =================================================


[buildozer]

log_level = 2
warn_on_root = 1
