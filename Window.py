import ctypes.util
import pygame
import pygame._sdl2 as pg_sdl2
import win32api
import win32con
import win32gui
import os

pygame.init()


def get_free_area():
	monitor_info = win32api.GetMonitorInfo(win32api.MonitorFromPoint((0, 0)))
	area = monitor_info.get("Work")
	area = (monitor_info.get("Monitor")[2], monitor_info.get("Monitor")[3] - (monitor_info.get("Monitor")[3]-area[3])*2)
	return area


def make_window_on_top():
	window = pg_sdl2.Window.from_display_module()
	sdl2_dll = ctypes.util.find_library("sdl2")
	sdl2_lib = ctypes.CDLL(sdl2_dll)
	sdl2_lib.SDL_Init(32)
	sdl2_lib.SDL_GetWindowFromID.restype = ctypes.POINTER(
		type("SDL_Window", (ctypes.Structure,), {})
	)
	win_handle = sdl2_lib.SDL_GetWindowFromID(ctypes.c_uint32(window.id))
	sdl2_lib.SDL_SetWindowAlwaysOnTop(win_handle, True)


def make_window_background_invisible(color: tuple[int, int, int] = (0, 0, 0)):
	# Create layered window
	hwnd = pygame.display.get_wm_info()["window"]
	win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
	                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
	# Set window transparency color
	win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*color), 0, win32con.LWA_COLORKEY)


def move_window(pos):
	os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % pos
