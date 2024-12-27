#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Поиск файла с заданным уровнем доступа


class TreeNode:
    def __init__(self, value, permissions):
        self.value = value  # Имя файла или каталога
        self.permissions = permissions  # Права доступа
        self.children = []  # Дочерние узлы

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        for child in args:
            self.add_child(child)

    def __repr__(self):
        return f"<{self.value}: {self.permissions}>"


def depth_limited_search(node, goal_perms, limit, found_files):
    if limit < 0:
        return found_files
    if node is None:
        return found_files

    # Если права доступа совпадают с заданными, добавляем файл в список
    if node.permissions == goal_perms:
        found_files.append(node.value)
        if len(found_files) >= 10:  # Останавливаемся, если найдено 10 файлов
            return found_files

    for child in node.children:
        result = depth_limited_search(child, goal_perms, limit - 1, found_files)
        if len(found_files) >= 10:
            return found_files  # Возвращаем найденные файлы, если достигли 10

    return found_files


def iterative_deepening_search(root, goal_perms):
    max_depth = 10  # Максимальная глубина для поиска
    all_found_files = []
    for limit in range(3, max_depth):  # Начинаем с глубины 3
        found_files = depth_limited_search(root, goal_perms, limit, [])
        all_found_files.extend(found_files)
        if len(all_found_files) >= 10:  # Если найдено 10 файлов, возвращаем их
            return all_found_files[:10]
    return all_found_files


# Построение дерева файловой системы с правами доступа
root = TreeNode("dir1", "rwxr-xr--")
root.add_child(TreeNode("file1", "rwxr-xr--"))
root.add_child(TreeNode("dir2", "rwxr--r--"))
root.children[0].add_child(TreeNode("file2", "rwxr-xr--"))
root.children[0].add_child(TreeNode("file3", "rw-r--r--"))
root.children[1].add_child(TreeNode("file4", "rwxr-xr--"))
root.children[1].add_child(TreeNode("dir3", "rwxr--r--"))
root.children[1].children[1].add_child(TreeNode("file5", "rw-r--r--"))
root.children[1].children[1].add_child(TreeNode("file6", "rwxr-xr--"))
root.children[1].children[1].add_child(TreeNode("file7", "rwxr-xr--"))

# Цель поиска
goal_permissions = "rwxr-xr--"

# Поиск файлов с заданными правами доступа
found_files = iterative_deepening_search(root, goal_permissions)
print("Найденные файлы с правами доступа", goal_permissions, ":", found_files)
