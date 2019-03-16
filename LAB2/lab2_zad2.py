from treelib import Tree, Node

reachable_states = {"Gdansk": [["Gdynia", 24], ["Koscierzyna", 58], ["Tczew", 33], ["Elblag", 63]],
                    "Gdynia": [["Gdansk", 24], ["Lebork", 60], ["Wladyslawowo", 33]],
                    "Elblag": [["Gdansk", 63], ["Tczew", 53]],
                    "Hel": ["Wladyslawowo", 35],
                    "Wladyslawowo": [["Leba", 66], ["Hel", 35], ["Gdynia", 42]],
                    "Tczew": [["Koscierzyna", 59], ["Gdansk", 33], ["Elblag", 53]],
                    "Leba": [["Ustka", 64], ["Lebork", 29], ["Wladyslawowo", 66]],
                    "Lebork": [["Leba", 29], ["Slupsk", 55], ["Koscierzyna", 58], ["Gdynia", 60]],
                    "Koscierzyna": [["Chojnice", 70], ["Bytow", 40], ["Lebork", 58], ["Gdansk", 58], ["Tczew", 59]],
                    "Ustka": [["Leba", 64], ["Slupsk", 21]],
                    "Slupsk": [["Ustka", 21], ["Lebork", 55], ["Bytow", 70]],
                    "Bytow": [["Slupsk", 70], ["Koscierzyna", 40], ["Chojnice", 65]],
                    "Chojnice": [["Bytow", 65], ["Koscierzyna", 70]]}
