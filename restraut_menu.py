menu={
    'Break Fast': { 'tiffin' :{'dosa':120,
                   'ildy':60,
                   'chapathi':80,
                   'parota':40,
                   'poori':100 ,
                   'pongal':150,
                   "vada":45,
                   'bajji':40,
                   "sambar vada":60,
                   "iddiyapam":180,
                   "panniyaram":150
                   },
                   "sandwich":{
                    "veg sandwich" :120,
                    "paneer sandwich" :150,
                    "bread toast" :100,
                    "corn sandwich" :150
                       
                   }
    },
    'Lunch': { 'Starters': {
        'panner tikka': 220,
        'palak panner' : 200,
        'mushroom gravy' : 220,
        'mushroom 65' : 180,
        'gobi manchurian' :250,
        'gobi 65' : 150,
        'chettinad panner gravy':300,
        'chettinad mushroom gravy' : '300',
        'BBQ veggies' : 250
        },
        'Main Course' : {
            'veg biriyani' :250,
            'mushroom biriyani' : 260,
            'paneer biriyani' :280,
            'veg pulao' :250,
            'mushroom pulao' : 260,
            'paneer pulao' :280,
            'veg fried rice' :250,
            'mushroom fried rice' : 260,
            'paneer fried rice' :280,
            'tomato rice' : 150,
            'coconut rice' : 150,
            'potato rice' : 150,
            'curd rice' : 150,
            'sambar rice' : 150,
            'veg meals' : 300
        },
        'Diet meals' : {
            'boiled veggies' : 300,
            "veggie lover's club sandwich" : 300,
            'avacado roast' : 400,
            'best baingan bharta' : 400,
        }
    },
    'Desserts' :{ 'sweet' :{
            'gulab jumun' :100,
            'rasamalai' :120,
            'rasagulla' : 120,
            'Brownie' :120,
            'Brownie with ice cream' : 160,
            'kunafa' : 220,
            'kunafa with ice cream' : 240,
            'gulab jamun kunafa' : 250,
        },
        'Juice' : {
            'Apple juice' :120,
            'orange juice' :120,
            'pomogranate juice' :120,
            'grape juice' :120,
            'pine Apple juice' :120,
            'Mango juice' :120,
            'water melon juice' :120,
        },
        'Shakes' : {
            'vanila shake' : 160,
            'chocolate shake' : 160,
            'oreo shake' : 160,
            'strawberry shake' : 160,
            'blueberry shake' : 160,
            'butterscoh shake' : 160,
            'black truffle shake' : 160,

        },
   

    },     
     'dinner' :{ 'Tiffin items' : {
        'naan' :100,
        'butter paneer masala' :200,
        'dosa':120,
        'ildy':60,
        'chapathi':80,
        'parota':40,
        'poori':100 ,
        'masala dosa' :140
    },   
    'rice' : {'veg biriyani' :250,
            'mushroom biriyani' : 260,
            'paneer biriyani' :280,
            'veg pulao' :250,
            'mushroom pulao' : 260,
            'paneer pulao' :280,
            'veg fried rice' :250,
            'mushroom fried rice' : 260,
            'paneer fried rice' :280,
        

    }

}
}
num=0
for a in menu:
    num=0
    print("-----------------")
    print(a)
    print("-----------------")
    dish=menu[a]
    for i in dish:
        num=0
        print("**************")
        print(i)
        print("**************")
        items=menu[a][i]
        
        for r,m in items.items():
            num+=1
            print(num,r,":",m)
            
    print("\n")

