-- Creating a database in Snowflake 
CREATE DATABASE OPENAI_DATABASE;
CREATE SCHEMA PUBLIC;

-- Paragraph pre-samples
DROP TABLE ANZEIGE_PRE;
CREATE TABLE ANZEIGE_PRE (
    PARAGRAPH       varchar(12),
    PARAGRAPH_TEXT  varchar(20000)
);

INSERT INTO ANZEIGE_PRE VALUES
('1', '<Kunde> <Kundeninfo> Selbstentwickelte Programme und Dienstleistungen sind wesentliche Bestandteile des Kerngeschäfts einer Krankenkasse und spielen eine wichtige Rolle bei der Digitalisierung im Bereich der Gesetzlichen Krankenversicherung. Der Schwerpunkt verlagert sich mehr und mehr auf papierlose Prozesse sowie digitale Services und Produkte, wodurch diese Entwicklungen die Versicherten stärker einbeziehen. Zukünftig werden die Anforderungen an die IT und die digitalen Produkte der Kassen an vielen Stellen flexibler und leistungsfähiger aus der Cloud heraus als aus herkömmlichen Rechenzentren erfüllt werden können.
Aus diesem Grund sollen zukünftig Cloud-Technologien und -Services der <Cloud-Anbieter> eingesetzt werden, um das Kundenerlebnis für die Versicherten zu verbessern, wobei stets auf Rechtskonformität und den Schutz der persönlichen Daten geachtet wird. Zusätzlich werden schrittweise Cloud-Services in interne Prozesse integriert, und alle zukünftigen digitalen Vorhaben werden auf ihre Umsetzbarkeit mit Cloud-Lösungen überprüft.'),
('1.1', 'Dieses Dokument dient dazu, gegenüber der Rechtsaufsicht nachzuweisen, wie die <Kunde> die Ziele des Datenschutzes <§ 80 SGB X> und der Informationssicherheit erreicht. Es beschreibt die technischen und organisatorischen Maßnahmen, die im Rahmen der Integrationspartnerschaft für digitale Services und KI geprüft, implementiert und weiterentwickelt werden. Ergänzend wird dargelegt, wie diese Maßnahmen kontinuierlich überwacht und angepasst werden, um den höchsten Standards hierzulande in der Datensicherheit zu entsprechen. Zudem wird erläutert, wie die Zusammenarbeit mit Partnern gestaltet wird <§ 11 BDSG> <Art. 28 DSGVO>, um den Schutz der Versichertendaten langfristig und nachhaltig zu gewährleisten.'), 
('1.2', 'Dieses Dokument und die nachfolgend beschriebenen Anwendungsfälle gelten innerhalb der <Kunde> für die Unternehmensbereiche IT Projekt- und Solutionsmanagement. Dies trägt zur Effizienz und Zielerreichung innerhalb <Kunde>.');

SELECT * FROM ANZEIGE_PRE;

-- Paragraph templates
DROP TABLE ANZEIGE_TEMP;
CREATE TABLE ANZEIGE_TEMP (
    PARAGRAPH       varchar(12),
    PARAGRAPH_TEXT  varchar(20000)
);

SELECT * FROM ANZEIGE_TEMP;

-- Paragraph templates
DROP TABLE ANZEIGE_PARAGRAPHS;
CREATE TABLE ANZEIGE_PARAGRAPHS (
    PARAGRAPH       varchar(20),
    PARAGRAPH_DESC  varchar(80),
    PARAGRAPH_URL  varchar(400)
);

INSERT INTO ANZEIGE_PARAGRAPHS VALUES
('§ 80 SGB X', 'Verarbeitung von Sozialdaten im Auftrag', 'https://www.gesetze-im-internet.de/sgb_10/__80.html'),
('§ 11 BDSG', 'Erhebung, Verarbeitung oder Nutzung personenbezogener Daten im Auftrag', 'https://dejure.org/gesetze/DSGVO/28.html'),
('Art. 28 DSGVO', 'Auftragsverarbeiter', 'https://dejure.org/gesetze/SGB_V/393.html');

SELECT * FROM ANZEIGE_PARAGRAPHS;