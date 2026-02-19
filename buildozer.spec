[app]

# (str) Title of your application
title = MyApp

# (str) Package name
package.name = myapp

# (str) Package domain (important)
package.domain = org.test

# (str) Source code location
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 0


# -------------------------------------------------
# ---------------- Android ------------------------
# -------------------------------------------------

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# Automatically accept SDK license
android.accept_sdk_license = True

# Enable AndroidX
android.enable_androidx = True
android.use_androidx = True

# Permissions (لو التطبيق محتاج إنترنت)
android.permissions = INTERNET

# (bool) Use private storage (مهم لتجنب مشاكل صلاحيات)
android.private_storage = True
