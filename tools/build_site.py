#!/usr/bin/env python3
"""
Builds the adamselite.com games site from the APPS list below.

    python3 tools/build_site.py

Writes:  index.html, apps/<slug>/index.html, apps/<slug>/privacy/index.html
To add or change an app, edit APPS and run the script again.
Every privacy policy is generated from the same template, so they all read the same way;
each app's entries describe what that app actually does (checked against its code).
"""
import html, os

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTACT = "support@adamselite.com"
PUBLISHER = "adamselite.com"
EFFECTIVE = "October 21, 2026"

GOOGLE_PARTNERS = "https://policies.google.com/technologies/partner-sites"
GOOGLE_PRIVACY = "https://policies.google.com/privacy"

APPS = [
    dict(
        slug="sling-slam", name="Sling Slam", package="com.adamselite.slingslam",
        icon="sling-slam-icon.png", repo="slingslam",
        effective="October 23, 2026",
        tagline="Lob boulders with a giant sling to smash the rocks rolling at your wall.",
        features=[
            "Pull back on the sling to aim and set power; a side view shows every shot's arc.",
            "Smash rolling boulders, jagged rocks and tumbling rock clusters before they reach your shield.",
            "Each level ends with a stone golem boss that soaks up stray stones and throws them back.",
            "Chained split shots, sling upgrades, power cells and gold.",
            "Scoreboard of your last 20 runs and a tutorial.",
        ],
        local_data="your high score, your last 20 runs (score, level reached and whether you used a continue), your sound setting and whether you finished the tutorial",
        erase="by clearing the app's data in your phone's settings, or by uninstalling the app",
        device=[
            "<strong>Vibration</strong> for short haptic feedback, such as when a rock hits your wall.",
        ],
        ads="a banner at the top of the screen, an occasional full-screen ad between games, and an optional ad you can choose to watch to continue after your shield runs out",
        consent="the game asks for your consent before personalized ads are shown; you can change your choice later with <strong>Privacy settings</strong> on the Scoreboard screen",
        purchase=None,
    ),
    dict(
        slug="trench-run", name="Trench Run", package="com.adamselite.trenchrun",
        icon="trench-run-icon.png", repo="Trench-Run",
        tagline="Tilt your phone to fly a fighter down a narrow trench at full speed.",
        features=[
            "Tilt to steer, climb and dive. No on-screen joystick.",
            "Dodge bridges, raised floors, walls and pillars; shoot down drones and turret lasers.",
            "Collect shield cells, laser upgrades and slow-mo orbs; pull them in with the tractor beam.",
            "Earn badges and chase your high score.",
            "Trench Run Pro: no ads, Zen mode, all badges and ad-free continues.",
        ],
        local_data="your scoreboard, badges, lifetime statistics and settings (such as sound and control preferences)",
        erase="with <strong>Clear All</strong> on the Scores &amp; Badges screen, or by uninstalling the app",
        device=[
            "<strong>Motion sensors</strong> (accelerometer) to steer. Readings are used live for control only and are never stored or sent anywhere.",
            "<strong>Vibration</strong> for haptic feedback during play.",
            "<strong>Text-to-speech</strong>: spoken warnings use your device's own text-to-speech engine.",
        ],
        ads="a banner on menu screens, an occasional full-screen ad between runs, and an optional ad you can choose to watch to continue after a crash",
        consent="the game asks for your consent before ads are personalized",
        purchase=("Trench Run Pro", "remove ads and unlock Pro features"),
    ),
    dict(
        slug="horizon-run", name="Horizon Run", package="com.adamselite.horizonrun",
        icon="horizon-run-icon.png", repo="horizon-run",
        tagline="Run toward the horizon of a tiny, curved planet. How far can you go?",
        features=[
            "Tilt to steer between trees, rocks, deer, foxes and bears rising over the horizon.",
            "Tap to jump, tap again for a high jump; hold to sprint.",
            "Collect flower trails and rare golden flowers; slow down with glowing snails.",
            "Badges, lifetime stats and your last 10 runs.",
            "Full Version upgrade: no ads plus extra features.",
        ],
        local_data="your best score, your last 10 runs (date, score, items collected and run length), lifetime stats, top 10, badges, settings and whether you finished the tutorial",
        erase="with <strong>Scores &rarr; Reset scores</strong> in the game, or by uninstalling the app",
        device=[
            "<strong>Motion sensors</strong> (accelerometer) to steer. Readings are used live for control only and are never stored or sent anywhere.",
            "<strong>Vibration</strong> for short haptic feedback, such as on a crash.",
        ],
        ads="an optional ad you can choose to watch to keep running after a crash, and an occasional ad between games",
        consent="the game asks for your consent before personalized ads are shown; you can change your choice later from the <strong>Privacy</strong> button on the Scores screen",
        purchase=("Full Version", "remove ads and unlock the full-version features"),
    ),
    dict(
        slug="stop-time", name="StopTime", package="com.adamselite.stoptime",
        icon="stop-time-icon.png", repo="StopTime",
        tagline="Stop the clock at exactly 1.00 second. Sounds easy. It isn't.",
        features=[
            "One button, one second: stop the clock at exactly 1.00.",
            "Easy mode shows the clock; in Hard mode it disappears while it runs.",
            "35 achievements to unlock, with separate stats for each mode.",
            "Light and dark themes.",
            "Optional one-time Remove Ads purchase.",
        ],
        local_data="your game statistics (tries, perfect stops and streaks), unlocked achievements and settings (Easy/Hard mode, light/dark theme, sound)",
        erase="with <strong>Reset all achievements</strong> in the app, or by uninstalling it",
        device=[],
        ads="a banner and an occasional full-screen ad",
        consent="the app asks for your consent before personalized ads are shown; you can change your choice at any time with <strong>Privacy settings</strong> on the Achievements screen",
        purchase=("Remove Ads", "turn off ads"),
    ),
    dict(
        slug="how-far-is-graceland", name="How Far Is Graceland", package="com.adamselite.gracelandmiles",
        icon="how-far-is-graceland-icon.png", repo="graceland",
        tagline="How far are you from Graceland? Find out, and follow the compass there.",
        features=[
            "One tap shows your distance to Graceland, in miles or kilometres.",
            "A live compass points the way.",
            "Day, evening and night backgrounds, with Elvis Time alongside your local time.",
            "Pro upgrade: no ads and more Elvis-related places.",
        ],
        local_data="your miles/kilometres setting, a count of distance checks (used to space out ads), and whether you own Pro",
        erase="by uninstalling the app or clearing its data in your phone's settings",
        device=[
            "<strong>Location</strong>, only with your permission and only when you ask for a distance: your position is used on your device to calculate the distance and direction to Graceland and the other places in the app. It is not stored by us, not sent to our servers (we have none) and not shared with anyone.",
            "<strong>Motion and orientation sensors</strong> to turn the compass. Readings are used live and never stored or sent anywhere.",
        ],
        ads="a banner and an occasional full-screen ad",
        consent="the app asks for your consent before personalized ads are shown; you can change your choice at any time with <strong>Privacy settings</strong> at the bottom of the main screen",
        purchase=("Pro", "remove ads and unlock extra places"),
    ),
    dict(
        slug="inner-circle", name="Inner Circle", package="com.example.innercircle",
        icon="inner-circle-icon.png", repo="Innercircle",
        tagline="Stay inside the ring as it closes in. Move less, score more.",
        features=[
            "A wandering ring closes in: keep inside it until it stops.",
            "The less you move, the higher you score.",
            "New shapes unlock as you level up, each with its own score multiplier.",
            "Practice mode, themes and stats.",
        ],
        local_data="your scores, best run, level progress, stats and settings",
        erase="with the reset option in the game, or by uninstalling it",
        device=[],
        offline=True,
        ads=None, consent=None, purchase=None,
    ),
    dict(
        slug="tuts-trumpets", name="Tut's Trumpets", package="com.randaladams.tuttrumpets",
        icon="tuts-trumpets-icon.png", repo="tut-trumpets",
        tagline="Play the two trumpets from Tutankhamun's tomb, from the 1939 BBC broadcast.",
        features=[
            "Silver and copper trumpets, with notes taken from the BBC's live broadcast of 16 April 1939.",
            "Press and hold to play; slide between notes.",
            "Listen to the full 1939 broadcast and read more about the trumpets.",
        ],
        local_data=None,
        erase=None,
        device=[],
        offline=True,
        links_out=True,
        ads=None, consent=None, purchase=None,
    ),
]

