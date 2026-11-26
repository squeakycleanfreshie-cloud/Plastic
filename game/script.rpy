style default:
    font "fonts/font.ttf"

style button_text:
    font "fonts/font.ttf"

style label_text:
    font "fonts/font.ttf"

style say_dialogue:
    font "fonts/font.ttf"

style say_label:
    font "fonts/font.ttf"

style input:
    font "fonts/font.ttf"

style quick_button_text:
    font "fonts/font.ttf"
    size 24
    idle_color "#ffffff"
    hover_color "#ffd27a"

style choice_button_text:
    font "fonts/font.ttf"
    size 40
    color "#ffffff"
    hover_color "#ffd27a"

define config.default_textshader = "typewriter"
default preferences.text_cps = 40

define s = Character("Sonny")
define g = Character("Granny")
define c = Character("Clara")
define b = Character("Bailey")

default kindness = 0
default honesty = 0
default courage = 0
default generosity = 0
default humility = 0
default pacience = 0
default loyalty = 0

image bg bedroom = im.Scale("images/bg bedroom.jpg", 1920, 1080)
image bg bus = im.Scale("images/bg bus.jpg", 1920, 1080)
image bg reception = im.Scale("images/reception.jpg", 1920, 1080)

# start of AI section

init python:
    import pygame_sdl2 as pygame

    class SignaturePad(renpy.Displayable):
        def __init__(self, w=700, h=250, **kwargs):
            super(SignaturePad, self).__init__(**kwargs)
            self.w = w
            self.h = h
            self.strokes = []
            self.drawing = False
        
        def render(self, width, height, st, at):
            r = renpy.Render(self.w, self.h)
            c = r.canvas()
            c.rect("#1a1a6e", (0, 0, self.w, self.h))
            c.rect("#ffffff", (4, 4, self.w - 8, self.h - 8))
            for stroke in self.strokes:
                for (px, py) in stroke:
                    c.circle("#1a1a6e", (int(px), int(py)), 2)
            return r

        def event(self, ev, x, y, st):
            inside = 0 <= x < self.w and 0 <= y < self.h
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1 and inside:
                self.drawing = True
                self.strokes.append([(x, y)])
                renpy.redraw(self, 0)
            elif ev.type == pygame.MOUSEMOTION and self.drawing and inside:
                lx, ly = self.strokes[-1][-1]
                dist = max(abs(x - lx), abs(y - ly))
                steps = max(1, int(dist / 1.5))
                for i in range(1, steps + 1):
                    t = i / float(steps)
                    self.strokes[-1].append((lx + (x - lx) * t, ly + (y - ly) * t))
                renpy.redraw(self, 0)
            elif ev.type == pygame.MOUSEBUTTONUP:
                self.drawing = False
            return None

        def clear(self):
            self.strokes = []
            self.drawing = False
            renpy.redraw(self, 0)

        def submit(self):
            if sum(len(s) for s in self.strokes) > 5:
                return True
            return None

define sigpad = SignaturePad()

screen sign_nda():
    modal True
    add Solid("#000000aa")
    frame:
        align (0.5, 0.5)
        padding (40, 30)
        vbox:
            spacing 20
            text "NEW DAWN STUDIOS: NDA" size 32
            text "I agree not to share any information about the Immerse Studio or its technology, or any confidnetial data I come across when working. This includes names/sensitive date of pacients and anything else." size 24
            text "Sign below:" size 24
            add sigpad
            hbox:
                spacing 30
                textbutton "Clear" action Function(sigpad.clear)
                textbutton "Sign" action Function(sigpad.submit)

# end of AI section

