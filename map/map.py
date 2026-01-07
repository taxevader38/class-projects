# =============== Imports ===============
from core.text import slowprint

class locations:
    def __init__(self):
        self.location_list = {
            "mountain pass": {
                "connected_to": ["hill town", "farmland"],
                "distance_km": []
            },

            "hill town": {
                "connected_to": ["mountain pass", "lake town", "farmland"],
                "distance_km": []
            },

            "lake town": {
                "connected_to": ["hill town", "riverside"],
                "distance_km": []
            },

            "farmland": {
                "connected_to": ["hill town", "riverside", "valley town"],
                "distance_km": []
            },

            "riverside": {
                "connected_to": ["lake town", "central city", "dam", "farmland"],
                "distance_km": []
            },

            "dam": {
                "connected_to": ["riverside", "industrial park"],
                "distance_km": []
            },

            "valley town": {
                "connected_to": ["farmland", "central city", "old woods"],
                "distance_km": []
            },

            "central city": {
                "connected_to": ["valley town", "industrial park"],
                "distance_km": []
            },

            "industrial park":{
                "connected_to": ["central city", "dam", "rail cargo"],
                "distance_km": []
            },

            "old woods": {
                "connected_to": ["valley town", "quarry town"],
                "distance_km": []
            },

            "university": {
                "connected_to": ["suburbs", "central city"],
                "distance_km": []
            },

            "rail cargo": {
                "connected_to": ["airport", "industrial park"],
                "distance_km": []
            },

            "quarry town": {
                "connected_to": ["old woods", "suburbs", "harbor town"],
                "distance_km": []
            },

            "suburbs": {
                "connected_to": ["quarry town", "university", "haor town", "downtown"],
                "distance_km": []
            },

            "airport": {
                "connected_to": ["rail cargo", "suburbs"],
                "distance_km": []
            },

            "harbor town": {
                "connected_to": ["quarry town", "suburbs", "lighthouse", "downtown"],
                "distance_km": []
            },

            "downtown": {
                "connected_to": ["suburbs", "stadium", "port docks"],
                "distance_km": []
            },

            "stadium": {
                "connected_to": ["downtown"],
                "distance_km": []
            },

            "lighthouse": {
                "connected_to": ["harbor town", "coast road", "port docks"],
                "distance_km": []
            },

            "port docks": {
                "connected_to": ["lighthouse", "shipyards", "downtown", "beach city"],
                "distance_km": []
            },

            "shipyards": {
                "connected_to": ["port docks"],
                "distance_km": []
            },

            "coast road": {
                "connected_to": ["lighthouse", "beach city", "fishing village"],
                "distance_km": []
            },

            "beach city": {
                "connected_to": ["coast road", "port docks"],
                "distance_km": []
            },

            "coast road": {
                "connected_to": ["lighthouse", "beach city", "fishing village"],
                "distance_km": []
            },
            
            "fishing village": {
                "connected_to": ["coast road"],
                "distance_km": []
            }
        }
        
# =============== Function Definitions ===============
# Normalize a name by stripping whitespace and converting to lowercase
def normalize(name: str) -> str:
    return name.strip().lower()

# Check if a location name is valid
def is_valid_location(name: str, locations: list) -> bool:
    """
    Check if the provided location name is in the list of valid locations
    """
    normalized_name = normalize(name)
    normalized_locations = [normalize(loc) for loc in locations]
    return normalized_name in normalized_locations

def print_map():
    """
    Print a simple text-based map of locations
    """
    slowprint("Map of Locations:", 0.03)
    print("                            [MT] Mountain Pass")
    print("                                 |")
    print("                                 |")
    print("                     [HL] Hill Town ---- [LK] Lake Town")
    print("                        |     \\\\             |")
    print("                        |      \\\\            |")
    print("                      [FM] Farmland ---- [RV] Riverside ---- [DM] Dam")
    print("                         |        \\\\         |                  |")
    print("                         |         \\\\        |                  |")
    print("                      [VT] Valley Town ---- [CT] Central City ---- [IP] Industrial Park")
    print("                                 |          |         |    \\\\               |")
    print("                                 |          |         |     \\\\              |")
    print("                             [OW] Old Woods |     [UN] University         [RC] Rail Cargo")
    print("                                 |          |         |                    |")
    print("                                 |          |         |                    |")
    print("                               [QT] Quarry Town ---- [SB] Suburbs ---- [AP] Airport")
    print("                                   |                 //   |      \\\\")
    print("                                   |                //    |       \\\\")
    print("                               [HT] Harbor Town ------- [DT] Downtown --- [ST] Stadium")
    print("                                   |                      |")
    print("                                   |                      |")
    print("                              [LF] Lighthouse ---- [PD] Port Docks ---- [WY] Shipyards")
    print("                                   |                      |")
    print("                                   |                      |")
    print("                              [CB] Coast Road -------- [BC] Beach City")
    print("                                   |")
    print("                                   |")
    print("                              [FV] Fishing Village")


