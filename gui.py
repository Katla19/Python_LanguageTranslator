import kivy 
from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
kivy.require("1.10.1")  
class Translatorgui(App):
    def build(self):
        layout =FloatLayout()
        label1=Label(
            text="Translator",
            size_hint=(0.2,0.2),
            pos_hint={"x":0.40,"y":0.85}
            )
        layout.add_widget(label1)
        submit=Button(
            text="Translate",
            size_hint=(0.4,0.2),
            font_size=20,
            pos_hint={"x":0.3,"y":0.05},
            background_color=(0.9,0.9,0.9,0.5),
            color=(1,1,1,1)
            )
        clear=Button(
            text="Clear",
            font_size=20,
            pos_hint={"x":0.6,"y":0.8},
            size_hint=(0.3,0.05),   
            on_press=self.clearme
        )
        layout.add_widget(clear)
        layout.add_widget(submit)
        submit.bind(on_press=self.showme)
        self.inputtext=TextInput(
            text="Enter text here",
            pos_hint={"x":0.1,"y":0.6},
            size_hint=(0.8,0.2),
            font_size=20,
            )    
        self.outputtext=TextInput(
            text="Output here",
            pos_hint={"x":0.1,"y":0.35},
            size_hint=(0.8,0.2),
            font_size=20,
            readonly=True,
            font_name="notosans.ttf"
            )  
        layout.add_widget(self.inputtext)
        layout.add_widget(self.outputtext)      
        return layout
    def showme(self,button):        
        string1=self.inputtext.text.strip()
        k=[]
        flag=0
        try:
            file = open("en-hn.txt", "r", encoding="utf8")
            flag = 0
            index = 0
            for line in file:  
                index += 1 
                if string1.lower() in line.lower():
                    flag = 1
                    break 
            file.close()
        except: pass
        try:
            file = open('en-hn.txt',encoding="utf8")
            content = file.readlines( )
            k=content[index-1]  
            file.close()
        except: pass 
        p=0
        o=0
        for i in range(2,len(k)):
            if(k[i]==" " and k[i-1]==" " and k[i-2]==" "):
                if(k[i]!=k[i+1]):
                    p+=1
                    if(p==1):
                        p=i
        if flag == 0 or (len(string1)+5)<p : 
            print('String"', string1 , '"Not Found')
            self.outputtext.text="file or word not found" 
        else:  
            print(k[p:])
            self.outputtext.text=u'{ans}'.format(ans=k[p:])
    def clearme(self,button):
        self.inputtext.text=""
if __name__ == "__main__":
    Translatorgui().run()