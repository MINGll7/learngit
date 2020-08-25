import pygame



class Settings():
    """存储所有设置"""
    def __init__(self):
        """"初始化游戏的静态设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = ((100,100,230))
        # 子弹设置

        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 20
        # 飞船的设置
        self.ship_limit = 2
        # 外星人设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏
        self.speedup_scale = 1.3
        # 外星人点数提高
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.bullet_speed_factor = 1.5
        self.ship_speed_factor = 2.0
        self.alien_speed_factor = 1.5

        # fleet_direction为1表示右移 -1表示左移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 10

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
