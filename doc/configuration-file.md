The configuration file format
=============================

## The basics

The configuration file specifies how the tables and columns of the
*Ditransitives*-style Filemaker data bases map to a CLDF data set.

By default the file is called `config.json` and located in the `etc/` folder of
a [cldfbench][cldfbench] project.  The location can be customised by moving the
file and modifying the python script in the cldfbench accordingly.

[cldfbench]: https://github.com/cldf/cldfbench/

The configuration is written in the [JSON format][json], as a key–value map that
specifies a number of supported properties, e.g.:

    {
        "custom_columns": { ... },
        "colname_maps": { ... },
        "required_columns": { ... },
        "bibtex_map": { ... }
    }

[json]: https://en.wikipedia.org/wiki/JSON

*Note 1:* Not all properties need to be specified in the file.  The program will
just use default values for any missing property.  In fact, the default settings
already cover the whole conversion process of a *Ditransitives*-style data base,
so it is only really necessary to add anything here when custom modifications
are made to a data set.

The most reliable way to find out about the default values for every property is
to check the file [`src/ditrans2cldf/config.py`](../src/ditrans2cldf/config.py)
in the source code.  It contains the defaults stored in as Python dictionary
called `DEFAULT_CONFIG`, which mirrors the structure from the JSON data.

*Note 2:* Make sure there is *no comma* after the last element of any list or
map, otherwise the config file will not be read correctly.  Even after years and
years of doing this the trailing comma problem never stopped biting me
occasionally.

## The supported properties

### `custom_columns`

The `custom_columns` property specifies, which columns should be added to the
tables of the resulting CLDF data set.  It contains a map of CLDF table names
to a list of column names to be added, e.g.:

    {
        "custom_columns": {
            "LanguageTable": ["Language_Family"],
            "CodeTable": ["Map_Icon"]
        }
    }

## `colname_maps`

The `colname_maps` property specifies the assignment of columns from Filemaker
tables to columns in the CLDF data set.  It contains a map of tables to maps of
column assignments, e.g.:

    {
        "colname_maps": {
            "languages": {
                "Family::name": "Language_Family"
            },
            "lcodes": {
                "mapicon": "Map_Icon"
            }
        }
    }

Note that the data layout is different between the Filemaker export and the CLDF
data.  The Filemaker export does not have a separate code table, while the CLDF
data set collapses language and construction parameters into one table.  For
this reason, the mapping requires the usage of intermediate table names that
cover the union of both table sets.  Column mapping uses the following table
names:

 * `languages`: Languages
 * `lparameters`: Language parameters
 * `lcodes`: Codes of language parameters
 * `lvalues`: Values of language parameters
 * `constructions`: Constructions
 * `cparameters`: Construction parameters
 * `ccodes`: Codes of construction parameters
 * `cvalues`: Values of construction parameters
 * `examples`: Example sentences

## `required_columns`

The `required_columns` property specifies which columns are considered mandatory
for a data set to be considered well-formed.  This property is used to find
errors and inconsistencies in a specific data set.  It contains a map of table
names to lists of column names, e.g.:

    {
        "required_columns": {
            "languages": ["Language_Family"],
            "lcodes": ["Map_Icon"]
        }
    }

Since sanity checking is done before the creation of the CLDF data set, this
property uses the same names as the `colname_maps` property above.

## `bibtex_map`

The `bibtex_map` specifies how columns from the *References* table in the
Filemaker export are mapped to [BibTeX][bibtex] fields in the bibliography of
the CLDF data set.  It is a map that maps column names to BibTeX field names,
e.g.:

    {
        "bibtex_map": {
            "Keywords": "keywords",
            "DOI": "doi"
        }
    }

[bibtex]: https://www.bibtex.org/
