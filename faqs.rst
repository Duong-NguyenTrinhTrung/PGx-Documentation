*1. What are ATC codes?*
=========================

ATC codes, or Anatomical Therapeutic Chemical Classification System codes, are a system used for the classification of drugs and medicines. The system is organized into different groups according to the organ or system on which they act and their therapeutic, pharmacological, and chemical properties. It is used internationally for the classification of medication and serves several purposes, such as facilitating health care professionals' search for specific drugs, aiding in the organization and analysis of drug utilization and research data, and supporting health care policy and management decisions.

The ATC classification system divides drugs into different groups at five different levels:

**1st level (Anatomical main group):** The drugs are divided into groups according to the organ or system on which they act, indicated by one letter (e.g., "A" for Alimentary tract and metabolism).

**2nd level (Therapeutic main group):** Two digits follow the letter, indicating the main therapeutic group of drugs.

**3rd level (Therapeutic/pharmacological subgroup):** One letter is added to specify the therapeutic or pharmacological subgroup.

**4th level (Chemical/therapeutic/pharmacological subgroup):** An additional letter is used to identify the chemical, therapeutic, or pharmacological subgroup within the main group.

**5th level (Chemical substance):** The final level specifies the chemical substance, denoted by two digits.

For example, the ATC code for Paracetamol (Acetaminophen) is N02BE01, where:

N indicates it is a Nervous system drug,
02 denotes it is an analgesic,
BE specifies it is an anilide,
01 identifies it as Paracetamol.
This systematic coding helps in ensuring uniform classification and usage of drugs across different countries and regions, facilitating international communication about drug use and research.


*2. Where can I get pharmacogenomics information from PGxDB?*
=============================================================

In PGxDB, we provide pharmacogenomics information from *an ATC code view*, *drug view* or *target view*

**From an ATC code view:** Use the "ATC code browser" page to browse to any ATC code of desire, then click on the button with tooltip "Click to show network" to open a right panel which shows all the drugs, drug-target interactions, and drug-disease association for all drugs associated with that ATC code. Users then would see in the tab "Network pharmacogenomics" beneath all the pharmacogenomics information available for those drugs and targets.

**From a drug view:** Use the "Drug browser" page to find any drug of desire, then click on the corresponding link in the "ATC code" column to re-direct to a panel which shows all the drug information, drug-target interactions, and drug-disease association for that drug. Users then would see in the tab "Network pharmacogenomics" beneath all the pharmacogenomics information available for that drug and its targets.

**From a target view:** Use the "Target browser" page to find any target of desire, then click specific drug in the "Interacting drugs" column to re-direct to a panel which shows all the drug information, drug-target interactions, and drug-disease association for that drug. Users then would see in the tab "Network pharmacogenomics" beneath all the pharmacogenomics information available for that drug and its targets.


*3. On a variant level, which information I can get from PGxDB?*
=============================================================

In PGxDB, users can search for any variant from the **"Variant browser"** page using the innput format: *Chromosome_Coordinate_Reference/Alternative allele*, example: *20_50581449_C/G*

Then the basic information of the gene where the variant occur are shown including "Gene ID",	"Gene symbol",	and "Primary transcript". The "Go to detail page" link on the right will re-direct to the specific page for that gene where all following information for each variant of that gene are list:
   - Basic variant annotation (sequence position, consequence, wildtypeAA, mutantAA, codon)
   - 40 the variant effect prediction scores and its MEAN value
   - Genebased burden association analysis result
User could apply filter, sort when browsing these information
