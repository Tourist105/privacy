#!/usr/bin/env python3
"""Generate privacy-i18n.json by translating the concise English privacy policy
into every target locale via the free Google Translate endpoint."""
import json, time, urllib.parse, urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "privacy-i18n.json"

SRC = {
    "title": "Privacy Policy",
    "updated": "Last updated July 2026. It covers every app I publish on Google Play.",
    "intro": "This one short policy covers every app I publish on Google Play. They all follow the same simple approach to your data.",
    "h_collect": "What I collect",
    "collect": "Nothing reaches me. There are no servers, no accounts, no analytics and no login. Some apps work with data right on your device, such as GPS, sensors, the microphone or the camera. That input is used live and then dropped, and it never leaves your phone unless you choose to share it.",
    "h_third": "Third parties",
    "third1": "Google AdMob shows one banner ad in each app, and my games also offer optional rewarded video ads that you actively choose to watch for an in-game bonus. In the European Economic Area and the UK you are asked for consent first. It may receive your advertising ID, a rough location based on your IP address, and your device, operating system and app version. Google's own privacy policy governs that. You can reset your advertising ID or turn off personalised ads in your device settings.",
    "third2": "A few apps can call Google's Gemini service, but only if you enter your own API key. Receipt Categorizer also reads text with Google ML Kit right on your device, and nothing is uploaded. The Google Play review prompt is handled entirely by Google.",
    "h_not": "What I never do",
    "notx": "No tracking, no profiling, no fingerprinting, no cookies and no selling of data. My utility apps use no analytics tools at all. My games use Google Firebase for stability and quality, described under Games below.",
    "h_perm": "Permissions",
    "perm": "Every permission is tied to a feature you actually use. Location gives coordinates, heading and speed. The camera scans receipts on your device. The microphone runs the sound meter. NFC reads tags you tap. Vibration gives you haptic feedback. Internet and the advertising ID serve the banner ad.",
    "h_games": "Games",
    "games": "My games (such as Ink Survivors) additionally use Google Firebase Analytics and Crashlytics so I can find crashes and improve the game. These services collect device information and anonymous gameplay events under Google's own privacy policy; nothing identifies you personally to me and nothing is sold. Game progress is saved only on your device. The games offer an optional Google Play Games sign-in for achievements, leaderboards and cloud saves; Google then processes your Play Games profile name, avatar and scores. Signing in is always optional and the games are fully playable without it. You can delete your Play Games data for these games at any time in your Google account's Play Games settings.",
    "h_rights": "Your data and rights",
    "rights": "Anything an app saves, such as waypoints, history or API keys, stays on your device. It is gone as soon as you uninstall the app or clear its data. Laws such as GDPR and CCPA let you ask to see or delete your data. Since I hold nothing about you, there is simply nothing for me to look up. These apps are not made for children.",
    "h_retention": "Data retention",
    "retention": "I run no servers, so none of your personal data is kept on my side. Anything an app creates on your device, such as routes, waypoints, history, settings and API keys, stays only on that device for as long as you keep it. It is deleted for good the moment you clear the app's data or uninstall the app. The data Google AdMob uses for the banner ad is kept by Google under Google's own privacy policy. You can reset your advertising ID or turn off personalised ads in your device settings at any time.",
    "h_contact": "Contact",
    "contact_pre": "Questions? Reach me at",
    "authoritative": "The English version is the one that counts.",
}
LOCALES = {
    "de":"de","fr":"fr","it":"it","es":"es","pt":"pt","nl":"nl","pl":"pl","ru":"ru","uk":"uk",
    "cs":"cs","da":"da","sv":"sv","ro":"ro","hu":"hu","el":"el","tr":"tr","ar":"ar","fa":"fa",
    "he":"iw","hi":"hi","bn":"bn","ur":"ur","th":"th","vi":"vi","id":"id","ms":"ms","tl":"tl",
    "ja":"ja","ko":"ko","zh-CN":"zh-CN","zh-TW":"zh-TW",
    "af":"af","am":"am","az-AZ":"az","be":"be","bg":"bg","bn-BD":"bn","ca":"ca","cs-CZ":"cs","da-DK":"da","de-DE":"de","el-GR":"el","es-419":"es","es-ES":"es","es-US":"es","et":"et","eu-ES":"eu","fa-AE":"fa","fa-AF":"fa","fa-IR":"fa","fi-FI":"fi","fil":"tl","fr-CA":"fr","fr-FR":"fr","gl-ES":"gl","gu":"gu","hi-IN":"hi","hr":"hr","hu-HU":"hu","hy-AM":"hy","is-IS":"is","it-IT":"it","iw-IL":"iw","ja-JP":"ja","ka-GE":"ka","kk":"kk","km-KH":"km","kn-IN":"kn","ko-KR":"ko","ky-KG":"ky","lo-LA":"lo","lt":"lt","lv":"lv","mk-MK":"mk","ml-IN":"ml","mn-MN":"mn","mr-IN":"mr","ms-MY":"ms","my-MM":"my","ne-NP":"ne","nl-NL":"nl","no-NO":"no","pa":"pa","pl-PL":"pl","pt-BR":"pt","pt-PT":"pt","rm":"rm","ru-RU":"ru","si-LK":"si","sk":"sk","sl":"sl","sq":"sq","sr":"sr","sv-SE":"sv","sw":"sw","ta-IN":"ta","te-IN":"te","tr-TR":"tr","zh-HK":"zh-TW","zu":"zu",
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
