from pynput import mouse




def on_move(x,y):
    pass

def on_click(x, y, button, pressed):
    

    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))



def check_mouse():
    with mouse.Events() as events:
        event = events.get(1.0)
        click = []
        try:
            if event.button == mouse.Button.left:
                if event.pressed:
                    click.append([event.pressed, event.x, event.y])
                    print('{0} at {1}'.format('Pressed' ,(event.x, event.y)))
                    return click
        except AttributeError:
            pass
            
        
    
