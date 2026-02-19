[app]

title = My Application
package.name = myapp
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

requirements = python3,kivy

orientation = portrait
fullscreen = 0


# -------- Android Specific --------

android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.build_tools = 34.0.0

android.enable_androidx = True
android.use_androidx = True
android.accept_sdk_license = True
