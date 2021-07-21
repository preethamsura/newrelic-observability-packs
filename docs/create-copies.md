In order to use the copy functionality:

./import.sh PACK_NAME --copy PATH_TO_JSON_FILE

PACK_NAME is the name of whichever observability pack that you want to use
PATH_TO_JSON_FILE is the path to the JSON file that describes the configuration for the create_copies.py script

JSON attributes (all fields are required):

length: number of files to be created

keyword_dict: object where every key corresponds to a keyword that will be searched for in your template files, the values are a list where the first entry will replace the keyword in the first file created and the nth entry will replace the keyword in the nth file created.

copies: list of objects consisting of a template_file and a target_location

   template_file: path to whatever template file is being used, this file will be searched for keyword matches
        
   target_location: filename and path of where the generated files should be saved, NOTE: this can contain the searched for keyword which will allow unique files to be generated

sample:
```json
{
  "length": 2,
  "keyword_dict": {
    "CLUSTER-NAME": [
      "test-odd-wire",
      "stg-frugal-watch"
    ]
  },
  "copies": [
    {
      "template_file": "./template_dashboards/KafkaPartitionDashboardTemplate.json",
      "target_location": "./packs/kafka/dashboards/KafkaPartitionDashboard(<CLUSTER-NAME>).json"
    },
    {
      "template_file": "./template_dashboards/Partition CPU Utilization Template.yml",
      "target_location": "./packs/kafka/alerts/Partition CPU Utilization (<CLUSTER-NAME>).yml"
    }
  ]
}
```
  
template files:
  template files should be the exact same format as file in the destination would be with the exception that everywhere there is the string "<KEYWORD>" (with KEYWORD being one of the defined search terms in the keyword_dict attribute of the JSON config file) it will be replaced by one of the appropriate values.
  NOTE: "<" and ">" symbols are required around the keyword otherwise the keyword will not be detected.
