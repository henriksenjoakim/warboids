import pygame
import random

#For FPS capping
clock = pygame.time.Clock()

#Screen adjustments
SCREEN_X = 600
SCREEN_Y = 900

#Visual elements
BLACK = (0, 0, 0)
BOIDS_IMG_FILENAME = "Aircraft_01.png"
HOIKS_IMG_FILENAME = "Aircraft_05.png"
PLAYER_IMG_FILENAME = "Aircraft_09.png"
BULLET_IMG_FILNAME = "Bullet.png"
BACKGROUND_IMG_FILENAME = "desert-backgorund.png"
CLOUDS_IMG_FILENAME = "clouds-transparent.png"
EXPLOSION_IMG_FILENAME_01 = "Explotion_001.png"
EXPLOSION_IMG_FILENAME_02 = "Explotion_002.png"
EXPLOSION_IMG_FILENAME_03 = "Explotion_003.png"
EXPLOSION_IMG_FILENAME_04 = "Explotion_004.png"
EXPLOSION_IMG_FILENAME_05 = "Explotion_005.png"
EXPLOSION_IMG_FILENAME_06 = "Explotion_006.png"
EXPLOSION_IMG_FILENAME_07 = "Explotion_007.png"
EXPLOSION_IMG_FILENAME_08 = "Explotion_008.png"
EXPLOSION_IMG_FILENAME_09 = "Explotion_009.png"
EXPLOSION_IMG_FILENAME_10 = "Explotion_010.png"
EXPLOSION_IMG_FILENAME_11 = "Explotion_011.png"
EXPLOSION_IMG_FILENAME_12 = "Explotion_012.png"
EXPLOSION_IMG_FILENAME_13 = "Explotion_013.png"
EXPLOSION_IMG_FILENAME_14 = "Explotion_014.png"
EXPLOSION_IMG_FILENAME_15 = "Explotion_015.png"
EXPLOSION_IMG_FILENAME_16 = "Explotion_016.png"
EXPLOSION_IMG_FILENAME_17 = "Explotion_017.png"
EXPLOSION_IMG_FILENAME_18 = "Explotion_018.png"
EXPLOSION_IMG_FILENAME_19 = "Explotion_019.png"

#Sound elements
MUSIC_FILENAME = "music.wav"
EXPLOSION_SND_FILNAME = "explosion.wav"
PEW_SND_FILENAME = "pew.wav"
JET_SND_FILENAME = "jet.ogg"
ATMO_SND_FILENAME = "atmo.wav"



#Simulation / Gameplay tweaks
boid_nums = 1
hoik_nums = 1

oids_speed_limit = 5
oids_sep_range = 10
oids_sep_factor = 0.05
oids_coh_factor = 0.05
hoik_sep_factor = 0.05
oids_com_factor = 0.002
oids_bnd_avd_factor = 1.5
oids_attack_range = 100
oids_reload_time = 0.1
oids_missile_spd_mod = 5
bounds_avoidance_mod = 5
boids_detection_range = 100
hoiks_detection_range = 150

player_missile_speed_mod = 10
screen_bnd = 100
upper_bnd_x = SCREEN_X - screen_bnd
upper_bnd_y = SCREEN_Y - screen_bnd

pygame.init()
pygame.mixer.init()

#Load Sound
pygame.mixer.music.load(MUSIC_FILENAME)

explosion_snd = pygame.mixer.Sound(EXPLOSION_SND_FILNAME)
pew_snd = pygame.mixer.Sound(PEW_SND_FILENAME)
jet_snd = pygame.mixer.Sound(JET_SND_FILENAME)
atmo_snd = pygame.mixer.Sound(ATMO_SND_FILENAME) 

#Visual Element Adjustments
screen = pygame.display.set_mode((SCREEN_X, SCREEN_Y))
pygame.display.set_caption('-- W a r b o i d s --')
no_vel = pygame.math.Vector2(0,-1)
playerPos = pygame.math.Vector2(SCREEN_X / 2, upper_bnd_y)
bg_scroll_spd = 10

