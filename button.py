# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 18:35:21 2021

@author: jiangqinwu
"""

import pygame.font

class Button:
    def __init__(self,ai_game,msg):
        "初始化按钮属性"
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #设置按钮的尺寸和其他属性
        self.width,self.height = 200,50
        self.button_color = (0,0,0)
        self.text_color = (225,38,0)
        self.font = pygame.font.SysFont(None,48)
        
        #创建按钮的rect实例，并将其居中对齐
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.center = self.screen_rect.center
        
        #按钮的标签秩序创建一次
        self._prep_msg(msg)
        self.msg = msg
        
    def _prep_msg(self,msg):
        "将msg渲染为图像，并使其在按钮上居中"
        self.msg_image = self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        "绘制一个用颜色填充的按钮，在绘制文本"
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        
    def draw_buttonup(self):
        "绘制一个用颜色填充的按钮，在绘制文本"
        self.msg_image = self.font.render(self.msg,True,(0,255,0),self.button_color)
        self.msg_image_rect.bottom = self.rect.top - self.rect.height
        self.screen.fill(self.button_color,self.msg_image_rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)
        
    def draw_buttonpass(self):
        "绘制一个用颜色填充的按钮，在绘制文本"
        self.msg_image = self.font.render(self.msg,True,(0,255,0),self.button_color)
        self.msg_image_rect.bottom = self.rect.top - 2*self.rect.height
        self.screen.fill(self.button_color,self.msg_image_rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)