label start:
    scene bg bedroom
    show doctor at center
    s "You wake up, energised for the day"
    s "after 6 years of training in university, your ready for your first day on the job, as a plastic surgeon"
    s "You recived your uniform in the mail."
    s "A white trenchcoat that reads 'New Dawn Studios'"
    s "This job is the best job in the world."
    s "new dawn is the plastic surgery place all of the celebrities go."
    s "so you can't be late for your first day!"
    s "You get out of bed and rush to make some folded eggs and avocado"
    s "you make yourself a cup of coffee and drink it as you rush out the door to get on the bus."
    scene bg bus with fade
    s "The bus is packed full, and smells bad, but you find an untaken seat sitting next to somebody."
    s "An older person walks next to you and scowls"
    g "Your a bit to young to be taking the seats up on a crowded bus"
    menu:
        "get up for her":
            s "You can have my seat."
            g "It is okay. It is just so rude how people like you don't stand up for old people like me."
            s "I offered you my seat."
            g "I said it is fine."
            s "You get up out of your seat, but she refuses to sit down in it."
            s "You continue the rest of the bus ride standing up."
            $ kindness += 1
            $ generosity += 1
            jump bus_ride

        "keep sitting down":
            s "sorry, I pay for the bus too, and I'm quite comfortable where I am."
            g "Humph!"
            s "She walks away, and interacts with another person the same age as you."
            s "You continue the rest of the bus ride rested in peace, listening to your podcast"
            $ kindness -= 1
            $ generosity -= 1
            jump bus_ride

label bus_ride:
    scene bg reception with fade
    s "You arrive just on time, and walk into the front desk"
    s "Hello. I just got this job, and its my first day."
    c "Hello, my name is Clara, and I'm the receptionist of New Dawn Studios"
    c "Your Sonny right?"
    s "yeah."
    c "Okay, I will give you a quick tour, and then I will hand you on to doctor Bailey."
    s "Sounds good."
    s "Clara walks you around the facilites. She shows you the break room, the surgery room, the consultation room, and finshes off by taking you to doctor Bailey."
    c "The studio is split up into 3 sections."
    c "First their is Surgery. Thats where we run all of our plastic surgery and botox ect sessions."
    c "Thats where you will be working the most."
    c "Then their is the wellness studios. This is where more non-invasive treatments are held"
    c "Like massages, skincare treatments, IV drips ect."
    c "And then their is the Immerse Studio"
    c "We run luxury immersive wellness sessions. I can't take you their until you sign your NDA at the end of this tour."
    s "Why?"
    c "The immerse studio is made using state of the art technology. We can't have it leaked to the outside."
    c "She continues to take you to everywhere."
    c "Eventually the tour finishes."
    c "thats the Facilities!"
    s "Wow, they are so beautiful"
    c "Yeah, they are. I am now going to take to you doctor Bailey."
    s "Sounds good."
    s "Clara walks you over to bailey, but when she scans the door to enter Baileys office, the door refuses her acsess"
    c "Sorry, We have problems with our doors, I'm going to just call over bailey"
    s "Okay"
    s "Clara walks away 10m and hops on the phone. They talk for 5 minutes, but you can't hear what clara is saying."
    s "She walks back towards you"
    c "I'm so sorry for this inconvinience, but she wants you to sign your NDA before you come in to meet her. It is just company policy."
    s "She walks you over to a small room with some comfortable seats and modern warm lighting."
    s "There is an Ipad on the desk in front of you."
    c "Just feel free to read through, and sign."
    $ sigpad.clear()
    call screen sign_nda
    s "You sign the ipad and tell Clara."
    c "Perfect! Lets get you straight to doctor Bailey."
    s "You and clara walk over to the door that was locked before."
    s "This time it gives you acsess"
    c "I'm going to leave you here. Its just stragiht down the hall to the final door."
    s "Thanks so much for your help!"
    c "No worries. See you later."
    s "You keep walking to the end of the corridor, until you reach Baileys office."
    s "You walk inside."
    b "hey sonny!"
    s "hello!"
    b "I have been waiting so long to see you. "
    b "Welcome to new dawn studios"
    b "You are going to love it here."
    s "She hands you a pass with your name and photo."
    s "Wow! How did you get my photo?"
    b "Our security system took photos of you while you were on you introductory tour."
    s "Wow, so advanced."
    b "Yeah, It is pretty advanced, Isn't it."
    s "You put on your pass."
    b "also you won't need that basic uniform your wearing. Please change into the one inside the change room"
    s "She points you in the direction of the changroom and you walk over to get changed."
    s "The uniform is really nice."

    return