#Load Images 
player_img = pygame.image.load(PLAYER_IMG_FILENAME).convert_alpha()
boids_img = pygame.image.load(BOIDS_IMG_FILENAME).convert_alpha()
hoiks_img = pygame.image.load(HOIKS_IMG_FILENAME).convert_alpha()
bullet_img = pygame.image.load(BULLET_IMG_FILNAME).convert_alpha()
background_img = pygame.image.load(BACKGROUND_IMG_FILENAME).convert_alpha()
cloud_img = pygame.image.load(CLOUDS_IMG_FILENAME).convert_alpha()
explosion_img_01 = pygame.image.load(EXPLOSION_IMG_FILENAME_01).convert_alpha()
explosion_img_02 = pygame.image.load(EXPLOSION_IMG_FILENAME_02).convert_alpha()
explosion_img_03 = pygame.image.load(EXPLOSION_IMG_FILENAME_03).convert_alpha()
explosion_img_04 = pygame.image.load(EXPLOSION_IMG_FILENAME_04).convert_alpha()
explosion_img_05 = pygame.image.load(EXPLOSION_IMG_FILENAME_05).convert_alpha()
explosion_img_06 = pygame.image.load(EXPLOSION_IMG_FILENAME_06).convert_alpha()
explosion_img_07 = pygame.image.load(EXPLOSION_IMG_FILENAME_07).convert_alpha()
explosion_img_08 = pygame.image.load(EXPLOSION_IMG_FILENAME_08).convert_alpha()
explosion_img_09 = pygame.image.load(EXPLOSION_IMG_FILENAME_09).convert_alpha()
explosion_img_10 = pygame.image.load(EXPLOSION_IMG_FILENAME_10).convert_alpha()
explosion_img_11 = pygame.image.load(EXPLOSION_IMG_FILENAME_11).convert_alpha()
explosion_img_12 = pygame.image.load(EXPLOSION_IMG_FILENAME_12).convert_alpha()
explosion_img_13 = pygame.image.load(EXPLOSION_IMG_FILENAME_13).convert_alpha()
explosion_img_14 = pygame.image.load(EXPLOSION_IMG_FILENAME_14).convert_alpha()
explosion_img_15 = pygame.image.load(EXPLOSION_IMG_FILENAME_15).convert_alpha()
explosion_img_16 = pygame.image.load(EXPLOSION_IMG_FILENAME_16).convert_alpha()
explosion_img_17 = pygame.image.load(EXPLOSION_IMG_FILENAME_17).convert_alpha()
explosion_img_18 = pygame.image.load(EXPLOSION_IMG_FILENAME_18).convert_alpha()
explosion_img_19 = pygame.image.load(EXPLOSION_IMG_FILENAME_19).convert_alpha()

#Backround elements adjustment
bg_ratio = background_img.get_width() / background_img.get_height()
cloud_ratio = cloud_img.get_width() / cloud_img.get_height()
bg_height = SCREEN_X * bg_ratio
cloud_height = SCREEN_X * (cloud_ratio /4)
yPosBG = 0

