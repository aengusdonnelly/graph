# SimpleMatirxGraph
## Beskrivning
SimpleMatrixGraph är ett bibliotek för att skapa simpla grafnätverk för att sortera och organisera relationer mellan olika typer av data. Minnet är i formen av en matrisstruktur. Biblioteket ger även möjligheten att kvantitativt och analaytiskt undersöka grafnätverket. Varje metod innehåller dokumentationskommentarer för underlättning av användbarheten, och bifogat finns en testkod för att demonstrera funktionaliteten.

## Användbarhet
SimpleMatrixGraph biblioteket låter dig:
* Skapa grafnätverk.
* Lägga till och ta bort hörn bestående av olika dattyper i grafen.
* Länka och avlänka kanter mellan hörn i grafen.
* Undersöka existens av kanter och hörn.
* Undersökka vilka grannar som ett hörn har och graden av hörnet.
* Undersöka avståndet mellan två hörn.
* Undersöka om två hörn är sammankopplade i ett eller flera led av kanter.

Programmet saknar användargränssnitt och är endast tänk att hanteras i minnet för andra implimentationer.

## Krav:
Systemet som biblioteket används i måste ha nympy installerat. Se **Installation**

## Installation:
1. Ladda hem SimpleMatirxGraph.py till relevant mapp
2. importera SimpleMatirxGraph.py i ditt script:

```python
from SimpleMatirxGraph.py import *
```
3. Installera numpy på din enhet:
```bash
pip install numpy
```
