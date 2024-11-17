# Eetlijst v5 wrapper

Dit python package heeft een hele simpele HTTP api en een aantal GraphQL scripts.

Om je eigen GraphQL scripts toe te voegen hoef je ze alleen maar in de resources folder te stoppen.
Zorg er wel voor dat de naam van het bestand ook de naam van de query is die je wilt uitvoeren (bijv. `GetBasicGroupInfo.graphql` -> `query GetBasicGroupInfo { ... }`). Er kunnen niet meerdere queries in een bestand staan. Dit is niet heel efficiënt met het oog op fragments hergebruiken, maar nu hoeft de graphql niet geparsed te worden en kan deze als string naar de eetlijst server gestuurd worden.

De GraphQL scripts zijn niet super optimaal, maar ze werken.

Pull requests zijn welkom, succes met scripts beunen.
