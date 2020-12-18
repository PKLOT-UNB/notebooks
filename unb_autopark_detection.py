import pandas as pd
import xml.etree.ElementTree as et 

DATA_PATH = "./2012-10-16_17_18_53.xml"

xtree = et.parse(DATA_PATH)
xroot = xtree.getroot() 

df_cols = ["id", "occupied", "width", "height", "xCenter", "yCenter", "Angle"]
rows = []

ids = []
occupied = []
position = []
width = []
height = []

tree= et.parse(DATA_PATH)
root= tree.getroot()

for x in root.iter('space'):
    s_id = None
    s_occupied = None
    s_height = None
    s_width = None
    s_xCenter = None
    s_yCenter = None
    s_angle = None

    root1 = et.Element('root')
    
    s_id = x.attrib.get("id")
    s_occupied = x.attrib.get("occupied")
    
    root1 = x

    for rect in root1.iter('rotatedRect'):
        root2 = et.Element('root')
        root2 = rect
        
        for center in root2.iter('center'):
            root3 = et.Element('root')

            s_xCenter = center.attrib.get("x")
            s_yCenter = center.attrib.get("y")
        
            root3 = center

        for size in root2.iter('size'):
            root3 = et.Element('root')

            s_height = size.attrib.get("h")
            s_width = size.attrib.get("w")

        for angle in root2.iter('angle'):
            root3 = et.Element('root')
            s_angle = angle.attrib.get("d")
  
    rows.append({
        "id": s_id,
        "occupied": s_occupied,
        "xCenter": s_xCenter,
        "yCenter": s_yCenter,
        "width": s_width,
        "height": s_height,
        "s_angle": s_angle
    })

out_df = pd.DataFrame(rows, columns = df_cols)
print(out_df)