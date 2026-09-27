package com.shineacademy.shine_academy_naroda

import android.content.Intent
import android.provider.Settings
import android.speech.tts.TextToSpeech
import android.view.WindowManager
import io.flutter.embedding.android.FlutterActivity
import io.flutter.embedding.engine.FlutterEngine
import io.flutter.plugin.common.MethodChannel

class MainActivity : FlutterActivity() {

    // Channel name must match exactly what Dart-side uses
    private val TTS_CHANNEL = "shine.academy/tts_settings"
    private val SECURITY_CHANNEL = "shine.academy/security"

    override fun configureFlutterEngine(flutterEngine: FlutterEngine) {
        super.configureFlutterEngine(flutterEngine)

        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, TTS_CHANNEL)
            .setMethodCallHandler { call, result ->

                when (call.method) {

                    // ─── Open Android TTS Settings page ───────────────────────
                    // Works on ALL Android versions including stripped AOSP panels.
                    // This is the most reliable way to get to TTS settings when the
                    // standard Accessibility → TTS path is missing from Settings UI.
                    "openTtsSettings" -> {
                        try {
                            val intent = Intent(Settings.ACTION_ACCESSIBILITY_SETTINGS)
                            intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK
                            startActivity(intent)
                            result.success("ACCESSIBILITY_SETTINGS_OPENED")
                        } catch (e: Exception) {
                            // Fallback 1: Try the direct TTS settings action
                            try {
                                val intent = Intent("com.android.settings.TTS_SETTINGS")
                                intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK
                                startActivity(intent)
                                result.success("TTS_SETTINGS_OPENED_DIRECT")
                            } catch (e2: Exception) {
                                // Fallback 2: Open plain Settings
                                try {
                                    val intent = Intent(Settings.ACTION_SETTINGS)
                                    intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK
                                    startActivity(intent)
                                    result.success("PLAIN_SETTINGS_OPENED")
                                } catch (e3: Exception) {
                                    result.error("SETTINGS_OPEN_FAILED", e3.message, null)
                                }
                            }
                        }
                    }

                    // ─── Open Language & Input settings (common AOSP path to TTS) ─
                    "openLanguageSettings" -> {
                        try {
                            val intent = Intent(Settings.ACTION_LOCALE_SETTINGS)
                            intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK
                            startActivity(intent)
                            result.success("LOCALE_SETTINGS_OPENED")
                        } catch (e: Exception) {
                            result.error("FAILED", e.message, null)
                        }
                    }

                    // ─── Query all installed TTS engines ──────────────────────────
                    // Returns a list of engine package names installed on the device.
                    // Used by the diagnostic screen to show what's available.
                    "getInstalledEngines" -> {
                        try {
                            val tts = TextToSpeech(this, null)
                            val engines = tts.engines
                            val engineNames = engines.map { it.name }
                            tts.shutdown()
                            result.success(engineNames)
                        } catch (e: Exception) {
                            result.success(listOf<String>()) // Return empty, don't crash
                        }
                    }

                    // ─── Set default TTS engine programmatically ──────────────────
                    // On Android 13 AOSP panels, this writes to the secure Settings
                    // database the same way "Settings → TTS → Select Engine" does.
                    // Does NOT require root. Uses the same API the Settings app uses.
                    "setGoogleTtsEngine" -> {
                        try {
                            // Write to secure settings — sets Google TTS as default engine
                            Settings.Secure.putString(
                                contentResolver,
                                "tts_default_synth",
                                "com.google.android.tts"
                            )
                            result.success("ENGINE_SET_OK")
                        } catch (e: SecurityException) {
                            // This can fail if the app doesn't have WRITE_SECURE_SETTINGS
                            // In that case, we fall back to opening the settings UI
                            result.error(
                                "SECURITY_EXCEPTION",
                                "Cannot write secure settings without WRITE_SECURE_SETTINGS permission. " +
                                "Use ADB: adb shell settings put secure tts_default_synth com.google.android.tts",
                                null
                            )
                        } catch (e: Exception) {
                            result.error("FAILED", e.message, null)
                        }
                    }

                    // ─── Get current default TTS engine ───────────────────────────
                    "getDefaultEngine" -> {
                        try {
                            val engine = Settings.Secure.getString(
                                contentResolver,
                                "tts_default_synth"
                            )
                            result.success(engine ?: "not_set")
                        } catch (e: Exception) {
                            result.success("unknown")
                        }
                    }

                    else -> result.notImplemented()
                }
            }

        // ─── Security Channel (Screen Protection) ───────────────────────
        MethodChannel(flutterEngine.dartExecutor.binaryMessenger, SECURITY_CHANNEL)
            .setMethodCallHandler { call, result ->
                if (call.method == "setScreenProtection") {
                    val enabled = call.argument<Boolean>("enabled") ?: false
                    if (enabled) {
                        window.addFlags(WindowManager.LayoutParams.FLAG_SECURE)
                    } else {
                        window.clearFlags(WindowManager.LayoutParams.FLAG_SECURE)
                    }
                    result.success(null)
                } else {
                    result.notImplemented()
                }
            }
    }
}
