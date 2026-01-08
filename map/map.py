# =============== Helpers ===============
def normalize(name: str) -> str:
    return name.strip().lower()

# =============== Map Class ===============
class Locations:
    def __init__(self):
        self.map = {

            # ======= NORTH =======
            "mountain pass": {"connections": {
                "hill town": {"distance": 26, "speed": 45, "traffic": 1.0},
                "farmland": {"distance": 32, "speed": 40, "traffic": 1.0},
            }},

            "hill town": {"connections": {
                "mountain pass": {"distance": 26, "speed": 45, "traffic": 1.0},
                "lake town": {"distance": 18, "speed": 55, "traffic": 1.0},
                "farmland": {"distance": 20, "speed": 45, "traffic": 1.0},
            }},

            "lake town": {"connections": {
                "hill town": {"distance": 18, "speed": 55, "traffic": 1.0},
                "riverside": {"distance": 23, "speed": 60, "traffic": 1.0},
            }},

            # ======= MIDLANDS =======
            "farmland": {"connections": {
                "hill town": {"distance": 20, "speed": 45, "traffic": 1.0},
                "riverside": {"distance": 13, "speed": 50, "traffic": 1.0},
                "valley town": {"distance": 15, "speed": 50, "traffic": 1.0},
                "mountain pass": {"distance": 32, "speed": 40, "traffic": 1.0},
            }},

            "riverside": {"connections": {
                "lake town": {"distance": 23, "speed": 60, "traffic": 1.0},
                "central city": {"distance": 16, "speed": 70, "traffic": 1.1},
                "dam": {"distance": 10, "speed": 45, "traffic": 1.1},
                "farmland": {"distance": 13, "speed": 50, "traffic": 1.0},
            }},

            "dam": {"connections": {
                "riverside": {"distance": 10, "speed": 45, "traffic": 1.1},
                "industrial park": {"distance": 14, "speed": 50, "traffic": 1.2},
            }},

            "valley town": {"connections": {
                "farmland": {"distance": 15, "speed": 50, "traffic": 1.0},
                "central city": {"distance": 21, "speed": 60, "traffic": 1.0},
                "old woods": {"distance": 11, "speed": 40, "traffic": 1.0},
            }},

            "old woods": {"connections": {
                "valley town": {"distance": 11, "speed": 40, "traffic": 1.0},
                "quarry town": {"distance": 17, "speed": 45, "traffic": 1.0},
            }},

            # ======= CORE CITY =======
            "central city": {"connections": {
                "riverside": {"distance": 16, "speed": 70, "traffic": 1.1},
                "valley town": {"distance": 21, "speed": 60, "traffic": 1.0},
                "industrial park": {"distance": 11, "speed": 50, "traffic": 1.3},
                "suburbs": {"distance": 8, "speed": 40, "traffic": 1.5},
                "university": {"distance": 5, "speed": 35, "traffic": 1.6},
            }},

            "industrial park": {"connections": {
                "central city": {"distance": 11, "speed": 50, "traffic": 1.3},
                "dam": {"distance": 14, "speed": 50, "traffic": 1.2},
                "rail cargo": {"distance": 7, "speed": 45, "traffic": 1.2},
            }},

            "rail cargo": {"connections": {
                "industrial park": {"distance": 7, "speed": 45, "traffic": 1.2},
                "airport": {"distance": 8, "speed": 60, "traffic": 1.1},
            }},

            "airport": {"connections": {
                "rail cargo": {"distance": 8, "speed": 60, "traffic": 1.1},
                "suburbs": {"distance": 19, "speed": 80, "traffic": 1.2},
            }},

            "university": {"connections": {
                "central city": {"distance": 5, "speed": 35, "traffic": 1.6},
                "suburbs": {"distance": 4, "speed": 30, "traffic": 1.5},
            }},

            "suburbs": {"connections": {
                "central city": {"distance": 8, "speed": 40, "traffic": 1.5},
                "university": {"distance": 4, "speed": 30, "traffic": 1.5},
                "airport": {"distance": 19, "speed": 80, "traffic": 1.2},
                "quarry town": {"distance": 18, "speed": 55, "traffic": 1.1},
                "harbor town": {"distance": 14, "speed": 45, "traffic": 1.4},
                "downtown": {"distance": 6, "speed": 30, "traffic": 1.7},
            }},

            "quarry town": {"connections": {
                "old woods": {"distance": 17, "speed": 45, "traffic": 1.0},
                "suburbs": {"distance": 18, "speed": 55, "traffic": 1.1},
                "harbor town": {"distance": 23, "speed": 55, "traffic": 1.0},
            }},

            # ======= COAST =======
            "harbor town": {"connections": {
                "quarry town": {"distance": 23, "speed": 55, "traffic": 1.0},
                "suburbs": {"distance": 14, "speed": 45, "traffic": 1.4},
                "lighthouse": {"distance": 10, "speed": 40, "traffic": 1.0},
                "downtown": {"distance": 7, "speed": 30, "traffic": 1.8},
                "port docks": {"distance": 8, "speed": 30, "traffic": 1.9},
            }},

            "downtown": {"connections": {
                "suburbs": {"distance": 6, "speed": 30, "traffic": 1.7},
                "harbor town": {"distance": 7, "speed": 30, "traffic": 1.8},
                "stadium": {"distance": 2, "speed": 25, "traffic": 2.0},
                "port docks": {"distance": 5, "speed": 30, "traffic": 1.9},
            }},

            "stadium": {"connections": {
                "downtown": {"distance": 2, "speed": 25, "traffic": 2.0},
            }},

            "lighthouse": {"connections": {
                "harbor town": {"distance": 10, "speed": 40, "traffic": 1.0},
                "port docks": {"distance": 6, "speed": 35, "traffic": 1.2},
                "coast road": {"distance": 8, "speed": 50, "traffic": 1.0},
            }},

            "port docks": {"connections": {
                "downtown": {"distance": 5, "speed": 30, "traffic": 1.9},
                "harbor town": {"distance": 8, "speed": 30, "traffic": 1.9},
                "shipyards": {"distance": 3, "speed": 25, "traffic": 1.3},
                "beach city": {"distance": 12, "speed": 50, "traffic": 1.1},
                "lighthouse": {"distance": 6, "speed": 35, "traffic": 1.2},
            }},

            "shipyards": {"connections": {
                "port docks": {"distance": 3, "speed": 25, "traffic": 1.3},
            }},

            "coast road": {"connections": {
                "lighthouse": {"distance": 8, "speed": 50, "traffic": 1.0},
                "beach city": {"distance": 12, "speed": 60, "traffic": 1.0},
                "fishing village": {"distance": 15, "speed": 45, "traffic": 1.0},
            }},

            "beach city": {"connections": {
                "coast road": {"distance": 12, "speed": 60, "traffic": 1.0},
                "port docks": {"distance": 12, "speed": 50, "traffic": 1.1},
            }},

            "fishing village": {"connections": {
                "coast road": {"distance": 15, "speed": 45, "traffic": 1.0},
            }},
        }

    # ================== Travel ==================
    def travel_time_minutes(self, from_loc, to_loc):
        from_loc = normalize(from_loc)
        to_loc = normalize(to_loc)

        if from_loc not in self.map:
            raise ValueError(f"Unknown location: {from_loc}")
        if to_loc not in self.map[from_loc]["connections"]:
            raise ValueError(f"No road from {from_loc} to {to_loc}")

        road = self.map[from_loc]["connections"][to_loc]
        hours = (road["distance"] / road["speed"]) * road["traffic"]
        return round(hours * 60, 1)
      
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
    print("\nMap of Locations:")
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
    print("                              [FV] Fishing Village\n")


