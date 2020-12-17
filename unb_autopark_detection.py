import pandas as pd
import xml.etree.ElementTree as et 

DATA_PATH = "./2012-10-16_17_18_53.xml"

xtree = et.parse(DATA_PATH)
xroot = xtree.getroot() 

df_cols = ["id", "occupied", "height", "width"]
rows = []

for node in xroot: 
    s_id = node.attrib.get("id")
    s_occupied = node.attrib.get("occupied")
    S_height = node.find("w").text 
    s_width = node.find("h").text

    rows.append({
        "id": s_id,
        "occupied": s_occupied,
        "height": S_height,
        "width": s_width
    })



out_df = pd.DataFrame(rows, columns = df_cols)

print(out_df)