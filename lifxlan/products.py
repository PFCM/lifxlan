# coding=utf-8
product_map = {1: "Original 1000",
               3: "Color 650",
               10: "White 800 (Low Voltage)",
               11: "White 800 (High Voltage)",
               18: "White 900 BR30 (Low Voltage)",
               20: "Color 1000 BR30",
               22: "Color 1000",
               27: "LIFX A19",
               28: "LIFX BR30",
               29: "LIFX+ A19",
               30: "LIFX+ BR30",
               31: "LIFX Z",
               32: "LIFX Z 2",
               36: "LIFX Downlight",
               37: "LIFX Downlight",
               38: "LIFX Beam",
               43: "LIFX A19",
               44: "LIFX BR30",
               45: "LIFX+ A19",
               46: "LIFX+ BR30",
               49: "LIFX Mini",
               50: "LIFX Mini Day and Dusk",
               51: "LIFX Mini White",
               52: "LIFX GU10",
               55: "LIFX Tile",
               59: "LIFX Mini Color",
               60: "LIFX Mini Day and Dusk",
               61: "LIFX Mini White"
               }

# Identifies which products are lights.
# Currently all LIFX products that speak the LAN protocol are lights.
# However, the protocol was written to allow addition of other kinds
# of devices, so it's important to be able to differentiate.
light_products = [1, 3, 10, 11, 18, 20, 22, 27, 28, 29, 30, 31, 32, 36, 37, 43, 44, 45, 46, 49, 50, 51, 52, 55, 59, 60, 61]

features_map = {1: {"color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False},
                3: {"color": True,
                    "temperature": True,
                    "infrared": False,
                    "multizone": False,
                    "chain": False},
                10: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                11: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                18: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                20: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                22: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                27: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                28: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                29: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
					 "chain": False},
                30: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
					 "chain": False},
                31: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": True,
					 "chain": False},
                32: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": True,
					 "chain": False},
                36: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                37: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                38: {"color": True,
                     "temperature": True,
					 "infrared": False,
					 "multizone": True,
					 "chain": False},
                43: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                44: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                45: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
					 "chain": False},
                46: {"color": True,
                     "temperature": True,
                     "infrared": True,
                     "multizone": False,
					 "chain": False},
                49: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                50: {"color": False,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                51: {"color": False,
                     "temperature": False,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                52: {"color": True,
                     "temperature": True,
                     "infrared": False,
                     "multizone": False,
					 "chain": False},
                55: {"color": True,
                     "temperature": True,
					 "infrared": False,
					 "multizone": False,
					 "chain": True},
                59: {"color": True,
                     "temperature": True,
					 "infrared": False,
					 "multizone": False,
					 "chain": False},
                60: {"color": False,
                     "temperature": True, #guess
					 "infrared": False,
					 "multizone": False,
					 "chain": False},
                61: {"color": False,
                     "temperature": False, #guess
					 "infrared": False,
					 "multizone": False,
					 "chain": False}
                }
