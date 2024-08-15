-- Creating a database in Snowflake 
CREATE DATABASE OPENAI_DATABASE;
CREATE SCHEMA PUBLIC;

-- Paragraph pre-samples
DROP TABLE ANZEIGE_PRE;
CREATE TABLE ANZEIGE_PRE (
    PARAGRAPH       varchar(12),
    PARAGRAPH_TITLE varchar(200),
    PARAGRAPH_TEXT  varchar(20000)
);

INSERT INTO ANZEIGE_PRE VALUES
('1', 'Einleitung in die Thematik', '<Kunde> <Kundeninfo> Selbstentwickelte Programme und Dienstleistungen sind wesentliche Bestandteile des Kerngeschäfts einer Krankenkasse und spielen eine wichtige Rolle bei der Digitalisierung im Bereich der Gesetzlichen Krankenversicherung. Der Schwerpunkt verlagert sich mehr und mehr auf papierlose Prozesse sowie digitale Services und Produkte, wodurch diese Entwicklungen die Versicherten stärker einbeziehen. Zukünftig werden die Anforderungen an die IT und die digitalen Produkte der Kassen an vielen Stellen flexibler und leistungsfähiger aus der Cloud heraus als aus herkömmlichen Rechenzentren erfüllt werden können.
Aus diesem Grund sollen zukünftig Cloud-Technologien und -Services der <Cloud-Anbieter> vom Anbieter <option_0_0> eingesetzt werden, um das Kundenerlebnis für die Versicherten zu verbessern, wobei stets auf Rechtskonformität und den Schutz der persönlichen Daten geachtet wird. Zusätzlich werden schrittweise Cloud-Services in interne Prozesse integriert, und alle zukünftigen digitalen Vorhaben werden auf ihre Umsetzbarkeit mit Cloud-Lösungen überprüft.'),
('1.1', 'Zweck und Ziel des Dokumentes', 'Dieses Dokument dient dazu, gegenüber der Rechtsaufsicht nachzuweisen, wie die <Kunde> die Ziele des Datenschutzes <§ 80 SGB X> und der Informationssicherheit (<option_3_42>, <option_3_43>, <option_3_44>) erreicht. Es beschreibt die technischen und organisatorischen Maßnahmen, die im Rahmen der Integrationspartnerschaft für digitale Services und KI geprüft, implementiert und weiterentwickelt werden. Ergänzend wird dargelegt, wie diese Maßnahmen kontinuierlich überwacht und angepasst werden, um den höchsten Standards hierzulande in der Datensicherheit zu entsprechen. Zudem wird erläutert, wie die Zusammenarbeit mit Partnern gestaltet wird <§ 11 BDSG> <Art. 28 DSGVO>, um den Schutz der Versichertendaten langfristig und nachhaltig zu gewährleisten.'), 
('1.2', 'Geltungsbereich', 'Dieses Dokument und die nachfolgend beschriebenen Anwendungsfälle nach <§ 393 SGB V> gelten innerhalb der <Kunde> für die Unternehmensbereiche IT Projekt- und Solutionsmanagement. Dies trägt zur Effizienz und Zielerreichung innerhalb <Kunde>.');

SELECT * FROM ANZEIGE_PRE;

-- Paragraph templates
DROP TABLE ANZEIGE_TEMP;
CREATE TABLE ANZEIGE_TEMP (
    PARAGRAPH       varchar(12),
    PARAGRAPH_TEXT  varchar(20000)
);

SELECT * FROM ANZEIGE_TEMP;

-- Paragraphs
DROP TABLE ANZEIGE_PARAGRAPHS;
CREATE TABLE ANZEIGE_PARAGRAPHS (
    PARAGRAPH       varchar(20),
    PARAGRAPH_DESC  varchar(80),
    PARAGRAPH_URL  varchar(400)
);

INSERT INTO ANZEIGE_PARAGRAPHS VALUES
('§ 80 SGB X', 'Verarbeitung von Sozialdaten im Auftrag', 'https://www.gesetze-im-internet.de/sgb_10/__80.html'),
('§ 11 BDSG', 'Erhebung, Verarbeitung oder Nutzung personenbezogener Daten im Auftrag', 'https://dejure.org/gesetze/BDSG_a.F./11.html'),
('Art. 28 DSGVO', 'Auftragsverarbeiter', 'https://dejure.org/gesetze/DSGVO/28.html'),
('§ 393 SGB V', 'Cloud-Einsatz im Gesundheitswesen & Verordnungsermächtigung', 'https://dejure.org/gesetze/SGB_V/393.html');

SELECT * FROM ANZEIGE_PARAGRAPHS;

-- Options
DROP TABLE ANZEIGE_OPTIONS;
CREATE TABLE ANZEIGE_OPTIONS(
    OPTION_DESC  varchar(20),
    OPTION_TEXT  varchar(4000)
);

INSERT INTO ANZEIGE_OPTIONS VALUES
('option_0_0', 'Google LLC'),
('option_1_0a', 'True'),
('option_1_0b', 'False'),
('option_1_1', 'Versichertendaten'),
('option_1_2', 'Versicherte'),
('option_1_3', 'Die Versichertendaten werden zur weiteren Bearbeitung temporär in der Cloud gespeichert.'),
('option_2_0', 'False'),
('option_3_0', 'True'),
('option_3_1', 'Versichertendaten'),
('option_3_2', 'Abrechnungserstellung'),
('option_3_3', 'True'),
('option_3_4', 'Versichertendaten'),
('option_3_5', 'Abrechnungserstellung'),
('option_3_6', 'False'),
('option_3_7', 'True'),
('option_3_8', 'Versichertendaten'),
('option_3_9', 'Abrechnungserstellung'),
('option_3_10', 'True'),
('option_3_11', 'False'),
('option_3_12', 'True'),
('option_3_13', 'False'),
('option_3_14', 'True'),
('option_3_15', 'False'),
('option_3_16', 'True'),
('option_3_17', 'False'),
('option_3_18', 'False'),
('option_3_19', 'False'),
('option_3_20', 'True'),
('option_3_21', 'False'),
('option_3_22', 'False'),
('option_3_23', 'True'),
('options_3_24', 'Im Design der Landing Zone werden die Elemente wie Netzwerke, Identitäts- und Zugriffsmanagement, Sicherheitsrichtlinien und Überwachungsdienste integriert. Für die Implementierung werden vordefinierte Lösungen genutzt werden, die den Einstieg erleichtern und Best Practices der Branche widerspiegeln.'),
('options_3_25', 'True'),
('options_3_26', 'Innerhalb der Landing Zone werden Identitäten und Zugriffsrechte durch ein zentrales Identitäts- und Zugriffsmanagementsystem verwaltet, das auf Identity and Access Management (IAM) basiert.'),
('options_3_27', 'True'),
('option_3_28', 'Maßnahmen zur Datenhoheit und Standortwahl. Die Daten werden verschlüsselungstechnisch geschützt. Verträge und Zertifizierungen (Compliance-Zertifizierungen). Transparenzberichte und Kundenbenachrichtigungen. Die Sicherheitspraktiken und Compliance wird regelmäßig von unabhängigen Dritten überprüft. Datenschutz- und Sicherheitszentrum.'),
('options_3_29', 'Durch gezielte Datenlokalisierung und Regionenauswahl. Mit Standardvertragsklauseln sowie zusätzliche Sicherheitsmaßnahmen. Dazu kommen Datenschutzbewertungen und Risikomanagement. Außerdem mittels Transparenz und Verantwortlichkeitsmanagement.'),
('options_3_30', 'Durch die Datenlokalisierung und Regionenauswahl. Vertragsvereinbarungen mit dem Anbieter. Einsatz von Verschlüsselung. Zugriffs- und Sicherheitskontrollen. Regelmäßige Überprüfung und Audits. Verpflichtung zur Benachrichtigung.'),
('options_3_31', 'Standardvertragsklauseln (SCCs). Zusätzliche technische, organisatorische und vertragliche Schutzmaßnahmen. Datenlokalisierung (Speicherung und Verarbeitung der Daten ausschließlich innerhalb der EU). Individuelle Risikobewertung für jede Datenübermittlung in ein Drittland durchführen. Klare Klauseln enthalten, die die Datenverarbeitung regeln.'),
('options_3_32', 'Daten ausschließlich in der EU oder anderen Regionen. Verschlüsselung. Challenging Government Requests. Zero Trust Architecture. Transparenzberichte. Anwendung der Standardvertragsklauseln (SCCs).'),
('options_3_33', 'Datenkontrolle und -speicherung. Verschlüsselung und Schlüsselverwaltung. Vertragliche Verpflichtungen. Transparenz und Kontrolle. Souveräne Cloud-Lösungen.'),
('options_3_34', 'Datenlokalisierung und -kontrolle. Verschlüsselung und Schlüsselverwaltung. Vertragliche Verpflichtungen. Transparenz und Kontrolle. Spezifische Compliance-Programme.'),
('options_3_35', 'Datenlokalisierung und -kontrolle. Verschlüsselung und Schlüsselverwaltung. Vertragliche Verpflichtungen. Transparenz und Kontrolle. Spezifische Compliance-Programme.'),
('options_3_36', 'Google Cloud Compliance Manager. Verschlüsselung und Schlüsselverwaltung. Audit-Logs und Überwachung. Datenschutz-Folgenabschätzung (DPIA). Vertragliche Verpflichtungen und Zertifizierungen.'),
('options_3_37', 'Google Kubernetes Engine (GKE). Compute Engine. Cloud Storage. Cloud Load Balancing. Cloud SQL und Cloud Spanner.'),
('options_3_38', 'Google Cloud Storage. Google Cloud Backup and DR. Google Cloud Spanner. Google Kubernetes Engine (GKE). Cloud Load Balancing'),
('options_3_39', 'Interoperabilität und offene Standards. Multi-Cloud-Management-Tools. Datenmigrationstools. Containerisierung. Vertragliche Flexibilität.'),
('options_3_40', 'True'),
('options_3_41', 'Identity and Access Management (IAM). VPC Service Controls. Cloud Audit Logs. Access Transparency. Policy Intelligence.'),
('options_3_42', 'Zugriffskontrolle und Authentifizierung. Verschlüsselung. Überwachung und Auditierung. Netzwerksicherheit. Schulung und Sensibilisierung. Zero-Trust-Architektur.'),
('options_3_43', 'Zertifizierungen und Audits. Physische Sicherheitskontrollen. Zugangsprotokolle und Überwachung. Regelmäßige Audits und Inspektionen. Zusammenarbeit mit dem Rechenzentrumsanbieter.'),
('options_3_44', 'Zertifizierungen und Audits. Physische Sicherheitskontrollen. Zugangsprotokolle und Überwachung. Regelmäßige Audits und Inspektionen. Zusammenarbeit mit dem Rechenzentrumsanbieter.'),
('options_3_45', 'True'),
('options_3_46', 'Zugriffskontrolle und Authentifizierung. Verschlüsselung. Überwachung und Auditierung. Netzwerksicherheit. Zero-Trust-Architektur. Schulung und Sensibilisierung.'),
('options_3_47', 'Daten werden im Ruhezustand standardmäßig mit AES-256 verschlüsselt. Daten werden während der Übertragung zwischen den Systemen verschlüsselt mittels TLS (Transport Layer Security). Mit Confidential Computing und Confidential VMs bleiben Daten auch während der Verarbeitung verschlüsselt.'),
('options_3_48', 'TLS (Transport Layer Security). IPSec-Tunnel. Managed SSL-Zertifikate. Verschlüsselung von VM-zu-VM-Datenverkehr.'),
('options_3_49', 'Confidential Computing und Confidential VMs werden Daten in-use verschlüsselt.'),
('options_3_50', '2'),
('options_3_51', 'Verschlüsselung at-rest. Verschlüsselung in-transit. Verschlüsselung in-use. KMS Schlüsselmanagement');

SELECT * FROM ANZEIGE_OPTIONS;