cloud_img = pygame.transform.scale(cloud_img, (SCREEN_X, cloud_height))
background_img = pygame.transform.scale(background_img, (SCREEN_X, bg_height))
player_img = pygame.transform.scale(player_img, (player_img.get_width() / 3, player_img.get_height() / 3))
boids_img = pygame.transform.scale(boids_img, (boids_img.get_width() / 4, boids_img.get_height() / 4))
hoiks_img = pygame.transform.scale(hoiks_img, (hoiks_img.get_width() / 4, hoiks_img.get_height() / 4))
explosion_img_01 = pygame.transform.scale(explosion_img_01,(explosion_img_01.get_width() / 2, explosion_img_01.get_height() / 2))
explosion_img_02 = pygame.transform.scale(explosion_img_02,(explosion_img_02.get_width() / 2, explosion_img_02.get_height() / 2))
explosion_img_03 = pygame.transform.scale(explosion_img_03,(explosion_img_03.get_width() / 2, explosion_img_03.get_height() / 2))
explosion_img_04 = pygame.transform.scale(explosion_img_04,(explosion_img_04.get_width() / 2, explosion_img_04.get_height() / 2))
explosion_img_05 = pygame.transform.scale(explosion_img_05,(explosion_img_05.get_width() / 2, explosion_img_05.get_height() / 2))
explosion_img_06 = pygame.transform.scale(explosion_img_06,(explosion_img_06.get_width() / 2, explosion_img_06.get_height() / 2))
explosion_img_07 = pygame.transform.scale(explosion_img_07,(explosion_img_07.get_width() / 2, explosion_img_07.get_height() / 2))
explosion_img_08 = pygame.transform.scale(explosion_img_08,(explosion_img_08.get_width() / 2, explosion_img_08.get_height() / 2))
explosion_img_09 = pygame.transform.scale(explosion_img_09,(explosion_img_09.get_width() / 2, explosion_img_09.get_height() / 2))
explosion_img_10 = pygame.transform.scale(explosion_img_10,(explosion_img_10.get_width() / 2, explosion_img_10.get_height() / 2))
explosion_img_11 = pygame.transform.scale(explosion_img_11,(explosion_img_11.get_width() / 2, explosion_img_11.get_height() / 2))
explosion_img_12 = pygame.transform.scale(explosion_img_12,(explosion_img_12.get_width() / 2, explosion_img_12.get_height() / 2))
explosion_img_13 = pygame.transform.scale(explosion_img_13,(explosion_img_13.get_width() / 2, explosion_img_13.get_height() / 2))
explosion_img_14 = pygame.transform.scale(explosion_img_14,(explosion_img_14.get_width() / 2, explosion_img_14.get_height() / 2))
explosion_img_15 = pygame.transform.scale(explosion_img_15,(explosion_img_15.get_width() / 2, explosion_img_15.get_height() / 2))
explosion_img_16 = pygame.transform.scale(explosion_img_16,(explosion_img_16.get_width() / 2, explosion_img_16.get_height() / 2))
explosion_img_17 = pygame.transform.scale(explosion_img_17,(explosion_img_17.get_width() / 2, explosion_img_17.get_height() / 2))
explosion_img_18 = pygame.transform.scale(explosion_img_18,(explosion_img_18.get_width() / 2, explosion_img_18.get_height() / 2))
explosion_img_18 = pygame.transform.scale(explosion_img_19,(explosion_img_19.get_width() / 2, explosion_img_19.get_height() / 2))

#Explosion animation
explosion_list = [explosion_img_01, explosion_img_02, explosion_img_03, explosion_img_04, explosion_img_05, explosion_img_06, explosion_img_07, explosion_img_08, explosion_img_09, explosion_img_10, explosion_img_11, explosion_img_12, explosion_img_13, explosion_img_14, explosion_img_15, explosion_img_16, explosion_img_17, explosion_img_18, explosion_img_19]

#Set up groups
boid_group = pygame.sprite.Group()
missile_group = pygame.sprite.Group()
playerGroup = pygame.sprite.Group()

