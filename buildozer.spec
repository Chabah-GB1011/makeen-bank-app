[app]

title = Makeen Bank & Empire
package.name = makeenbank
package.domain = org.makeen
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,css,js
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.archs = arm64-v8a
android.accept_sdk_license = True

# إعدادات الإصدارات الثابتة المتوافقة كلياً
android.api = 31
android.minapi = 21
android.ndk = 25
android.gradle_version = 7.4.2
android.enable_androidx = True

[buildozer]
log_level = 2
warn_on_root = 1
