from basic import db, Products

db.create_all()

car = Products("Ferrari", "https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F5d35eacaf1176b0008974b54%2F0x0.jpg%3FcropX1%3D790%26cropX2%3D5350%26cropY1%3D784%26cropY2%3D3349", 40000)
watch = Products("Titan Watch", "https://staticimg.titan.co.in/Titan/Catalog/1829QL01_1.jpg?pView=pdp",  800)
villa = Products("Villa", "https://thumbor.forbes.com/thumbor/fit-in/1200x0/filters%3Aformat%28jpg%29/https%3A%2F%2Fspecials-images.forbesimg.com%2Fimageserve%2F1026205392%2F0x0.jpg", 2000000)

db.session.add_all([car, watch, villa])
