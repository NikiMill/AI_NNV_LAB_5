#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Поиск в файловой системе

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}>"


def depth_limited_search(node, goal, limit, path):
    if limit < 0:
        return "cutoff"
    if node is None:
        return None
    # Добавим текущий узел в путь
    path.append(node.value)
    if node.value == goal:
        return path[:]  # Возвращаем путь до текущего узла

    for child in node.children:
        result = depth_limited_search(child, goal, limit - 1, path)
        if result is True:
            return True
        elif result == "cutoff":
            cutoff = "cutoff"
        elif result is not None:
            return result  # Возвращаем найденный путь

    # Удаляем узел из пути, если нет результата в его ветке
    path.pop()
    return cutoff if 'cutoff' in locals() else None


def iterative_deepening_search(root, goal):
    max_depth = 10  # Максимальная глубина для поиска
    for limit in range(max_depth):
        path = []  # Путь от корня до целевого узла
        result = depth_limited_search(root, goal, limit, path)
        if result is not None:
            return ' -> '.join(result)  # Форматируем вывод пути
    return "Целевой файл не найден"


# Построение дерева
root = TreeNode("dir1")
root.add_child(TreeNode("dir2"))
root.add_child(TreeNode("dir3"))
root.children[0].add_child(TreeNode("file4"))
root.children[1].add_child(TreeNode("file5"))
root.children[1].add_child(TreeNode("file6"))

# Цель поиска
goal = "file5"

# Проверка существования узла и получение пути
path = iterative_deepening_search(root, goal)
print(path)  # Ожидаемый вывод: dir1 -> dir3 -> file5
