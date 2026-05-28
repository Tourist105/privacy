#!/usr/bin/env python3
"""Generate privacy-i18n.json by translating the concise English privacy policy
into every target locale via the free Google Translate endpoint."""
import json, time, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "privacy-i18n.json"

SRC = {
    "title": "Privacy Policy",
    "updated": "Last updated May 2026 · Applies to every ch.roethlisberger.* app.",
    "intro": "One short policy for every app I publish on Google Play — they all share the same minimal data practices.",
    "h_collect": "What I collect",
    "collect": "Directly: nothing. No servers, no accounts, no analytics, no login. Some apps process data only on your device — GPS, sensor, microphone or camera input is used live and then discarded, and never leaves your phone unless you choose to share it.",
    "h_third": "Third parties",
    "third1": "Google AdMob shows one banner ad per app and may receive your advertising ID, coarse IP-based location, and device, OS and app version, governed by Google's privacy policy. You can reset the advertising ID or opt out of personalised ads in your device settings.",
    "third2": "A few apps can optionally call Google's Gemini API, but only if you enter your own API key. Receipt Categorizer also uses on-device Google ML Kit text recognition (nothing is uploaded). The Google Play in-app review prompt is handled entirely by Google.",
    "h_not": "What I never do",
    "notx": "No tracking, no profiling, no fingerprinting, no cookies, no selling of data, and no analytics SDKs such as Firebase Analytics or Crashlytics.",
    "h_perm": "Permissions",
    "perm": "Each permission maps to a feature you use: location for coordinates, heading and speed; camera for on-device receipt scanning; microphone for the sound meter; NFC to read tags you tap; vibration for haptic feedback; and internet plus the advertising ID for the banner ad.",
    "h_rights": "Your data and rights",
    "rights": "Anything an app stores — waypoints, history, API keys — stays on your device and is removed when you uninstall it or clear its data. Under GDPR, CCPA and similar laws you may request access or deletion, but since no data about you exists on my side, there is nothing to retrieve. These apps are not directed at children.",
    "h_contact": "Contact",
    "contact_pre": "Questions? Reach me at",
    "authoritative": "The English version is authoritative.",
}
LOCALES = {
    "de":"de","fr":"fr","it":"it","es":"es","pt":"pt","nl":"nl","pl":"pl","ru":"ru","uk":"uk",
    "cs":"cs","da":"da","sv":"sv","ro":"ro","hu":"hu","el":"el","tr":"tr","ar":"ar","fa":"fa",
    "he":"iw","hi":"hi","bn":"bn","ur":"ur","th":"th","vi":"vi","id":"id","ms":"ms","tl":"tl",
    "ja":"ja","ko":"ko","zh-CN":"zh-CN","zh-TW":"zh-TW",
}

def gtx(text, tl):
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=en&tl=%s&dt=t&q=%s" % (
        tl, urllib.parse.quote(text))
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    data = json.loads(urllib.request.urlopen(req, timeout=25).read().decode("utf-8"))
    return "".join(seg[0] for seg in data[0] if seg[0])

def batch(strings, tl):
    full = gtx("\n".join(strings), tl)
    out = full.split("\n")
    if len(out) == len(strings):
        return [s.strip() for s in out]
    res = []
    for s in strings:
        res.append(gtx(s, tl).strip()); time.sleep(0.05)
    return res

def main():
    keys = list(SRC.keys()); vals = [SRC[k] for k in keys]
    result = {"en": dict(SRC)}
    for loc, code in LOCALES.items():
        for a in range(3):
            try:
                result[loc] = {k: v for k, v in zip(keys, batch(vals, code))}
                print(f"  {loc} ok"); break
            except Exception as e:
                print(f"  {loc} retry {a}: {e}"); time.sleep(1.0)
        time.sleep(0.1)
    result["de-CH"] = dict(result["de"])
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {OUT} ({len(result)} locales)")

if __name__ == "__main__":
    main()
