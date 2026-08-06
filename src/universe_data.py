from esi_helpers import *
import json

# Parses json return and writes to file
def save_json_file(data: dict, path: str) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def save_region_information(esi: ESIHelper) -> None:
    regions = {}
    for region_id in esi.get_regions():
        regions[region_id] = esi.get_region_info(region_id)
        print(f"{regions[region_id]['name']} data loaded and saved.")
    
    save_json_file(regions, esi.REGION_INFORMATION_FILE)

def save_region_list(esi: ESIHelper) -> None:
    save_json_file(esi.get_regions(), esi.REGION_LIST_FILE)

# Saves a bunch of data about the universe
def main() -> None:
    esi = ESIHelper({
        "compatibility_date" : "2026-07-21"
    })

    # save_region_information(esi)
    save_region_list(esi)

if __name__ == "__main__":
    main()