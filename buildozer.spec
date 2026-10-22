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

# (list) Application requirements
# Add python3, kivy, and our tools
requirements = python3,kivy,pillow,qrcode

# (str) Supported orientation (landscape or portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# (e.g. INTERNET to load local files or network if needed)
android.permissions = INTERNET

# (str) Supported architectures
android.archs = arm64-v8a

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1