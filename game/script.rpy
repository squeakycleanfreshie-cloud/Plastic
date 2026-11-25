define config.default_textshader = "typewriter"
default preferences.text_cps = 40

define s = Character("Sonny")
define g = Character("Granny")
define c = Character("Clara")

default kindness = 0
default honesty = 0
default courage = 0
default generosity = 0
default humility = 0
default pacience = 0
default loyalty = 0

image bg bedroom = im.Scale("images/bg bedroom.jpg", 1920, 1080)

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
    # scene bg bus with fade
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
    s "You arrive just on time, and walk into the front desk"
    s "Hello. I just got this job, and its my first day."
    c "Hello, my name is Clara, and I'm the receptionist of New Dawn Studios"
    c "Your Sonny right?"
    s "yeah."
    c "Okay, I will give you a quick tour, and then I will hand you on to doctor Bailey."
    s "Sounds good."



    return
