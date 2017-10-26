# There are a total of n courses you have to take, labeled from 0 to n - 1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
# 2, [(course, prerequisite)]

class Solution1:
	def can_finish(num_courses, prerequisites):
		graph = [[] for i in range(num_courses)]
		visited = [0] * num_courses

		for course, pre in prerequisites:
			graph[course].append(pre)

		for i in range(num_courses):
			if not self.dfs(i, graph, visited):
				return False

		return True

	def dfs(course, graph, visited):
		if visited[course] == -1:
			return False
		if visited[course] == 1:
			return True

		visited[course] = -1
		for next_course in graph[course]:
			if not self.dfs(next_course, graph, visited)
				return False

		visited[course] = 1
		return True

class Solution2:
	def can_finish(num_courses, prerequisites):
		graph = [set() for _ in range(num_courses)]
		in_degree = [0] * num_courses

		for (b, a) in prerequisites:
			in_degree[b] += 1
			graph[a].add(b)

		q = []
		for i, d in enumerate(in_degree):
			if d == 0:
				q.append(i)

		n = 0
		while len(q):
			n += 1
			a = q.pop()
			while graph[a]:
				b = graph[a].pop()
				in_degree[b] -= 1
				if in_degree == 0:
					q.append(b)

		return n == num_courses