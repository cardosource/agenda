[app]

# Configurações Básicas
title = Demo
package.name = demo
package.domain = https://github.com/cardosource/agenda
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Requisitos Modernos (Python 3.9+ e Kivy 2.2+)
requirements = 
    python3==3.9.13,
    kivy==2.2.1,
    android,
    pillow,
    openssl

orientation = portrait
fullscreen = 0

# Configurações ANDROID (Atualizadas 2024)
android.api = 33               # Android 13 (última estável)
android.minapi = 21            # Android 5.0 (mínimo)
android.targetapi = 33         # Igual ao android.api
android.sdk = 33
android.ndk = 25b             # NDK mais estável para Kivy

# Permissões Essenciais (Android 12+)
android.permissions = 
    INTERNET,
    ACCESS_NETWORK_STATE,
    ACCESS_WIFI_STATE,
    WRITE_EXTERNAL_STORAGE,
    READ_EXTERNAL_STORAGE,
    CAMERA,
    RECORD_AUDIO,
    WAKE_LOCK,
    VIBRATE

# Otimizações para Android Moderno
android.enable_androidx = True
android.enable_jetifier = True
android.manifest_placeholders = 
    android:targetSandboxVersion="2",
    android:appComponentFactory="androidx.core.app.CoreComponentFactory"

# Suporte a 64-bit (Obrigatório na Play Store)
android.arch = 
    arm64-v8a,   # Celulares modernos
    armeabi-v7a  # Compatibilidade com antigos

# Bibliotecas Nativas (Evitam crashes)
android.add_libs_armeabi_v7a = libsqlite3.so, libcrypto.so
android.add_libs_arm64_v8a = libsqlite3.so, libcrypto.so

# Configurações de Hardware (opcional)
android.features = 
    android.hardware.camera,
    android.hardware.camera.autofocus,
    android.hardware.microphone

[buildozer]
log_level = 2
warn_on_root = 1
