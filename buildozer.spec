[app]

# (str) Title of your application
title = My Anime App

# (str) Package name
package.name = myanimeapp

# (str) Package domain (change to anything unique)
package.domain = org.test

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0


# ================= ANDROID =================

# (str) Android API to use
android.api = 34

# (str) Minimum API your APK will support
android.minapi = 21

# (int) Android SDK version
android.sdk = 34

# (str) Android NDK version (المهم هنا 👇)
android.ndk = 25c

# (bool) Accept SDK license automatically
android.accept_sdk_license = True

# (list) Permissions
android.permissions = INTERNET


# =================================================


[buildozer]

# (int) Log level
log_level = 2

# (int) Warn on root
warn_on_root = 1
