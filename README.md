# Global South institutional usages

Scripts to find institutional usages in Pensoft treatments and determine whether they correspond to Global South countries or Global North.
The results are in 

How to reproduce:
1. Execute SPARQL query in [sparql_query.rq](https://github.com/mdmtrv/global_south/blob/main/sparql_query.rq) against the OpenBiodiv2020 repository in the [OpenBiodiv GraphDB database](http://graph.openbiodiv.net/sparql) to find institutional code usages in taxonomic literature and the corresponding article DOIs.
2. Run [process_treatements_per_institution.py](https://github.com/mdmtrv/global_south/blob/main/process_treatements_per_institution.py) to perform API calls to GBIF's API and determine the name of each institution and the country (country code) where it is located:

 ```python process_treatements_per_institution.py```
 
3. Run [codes_to_country_names.py](https://github.com/mdmtrv/global_south/blob/main/codes_to_country_names.py) to resolve country codes to country names and determine category (GN or GS):

```python codes_to_country_names.py```

The script produces a CSV file with the resulting data: [final_results.csv](https://github.com/mdmtrv/global_south/blob/main/final_results.csv)
4. Manually look up institution names and country names which were not resolved with the API calls to GBIF. When there is no record in GBIF for a given institution code, use the DOIs in [final_results.csv](https://github.com/mdmtrv/global_south/blob/main/final_results.csv) to look within the publications for the full name of the institution.
We used this method to manually enrich the first 156 records. 
The file with the enhanced results is: [final_results_enriched.csv](https://github.com/mdmtrv/global_south/blob/main/final_results_enriched.csv)
