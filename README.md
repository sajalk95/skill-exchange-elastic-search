# skill-exchange-elastic-search
Bulk load data to elastic search

## To setup the environment:
```makefile
make venv
```

## To create mappings:
```makefile
make create-locations-mapping
make create-jobs-mapping
make create-candidates-mapping
```

## To delete index:
```makefile
make delete-locations-index
make delete-jobs-index
make delete-candidates-index
```

## To load data:
```makefile
make load-locations-data
make load-jobs-data
make load-candidates-data
```
Note: Load data module creates mappings automatically. So there's no need to create mappings first if only data is to be loaded to elastic search.
