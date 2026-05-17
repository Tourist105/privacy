# Privacy Policy — ch.roethlisberger.* portfolio

**Last updated: 2026-05-17**
**Applies to all 15 apps listed below.**

This single privacy policy covers all apps published by Nils Röthlisberger
on Google Play under the `ch.roethlisberger.*` namespace. We use one
combined policy because all apps share the same minimal data practices.

## 1. Apps covered

Flashlight (LED Torch & SOS), Compass (True North & GPS), GeoFinder
(GPS Coordinates), Bubble Level & Ruler, Protractor (Angle Meter), Stud
Finder, Sound Meter, GPS Speedometer, NFC Reader, Vibration Meter, Metal
Detector, NATO & Morse Translator, Receipt Categorizer, Email Tone
Rewriter, Unit Converter Lite.

## 2. What data we collect

**Directly: nothing.**

We do not run servers, do not maintain user accounts, and do not collect
analytics. None of the apps requires login or sign-up.

Some apps may temporarily process data ON YOUR DEVICE only:

- **GeoFinder, Compass, GPS Speedometer:** GPS coordinates are read from
  your device's location services to show position / heading / speed. The
  coordinates never leave your device unless YOU choose to share them via
  the system Share menu.
- **Stud Finder, Metal Detector, Compass:** Magnetometer + accelerometer
  readings are processed in real time and discarded.
- **Sound Meter, Vibration Meter:** Microphone / accelerometer samples
  are read in real time and discarded; no audio is saved.
- **Receipt Categorizer:** Photo is processed locally via Google ML Kit
  (offline on-device text recognition). The receipt OCR text is then
  optionally categorized via a single short API call to Google's Gemini
  endpoint (only if YOU have entered an API key in the app settings).
- **NFC Reader:** Tag content is read and optionally sent to Google's
  Gemini endpoint for plain-language explanation (only if YOU have
  entered an API key).
- **Email Tone Rewriter:** Email draft you paste is sent to Google's
  Gemini endpoint for rewriting (only if YOU have entered an API key).
  Sent text is not retained by us.

## 3. Data shared with third parties

**Google AdMob** displays a single banner ad in each app. AdMob may
collect:
- Advertising ID (resettable from your device settings)
- IP address, device type, OS version, app version
- General location (city-level from IP)

This data is used by Google for ad personalization and fraud prevention,
governed by Google's privacy policy at
https://policies.google.com/privacy. You can opt out of personalized
ads in your Android device settings → Google → Ads.

**Google Gemini API** (only in NFC Reader, GeoFinder, Receipt Categorizer,
Email Tone Rewriter — and only when YOU have entered a Gemini API key):
the specific request you initiate (NFC tag bytes, address text, receipt
OCR text, or email draft) is sent over HTTPS to Google's Gemini endpoint
using YOUR API key. Google's data handling for the Gemini API is governed
by their AI Terms at https://ai.google.dev/gemini-api/terms.

**Google Play In-App Review API**: when an app shows the Play rating
prompt, Google handles the review submission entirely. We never see your
rating or review content.

**Google ML Kit Text Recognition** (Receipt Categorizer only): runs
fully on-device using a bundled model. No images are uploaded.

## 4. Data NOT collected / NOT used

We do NOT:
- Operate any server that receives your data
- Use Firebase Analytics, Crashlytics, or any third-party SDK other than
  AdMob + Google Play services
- Sell, rent or share data with advertisers beyond what AdMob does
- Use trackers, beacons, or fingerprinting
- Build user profiles
- Use cookies (we don't have a web component)

## 5. Permissions and why we ask for them

- **Internet + Network State**: required to load the AdMob banner ad and
  (in 4 apps) to optionally reach Google's Gemini API.
- **Camera** (Receipt Categorizer): to photograph receipts for on-device
  OCR. Photos are not uploaded.
- **Microphone** (Sound Meter): to measure sound pressure level. Audio
  is not recorded or saved.
- **Location (fine + coarse)** (GeoFinder, Compass, GPS Speedometer):
  to determine your position for the app's stated purpose. Not uploaded.
- **NFC** (NFC Reader): to read NFC tags you tap.
- **Vibrate** (Stud Finder, Metal Detector, others): for haptic feedback.
- **AD_ID** (`com.google.android.gms.permission.AD_ID`): required by
  AdMob on Android 13+ to deliver ads.

## 6. Children's privacy

These apps are not directed at children under 13. We do not knowingly
collect any data from children. If you believe a child has provided us
with personal data, please contact us and we will delete it.

## 7. Data retention

Anything stored locally on your device (waypoints in GeoFinder, receipt
history in Receipt Categorizer, API keys in any AI app) is kept on your
device only. Uninstalling the app deletes all of it. You can also clear
the app's data in Android Settings → Apps → [app name] → Storage.

## 8. Your rights

Under GDPR, CCPA and similar laws you have the right to know what data
we hold about you, request a copy, request deletion, and lodge a
complaint with your local data-protection authority. Since we hold no
data about you on any server, these rights are honoured by default —
your data simply doesn't exist on our side.

## 9. Changes to this policy

If we materially change this policy, we will update the "Last updated"
date at the top. Continued use of the apps after the update means
acceptance.

## 10. Contact

Nils Röthlisberger
nils.roethlisberger@gmx.ch

GitHub: https://github.com/Tourist105 (private repos for most apps)
