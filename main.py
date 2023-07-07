from os.path import dirname
from os.path import join
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
# from kivy.properties import ListProperty
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.core.text import LabelBase
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from functools import partial
from kivy.core.window import Window
from kivy.config import Config
import os
from random import choices







# Builder.load_file(join(dirname(__file__), 'pickup.kv'))

KOREAN_FONT = os.getcwd() + '/data/fonts/DNFBitBitTTF.ttf'
LabelBase.register(name='korean', fn_regular=KOREAN_FONT)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '600')
   
# list_str = [5,4,3]
# finish = 0
# count = 0

# five = 0.6
# star_5 = ['야에 미코','다이루크', '치치', '각청', '데히야', '타이나리' , '모나','진']
# weights_5 = [50] + [7.1] * 7

# star_4 = ['키라라','운근','중운','베넷','행추','시노부', '케이아','레일라','신염','사유', '레이저','북두','도리','카베','노엘']
# weights_4 = [16.6]*3 + [4.1]*12

# star_3 = ['장병기','한손검','양손검','법구','활']
# weights_3 = [20]*5

# stack = 0

choices_sort = []
# choices_c = []
# rect_color = ListProperty([1, 1, 1, 1])

class pickup_slot (Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.count = 0
        self.stack = 0
        self.five = 0.6
        self.choices_c = []
        self.choice_c = []
        self.list_str = [5,4,3]
        self.star_5 = ['야에 미코','다이루크', '치치', '각청', '데히야', '타이나리' , '모나','진']
        self.weights_5 = [50] + [7.1] * 7

        self.star_4 = ['키라라','운근','중운','베넷','행추','시노부', '케이아','레일라','신염','사유', '레이저','북두','도리','카베','노엘']
        self.weights_4 = [16.6]*3 + [4.1]*12

        self.star_3 = ['장병기','한손검','양손검','법구','활']
        self.weights_3 = [20]*5
 

    def randum_pick(self) : 
        self.choices_c.clear()
        for i in range(1, 10):
            if self.count < 73:
                self.choice_c = choices(self.list_str, weights=[self.five, 5.1, 94.3], k=1)
                self.count += 1
                self.choices_c.append(self.choice_c[0])
                if 5 == self.choice_c[0]:
                    # self.finish += self.count
                    self.count = 0
                    self.five = 0.6
            elif 73 <= self.count <= 90:
                self.five += 6
                self.choice_c = choices(self.list_str, weights=[self.five, 5.1, 94.3], k=1)
                self.count += 1
                self.choices_c.append(self.choice_c[0])
                # 74 이상 확률 증가 확인용
                # print(f'{count}번쨰 증가 확률 : {five}')
                if 5 == self.choice_c[0]:
                    # self.finish += self.count
                    self.count = 0
                    self.five = 0.6
    # 10연차시 4성 이상 100퍼 포함 // 테이블에 4성이나 5성이 있으면 345중 랜덤 1개

        if 4 not in self.choices_c and 5 not in self.choices_c :
            self.choices_c.append(4)
            self.count +=1
        elif 4 in self.choices_c or 5 in self.choices_c :
            self.choice_c = choices(self.list_str, weights=[self.five, 5.1, 94.3], k=1)
            self.choices_c.append(self.choice_c[0])
            self.count += 1
        self.choices_sort = sorted(self.choices_c,reverse=True)
        for i, j in enumerate(self.choices_sort):
            if j == 3:
                self.choices_3 = choices(self.star_3, weights= self.weights_3, k=1)
                self.choices_sort[i] = self.choices_3[0]
            elif j == 4:
                self.choices_4 = choices(self.star_4, weights= self.weights_4, k=1)
                self.choices_sort[i] = self.choices_4[0]
            elif j == 5:
                if self.stack == 0:
                    self.choices_5 = choices(self.star_5, weights=self.weights_5, k=1)
                    self.choices_sort[i] = self.choices_5[0]
                    if self.choices_sort[i] == '야에 미코' :
                        self.stack = 0
                    else :
                        self.stack = 1
                elif self.stack == 1:
                    self.choices_sort[i] = '야에 미코'
                    self.stack = 0
        return self.choices_sort, sorted(self.choices_c,reverse=True),self.count,self.stack
    

class pickup_run(GridLayout) :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pickup_instance = pickup_slot()
        self.cols = 5
        self.star_list = []
        self.character_list = []
        with self.canvas.before:
            self.background = Image(source=os.getcwd() + '/data/image/배경.png', size=(Window.width, Window.height),  # 화면 전체 크기로 설정
                                    size_hint=(None, None), pos = (0,0))
        for i in range(1,11) : 
            self.star_list.append(f'star{i}')
            self.character_list.append(f'character{i}')
        for i in range(5) :
            self.star_list[i] = Label(text = "",size_hint = (1,0.1))
            self.add_widget(self.star_list[i])
        for i in range(5) :
            self.character_list[i] = Button(background_normal = os.getcwd() + '/data/image/wind.png', size_hint=(1, 1))
            self.add_widget(self.character_list[i])
        for i in range(5,10) : 
            self.star_list[i] = Label(text = "",size_hint = (1,0.1))
            self.add_widget(self.star_list[i])  
        for i in range(5,10) :
            self.character_list[i] = Button(background_normal = os.getcwd() + '/data/image/wind.png', size_hint=(1, 1))
            self.add_widget(self.character_list[i])                         
        self.add_widget(Button(text = "click",on_press = self.on_pick,size_hint = (1,0.3)))
        self.add_widget(Button(text = "reset",on_press = self.on_reset,size_hint = (1,0.3)))
        self.count_label = Label(text = '',size_hint = (1,0.3))
        self.add_widget(self.count_label)
        self.stack_label = Label(text = '' , size_hint =(1,0.3) )
        self.add_widget(self.stack_label)
        
    def on_pick (self, instance) :
        self.star_list2 = []
        self.character_list2 = []
        name ,star, self.counti , self.stacki= self.pickup_instance.randum_pick()
        for i in range(1,11) : 
            self.star_list2.append(f'star{i}')
            self.character_list2.append(f'character{i}')
        for i in range(10):
            self.star_list[i].text = str(name[i])
            self.star_list[i].font_name = 'korean'
            if star[i] == 5 :
                self.character_list[i].background_normal = os.getcwd() + f'/data/image/5성카드.png'
            elif star[i] == 4 : 
                self.character_list[i].background_normal = os.getcwd() + f'/data/image/4성카드.png'
            elif star[i] == 3 :
                self.character_list[i].background_normal = os.getcwd() + f'/data/image/3성카드.png'
        for i in range(10):
            self.character_list[i].img = self.character_list[i]
            self.character_list[i].ch_source = os.getcwd() + f'/data/image/{name[i]}.png'
            self.character_list[i].bind(on_press=self.open_card)
            # self.character_list[i].bind(on_press=lambda instance, img=self.character_list[i], ch_source=os.getcwd() + f'/data/image/{name[i]}.png': self.open_card(instance, img, ch_source))
            # self.character_list[i].font_name = 'korean'
        del name,star
        self.count_label.text = str(self.counti)
        self.stack_label.text = str(self.stacki)

            
    def on_reset (self,instance) : 
        self.star_list2 = []
        self.character_list2 = []
        self.ranpick = pickup_slot()
        self.name , self.star, self.counti, self.stack= self.ranpick.randum_pick()
        for i in range(1,11) : 
            self.star_list2.append(f'star{i}')
            self.character_list2.append(f'character{i}')
        for i in range(10):
            self.star_list[i].text = ''
            self.character_list[i].background_normal = os.getcwd() + f'/data/image/wind.png'
            
    def open_card(self, instance):
        img = instance.img
        ch_source = instance.ch_source
        img.background_normal = ch_source
        del img, ch_source
        
    
    
class pickApp(App) :
    def build(self):
        return pickup_run()
        
if __name__ == "__main__" :
    pickApp().run()
        
    
    # # 가챠시 모션 다르게 설정가능
    # if 5 in choices:
    #     print('특수 화면')
    #     stack += 1
    #     if '야에 미코' in choices_sort:
    #         stack = 0
    # else:
    #         print("일반 화면")