#Boid abstract class
class OidSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = boids_img
        self.exploding = False
        self.position = pygame.math.Vector2(random.randint(screen_bnd, upper_bnd_x),random.randint(screen_bnd, upper_bnd_y))
        self.velocity = pygame.math.Vector2(random.uniform(-1, 1) *oids_speed_limit , random.uniform(-1, 1)) * oids_speed_limit
        self.rect = pygame.rect.Rect(self.position.x, self.position.y, self.image.get_width(), self.image.get_height())
        self.startDiag = pygame.time.get_ticks()
        self.explosionRotation = random.randint(0,359)
        self.explosion_frame_nr = 0
        self.range = boids_detection_range
          
    #For debugging things
    def debug(self):
        if ((pygame.time.get_ticks() - self.startDiag) / 1000) > 1:
            print ("vel: " + str(self.velocity))
            print ("pos: " + str(self.position))
            print("rectx: " + str(self.rect.x))
            print("recty: " + str(self.rect.y))
            self.startDiag = pygame.time.get_ticks()

    #For initiating boid destruction
    def explode(self):
        if self.exploding == False:
            pygame.mixer.Sound.play(explosion_snd)
        self.exploding = True
    
    #Center of mass method. Boids gather around its nearby average center
    def _com_rule(self, boid_group):
        com_p = pygame.math.Vector2(0, 0)
        num_boids = 0
        for boid in boid_group:
            if boid != self:
                if isinstance(boid, MissileSprite) == False or isinstance(boid, HoikSprite) == False:
                    if self.position.distance_to(boid.position) < self.range:
                        num_boids += 1
                        com_p += boid.position
        if num_boids > 0:
            com_p = com_p / num_boids
            com_p = com_p - self.position
            com_p = com_p * oids_com_factor
        return com_p
    
    #Seperation rule. Boids keep distance from each other
    def _sep_rule(self, boid_group):
        sep_v = pygame.math.Vector2(0, 0)
        for boid in boid_group:
            if boid != self:
                if self.position.distance_to(boid.position) < oids_sep_range:
                    sep_v += (self.position - boid.position)
        sep_v * oids_sep_factor
        return sep_v
    
    #Coherence rule. Boids try to match the nearby group velocity
    def _coh_rule(self, boid_group):
        coh_p = pygame.math.Vector2(0, 0)
        num_boids = 0  
        for boid in boid_group:
            if boid != self:
                if isinstance(boid, MissileSprite) == False or isinstance(boid, HoikSprite) == False:
                    if self.position.distance_to(boid.position) < self.range:
                        coh_p += boid.velocity
                        num_boids += 1
        if num_boids > 0:
            coh_p = coh_p / num_boids
            coh_p = (coh_p - self.velocity) * oids_coh_factor
        return coh_p
    
    #Avoidance roule for screen edges. It's a bit funky this one.
    def _avoid_bounds_rule(self):
        avd_bnd_v = pygame.math.Vector2(0, 0)
        if self.position.x < screen_bnd:
            avd_bnd_v.x = avd_bnd_v.x + bounds_avoidance_mod  
        if self.position.x > upper_bnd_x:
            avd_bnd_v.x = avd_bnd_v.x - bounds_avoidance_mod 
        if self.position.y < screen_bnd:
            avd_bnd_v.y = avd_bnd_v.y + bounds_avoidance_mod 
        if self.position.y > upper_bnd_y:
            avd_bnd_v.y = avd_bnd_v.y - bounds_avoidance_mod 
        return avd_bnd_v
    
    #Speed Rule. Sets a max speed as many vectors adds up.
    def _speed_rule(self):
        if self.velocity.magnitude() > oids_speed_limit:
            if self.velocity.magnitude != 0:
                self.velocity = (self.velocity / self.velocity.magnitude()) * oids_speed_limit

    def update(self, boid_group):
        if self.exploding == True:
            self.image = explosion_list[self.explosion_frame_nr]
            self.image = pygame.transform.rotate(explosion_list[self.explosion_frame_nr], self.explosionRotation)
            self.rect = pygame.rect.Rect(self.position.x - (self.image.get_width()/2), self.position.y - (self.image.get_width()/2), self.image.get_width(), self.image.get_height())
            self.explosion_frame_nr += 1
            if self.explosion_frame_nr == 19:
                self.kill()
                self.remove(boid_group)
        else:
            com_v = self._com_rule(boid_group)
            coh_v = self._coh_rule(boid_group)
            sep_v = self._sep_rule(boid_group)
            avd_hoik_v = self.avoid_hoik_rule(boid_group)
            avd_bnd_v = self._avoid_bounds_rule()
            
            self.velocity += com_v + coh_v  + sep_v + avd_bnd_v + avd_hoik_v
            self._speed_rule()
            self.position += self.velocity
            
            self.rect.x = self.position.x - (self.image.get_width()/2)
            self.rect.y = self.position.y - (self.image.get_height()/2)
            
            angle = self.velocity.angle_to(no_vel)
            self.image = pygame.transform.rotate(boids_img, angle)

