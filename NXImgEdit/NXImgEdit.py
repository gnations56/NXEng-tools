import imgui
from pysdl2 import *
import ctypes
import OpenGL.GL as gl
from imgui.integrations.sdl2 import SDL2Renderer

#initializing the imgui context
imgui.create_context()
imgui.get_io().display_size = 100,100
imgui.get_io().fonts.get_tex_data_as_rbga32()

#start new frame
imgui.new_frame()

#open new window
imgui.begin("NXImgEdit",True)

#draw text label inside the window
imgui.text("Hi")
imgui.end()

imgui.render()
imgui.end_frame()
