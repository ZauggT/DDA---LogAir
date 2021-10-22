Dieses Datenset wurde mit einem LogAir Gerät und der LogAir App erfasst. (ID: LACF-004)

- Infos zum LogAir Gerät: https://logair.io/documentation/
	- Das Gerät misst:
		- Temperatur
		- PM2.5 / PM10 Werte
		- Luftfouchtigkeit

		- Zeitstempel
		- Koordinaten
		- Geschwindigkeit

- Die LogAir App zeigt die gesammelten Daten an. Und ist unter https://logair.io/documentation/ downloadbar (aber nur für Android)

- LogAir Daten über API beziehen, ist aber KAPUTT: https://api.logair.unige.ch/v1/service/device/latest?device_id=LACF-004&latest=10
- Lösung: https://api.logair.unige.ch/v1/service/device/latest?device_id=LA-CF&latest=10 (ohne bestimmte device ID)

--> Der zweite Link spuckt alle Daten aus von der API.
--> latest=10 (letzte 10 Datenpunkte) // latest=1000(letzte 1000 Datenpunkte)


Mein Ziel ist es aus diesen Daten eine Visualisierung zur Luftqualität in Luzern zu machen. Weil es in Luzern nur stationäre Messstationen hat.
Die Messdaten der Stadtionen geben nur Lokal Messwerte heraus, die dann als Globale Luftqualität herausgegeben werden.
Aber wie sieht die Luftqualität in der Stadt Luzern wirklich aus?
Welche Orte in der Stadt könnten ein Risiko darstellen und wie könnte die Zukunft von Luzern in Beziehung zu der Luftqualität aus.

Die Datenerhebung war eine Challenge...
Das Gerät hat einige noch zu Optimierende Punkte:
- Durch das benutzen gab es Wackelkontakt vom PM-Messgerät http://www.plantower.com/en/ und es hat teilweise keine Messungen gemacht.
- Das Gerät hat eine SD-Karte zerstört (nicht mehr formatierbar). Möglicherweise well keine Shutdownsequenz eingebaut wurde.
- Die API für die Daten ist out of date oder kaputt, wenn man auf eine bestimmte Geräte ID zugreifen will.
- Der Standort bei der LogAir App muss immer eingeschaltet sein und nicht nur bei der Nutzung des Geräts.


---------------------------------------------------------------------------------------------------------------------------------------------