class BoidSprite(OidSprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)

    #Special rule to avoid hoiks and missiles specifically
    def avoid_hoik_rule(self, boid_group):
        avdh_v = pygame.math.Vector2(0, 0)
        for boid in boid_group:
            if boid != self:
                if isinstance(boid, HoikSprite) or isinstance(boid,  MissileSprite):
                    if self.position.distance_to(boid.position) < self.range:
                        avdh_v += (self.position - boid.position)
        avdh_v * hoik_sep_factor
        return avdh_v
        
class HoikSprite(OidSprite):
    def __init__(self):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = hoiks_img
        self.startTimeReload = pygame.time.get_ticks()
        self.losRect = pygame.rect.Rect(self.position.x- (self.image.get_width()/2), self.position.y - oids_attack_range, self.image.get_width(), oids_attack_range)
        self.range = hoiks_detection_range

    #Special rule for launching missiles at boids. Uses the LoS rect to determine when to shoot. Wanted to use a smarter algorithm but I couldnt seem to get it working.
    def _attack_boid(self, b_group):
        self.elapsedTime = (pygame.time.get_ticks() - self.startTimeReload) / 1000
        fired = False
        for boid in b_group:
            if boid != self:
                if isinstance(boid, HoikSprite) == False or isinstance(boid, MissileSprite) == False:
                    if self.position.distance_to(boid.position) < oids_attack_range:
                        if self.elapsedTime > oids_reload_time:
                            if fired == False:
                                if pygame.Rect.colliderect(self.losRect, boid.rect):
                                    #Cant pass the vectors directly to the missile class or things breaks for some incredebly strange reason!
                                    #decomposing the vectors into floats and instantiating a new vector works
                                    #missile = MissileSprite(self.position, self.velocity)
                                    velx = self.velocity.x
                                    vely = self.velocity.y
                                    posx = self.position.x
                                    posy = self.position.y
                                    missile = MissileSprite(pygame.math.Vector2(posx, posy), pygame.math.Vector2(velx, vely) * oids_missile_spd_mod)
                                    boid_group.add(missile)
                                    self.startTimeReload = pygame.time.get_ticks()
                                    fired = True

    def update(self, boid_group):
        if self.exploding == True:
            pass
        else:
            com_v = self._com_rule(boid_group)
            sep_v = self._sep_rule(boid_group)
            avd_v = self._avoid_bounds_rule()

            self.velocity += com_v + avd_v + sep_v
            self._speed_rule()
            self.position += self.velocity

            self.rect.x = self.position.x - (self.image.get_width()/2)
            self.rect.y = self.position.y - (self.image.get_height()/2)
            self.losRect.x = self.position.x - (self.image.get_width()/2)
            self.losRect.y = self.position.y + oids_attack_range

            angle = self.velocity.angle_to(no_vel)
            self.image = pygame.transform.rotate(hoiks_img, angle) 

            self._attack_boid(boid_group)

#Missile sprite. When collding with boids it calls their exploding method. Can enable all the inherited Oid rules to make it a seeker missile (but that turned out to be too over powered)
class MissileSprite(OidSprite):
    def __init__(self, position, velocity):
        super().__init__()
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.position = position
        self.velocity = velocity
        self.startTimeLifeSpan = pygame.time.get_ticks()
        pygame.mixer.Sound.play(pew_snd)

    def _detonate(self, boid_group):
        for boid in boid_group:
            if boid != self:
                if isinstance(boid, MissileSprite) == False:
                    if isinstance(boid, HoikSprite) == False:
                        if pygame.Rect.colliderect(self.rect, boid.rect):
                            boid.explode()
                            self.kill()
                            self.remove(boid_group)

    def update(self, boid_group):
        self.elapsedTime = (pygame.time.get_ticks() - self.startTimeLifeSpan) / 1000
        if self.elapsedTime > 3:
            self.kill()
            self.remove(boid_group)

        #Homeing mode
        #com_v = self._com_rule(boid_group)
        #self.velocity += com_v
        self.position += self.velocity
        
        self.rect.x = self.position.x - (self.image.get_width()/2)
        self.rect.y = self.position.y - (self.image.get_height()/2)

        angle = self.velocity.angle_to(no_vel)
        self.image = pygame.transform.rotate(bullet_img, angle)
        self._detonate(boid_group)

