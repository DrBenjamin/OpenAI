-- Creating a database in Snowflake 
CREATE DATABASE OPENAI_DATABASE;
CREATE SCHEMA PUBLIC;
USE DATABASE OPENAI_DATABASE;
USE SCHEMA PUBLIC;

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
('1.1', 'Zweck und Ziel des Dokumentes', 'Dieses Dokument dient dazu, gegenüber der Rechtsaufsicht nachzuweisen, wie die <Kunde> die Ziele des Datenschutzes <§ 80 SGB X> und der Informationssicherheit (<option_3_42>, <option_3_43>) erreicht. Es beschreibt die technischen und organisatorischen Maßnahmen, die im Rahmen der Integrationspartnerschaft für digitale Services und KI geprüft, implementiert und weiterentwickelt werden. Ergänzend wird dargelegt, wie diese Maßnahmen kontinuierlich überwacht und angepasst werden, um den höchsten Standards hierzulande in der Datensicherheit zu entsprechen. Zudem wird erläutert, wie die Zusammenarbeit mit Partnern gestaltet wird <§ 11 BDSG> <Art. 28 DSGVO>, um den Schutz der Versichertendaten langfristig und nachhaltig zu gewährleisten.'), 
('1.2', 'Geltungsbereich', 'Dieses Dokument und die nachfolgend beschriebenen Anwendungsfälle nach <§ 393 SGB V> gelten innerhalb der <Kunde> für die Unternehmensbereiche IT Projekt- und Solutionsmanagement. Dies trägt zur Effizienz und Zielerreichung innerhalb <Kunde>.'),
('1.3', 'Anwendungsbereich', '1.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('1.3.1', 'Anwendungsfälle', '1.3.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('1.3.2', 'Geschäftsnutzen', '1.3.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2', 'Rechtliche Grundlagen', '2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.1', 'Verarbeitung von Sozialdaten im Auftrag ($ 80 SGB X)', '2.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.2', 'Auftragsverarbeiter', '2.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.3', 'Cloud-Einsatz im deutschen Gesundheitswesen ($ 391 Abs. 1 SGB V)', '2.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.4', 'Datenschutz und Datensicherheit', '2.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.4.1', 'Datenkategorien und deren Schutzbedarf', '2.4.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.4.2', 'Vereinbarung zur Auftragsverarbeitung', '2.4.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.4.3', 'Datenschutz-Folgenabschätzung', '2.4.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.4.4', 'Räumliche Beschränkung der Datenverarbeitung', '2.4.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('2.4.5', 'Sicherheit der Datenverarbeitung', '2.4.5 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3', 'Zentrale Aspekte der Nutzung von Cloud-Computing', '3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.1', 'Definition und Zweck des Cloud-Computing', '3.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.2', 'Aufgabenbezug', '3.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.3', 'Wirtschaftlichkeitsbetrachtung', '3.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.4', 'Vermeidung des Vendor Lock-In', '3.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.4.1', 'Cloud-Agnostik', '3.4.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.4.2', 'Multi-Cloud-Ansatz', '3.4.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.4.3', 'Verwendung Drittanbieterprodukte', '3.4.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.4.4', 'Heterogene IT-Umgebung', '3.4.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('3.5', 'Exit-Strategie', '3.5 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4', 'Cloud-Sicherheitskonzept', '4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.1', 'Beschreibung des Datenflusses', '4.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.2', 'Identität und Zugriff', '4.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.2.1', 'Least-Privilege-Prinzip', '4.2.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.2.2', 'Multifactor Authentification', '4.2.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.3', 'Rollen und Berechtigungen', '4.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.3.1', 'Berechtigungsgruppen', '4.3.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.3.2', 'Rollenzuweisungen', '4.3.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.3.3', 'Administration von Privileged Identity Management', '4.3.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.3.4', 'Benutzerverwaltung', '4.3.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.4', 'Verschlüsselung von Daten', '4.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.4.1', 'Verschlüsselung ruhender Daten', '4.4.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.4.2', 'Customer Managed Keys', '4.4.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.4.3', 'Google Key Vauld', '4.4.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.4.4', 'Verschlüsselung von Übertragungsdaten', '4.4.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.4.5', 'Verschlüsselung beim Datentransport', '4.4.5 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5', 'Netzwerk', '4.5 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.1', 'Network Security Groups', '4.5.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.2', 'Virtual Networks', '4.5.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.3', 'Private Endpoints', '4.5.3 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.4', 'VPN-Gateway', '4.5.4 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.5', 'Private DNS Resolver', '4.5.5 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.6', 'Schutz vor Distributed Denial of Service', '4.5.6 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.5.7', 'Firewallfreigaben und Berechtigungskonzept', '4.5.7 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.6', 'Monitoring und Logging', '4.6 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.7', 'Google Policies', '4.7 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('4.8', 'Weitere Services', '4.8 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('5', 'Zertifizierungen', '5 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('5.1', 'C5-Zertifizierung', '5.1 Lorem ipsum dolor sit amet, consectetur adipiscing elit'),
('5.2', 'ISO 27001', '5.2 Lorem ipsum dolor sit amet, consectetur adipiscing elit');

SELECT * FROM ANZEIGE_PRE;

-- Paragraph templates
DROP TABLE ANZEIGE_TEMP;
CREATE TABLE ANZEIGE_TEMP (
    PARAGRAPH       varchar(12),
    PARAGRAPH_TITLE varchar(200),
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
('option_3_24', 'Im Design der Landing Zone werden die Elemente wie Netzwerke, Identitäts- und Zugriffsmanagement, Sicherheitsrichtlinien und Überwachungsdienste integriert. Für die Implementierung werden vordefinierte Lösungen genutzt werden, die den Einstieg erleichtern und Best Practices der Branche widerspiegeln.'),
('option_3_25', 'True'),
('option_3_26', 'Innerhalb der Landing Zone werden Identitäten und Zugriffsrechte durch ein zentrales Identitäts- und Zugriffsmanagementsystem verwaltet, das auf Identity and Access Management (IAM) basiert.'),
('option_3_27', 'True'),
('option_3_28', 'Maßnahmen zur Datenhoheit und Standortwahl. Die Daten werden verschlüsselungstechnisch geschützt. Verträge und Zertifizierungen (Compliance-Zertifizierungen). Transparenzberichte und Kundenbenachrichtigungen. Die Sicherheitspraktiken und Compliance wird regelmäßig von unabhängigen Dritten überprüft. Datenschutz- und Sicherheitszentrum.'),
('option_3_29', 'Durch gezielte Datenlokalisierung und Regionenauswahl. Mit Standardvertragsklauseln sowie zusätzliche Sicherheitsmaßnahmen. Dazu kommen Datenschutzbewertungen und Risikomanagement. Außerdem mittels Transparenz und Verantwortlichkeitsmanagement.'),
('option_3_30', 'Durch die Datenlokalisierung und Regionenauswahl. Vertragsvereinbarungen mit dem Anbieter. Einsatz von Verschlüsselung. Zugriffs- und Sicherheitskontrollen. Regelmäßige Überprüfung und Audits. Verpflichtung zur Benachrichtigung.'),
('option_3_31', 'Standardvertragsklauseln (SCCs). Zusätzliche technische, organisatorische und vertragliche Schutzmaßnahmen. Datenlokalisierung (Speicherung und Verarbeitung der Daten ausschließlich innerhalb der EU). Individuelle Risikobewertung für jede Datenübermittlung in ein Drittland durchführen. Klare Klauseln enthalten, die die Datenverarbeitung regeln.'),
('option_3_32', 'Daten ausschließlich in der EU oder anderen Regionen. Verschlüsselung. Challenging Government Requests. Zero Trust Architecture. Transparenzberichte. Anwendung der Standardvertragsklauseln (SCCs).'),
('option_3_33', 'Datenkontrolle und -speicherung. Verschlüsselung und Schlüsselverwaltung. Vertragliche Verpflichtungen. Transparenz und Kontrolle. Souveräne Cloud-Lösungen.'),
('option_3_34', 'Datenlokalisierung und -kontrolle. Verschlüsselung und Schlüsselverwaltung. Vertragliche Verpflichtungen. Transparenz und Kontrolle. Spezifische Compliance-Programme.'),
('option_3_35', 'Datenlokalisierung und -kontrolle. Verschlüsselung und Schlüsselverwaltung. Vertragliche Verpflichtungen. Transparenz und Kontrolle. Spezifische Compliance-Programme.'),
('option_3_36', 'Google Cloud Compliance Manager. Verschlüsselung und Schlüsselverwaltung. Audit-Logs und Überwachung. Datenschutz-Folgenabschätzung (DPIA). Vertragliche Verpflichtungen und Zertifizierungen.'),
('option_3_37', 'Google Kubernetes Engine (GKE). Compute Engine. Cloud Storage. Cloud Load Balancing. Cloud SQL und Cloud Spanner.'),
('option_3_38', 'Google Cloud Storage. Google Cloud Backup and DR. Google Cloud Spanner. Google Kubernetes Engine (GKE). Cloud Load Balancing'),
('option_3_39', 'Interoperabilität und offene Standards. Multi-Cloud-Management-Tools. Datenmigrationstools. Containerisierung. Vertragliche Flexibilität.'),
('option_3_40', 'True'),
('option_3_41', 'Identity and Access Management (IAM). VPC Service Controls. Cloud Audit Logs. Access Transparency. Policy Intelligence.'),
('option_3_42', 'Zugriffskontrolle und Authentifizierung. Verschlüsselung. Überwachung und Auditierung. Netzwerksicherheit. Schulung und Sensibilisierung. Zero-Trust-Architektur.'),
('option_3_43', 'Zertifizierungen und Audits. Physische Sicherheitskontrollen. Zugangsprotokolle und Überwachung. Regelmäßige Audits und Inspektionen. Zusammenarbeit mit dem Rechenzentrumsanbieter.'),
('option_3_44', 'Zertifizierungen und Audits. Physische Sicherheitskontrollen. Zugangsprotokolle und Überwachung. Regelmäßige Audits und Inspektionen. Zusammenarbeit mit dem Rechenzentrumsanbieter.'),
('option_3_45', 'True'),
('option_3_46', 'True'),
('option_3_47', 'Diese Protokollierung erfolgt in sogenannten Audit-Logs und Zugriffprotokollen, die aufzeichnen, wer wann welche Änderungen an den Daten vorgenommen hat.'),
('option_3_48', 'Datenexport mitels APIs zur Verfügung. Datenzugriff für einen begrenzten Zeitraum nach Vertragsbeendigung. Datenlöschung nach der Beendigung des Vertrags. Unterstützung bei der Migration.'),
('option_3_49', 'Datenmigration, Datenexport und Datenlöschung'),
('option_3_50', 'Datenlöschungsprozess, Zertifizierung und Nachweis (Löschbestätigung und Audit-Logs).'),
('option_3_51', 'Zugriffskontrolle und Authentifizierung. Verschlüsselung. Überwachung und Auditierung. Netzwerksicherheit. Zero-Trust-Architektur. Schulung und Sensibilisierung.'),
('option_3_52', 'Daten werden im Ruhezustand standardmäßig mit AES-256 verschlüsselt. Daten werden während der Übertragung zwischen den Systemen verschlüsselt mittels TLS (Transport Layer Security). Mit Confidential Computing und Confidential VMs bleiben Daten auch während der Verarbeitung verschlüsselt.'),
('option_3_53', 'TLS (Transport Layer Security). IPSec-Tunnel. Managed SSL-Zertifikate. Verschlüsselung von VM-zu-VM-Datenverkehr.'),
('option_3_54', 'Confidential Computing und Confidential VMs werden Daten in-use verschlüsselt.'),
('option_3_55', '2'),
('option_3_56', 'Verschlüsselung at-rest. Verschlüsselung in-transit. Verschlüsselung in-use. KMS Schlüsselmanagement');

SELECT * FROM ANZEIGE_OPTIONS;