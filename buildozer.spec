[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy==2.2.1

orientation = portrait
fullscreen = 0

# -------- Android --------

android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True
android.enable_androidx = True
android.use_androidx = True
