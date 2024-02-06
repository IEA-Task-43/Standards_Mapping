This is a repository of data supporting IEA Task 43's Data Standards Gap Analysis

This repository contains the following data files:

- Keywords_Cat.csv: category groups and the associated keyowrds
- Norm_Category.csv: category-standard mapping
- Norm_Keyword.csv: standard-keyword mapping
                   (more details are provided in readme_standards_keywords.txt)
- 201214_Definition_Life-cycle-phases_en+de.xlsx: Definition and description of life cycle phases of wind turbines/farms
                   (more details in readme_standards_keywords.txt)


```
In [1]: # Load the data
   ...: import pandas as pd
   ...: norm_category_df = pd.read_csv('Norm_Category.csv', delimiter=';')
   ...: norm_keyword_df = pd.read_csv('Norm_Keyword.csv', delimiter=';')
   ...: keywords_cat_df = pd.read_csv('Keywords_Cat.csv', delimiter=';')

In [2]: # Function to list all available categories
   ...: def list_categories():
   ...:     return norm_category_df['Category'].unique()
   ...: 
   ...: # Function to list all available categories
   ...: def list_keywords():
   ...:     return norm_keyword_df['Key Words'].unique()
   ...: 
   ...: # Function to list all standards for a selected Keyword
   ...: def list_standards_for_keyword(keyword):
   ...:     return norm_keyword_df[norm_keyword_df['Key Words'] == keyword]['Norm'].unique()
   ...: 
   ...: # Function to list all standards for a selected category
   ...: def list_standards_for_category(category):
   ...:     return norm_category_df[norm_category_df['Category'] == category]['Norm'].unique()
   ...: 

In [3]: # print categories
   ...: print("Available Categories:")
   ...: print(list_categories())
Available Categories:
['General' 'Modelling and Data Collection' 'Assessment' 'Condition' 'Risk'
 'RAMS' 'Management' 'Wind Energy Specific' 'Other Industry Specific'
 'Wind Energy Off Shore Risk']

In [4]: # print standards for risk category
   ...: selected_category = "Risk"
   ...: print(f"\nStandards for {selected_category} category:")
   ...: print(list_standards_for_category(selected_category))

Standards for Risk category:
['DIN EN 16991' 'DIN EN IEC 62933-5-2' 'DIN EN IEC 63223 VDE 0109-101'
 'DIN SPEC 91331' 'DIN VDE 0175-110 VDE 0175-110'
 'IEC 88/798/CD CEI 88/798/CD IEC/TS 61400-28' 'ANSI/UL 4143'
 'BS EN IEC 61400-24:2019' 'DIN 18009-1' 'DIN EN 1991-1-7' 'DIN EN 17666']

In [5]: # print keywords
   ...: print("Available Keywords:")
   ...: print(list_keywords())
Available Keywords:
['catalogues' 'classes' 'construction' 'constructional products' 'data'
 'data structures' 'decree' 'definitions' 'diagrams' 'documents'
 'establishment' 'evaluations' 'harmonization' 'harmonized' 'process'
 'product data' 'specifications' 'standards' 'structure' 'systemology'
 'templates' 'originals' 'texture' 'architecture (it)' 'bim'
 'building information modeling' 'construction works' 'data exchange'
 'data formats' 'data management' 'data models' 'data records'
 'extensible markup language' 'geographic information systems' 'gis'
 'information exchange' 'infrastructure' 'integration' 'languages' 'links'
 'metadata' 'modeling language' 'modelling' 'models' 'networking'
 'semantics' 'syntax' 'logic operation' 'xml' 'patterns' 'buildings'
 'concepts' 'construction operations' 'delivery' 'demand' 'documentation'
 'information' 'information interchange' 'information management'
 'information models' 'information representation'
 'information technology' 'level' 'life cycles' 'performance' 'principles'
 'supply schedule' 'impulses' 'vibration' 'vocabulary' 'impact' 'lay'
 'shock' 'mechanic' 'activity' 'components' 'computer applications'
 'coordination' 'data field' 'data processing' 'developments'
 'document management' 'documentation systematics' 'information handling'
 'information transfer' 'organization' 'planning' 'project management'
 'records (documents)' 'representations' 'specification (approval)'
 'structuring' 'technical installations' 'technical products'
 'ingredients' 'acoustics' 'analysis' 'condition monitoring'
 'condition tests' 'general conditions' 'hazard analysis' 'hazards'
 'machine performances' 'machines' 'measurement' 'measuring techniques'
 'mechanical engineering' 'monitoring' 'personnel' 'reliability'
 'safety of machinery' 'surveillance (approval)' 'testing' 'training'
 'engines' 'classification' 'commissioning' 'condition' 'defects'
 'degradation' 'maintenance' 'management' 'observation' 'plans' 'scales'
 'status' 'structural works' 'technology' 'flatwork ironers' 'shortage'
 'data analysis' 'diagnosis' 'machine vibration' 'mechanical testing'
 'vibration engineering' 'vibration measurement' 'applicability'
 'framework' 'industrial facilities' 'industrial plants' 'industries'
 'inspection' 'plant' 'risk' 'risk analysis' 'risk assessment' 'scope'
 'danger' 'distribution of electricity' 'electric power systems'
 'electrical' 'electrical equipment' 'electrical installations'
 'electrochemistry' 'energy' 'energy economy' 'energy management'
 'energy storage' 'energy storage devices' 'environment' 'safety'
 'distress' 'asset management' 'circuit networks' 'effectiveness'
 'energy supply systems (buildings)' 'industrial management'
 'power supply system' 'supply systems' 'terminology'
 'assessment of technological consequences' 'classification systems'
 'contracts' 'cooperation' 'cultural elements' 'culture'
 'danger potentials' 'disasters' 'economics' 'environmental aspects'
 'financing' 'insolvencies' 'internal politics' 'international'
 'international agreements' 'international politics' 'law' 'logistics'
 'markets (economy)' 'money' 'procedure of projects' 'project'
 'quality management' 'resources' 'risk area' 'risk groups'
 'risk management' 'selling' 'taxes' 'business processes' 'cyber security'
 'energy technology' 'enterprises' 'intelligent networks' 'it security'
 'operational safety' 'smart grid' 'societal resilience' 'surveys'
 'no keyword' 'applications' 'dependability management' 'finance'
 'financial management' 'implementation' 'life (durability)'
 'management systems' 'mapping' 'quality' 'reliability management' 'use'
 'inserts' 'mission' 'assets' 'competence' 'investments'
 'maintenance cost' 'maintenance work' 'quality assurance' 'repair'
 'office management' 'administration' 'decision-making' 'improvement'
 'influence factors' 'optimization' 'procedures' 'sustainability'
 'examination (quality assurance)' 'guide books' 'guidelines'
 'instructions' 'methods of analysis' 'safety engineering'
 'security management' 'computer hardware' 'computer software'
 'functional capability' 'hardware' 'quality assurance systems'
 'quality control' 'reability related program' 'software' 'verification'
 'communication' 'communication systems' 'communication technology'
 'control engineering' 'control technology' 'efficiency'
 'electrical engineering' 'power generating plant' 'power measurement'
 'power measurement (electric)' 'process control' 'rating tests'
 'wind power' 'wind power stations' 'wind turbines' 'output capacity'
 'power' 'behaviour' 'data acquisition' 'electric power generation'
 'electricity' 'generators' 'mechanical load' 'mechanical properties'
 'stress' 'testing conditions' 'turbines' 'wind turbine generator systems'
 'wind-electric power stations' 'wind-powered devices' 'climate'
 'environmental condition' 'locations' 'suitability'
 'acoustic measurement' 'acoustic signals' 'acoustic testing' 'design'
 'electric generators' 'electric machines' 'environmental conditions'
 'installations' 'noise measurement' 'power generation'
 'rotating electric machines' 'safety requirements' 'sound level'
 'sound power' 'sound propagation' 'turbogenerators'
 'distinguishing signs' 'electric power stations' 'encoding'
 'identification' 'identification system' 'marking' 'marks'
 'power station engineering' 'products' 'products documentation'
 'systematics' 'technical documents' 'codification' 'calibration'
 'measurement set-up' 'measuring results' 'active power' 'bond'
 'compatibility' 'compatibility tests' 'durability'
 'electrical properties' 'grids' 'mains supply' 'network protection'
 'ratings' 'voltage' 'voltage dips' 'nets' 'permanency'
 'electrical properties and phenomena' 'network' 'bending strength'
 'electrical testing' 'simulation' 'test results' 'aerospace transport'
 'checks' 'control equipment' 'cryogenic' 'cryogenics' 'exchange'
 'high temperature' 'high temperatures' 'interfaces'
 'maximum temperatures' 'mechanical interfaces' 'mechanics' 'operation'
 'outer space' 'performance tests' 'protocols' 'space safety'
 'space technology' 'space transport' 'space vehicles' 'spacecraft'
 'spacecraft instruments' 'temperature' 'temperature control'
 'temperature range' 'thermal' 'thermal environment' 'thermal stress'
 'records' 'axis of rotation' 'axles' 'gear boxes' 'measuring equipment'
 'rotors' 'vibration resistance tests' 'vibration severity'
 'vibration tests' 'gearing' 'availability' 'further operating'
 'wind farms' 'extensions' 'onshore' 'wind loading'
 'electrical protection equipment' 'electrical safety'
 'cost benefit analysis' 'lightning protection'
 'protection against electric shocks' 'operating conditions'
 'power generating installation' 'renewable energy' 'size classification'
 'solar power' 'users' 'water power' 'conformity' 'conformity testing'
 'timers' 'data transmission' 'data types' 'datex services'
 'intelligent transport systems' 'metamodel'
 'open systems interconnection' 'osi' 'properties' 'public transport'
 'road systems' 'road transport' 'road vehicles' 'short-distance traffic'
 'telematics' 'teleprocessing' 'traffic'
 'traffic and traveller information' 'traffic control' 'uml'
 'unified modeling language' 'tti' 'dimensioning' 'engineers'
 'fire conditions' 'fire hazards' 'fire load' 'fire protection'
 'fire protection measures' 'fire resistance' 'fire risks' 'fire safety'
 'fire safety in buildings' 'fire spread prevention' 'firefighting'
 'generic specification' 'hazard prevention in buildings'
 'protective measures' 'purpose of protection' 'rescue'
 'safety verification' 'transport facilities (construction works)'
 'accident prevention' 'basis' 'bridges' 'civil engineering'
 'collisions (accident)' 'computation' 'effects' 'eurocode' 'explosions'
 'impacts' 'mathematical calculations' 'mechanical hazards'
 'shock resistance' 'stability' 'structural engineering drawings'
 'structures' 'calculation' 'trusses' 'characteristics' 'costs'
 'criterion' 'digitalization' 'elements' 'equipment' 'functions'
 'integrity' 'methods' 'natural gas' 'natural gas industries'
 'oil industries' 'petrochemistry' 'petroleum' 'reliability data'
 'technical data sheets' 'maintainability' 'net-control stations'
 'rail tracks' 'rail transport' 'railway applications'
 'railway installations' 'railway operation' 'railways' 'specification'
 'sheets' 'environment (working)' 'winds' 'offshore construction works'
 'erecting (construction operation)' 'installation' 'structural design'
 'shaping' 'cultivation' 'presentations' 'bodies' 'nursing' 'cabling'
 'damage prevention' 'erection' 'hazard removal' 'offshore'
 'operation manuals' 'property insurance' 'safety measures'
 'user information']

In [6]: # print standards for risk category
   ...: selected_keyword = "mechanical hazards"
   ...: print(f"\nStandards for {selected_keyword} keyword:")
   ...: print(list_standards_for_keyword(selected_keyword))

Standards for mechanical hazards keyword:
['DIN EN 1991-1-7']
```
