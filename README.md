# datasetregister
This repository is a part of the [Network Archives Design and Digital culture](https://nadd.network/).

It contains the code for:
* Generating the dataset descriptions as used for the [Dataset register](https://datasetregister.netwerkdigitaalerfgoed.nl/).
* A placeholder website that is used for `data.nadd.network`.

## Datasetwriter
This is a Python script that takes the descriptions for the different datasets, as described in the `datasets.toml` file, and uses the `nadd-base.json` file as a template to write the different descriptions.

To run we recommend installing [`uv`](https://docs.astral.sh/uv/) and then doing a `uv sync` in the root of this project. After that a `uv run datasetwriter.py` should be sufficient to write the JSONLD descriptions. Note that the script automatically changes the 'dateModified' property.

## Credits
This code was written by [Hay Kranen](https://www.haykranen.nl/).

## License
[Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/).