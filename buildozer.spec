[app]

# Title of your application
title = MyApp

# Package name
package.name = myapp

# Package domain (important)
package.domain = org.test

# Source code location
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version (مهم جداً)
version = 0.1

# Application requirements
requirements = python3,kivy==2.3.0,kivymd==1.2.0

# Supported orientation
orientation = portrait

# Fullscreen mode
fullscreen = 0


# ---------------------------------------------
# ---------------- Android --------------------
# ---------------------------------------------

# Target Android API
android.api = 33

# Minimum API
android.minapi = 21

# Android NDK version
android.ndk = 25b

# Automatically accept SDK license
android.accept_sdk_license = True

# Enable AndroidX
android.enable_androidx = True
android.use_androidx = True

# Permissions (لو التطبيق محتاج إنترنت)
android.permissions = INTERNET

# Use private storage
android.private_storage = True