# ----------------------------------------------------------------------------- page parts

def page(title, desc, body, nav):
    links = "".join(f'<a href="{h}">{t}</a>' for t, h in nav)
    return f"""<!doctype html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="stylesheet" href="/assets/style.css">
</head><body>
<header><div class="wrap"><a class="brand" href="/">adamselite.com</a><nav>{links}</nav></div></header>
<main><div class="wrap">
{body}
</div></main>
<footer><div class="wrap">&copy; 2026 adamselite.com &middot; <a href="mailto:{CONTACT}">{CONTACT}</a></div></footer>
</body></html>
"""

def home():
    cards = "\n".join(f"""<a class="card" href="/apps/{a['slug']}/">
  <img src="/assets/{a['icon']}" alt="{html.escape(a['name'])} icon" width="96" height="96">
  <div><h3>{html.escape(a['name'])}</h3><p>{html.escape(a['tagline'])}</p><span class="tag">Android</span></div>
</a>""" for a in APPS)
    body = f"""<h1>Games &amp; apps</h1>
<p class="lead">Mobile games and apps by adamselite.com.</p>
<div class="grid">
{cards}
</div>
<h2>Support</h2>
<p>Questions about any of our apps? Email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>"""
    return page("adamselite.com", "Mobile games and apps by adamselite.com.", body,
                [("Apps", "/"), ("Support", f"mailto:{CONTACT}")])

