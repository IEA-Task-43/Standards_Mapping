This is a repository of data supporting IEA Task 43's Data Standards Gap Analysis

This repository contains the following data files:

- Keywords_Cat.csv: category groups and the associated keyowrds
- Norm_Category.csv: 
- Norm_Keyword.csv:
                   (more details are provided in readme_standards_keywords.txt)
- 201214_Definition_Life-cycle-phases_en+de.xlsx: Definition and description of life cycle phases of wind turbines/farms
                   (more details in readme_standards_keywords.txt)


```

In [4]: print("Available Categories:")
   ...: print(list_categories())
Available Categories:
['General' 'Modelling and Data Collection' 'Assessment' 'Condition' 'Risk'
 'RAMS' 'Management' 'Wind Energy Specific' 'Other Industry Specific'
 'Wind Energy Off Shore Risk']

In [5]: 

In [5]: selected_category = "Risk"
   ...: print(f"\nStandards for {selected_category}:")
   ...: print(list_standards_for_category(selected_category))
   ...: 

Standards for Risk:
['DIN EN 16991' 'DIN EN IEC 62933-5-2' 'DIN EN IEC 63223 VDE 0109-101'
 'DIN SPEC 91331' 'DIN VDE 0175-110 VDE 0175-110'
 'IEC 88/798/CD CEI 88/798/CD IEC/TS 61400-28' 'ANSI/UL 4143'
 'BS EN IEC 61400-24:2019' 'DIN 18009-1' 'DIN EN 1991-1-7' 'DIN EN 17666']

In [6]: 

In [6]: selected_standard = 'DIN EN 16991'
   ...: print(f"\nCategories associated with {selected_standard}:")
   ...: print(list_categories_for_standard(selected_standard))
   ...: 
   ...: 

Categories associated with DIN EN 16991:
['General' 'Assessment' 'Risk' 'Other Industry Specific']
```
