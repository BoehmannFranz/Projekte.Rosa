# Rosa — Explorativer Bot für Streaming-Validierung (Archiviert)

**Status:** Archiviert / Nicht zur Nutzung bestimmt  
**Zweck:** Technischer Proof-of-Concept zur **Forschung von Erkennungs- und Validierungsmechanismen** bei Musikstreams auf Plattformen wie YouTube und Spotify.  
**Kernaussage:** Der Ansatz ist wirtschaftlich unsinnig, rechtlich riskant und verstößt gegen die Nutzungsbedingungen der Plattformen. Das Repository dient ausschließlich der **Dokumentation von Erkenntnissen**, nicht der Anwendung.

---

## ⚠️ Rechtlicher & ethischer Hinweis

- Das künstliche Erhöhen von Views/Plays **verstößt gegen die AGB** von YouTube/Spotify, kann zu **Sperren, Takedowns, Rückforderungen** und weiteren **rechtlichen Konsequenzen** führen.  
- Dieses Projekt wird **nicht weiterentwickelt** und soll **nicht** ausgeführt, verbreitet oder nachgebaut werden.  
- Ziel war die **Analyse von Limitierungen und Erkennungslogiken**, nicht der produktive Einsatz.

---

## Projektüberblick

**Kurzbeschreibung:**  
„Rosa“ automatisiert mit Selenium den Login in Spotify, die Suche nach Künstler/Titel und das Starten von Songs, um Validierungsgrenzen, Mindest-Playzeiten und Erkennungsmechanismen zu beobachten.

**Technischer Stack (Code zeigt u. a.):**
- Python 3  
- Selenium WebDriver (Chrome)  
- Zufalls-Timing/„Humanisierung“ der Play-Dauer  
- Element-Selektion via XPath

> Wichtige interne Datei: `accounts.py` (nicht enthalten) – enthält Zugangsdaten; schon aus Sicherheitsgründen **nie** in Repositories ablegen.

---

## Zentrale Erkenntnisse aus dem PoC

1. **Zeitliche Mindestgrenzen**  
   Sowohl YouTube als auch Spotify scheinen **zeitliche Mindestanforderungen** für „gültige“ Plays/Views zu haben. Details sind **nicht öffentlich** dokumentiert.

2. **Intransparente Anerkennung**  
   Die **Anerkennungsmechanismen** (welcher Play als „gültig“ zählt) sind **nicht offengelegt** und ändern sich vermutlich dynamisch.

3. **Wirtschaftlichkeit: negativ**  
   Bis zu **10.000 automatisierte Plays pro Song** waren technisch erreichbar; **Stromkosten** und Infrastrukturaufwand **übersteigen** die potenziellen Einnahmen deutlich.

4. **Parallelisierung ≠ Lösung**  
   Eine effektive Skalierung würde **Bot-Netzwerke und viele Accounts** erfordern – **zu hoher Aufwand**, zusätzliche **Risiken**.

5. **Anerkennungsquote (Beispielmessung)**  
   - Nach ~6 Monaten Testlauf wurden auf YouTube nur ca. **10 %** der registrierten Klicks als gültig anerkannt.  
   - Beispiel: **~90.000** registrierte Klicks vs. **~9.000** anerkannte/vergütete.  
   - Vertrieb/Distributor ist an die Plattform-Anerkennung gebunden.

6. **Marktbeobachtung**  
   Recherchen legen nahe, dass Plattformen **Botnetze erkennen und drosseln**, aber nicht jedes Verhalten sofort sanktionieren. **These:** Professionelle, seit 2020 existierende Netzwerke könnten im Markt agieren – **nicht verifiziert**, aber Indizien vorhanden.  

---

## Warum das Projekt eingestellt wurde

- **Rechtliche und vertragliche Risiken** (AGB-Verstöße)  
- **Negative Kosten-Nutzen-Bilanz** (Energie, Infrastruktur, Maintenance)  
- **Geringe Planbarkeit** (dynamische Erkennungsmechanismen, Quoten)  
- **Reputationsrisiko** gegenüber Plattformen, Partnern und Fans

---

## Dateistruktur (relevant)

- `main.py` / Funktionskern (z. B. `VioletInAction`) – steuert Login, Suche, Play  
- `accounts.py` – Zugangsdaten (nicht enthalten, niemals committen)  
- sonstige Imports: Selenium, `time`, `random`, `webdriver`-Konfiguration

> **Keine** Run-Anleitung enthalten. Das Projekt ist **nicht** für die Ausführung vorgesehen.

---

## Risiken & Grenzen

- **Account-Sperren / Katalog-Entzug**  
- **Revenue-Clawbacks** durch Plattformen/Distributor  
- **Sicherheitsrisiken** durch Umgang mit Zugangsdaten  
- **Technische Fragilität** (DOM/XPath ändern sich häufig)

---

## Empfohlene, legitime Alternativen

- **Plattform-konforme Promotion**: Editorial & Algorithmic Pitching, Pre-Saves, Release-Kalender, Fan-Engagement  
- **Datengetriebene Kampagnen**: A/B-Tests für Creatives, Zielgruppen-Segmente, Conversion-Tracking (legal, DSGVO-konform)  
- **Kollaborationen & Playlists**: Kuratoren-Outreach, UGC-Strategien, Shorts/Reels mit organischer Hook  
- **Katalog-Optimierung**: Sauberes ISRC/Metadata, Canvas/Thumbnails, Chaptering, regelmäßiger Release-Rhythmus  
- **Transparente Analytics**: Plattform-Insights, Distributoren-Reports, eigene Dashboards (keine künstlichen Plays)

---

## Lizenz

Kein Lizenzrecht zur Nutzung – **„No License / Read-Only“**.  
Jede Verwendung, Ausführung oder Ableitung ist **nicht gestattet**.

---

## Haftungsausschluss

Dieses Repository dokumentiert einen **eingestellten Forschungs-PoC**.  
Es erhebt **keinen Anspruch auf Vollständigkeit** und darf **nicht** als Anleitung verstanden werden. Nutzung auf eigene Gefahr; der Autor lehnt jede Haftung ab.

---

## Kontakt

Für Fragen zur **analytics-basierten, regelkonformen** Musik-Promotion und Messung von Kampagnen-Effekten gern melden.
