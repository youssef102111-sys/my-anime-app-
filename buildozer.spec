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

android.api = 33
android.minapi = 21
android.archs = arm64-v8a

icon.filename = icon.png
android.presplash.filename = icon.png


[buildozer]

log_level = 2
warn_on_root = 1
