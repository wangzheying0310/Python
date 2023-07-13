#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time : 2022/8/19 13:28
# @Author : zhw
# @File : web_keywords.py
from pathlib import Path
from typing import Any, TypeVar, Union, Pattern, Callable, Optional, Literal
from contextlib import contextmanager
from playwright.sync_api import Page, ElementHandle, TimeoutError, Locator, FrameLocator, expect, Route, Request

from utils.handle_path import project_path
from utils.record_log import Logger

Element = TypeVar("Element", ElementHandle, Locator)


class WebKeywords:
    log = Logger()

    def __init__(self, page: Page):
        self.page = page

    def get(self, url: str, **kwargs):
        """
        前往url
        :param url: 测试环境url
        :return:
        """
        try:
            self.page.goto(url, timeout=20000, **kwargs)
            self.log.info(f"前往{url}")
        except TimeoutError:
            self.log.exception(f"前往{url}, 失败")
            raise AssertionError

    def search_element(self, location: str, has_text: str = None, has: str | Locator = None) -> Locator:
        """
        获取元素
        :param location: 定位方式
        :param has_text: 过滤元素需要的文本
        :param has: 过滤元素需要的定位方式或元素
        :return: Locator
        """
        if isinstance(has, str):
            return self.page.locator(location).filter(has_text=has_text, has=self.page.locator(has))
        else:
            return self.page.locator(location).filter(has_text=has_text, has=has)

    def search_inner_element(self, location: Locator, inner_location: str, has_text: str = None,
                             has: str | Locator = None) -> Locator:
        """
        获取元素中的元素
        :param location: 元素
        :param inner_location: 定位方式
        :param has_text: 过滤元素需要的文本
        :param has: 过滤元素需要的定位方式或元素
        :return: Locator
        """
        if isinstance(has, str):
            return location.locator(inner_location).filter(has_text=has_text, has=self.page.locator(has))
        else:
            return location.locator(inner_location).filter(has_text=has_text, has=has)

    def find_element(self, location: str, **kwargs) -> ElementHandle:
        """
        获取一个元素
        :param location: 定位方式
        :return: ElementHandle
        """
        # return self.page.query_selector(location, **kwargs)
        return self.page.locator(location, **kwargs).element_handle()

    def find_elements(self, location: str, **kwargs) -> list[ElementHandle]:
        """
        获取一组元素
        :param location: 定位方式
        :return: list[ElementHandle]
        """
        # return self.page.query_selector_all(location)
        return self.page.locator(location, **kwargs).element_handles()

    def send_keys(self, location: str | Element, text: str, **kwargs):
        """
        输入文本
        :param location: 定位方式或者元素
        :param text: 要输入的文本
        :return:
        """
        try:
            self.page.fill(location, text, **kwargs) if isinstance(location, str) else location.fill(text, **kwargs)
            self.log.info(f"输入文本, 定位方式: {str(location)}, 文本内容: {text}")
        except TimeoutError:
            self.log.exception(f"输入文本, 定位方式: {str(location)}, 文本内容: {text}, 失败")
            raise AssertionError

    def click(self, location: str | Element, **kwargs):
        """
        点击
        :param location: 定位方式或者元素
        :return:
        """
        try:
            self.page.click(location, **kwargs) if isinstance(location, str) else location.click(**kwargs)
            self.log.info(f"点击, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"点击, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def context_click(self, location: str | Element, **kwargs):
        """
        右击
        :param location: 定位方式或者元素
        :return:
        """
        try:
            self.page.click(location, button="right", **kwargs) if isinstance(location, str) \
                else location.click(button="right", **kwargs)
            self.log.info(f"右击, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"右击, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def double_click(self, location: str | Element, **kwargs):
        """
        双击
        :param location: 定位方式或者元素
        :return:
        """
        try:
            self.page.dblclick(location, **kwargs) if isinstance(location, str) else location.dblclick(**kwargs)
            self.log.info(f"双击, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"双击, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def shortcuts_click(self, location: str | Element, modifiers: list, **kwargs):
        """
        快捷键+鼠标点击
        :param location: 定位方式或者元素
        :param modifiers: 快捷键 ["Alt", "Control", "Meta", "Shift"]
        :return:
        """
        try:
            self.page.click(location, modifiers=modifiers, **kwargs) if isinstance(location, str) \
                else location.click(modifiers=modifiers, **kwargs)
            self.log.info(f"按住快捷键: {''.join(modifiers)}点击, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"按住快捷键: {''.join(modifiers)}点击, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def hover(self, location: str | Element, **kwargs):
        """
        悬浮
        :param location: 定位方式或者元素
        :return:
        """
        try:
            self.page.hover(location, **kwargs) if isinstance(location, str) else location.hover(**kwargs)
            self.log.info(f"悬浮, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"悬浮, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def wait(self, timeout: int | float):
        """
        等待
        :param timeout: 等待时间 毫秒(ms)
        :return:
        """
        self.page.wait_for_timeout(timeout)
        self.log.info(f"等待: {timeout}毫秒")

    def keyboard_press(self, shortcuts: str, delay: int | float = None):
        """
        键盘输入快捷键(组合)
        :param shortcuts: 快捷键: "Control+A+Backspace"
        :param delay: keydown和keyup之间的延时 毫秒(ms)
        :return:
        """
        try:
            self.page.keyboard.press(shortcuts, delay=delay)
            self.log.info(f"输入快捷键: {shortcuts}")
        except TimeoutError:
            self.log.exception(f"输入快捷键: {shortcuts}, 失败")
            raise AssertionError

    def keyboard_insert_text(self, text: str):
        """
        键盘输入文本
        :param text: 输入文本
        :return:
        """
        try:
            self.page.keyboard.insert_text(text)
            self.log.info(f"键盘输入文本: {text}")
        except TimeoutError:
            self.log.exception(f"键盘输入文本: {text}, 失败")
            raise AssertionError

    def upload_file(self, location: str | Element, file: str | Path | list[str | Path]):
        """
        上传文件
        :param location: 定位方式或者元素
        :param file: 上传的文件
        :return:
        """
        try:
            with self.page.expect_file_chooser() as fc_info:
                self.page.click(location) if isinstance(location, str) else location.click()
            file_chooser = fc_info.value
            if "/" not in file and "\\" not in file:
                file = project_path() / Path(f"app/datas/download_datas/{file}")
            file_chooser.set_files(file)
            self.log.info(f"上传文件: {file}, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"上传文件: {file}, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def download_file(self, location: str | Element, file: str | Path, timeout: int = 30000):
        """
        下载文件
        :param location: 定位方式或者元素
        :param file: 下载的文件 例: abc.xlsx
        :param timeout: 下载超时时间
        :return:
        """
        try:
            with self.page.expect_download(timeout=timeout) as download_info:
                self.page.click(location) if isinstance(location, str) else location.click()
            download = download_info.value
            if "/" not in file and "\\" not in file:
                file = project_path() / Path(f"app/datas/download_datas/{file}")
            download.save_as(file)
            self.log.info(f"下载文件: {file}, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"下载文件: {file}, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def element_position_message(self, location: str | Element, **kwargs) -> dict[str, int | float]:
        """
        获取元素位置信息
        :param location: 定位方式或者元素
        :return: dict({"x":1,"y":1,"width":1,"height":1})
        """
        try:
            ele_box = self.search_element(location, **kwargs).bounding_box() if isinstance(location, str) \
                else location.bounding_box()
            self.log.info(f"获取元素位置信息, 定位方式: {str(location)}")
            return ele_box
        except TimeoutError:
            self.log.exception(f"获取元素位置信息, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def element_center(self, location: str | Element, **kwargs) -> dict[str, int | float]:
        """
        获取元素中心位置
        :param location: 定位方式或者元素
        :return: dict({"x":1,"y":1})
        """
        try:
            ele_box = self.element_position_message(location, **kwargs)
            ele_center = {
                "x": ele_box["x"] + ele_box["width"] / 2,
                "y": ele_box["y"] + ele_box["height"] / 2
            }
            self.log.info(f"获取元素中心位置, 定位方式: {str(location)}")
            return ele_center
        except TimeoutError:
            self.log.exception(f"获取元素中心位置, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def _drag(self, source_ele_center: dict[str, int | float], x: int | float, y: int | float, steps: int = None):
        """
        拖拽
        :param source_ele_center: 起点元素中心位置
        :param x: x方向偏移量(px)
        :param y: y方向偏移量(px)
        :param steps: 拖拽时间 秒(s)
        :return:
        """
        try:
            self.page.mouse.move(source_ele_center["x"], source_ele_center["y"])
            self.page.mouse.down()
            self.page.mouse.move(source_ele_center["x"] + x, source_ele_center["y"] + y, steps=steps)
            self.page.mouse.up()
        except Exception as e:
            self.log.exception(str(e))

    def drag_to(self, source: str | Locator, target: str | Locator, **kwargs):
        """
        拖拽
        :param source: 起点元素定位方式或者元素
        :param target: 目标元素定位方式或者元素
        :return:
        """
        try:
            ele_start = self.search_element(source, **kwargs) if isinstance(source, str) else source
            ele_end = self.search_element(target, **kwargs) if isinstance(target, str) else target
            ele_start.drag_to(ele_end)
            self.log.info(f"拖拽, 起点元素定位方式: {str(source)}, 目标元素定位方式: {str(target)}")
        except TimeoutError:
            self.log.exception(f"拖拽, 起点元素定位方式: {str(source)}, 目标元素定位方式: {str(target)}, 失败")
            raise AssertionError

    def row_drag_and_drop(self, source: str, target: str, **kwargs):
        """
        拖拽
        :param source: 起点元素定位方式
        :param target: 目标元素定位方式
        :return:
        """
        try:
            self.page.drag_and_drop(source, target, **kwargs)
            self.log.info(f"拖拽, 起点元素定位方式: {str(source)}, 目标元素定位方式: {str(target)}")
        except TimeoutError:
            self.log.exception(f"拖拽, 起点元素定位方式: {str(source)}, 目标元素定位方式: {str(target)}, 失败")
            raise AssertionError

    def drag_and_drop(self, source: str | Element, target: str | Element, **kwargs):
        """
        拖拽
        :param source: 起点元素定位方式或者元素
        :param target: 目标元素定位方式或者元素
        :return:
        """
        try:
            source_ele_box = self.element_position_message(source, **kwargs)
            target_ele_box = self.element_position_message(target, **kwargs)

            x = target_ele_box["x"] - source_ele_box["x"]
            y = target_ele_box["y"] - source_ele_box["y"]

            source_ele_center = self.element_center(source, **kwargs)
            self._drag(source_ele_center, x, y)
            self.log.info(f"拖拽, 起点元素定位方式: {str(source)}, 目标元素定位方式: {str(target)}")
        except TimeoutError:
            self.log.exception(f"拖拽, 起点元素定位方式: {str(source)}, 目标元素定位方式: {str(target)}, 失败")
            raise AssertionError

    def drag_and_drop_by_offset(self, source: str | Element, x: int | float, y: int | float, steps: int = None,
                                **kwargs):
        """
        拖拽
        :param source: 起点元素定位方式或者元素
        :param x: x方向偏移量(px)
        :param y: y方向偏移量(px)
        :param steps: 拖拽时间 秒(s)
        :return:
        """
        try:
            center_offset_x = kwargs.get("center_offset_x")
            center_offset_y = kwargs.get("center_offset_y")
            kwargs.clear()
            source_ele_center = self.element_center(source, **kwargs)
            if center_offset_x:
                source_ele_center["x"] += center_offset_x
            if center_offset_y:
                source_ele_center["y"] += center_offset_y
            self._drag(source_ele_center, x, y, steps)
            self.wait(500)
            self.log.info(f"拖拽, 起点元素定位方式: {str(source)}, x方向偏移量{x}px, y方向偏移量{y}px")
        except TimeoutError:
            self.log.exception(f"拖拽, 起点元素定位方式: {str(source)}, x方向偏移量{x}px, y方向偏移量{y}px, 失败")
            raise AssertionError

    def execute_script(self, expression: str, arg: Any = None) -> Any:
        """
        执行js
        :param expression: js表达式 例1:"x => x*8" 例2:"document.body"
                            el = page.evaluate("node => node.outerHTML", element)  element是ElementHandle, 不能是Locator
        :param arg: js函数参数
        :return: js执行后的返回值, Any
        """
        try:
            result = self.page.evaluate(expression, arg)
            self.log.info(f"执行js, 表达式: {expression}, 参数: {arg}")
            return result
        except TimeoutError:
            self.log.exception(f"执行js, 表达式: {expression}, 参数: {arg}, 失败")
            raise AssertionError

    def scroll(self, location: str | Element, **kwargs):
        """
        滚动条滚动到可视区域(DOM节点必须存在才能使用)
        :param location: 定位方式或者元素
        :return:
        """
        try:
            element = self.search_element(location, **kwargs) if isinstance(location, str) else location
            element.scroll_into_view_if_needed()
            self.log.info(f"滚动条滚动到可视区域, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"滚动条滚动到可视区域, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def scroll_by_offset(self, location: str | Element, x: int | float = 0, y: int | float = 0, **kwargs):
        """
        滚动条滚动
        :param location: 定位方式或者元素
        :param x: x方向偏移量
        :param y: y方向偏移量
        :return:
        """
        try:
            self.page.hover(location, **kwargs) if isinstance(location, str) else location.hover(**kwargs)
            self.page.mouse.wheel(x, y)
            self.log.info(f"滚动条滚动, x方向偏移量{x}px, y方向偏移量{y}px, 定位方式: {str(location)}")
        except TimeoutError:
            self.log.exception(f"滚动条滚动, x方向偏移量{x}px, y方向偏移量{y}px, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def element_attribute(self, location: str | Element, name: str) -> str:
        """
        获取元素属性
        :param location: 定位方式或者元素
        :param name: 属性名
        :return: 属性值
        """
        try:
            attribute_value = self.page.get_attribute(location, name) if isinstance(location, str) \
                else location.get_attribute(name)
            self.log.info(f"获取元素属性, 定位方式: {str(location)}, 属性名: {name}, 属性值: {attribute_value}")
            return attribute_value
        except TimeoutError:
            self.log.exception(f"获取元素属性, 定位方式: {str(location)}, 属性名: {name}, 失败")
            raise AssertionError

    def element_attribute_style(self, location: str | Element, name: str) -> str:
        """
        获取元素style属性里的具体的属性
        :param location: 定位方式或者元素
        :param name: style属性里的具体的属性名
        :return: 属性值
        """
        try:
            if name == "display":
                self.wait(500)
            style_value = self.page.get_attribute(location, "style") if isinstance(location, str) \
                else location.get_attribute("style")
            if style_value:
                style_list = style_value.replace("; ", ";").split(";")[:-1] if ";" in style_value else [style_value]
                style_dict = {}
                for style_item in style_list:
                    style_kv = style_item.replace(": ", ":").split(":")
                    style_dict[style_kv[0]] = style_kv[1]
                self.log.info(
                    f"获取元素style属性的具体属性值, 定位方式: {str(location)}, 属性名: {name}, 属性值: {style_dict.get(name)}")
                return style_dict.get(name)
        except TimeoutError:
            self.log.exception(f"获取元素style属性的具体属性值, 定位方式: {str(location)}, 属性名: {name}, 失败")
            raise AssertionError

    def element_inner_text(self, location: str | Element) -> str:
        """
        获取元素文本
        :param location: 定位方式或者元素
        :return: 元素文本
        """
        try:
            text = self.page.inner_text(location) if isinstance(location, str) else location.inner_text()
            self.log.info(f"获取元素文本:{text}, 定位方式: {str(location)}")
            return text
        except TimeoutError:
            self.log.exception(f"获取元素文本, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def element_text_context(self, location: str | Element) -> str:
        """
        获取元素文本
        :param location: 定位方式或者元素
        :return: 元素文本
        """
        try:
            text = self.page.text_content(location) if isinstance(location, str) else location.text_content()
            self.log.info(f"获取元素文本:{text}, 定位方式: {str(location)}")
            return text
        except TimeoutError:
            self.log.exception(f"获取元素文本, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def input_value(self, location: str | Element) -> str:
        """
        获取input输入框里的回填值
        :param location: 定位方式或者元素
        :return:
        """
        try:
            text = self.page.input_value(location) if isinstance(location, str) else location.input_value()
            self.log.info(f"获取input输入框里的回填值: {text}, 定位方式: {str(location)}")
            return text
        except TimeoutError:
            self.log.exception(f"获取input输入框里的回填值, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def screenshot(self, image_path: str | Path, **kwargs):
        """
        全屏截图
        :param image_path: 图片地址
        :return:
        """
        try:
            self.page.screenshot(path=image_path, full_page=True, **kwargs)
            self.log.info(f"全屏截图, 图片地址: {image_path}")
        except TimeoutError:
            self.log.exception(f"全屏截图, 图片地址: {image_path}, 失败")
            raise AssertionError

    def element_screenshot(self, location: str | Element, image_path: str | Path = None, **kwargs) -> None | bytes:
        """
        元素截图
        :param location: 定位方式或者元素
        :param image_path: 图片地址
        :return:
        """
        try:
            element = self.search_element(location) if isinstance(location, str) else location
            img = element.screenshot(path=image_path, **kwargs)
            self.log.info(f"元素截图, 图片地址: {image_path}, 定位方式: {str(location)}")
            return img
        except TimeoutError:
            self.log.exception(f"元素截图, 图片地址: {image_path}, 定位方式: {str(location)}, 失败")
            raise AssertionError

    def is_visible(self, location: str | Locator, timeout: float = None) -> bool:
        """
        判断元素是否可见
        :param location: 定位方式或者元素
        :param timeout: 超时时间 毫秒(ms)
        :return: bool
        """
        try:
            locator = self.search_element(location) if isinstance(location, str) else location
            expect(locator).to_be_visible(timeout=timeout or None)
            return True
        except AssertionError:
            return False

    def is_hidden(self, location: str | Locator, timeout: float = None) -> bool:
        """
        判断元素是否隐藏
        :param location: 定位方式或者元素
        :param timeout: 超时时间 毫秒(ms)
        :return: bool
        """
        try:
            locator = self.search_element(location) if isinstance(location, str) else location
            expect(locator).to_be_hidden(timeout=timeout or None)
            return True
        except AssertionError:
            return False

    def show_console(self):
        """打印浏览器控制台输出"""
        self.page.on("console", lambda msg: self.log.info(msg.text))

    def focus_locator_press(self, location: str | Element, key, *args, **kwargs):
        """
        定位元素，然后给元素输入键盘值
        :param location: 定位方式或元素
        :param key: 键盘值,  `F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`,
                            `Backspace`, `Tab`,`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`,
                            `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`, etc.
        :param args:
        :param kwargs:
        :return:
        """
        try:
            ele = self.search_element(location) if isinstance(location, str) else location
            ele.press(key, *args, **kwargs)
            self.log.info(f"输入快捷键{key}")
        except Exception as e:
            self.log.exception(f"输入快捷键{key}失败, {e}")
            raise AssertionError

    def search_frame(self, frame: str | FrameLocator, inner_frame: str = None) -> FrameLocator:
        """
        定位frame
        :param frame: frame的定位方式或frame
        :param inner_frame: frame的定位方式
        :return:
        """
        try:
            return self.page.frame_locator(frame) if isinstance(frame, str) else frame.frame_locator(inner_frame)
        except Exception as e:
            self.log.exception(f"定位frame: {frame}中的{inner_frame}失败, {e}")
            raise AssertionError

    def frame_search_elements(self, frame: str | FrameLocator, location: str) -> Locator:
        """
        定位在frame里面的元素
        :param frame: frame的定位方式
        :param location: frame里面的定位方式
        :return:
        """
        try:
            return self.page.frame_locator(frame).locator(location) if isinstance(frame, str) \
                else frame.locator(location)
        except Exception as e:
            self.log.exception(f"定位frame: {frame}中的{location}失败, {e}")
            raise AssertionError

    def frame_is_visible(self, frame: str | FrameLocator, location: str, timeout: int | float = 3000) -> bool:
        """
        判断frame中元素是否可见
        :param frame: 定位方式或者frame
        :param location: 定位方式
        :param timeout: 超时时间 毫秒(ms)
        :return: bool
        """
        flag = False
        for _ in range(timeout // 500):
            flag = self.frame_search_elements(frame, location).count()
            if flag != 0:
                flag = True
                break
            else:
                flag = False
                self.wait(500)
        return flag

    def frame_is_hidden(self, frame: str | FrameLocator, location: str, timeout: int | float = 3000) -> bool:
        """
        判断frame中元素是否隐藏
        :param frame: 定位方式或者frame
        :param location: 定位方式
        :param timeout: 超时时间 毫秒(ms)
        :return: bool
        """
        flag = False
        for _ in range(timeout // 500):
            flag = self.frame_search_elements(frame, location).count()
            if flag == 0:
                flag = True
                break
            else:
                flag = False
                self.wait(500)
        return flag

    def is_scroll_bottom(self, location: str | ElementHandle) -> bool:
        """
        滚动条是否到达底部
        :param location: 定位方式
        :return:
        """
        element = self.find_element(location) if isinstance(location, str) else location
        client_height = self.execute_script("node => node.clientHeight", element)
        scroll_top = self.execute_script("node => node.scrollTop", element)
        scroll_height = self.execute_script("node => node.scrollHeight", element)
        return scroll_height - (client_height + scroll_top) < 1

    @contextmanager
    def expect_route(self, url: Union[str, Pattern[str], Callable[[str], bool]],
                     handler: Union[
                         Callable[["Route"], Any],
                         Callable[["Route", "Request"], Any],
                     ],
                     *,
                     times: Optional[int] = None):
        self.page.route(url, handler, times=times)
        self.log.info(f"注册监听事件， 监听{url}")
        yield
        self.page.unroute(url, handler)
        self.log.info(f"注销监听事件， 取消监听{url}")

    def wait_selector(self, selector: str,
                      *,
                      timeout: float | None = None,
                      state: Literal["attached", "detached", "hidden", "visible"] | None = None,
                      strict: bool | None = None):

        self.page.wait_for_selector(selector, timeout=timeout, state=state, strict=strict)

