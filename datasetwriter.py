"""
Creates dataset descriptions based on the values given in the datasets.toml
file, and parses those using the nadd-base.json template.
"""
from copy import deepcopy
from datetime import datetime
from pathlib import Path
import json
import tomli

class DatasetWriter:
    def __init__(self, datasets_path:Path, template_path:Path):
        self.datasets = self._load_datasets(datasets_path)
        self.template = self._load_template(template_path)

    def _load_datasets(self, datasets_path:Path) -> dict:
        if not datasets_path.exists():
            raise FileNotFoundError(datasets_path)

        with open(datasets_path, "rb") as f:
            datasets = tomli.load(f)

        return datasets

    def _load_template(self, template_path:Path) -> dict:
        if not template_path.exists():
            raise FileNotFoundError(template_path)

        with open(template_path) as f:
            return json.load(f)

    def write(self):
        # Loop over the datasets, fill in the template and
        # write them
        for dset in self.datasets["datasets"]:
            data = deepcopy(self.template)
            data["@id"] = dset["id"]
            data["name"] = dset["name"]
            data["dateModified"] = datetime.now().isoformat("T")[0:16]
            data["description"] = [
                {
                    "@language" : "nl",
                    "@value" : dset["description_nl"]
                },
                {
                    "@language" : "en",
                    "@value" : dset["description_en"]
                }
            ]

            dist = data["distribution"][0]
            dist["name"] = "%s SPARQL query" % dset["name"]
            dist["contentUrl"] = "https://query.wikidata.org/#%s" % dset["sparql_query"]

            export_path = Path("%s.jsonld" % dset["slug"])

            with open(export_path, "w") as f:
                f.write(json.dumps(data, indent = 4))

writer = DatasetWriter(
    datasets_path = Path("./datasets.toml"),
    template_path = Path("./nadd-base.json")
)

writer.write()