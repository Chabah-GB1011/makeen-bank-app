[app]

# (str) Title of your application
title = Makeen Bank & Empire

# (str) Package name
package.name = makeenbank

# (str) Package domain (needed for android/ios packaging)
package.domain = org.makeen

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (include all required text/media extensions)
source.include_exts = py,png,jpg,kv,atlas,html,css,js

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET

# (str) Supported architectures
android.archs = arm64-v8a

# Automatically accept Android SDK licenses
android.accept_sdk_license = True

# Target Android API & NDK Configuration
android.api = 31
android.minapi = 21
android.ndk = 25
android.gradle_version = 7.4.2

# Enable AndroidX
android.enable_androidx = True

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
