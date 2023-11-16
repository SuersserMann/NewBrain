import pyecharts

value = [46, 54, 45, 82, 45]
attr = ["China", "Canada", "Brazil", "Russia", "United States"]
map1 = pyecharts.Map("世界地图", width=1200, height=600)
map1.add("", attr, value, maptype="world", is_visualmap=True,
         visual_text_color='#000', is_map_symbol_show=False)
map1.render()
