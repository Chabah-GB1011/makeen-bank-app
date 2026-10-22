[app]

# (str) Title of your application
title = Makeen Bank & Empire

# (str) Package name
package.name = makeenbank

# (str) Package domain (needed for android packaging)
package.domain = org.makeen

# (str) Source files where the let's include everything
source.dir = .

# (list) Source files to include (let's add html, css, js and png for the QR code)
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy,pillow,qrcode

# (str) Supported orientation (landscape or portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (str) Supported architectures
android.archs = arm64-v8a

# Automatically accept Android SDK licenses
android.accept_sdk_license = True

# (int) Target Android API
android.api = 31

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
