import pygame
import sys

# Pygame'i başlat
pygame.init()

# Pencere boyutlarını tanımla
WINDOW_SIZE = (800, 600)
GRID_SIZE = 50

# Renk tanımları
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Pencereyi oluştur
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Mantık Kapıları Simülasyonu")

# Buton görsellerini yükle ve boyutlarını küçült
scale_factor = 21
stop_button_image = pygame.image.load('stop_button.png')
stop_button_image = pygame.transform.scale(stop_button_image, (stop_button_image.get_width() // scale_factor, stop_button_image.get_height() // scale_factor))

reset_button_image = pygame.image.load('reset_button.png')
reset_button_image = pygame.transform.scale(reset_button_image, (reset_button_image.get_width() // scale_factor, reset_button_image.get_height() // scale_factor))

start_button_image = pygame.image.load('start_button.png')
start_button_image = pygame.transform.scale(start_button_image, (start_button_image.get_width() // scale_factor, start_button_image.get_height() // scale_factor))

# Kapılar butonunu yükle ve kareye sığacak şekilde boyutu
kapilar_button_image = pygame.image.load('kapilar_button.png')
kapilar_button_image = pygame.transform.scale(kapilar_button_image, (GRID_SIZE, GRID_SIZE))

# Butonlar tuşunu sıgrıdmak için
buttons_button_image = pygame.image.load('buttons.png')
buttons_button_image = pygame.transform.scale(buttons_button_image, (GRID_SIZE, GRID_SIZE))

# Tabloyazi butonunu yükle
tabloyazi_button_image = pygame.image.load('tabloyazi.png')
tabloyazi_button_image = pygame.transform.scale(tabloyazi_button_image, (GRID_SIZE, GRID_SIZE))

# Butonların pozisyonlarını ayarla
stop_button_rect = stop_button_image.get_rect()
stop_button_rect.center = (WINDOW_SIZE[0] - GRID_SIZE // 2, WINDOW_SIZE[1] - GRID_SIZE // 2)

reset_button_rect = reset_button_image.get_rect()
reset_button_rect.center = (WINDOW_SIZE[0] - 1.5 * GRID_SIZE, WINDOW_SIZE[1] - GRID_SIZE // 2)

start_button_rect = start_button_image.get_rect()
start_button_rect.center = (WINDOW_SIZE[0] - 2.5 * GRID_SIZE, WINDOW_SIZE[1] - GRID_SIZE // 2)

kapilar_button_rect = kapilar_button_image.get_rect()
kapilar_button_rect.topleft = (0, 0)

buttons_button_rect = buttons_button_image.get_rect()
buttons_button_rect.topleft = (GRID_SIZE, 0)

tabloyazi_button_rect = tabloyazi_button_image.get_rect()
tabloyazi_button_rect.topleft = (2 * GRID_SIZE, 0)

# Mantık kapılarının görsellerini yükle ve boyutlarını küçült
and_gate_image = pygame.image.load('and.png')
and_gate_image = pygame.transform.scale(and_gate_image, (and_gate_image.get_width() // scale_factor, and_gate_image.get_height() // scale_factor))

or_gate_image = pygame.image.load('or.png')
or_gate_image = pygame.transform.scale(or_gate_image, (or_gate_image.get_width() // scale_factor, or_gate_image.get_height() // scale_factor))

not_gate_image = pygame.image.load('not.png')
not_gate_image = pygame.transform.scale(not_gate_image, (not_gate_image.get_width() // scale_factor, not_gate_image.get_height() // scale_factor))

nand_gate_image = pygame.image.load('nand.png')
nand_gate_image = pygame.transform.scale(nand_gate_image, (nand_gate_image.get_width() // scale_factor, nand_gate_image.get_height() // scale_factor))

nor_gate_image = pygame.image.load('nor.png')
nor_gate_image = pygame.transform.scale(nor_gate_image, (nor_gate_image.get_width() // scale_factor, nor_gate_image.get_height() // scale_factor))

xor_gate_image = pygame.image.load('xor.png')
xor_gate_image = pygame.transform.scale(xor_gate_image, (xor_gate_image.get_width() // scale_factor, xor_gate_image.get_height() // scale_factor))

xnor_gate_image = pygame.image.load('xnor.png')
xnor_gate_image = pygame.transform.scale(xnor_gate_image, (xnor_gate_image.get_width() // scale_factor, xnor_gate_image.get_height() // scale_factor))

# Diğer buton ve LED görsellerini yükle ve boyutlandır
red_button_image = pygame.image.load('red_button.png')
red_button_image = pygame.transform.scale(red_button_image, (red_button_image.get_width() // scale_factor, red_button_image.get_height() // scale_factor))

green_button_image = pygame.image.load('green_button.png')
green_button_image = pygame.transform.scale(green_button_image, (green_button_image.get_width() // scale_factor, green_button_image.get_height() // scale_factor))

# led_on ve led_off görsellerini yükle ve boyutlarını büyüt
led_scale_factor = 0.127  # Bu faktörle led görsellerini büyüteceğiz
led_off_image = pygame.image.load('led_off.png')
led_off_image = pygame.transform.scale(led_off_image, (int(led_off_image.get_width() * led_scale_factor), int(led_off_image.get_height() * led_scale_factor)))

led_on_image = pygame.image.load('led_on.png')
led_on_image = pygame.transform.scale(led_on_image, (int(led_on_image.get_width() * led_scale_factor), int(led_on_image.get_height() * led_scale_factor)))

# Tablonun görselini yükle
tablo_image = pygame.image.load('tablo.png')

# Mantık kapıları ve butonlar için pozisyonları ayarla
gate_images = [and_gate_image, or_gate_image, not_gate_image, nand_gate_image, nor_gate_image, xor_gate_image, xnor_gate_image]
gate_positions = [(100, 100), (200, 100), (300, 100), (400, 100), (500, 100), (600, 100), (700, 100)]
button_images = [red_button_image, green_button_image, led_off_image, led_on_image]
button_positions = [(100, 200), (200, 200), (300, 200), (400, 200)]
gates_visible = False
buttons_visible = False
tablo_visible = False
selected_gate = None  # Seçilen kapıyı takip etmek için bir değişken
place_gate = False  # Kapının yerleştirileceğini takip eden bir değişken
selected_gate_type = None  # Seçilen kapının türünü takip eden bir değişken

logic_gates = []
"""""
class LogicElement:
    def __init__(self, x, y, image, label):
        self.x = x
        self.y = y
        self.image = image
        self.label = label

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

# Mantık kapıları için alt sınıflar oluşturun
class LogicGate(LogicElement):
    def __init__(self, x, y, image, label, input_count):
        super().__init__(x, y, image, label)
        self.input_count = input_count

class ANDGate(LogicGate):
    def __init__(self, x, y, image, label="AND", input_count=2):
        super().__init__(x, y, image, label, input_count)

class ORGate(LogicGate):
    def __init__(self, x, y, image, label="OR", input_count=2):
        super().__init__(x, y, image, label, input_count)

# Giriş çıkış elemanları için sınıflar oluşturun
class IOElement(LogicElement):
    def __init__(self, x, y, image, label, color, start_value):
        super().__init__(x, y, image, label)
        self.color = color
        self.start_value = start_value
"""

#BU KODLAR YUZUNDEN ETİKET İÇİN HATALAR ALIYORDUM OYUZDEN ONLARI KALDIRDIM

class LogicGate:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def evaluate(self):
        pass

class ANDGate(LogicGate):
    def evaluate(self, input1, input2):
        return input1 and input2

class ORGate(LogicGate):
    def evaluate(self, input1, input2):
        return input1 or input2

class NOTGate(LogicGate):
    def evaluate(self, input1):
        return not input1

class NANDGate(LogicGate):
    def evaluate(self, input1, input2):
        return not (input1 and input2)

class NORGate(LogicGate):
    def evaluate(self, input1, input2):
        return not (input1 or input2)

class XORGate(LogicGate):
    def evaluate(self, input1, input2):
        return input1 != input2

class XNORGate(LogicGate):
    def evaluate(self, input1, input2):
        return input1 == input2

def draw_grid():
    for x in range(0, WINDOW_SIZE[0], GRID_SIZE):
        for y in range(0, WINDOW_SIZE[1], GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

# main döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos
            if stop_button_rect.collidepoint(mouse_pos):
                running = False
            elif reset_button_rect.collidepoint(mouse_pos):
                print("Reset button clicked")
                # Reset işlemleri burada yapılacak
                logic_gates.clear()
            elif start_button_rect.collidepoint(mouse_pos):
                print("Start button clicked")
                # Start işlemleri burada yapılacak
                for gate in logic_gates:
                    print(f"{type(gate).__name__} output: {gate.evaluate(1, 1)}")  # Girişler örnek olarak verildi
            elif kapilar_button_rect.collidepoint(mouse_pos):
                print("Kapılar button clicked")
                gates_visible = not gates_visible
                selected_gate = None  # Her kapı butonu tıklandığında seçili kapıyı sıfırla
            elif buttons_button_rect.collidepoint(mouse_pos):
                print("Buttons button clicked")
                buttons_visible = not buttons_visible
            elif tabloyazi_button_rect.collidepoint(mouse_pos):
                print("Tabloyazi button clicked")
                tablo_visible = not tablo_visible
            elif gates_visible:
                # Kullanıcının tıkladığı kapıyı seç
                for i, gate_position in enumerate(gate_positions):
                    gate_rect = gate_images[i].get_rect(topleft=gate_position)
                    if gate_rect.collidepoint(mouse_pos):
                        selected_gate = gate_images[i]
                        selected_gate_type = i
                        place_gate = True
                        print(f"Selected gate: {selected_gate_type}")
                    elif place_gate:
                        # Seçilen kapıyı tıklanan pozisyona yerleştir
                        gate_x = (mouse_pos[0] // GRID_SIZE) * GRID_SIZE
                        gate_y = (mouse_pos[1] // GRID_SIZE) * GRID_SIZE
                    if selected_gate_type == 0:
                            logic_gates.append(ANDGate(gate_x, gate_y, selected_gate))
                    elif selected_gate_type == 1:
                            logic_gates.append(ORGate(gate_x, gate_y, selected_gate))
                    elif selected_gate_type == 2:
                            logic_gates.append(NOTGate(gate_x, gate_y, selected_gate))
                    elif selected_gate_type == 3:
                            logic_gates.append(NANDGate(gate_x, gate_y, selected_gate))
                    elif selected_gate_type == 4:
                            logic_gates.append(NORGate(gate_x, gate_y, selected_gate))
                    elif selected_gate_type == 5:
                            logic_gates.append(XORGate(gate_x, gate_y, selected_gate))
                    elif selected_gate_type == 6:
                        logic_gates.append(XNORGate(gate_x, gate_y, selected_gate))
                        place_gate = False  # Yerleştirme işlemi tamamlandıktan sonra place_gate'i False olarak ayarla
                        print(f"Placed gate at: ({gate_x}, {gate_y})")

        # Ekranı oluştur
        screen.fill(WHITE)

        # Kareleri oluştur
        draw_grid()

        # Butonları çiz
        screen.blit(stop_button_image, stop_button_rect.topleft)
        screen.blit(reset_button_image, reset_button_rect.topleft)
        screen.blit(start_button_image, start_button_rect.topleft)
        screen.blit(kapilar_button_image, kapilar_button_rect.topleft)
        screen.blit(buttons_button_image, buttons_button_rect.topleft)
        screen.blit(tabloyazi_button_image, tabloyazi_button_rect.topleft)

        # Mantık kapılarını çiz
        if gates_visible:
            for i, gate_image in enumerate(gate_images):
                screen.blit(gate_image, gate_positions[i])

        # Diğer butonları ve LED'leri çiz
        if buttons_visible:
            for i, button_image in enumerate(button_images):
                screen.blit(button_image, button_positions[i])

        # Tablonun görselini çiz
        if tablo_visible:
            screen.blit(tablo_image, (
            WINDOW_SIZE[0] // 2 - tablo_image.get_width() // 2, WINDOW_SIZE[1] // 2 - tablo_image.get_height() // 2))

        # Yerleştirilen mantık kapılarını çiz
        for gate in logic_gates:
            gate.draw(screen)

        # Ekranı güncelle
        pygame.display.flip()

#cıkıs
pygame.quit()
sys.exit()