def app_page(a):
    feats = "\n".join(f"<li>{html.escape(f)}</li>" for f in a["features"])
    body = f"""<div class="hero"><img src="/assets/{a['icon']}" alt="{html.escape(a['name'])} icon" width="128" height="128">
<div><h1>{html.escape(a['name'])}</h1><p class="lead">{html.escape(a['tagline'])}</p></div></div>
<ul>
{feats}
</ul>
<h2>Support</h2>
<p>Questions or problems? Email <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<p><a href="/apps/{a['slug']}/privacy/">Privacy policy</a></p>"""
    return page(a["name"], a["tagline"], body,
                [("All apps", "/"), ("Privacy", f"/apps/{a['slug']}/privacy/"), ("Support", f"mailto:{CONTACT}")])

def privacy_page(a):
    n = html.escape(a["name"])
    ads, purchase, offline = a.get("ads"), a.get("purchase"), a.get("offline")
    short = ["We don't ask for your name, email or any account. There is no sign-in."]
    if a.get("local_data"):
        short.append("Your progress and settings are stored only on your device.")
    else:
        short.append("The app doesn't save any personal information.")
    if any("Location" in d for d in a["device"]):
        short.append("Your location is used only on your device, only when you ask, and is never sent to us.")
    if ads:
        short.append(("The free version shows" if purchase else "The app shows") + " ads from Google AdMob. Google may collect device information to serve and measure those ads, as described below.")
    if purchase:
        short.append(f"The optional {html.escape(purchase[0])} purchase is handled by Google Play. We never see your payment details.")
    if offline:
        short.append("The app doesn't connect to the internet, shows no ads and has no purchases.")

    s = [f"""<h1>{n} Privacy Policy</h1>
<p class="lead">Effective {a.get('effective', EFFECTIVE)}</p>
<p>This policy explains what information the {n} app for Android (<code>{a['package']}</code>, "the app") uses, and why. The app is published by {PUBLISHER} ("we", "us"). If you have questions, contact <a href="mailto:{CONTACT}">{CONTACT}</a>.</p>
<h2>The short version</h2>
<ul>{''.join(f'<li>{x}</li>' for x in short)}</ul>"""]

    if a.get("local_data"):
        s.append(f"""<h2>Information stored on your device</h2>
<p>The app saves {a['local_data']} on your device so they're there next time. We don't receive this information. You can erase it {a['erase']}. If you use Android's built-in backup, your device may include this data in its backup to your Google account, under Google's terms.</p>""")
    else:
        s.append("""<h2>Information stored on your device</h2>
<p>The app doesn't save any personal information. Android may keep its normal app settings, which are deleted when you uninstall the app.</p>""")

    dev = list(a["device"])
    if a.get("links_out"):
        dev.append("<strong>Links</strong>: the info screen can open web pages (Wikipedia and the BBC) in your browser. Those sites have their own privacy policies.")
    if offline:
        dev.append("<strong>No internet access</strong>: the app does not request internet permission, so it cannot send anything off your device.")
    else:
        dev.append("<strong>Internet access</strong> is used only to load ads in the free version and to process purchases through Google Play." if purchase
                   else "<strong>Internet access</strong> is used only to load ads.")
    s.append("<h2>Device features the app uses</h2>\n<ul>" + "".join(f"<li>{d}</li>" for d in dev) + "</ul>")

    if ads:
        consent = (f"<p>Where required by law (for example in the European Economic Area, the UK and Switzerland), {a['consent']}.</p>"
                   if a.get("consent") else "")
        s.append(f"""<h2>Advertising{' (free version)' if purchase else ''}</h2>
<p>{'The free version shows' if purchase else 'The app shows'} ads from Google AdMob, a service of Google LLC: {a['ads']}. To deliver, measure and limit ads, and to prevent fraud, Google may collect and process information such as your device's advertising ID and other device identifiers, your IP address and the approximate location derived from it, device and app information, and how you interact with ads. This information is collected by Google, not by us. Learn more in <a href="{GOOGLE_PARTNERS}">How Google uses information from sites or apps that use its services</a> and the <a href="{GOOGLE_PRIVACY}">Google Privacy Policy</a>.</p>
{consent}<p>You can reset your advertising ID or opt out of ad personalization in your device's settings (Settings &rarr; Google &rarr; Ads, or Settings &rarr; Privacy &rarr; Ads, depending on your device).</p>""")
        if purchase:
            s.append(f"<p>Once you own {html.escape(purchase[0])}, the app no longer shows ads.</p>")

    if purchase:
        s.append(f"""<h2>Purchases</h2>
<p>The optional {html.escape(purchase[0])} upgrade is sold through Google Play to {purchase[1]}. Google processes the payment and tells the app only whether you own it, so it can be restored after a reinstall. We don't receive your name, payment card or billing details. See the <a href="{GOOGLE_PRIVACY}">Google Privacy Policy</a>.</p>""")

    s.append(f"""<h2>Children</h2>
<p>The app is not directed to children under 13, and we don't knowingly collect personal information from children. If you believe a child has provided personal information through the app, contact us and we'll help address it.</p>
<h2>Sharing and selling</h2>
<p>We don't sell or share personal information, because we don't collect it.{' Information collected by Google for ads or purchases is governed by Google&#39;s policies linked above.' if (ads or purchase) else ''}</p>
<h2>Changes to this policy</h2>
<p>If we change this policy, we'll update this page and its effective date.</p>
<h2>Contact</h2>
<p class="note">{PUBLISHER} &middot; <a href="mailto:{CONTACT}">{CONTACT}</a></p>""")

    return page(f"{a['name']} Privacy Policy", f"Privacy policy for the {a['name']} app.", "\n".join(s),
                [(a["name"], f"/apps/{a['slug']}/"), ("All apps", "/"), ("Support", f"mailto:{CONTACT}")])

def redirect(to):
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><title>Moved</title>
<link rel="canonical" href="{to}"><meta http-equiv="refresh" content="0; url={to}">
</head><body><p>This page has moved to <a href="{to}">{to}</a>.</p></body></html>
"""

def write(rel, text):
    p = os.path.join(SITE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(text)

if __name__ == "__main__":
    write("index.html", home())
    for a in APPS:
        write(f"apps/{a['slug']}/index.html", app_page(a))
        write(f"apps/{a['slug']}/privacy/index.html", privacy_page(a))
    # Trench Run's first pages lived at /trench-run/; keep those addresses working.
    write("trench-run/index.html", redirect("/apps/trench-run/"))
    write("trench-run/privacy/index.html", redirect("/apps/trench-run/privacy/"))
    print("built", len(APPS), "apps")
