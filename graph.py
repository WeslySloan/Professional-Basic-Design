import turtle
import math

class Node:
    def __init__(self, data):
        self.data = data
        self.neighbors = []
        self.weights = []

    def add_neighbor(self, node, weight):
        self.neighbors.append(node)
        self.weights.append(weight)


class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, data):
        node = Node(data)
        self.nodes.append(node)

    def add_edge(self, data1, data2, weight):
        node1 = self.find_node(data1)
        node2 = self.find_node(data2)
        if node1 and node2:
            node1.add_neighbor(node2, weight)
            node2.add_neighbor(node1, weight)

    def find_node(self, data):
        for node in self.nodes:
            if node.data == data:
                return node
        return None

    def display(self):
        turtle.speed(2)
        angle = 360 / len(self.nodes)
        radius = 200

        # 그래프 그리기
        for i, node in enumerate(self.nodes):
            turtle.penup()
            turtle.goto(radius * math.cos(math.radians(angle * i)), radius * math.sin(math.radians(angle * i)))
            turtle.pendown()
            turtle.circle(20)

            turtle.penup()
            turtle.goto(radius * math.cos(math.radians(angle * i)), radius * math.sin(math.radians(angle * i)) - 20)
            turtle.pendown()
            turtle.write(node.data, align="center")

            for j, neighbor in enumerate(node.neighbors):
                turtle.penup()
                turtle.goto(radius * math.cos(math.radians(angle * i)), radius * math.sin(math.radians(angle * i)))
                turtle.pendown()
                turtle.goto(radius * math.cos(math.radians(angle * self.nodes.index(neighbor))), radius * math.sin(math.radians(angle * self.nodes.index(neighbor))))

                # 가중치 표시
                weight_x = (radius * math.cos(math.radians(angle * i)) + radius * math.cos(math.radians(angle * self.nodes.index(neighbor)))) / 2
                weight_y = (radius * math.sin(math.radians(angle * i)) + radius * math.sin(math.radians(angle * self.nodes.index(neighbor)))) / 2
                turtle.penup()
                turtle.goto(weight_x, weight_y)
                turtle.pendown()
                turtle.write(node.weights[j], align="center")

        # 최소 신장 트리 표시
        turtle.color("green")
        for node in self.nodes:
            for neighbor, weight in zip(node.neighbors, node.weights):
                if node.data < neighbor.data:  # 간선을 한 번만 그리도록 중복 제거
                    turtle.penup()
                    turtle.goto(radius * math.cos(math.radians(angle * self.nodes.index(node))), radius * math.sin(math.radians(angle * self.nodes.index(node))))
                    turtle.pendown()
                    turtle.goto(radius * math.cos(math.radians(angle * self.nodes.index(neighbor))), radius * math.sin(math.radians(angle * self.nodes.index(neighbor))))

        turtle.done()


# 그래프 생성
graph = Graph()

# 노드 추가
graph.add_node(1)
graph.add_node(2)

# 노드 추가
graph.add_node(3)
graph.add_node(4)
graph.add_node(5)

# 간선 추가
graph.add_edge(1, 2, 4)  # 노드 1과 노드 2 사이의 간선 가중치 4
graph.add_edge(1, 3, 2)  # 노드 1과 노드 3 사이의 간선 가중치 2
graph.add_edge(2, 3, 1)  # 노드 2와 노드 3 사이의 간선 가중치 1
graph.add_edge(3, 4, 5)  # 노드 3과 노드 4 사이의 간선 가중치 5
graph.add_edge(4, 5, 3)  # 노드 4와 노드 5 사이의 간선 가중치 3

# 그래프 시각화
graph.display()

graph.add