#The players own warhoik. at the bottom of the screen. can go left and right by using the arrow keys. Space for firing ze missiles
class PlayerSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.pos = playerPos
        self.rect = pygame.rect.Rect(self.pos.x - (self.image.get_width()/2), self.pos.y - (self.image.get_height()/2), self.image.get_width(), self.image.get_height())
        self.spacePressed = False

    def update(self):
        #Left right input
        if pygame.key.get_pressed()[pygame.K_RIGHT] == True:
            if self.pos.x < SCREEN_X - (self.image.get_width()/4):
                self.pos.x += 10
        if pygame.key.get_pressed()[pygame.K_LEFT] == True:
            if self.pos.x > (self.image.get_width() / 4):
                self.pos.x -= 10

        self.rect.x = self.pos.x - (self.image.get_width()/2)
        self.rect.y = self.pos.y - (self.image.get_height()/2)

        #Fire ze missiles
        if pygame.key.get_pressed()[pygame.K_SPACE] == True:
            if self.spacePressed == False:
                boid_group.add(MissileSprite(pygame.math.Vector2(self.pos.x, self.pos.y ), no_vel * player_missile_speed_mod))
                self.spacePressed = True
        if pygame.key.get_pressed()[pygame.K_SPACE] == False:
            self.spacePressed = False

#Sorting out the rest of the inputs. Press 1 for spawning boids, 2 for spawning hoiks and Space for missiles        
class InputDetection():
    def __init__(self):
        self.onePressed = False
        self.twoPressed = False
    
    def monitor(self, boid_group):
        if pygame.key.get_pressed()[pygame.K_1] == True:
            if self.onePressed == False:
                boid_group.add(BoidSprite())
                self.onePressed = True
        if pygame.key.get_pressed()[pygame.K_1] == False:
            self.onePressed = False

        if pygame.key.get_pressed()[pygame.K_2] == True:
            if self.twoPressed == False:
                boid_group.add(HoikSprite())
                self.twoPressed = True
        if pygame.key.get_pressed()[pygame.K_2] == False:
            self.twoPressed = False

#Instantiate things
for _ in range(boid_nums):
    boid_group.add(BoidSprite())

for _ in range(hoik_nums):
    boid_group.add(HoikSprite())

player = PlayerSprite()
playerGroup.add(PlayerSprite())
input = InputDetection()

pygame.mixer.music.play(-1)
pygame.mixer.Sound.play(atmo_snd,-1)
pygame.mixer.Sound.play(jet_snd, -1)
pygame.mixer.music.set_volume(0.8)
pygame.mixer.Sound.set_volume(jet_snd, 0.5)
pygame.mixer.Sound.set_volume(atmo_snd, 0.7)

run = True
if __name__ == "__main__":
    while run:
        # FPS cap / 30 for retro goodie, 60 for zoomermode
        clock.tick(30) 
        #Quitter
        event = pygame.event.poll()
        if event.type == pygame.QUIT:
            break
        #Pause game
        #if event.type == pygame.MOUSEBUTTONDOWN:
        #    pause = True
        #    while pause:
        #        event2 = pygame.event.poll()
        #        if event2.type == pygame.MOUSEBUTTONDOWN:
        #            pause = False
        #            break
        
        input.monitor(boid_group)

        #Clear screen for next frame
        screen.fill(BLACK)

        #Draw background elements and make them scroll
        screen.blit(background_img, (0,yPosBG))
        screen.blit(background_img, (0,yPosBG - bg_height))
        screen.blit(background_img, (0,yPosBG + bg_height))
        screen.blit(cloud_img, (0, (yPosBG * 10 ) - cloud_height))
        yPosBG += bg_scroll_spd
        if yPosBG >= bg_height:
            yPosBG = 0

        #Draw Sprites
        playerGroup.update()
        boid_group.update(boid_group)
        missile_group.update(missile_group)
        boid_group.draw(screen)
        missile_group.draw(screen)
        playerGroup.draw(screen)
        
        #Update
        pygame.display.update()

print("Game Over")

