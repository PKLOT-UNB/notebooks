import pandas as pd
import xml.etree.ElementTree as et 

DATA_PATH = "./2012-10-16_17_18_53.xml"

xtree = et.parse(DATA_PATH)
xroot = xtree.getroot() 

df_cols = ["id", "occupied", "height", "width", "xCenter", "yCenter"]
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

    root1 = et.Element('root')
    
    s_id = x.attrib.get("id")
    s_occupied = x.attrib.get("occupied")
    
    root1 = x

    for rect in root1.iter('rotatedRect'):
        root2 = et.Element('root')
        # print(rect)

        root2 = rect

        # print()
        # s_height = rect.attrib.get("h")
        # s_width = rect.attrib.get("w")
        
        for center in root2.iter('center'):
            root3 = et.Element('root')

            s_xCenter = center.attrib.get("x")
            s_yCenter = center.attrib.get("y")
        
            root3 = center

        # for tech in root2.iter('size'):
        #     root3 = et.Element('root')
        #     print(tech)
        #     # root3=(tech)
        
        # for item in root2.iter('angle'):
        #     root3 = et.Element('root')
        #     print(item)
        #     root3=(item)

    rows.append({
        "id": s_id,
        "occupied": s_occupied,
        "xCenter": s_xCenter,
        "yCenter": s_yCenter,
        "height": s_height,
        "width": s_width
    })



           # for yr in root3.iter('size'):
            #     root4 = et.Element('angle')
            #     print(yr)
            #     root4=yr
            #     for gas in root4.iter('Non-CO2'):
            #         root5 = et.Element('root')
            #         print(gas)
            #         root5=gas

# for node in xroot: 
#     s_id = node.attrib.get("id")
#     s_occupied = node.attrib.get("occupied")
#     S_height = node.find("w").text 
#     s_width = node.find("h").text

#     rows.append({
#         "id": s_id,
#         "occupied": s_occupied,
#         "height": S_height,
#         "width": s_width
#     })


out_df = pd.DataFrame(rows, columns = df_cols)
print(out_df)