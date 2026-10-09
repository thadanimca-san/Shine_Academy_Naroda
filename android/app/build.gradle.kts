plugins {
    id("com.android.application")
    // The Flutter Gradle Plugin must be applied after the Android and Kotlin Gradle plugins.
    id("dev.flutter.flutter-gradle-plugin")
}

android {
    namespace = "com.shineacademy.shine_academy_naroda"
    compileSdk = flutter.compileSdkVersion
    ndkVersion = flutter.ndkVersion

    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }

    buildFeatures {
        resValues = true
    }

    defaultConfig {
        // TODO: Specify your own unique Application ID (https://developer.android.com/studio/build/application-id.html).
        applicationId = "com.shineacademynaroda"
        // You can update the following values to match your application needs.
        // For more information, see: https://flutter.dev/to/review-gradle-config.
        minSdk = flutter.minSdkVersion
        targetSdk = flutter.targetSdkVersion
        versionCode = flutter.versionCode
        versionName = flutter.versionName
    }

    flavorDimensions += "app_type"

    productFlavors {
        create("primary") {
            dimension = "app_type"
            applicationIdSuffix = ".primary"
            resValue("string", "app_name", "Shine Primary")
        }
        create("middle") {
            dimension = "app_type"
            applicationIdSuffix = ".middle"
            resValue("string", "app_name", "Shine Middle")
        }
        create("highschool") {
            dimension = "app_type"
            applicationIdSuffix = ".highschool"
            resValue("string", "app_name", "Shine HighSchool")
        }
        create("commerce") {
            dimension = "app_type"
            applicationIdSuffix = ".commerce"
            resValue("string", "app_name", "Shine Commerce")
        }
        create("achievers") {
            dimension = "app_type"
            applicationIdSuffix = ".achievers"
            resValue("string", "app_name", "Shine Achievers")
        }
        create("skillup") {
            dimension = "app_type"
            applicationIdSuffix = ".skillup"
            resValue("string", "app_name", "Shine SkillUp")
        }
    }

    buildTypes {
        release {
            // TODO: Add your own signing config for the release build.
            // Signing with the debug keys for now, so `flutter run --release` works.
            signingConfig = signingConfigs.getByName("debug")
            isMinifyEnabled = false
            isShrinkResources = false
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}

kotlin {
    compilerOptions {
        jvmTarget = org.jetbrains.kotlin.gradle.dsl.JvmTarget.JVM_17
    }
}

flutter {
    source = "../.."
}
