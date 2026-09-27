import Flutter
import UIKit

@main
@objc class AppDelegate: FlutterAppDelegate, FlutterImplicitEngineDelegate {
  private var secureTextField: UITextField?

  override func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let controller : FlutterViewController = window?.rootViewController as! FlutterViewController
    let securityChannel = FlutterMethodChannel(name: "shine.academy/security",
                                              binaryMessenger: controller.binaryMessenger)
    
    securityChannel.setMethodCallHandler({
      [weak self] (call: FlutterMethodCall, result: @escaping FlutterResult) -> Void in
      if call.method == "setScreenProtection" {
        guard let args = call.arguments as? [String: Any],
              let enabled = args["enabled"] as? Bool else {
          result(FlutterError(code: "INVALID_ARGS", message: "enabled boolean required", details: nil))
          return
        }
        self?.setSecureState(enabled: enabled, view: controller.view)
        result(nil)
      } else {
        result(FlutterMethodNotImplemented)
      }
    })

    return super.application(application, didFinishLaunchingWithOptions: launchOptions)
  }

  private func setSecureState(enabled: Bool, view: UIView) {
    if enabled {
      if secureTextField == nil {
        secureTextField = UITextField()
        secureTextField?.isSecureTextEntry = true
        secureTextField?.isUserInteractionEnabled = false
        if let window = self.window {
          window.addSubview(secureTextField!)
          secureTextField?.layer.sublayers?.first?.addSublayer(window.layer)
        }
      }
    } else {
      secureTextField?.removeFromSuperview()
      secureTextField = nil
    }
  }

  func didInitializeImplicitFlutterEngine(_ engineBridge: FlutterImplicitEngineBridge) {
    GeneratedPluginRegistrant.register(with: engineBridge.pluginRegistry)
  }
}
