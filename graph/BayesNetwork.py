#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import sys
import time

class Network:
	def __init__(self, networkfilename, data):
		self.nodes = {}
		self.data = data

		try:
			netfile = file(networkfilename,'r')
		except IOError:
			print "NetworkStatus file '%s' not found!" % networkfilename
			print "--Program Terminated.--"
			sys.exit(-1)

		nodesIndex = netfile.readline().split(',')
		for nodeIndex in nodesIndex:
			self.addNode(int(nodeIndex))

		while True:
			line = netfile.readline()
			if len(line) == 0:
				break
			(nodeFromIndex,nodeToIndex,lineDuration) = line.split(',')
			self.addArrow(int(nodeFromIndex), int(nodeToIndex), int(lineDuration))

		netfile.close()

		self.startNodes = [1]
		self.nodes[1].startTime = -5
		self.careNodes = [4,6]

		def setChildrenTimeTag(currNodeIndex, startTime):
			if startTime < self.nodes[currNodeIndex].startTime:
				self.nodes[currNodeIndex].startTime = startTime

			if len(self.nodes[currNodeIndex].children)==0:
				return
			else:
				# print self.nodes[currNodeIndex].children
				for (childNodeIndex, duration) in self.nodes[currNodeIndex].children:
					setChildrenTimeTag(childNodeIndex, startTime+duration)

		for startNodeIndex in self.startNodes:
			setChildrenTimeTag(startNodeIndex, self.nodes[startNodeIndex].startTime)

		# for node in self.nodes.itervalues():
		# 	print node.startTime

	def addNode(self, nodeIndex):
		if not self.nodes.has_key(nodeIndex):
			self.nodes[nodeIndex] = Node()
		else:
			print "NodeIndex '%i' already exists!" % nodeIndex
	def addArrow(self, nodeFromIndex, nodeToIndex, lineDuration):
		if not self.nodes.has_key(nodeFromIndex):
			print "NodeIndex '%s' doesn't exist in the graph!" %nodeFromIndex
			return
		elif not self.nodes.has_key(nodeToIndex):
			print "NodeIndex '%s' doesn't exist in the graph!" %nodeToIndex
			return
		else:
			self.nodes[nodeToIndex].pi.append((nodeFromIndex, lineDuration))
			self.nodes[nodeFromIndex].children.append((nodeToIndex, lineDuration))
			# (2,5) means from this node to node 2, the time duration is 5

			# Calculate prob of the node given parents
			# rst_filter_list = [[]]
			# self.nodes[nodeToIndex].prob = data.count_prob()
			# Independent or not? This is a problem
	def getStartNodes(self):
		return self.startNodes
	def getProb(self, nodeIndex, nodeValue=1):
		StartTime = 0
		CurrTime = time.time()
		duration = CurrTime - StartTime

		duration = 0

		# for startNodeIndex in self.startNodes:
		# 	cumuTime = self.nodes[startNodeIndex].startTime
		# 	bfsQueue = [self.nodes[startNodeIndex].children]
		# 	while cumuTime <= duration:
		# 		cumuTime += 
		cond_filter_list = []
		cond_all_filter_list = []
		rst_filter_list = [(nodeIndex, nodeValue)]
		for (nodeIndex, node) in self.nodes.items():
			cond_all_filter_list.append((nodeIndex, 1))
			if node.startTime <= duration:
				cond_filter_list.append((nodeIndex, 1))
				# We only consider 0 or 1
				# 0 means it hasn't happended
				# 1 means the event has happened
		# print cond_filter_list
		# print cond_all_filter_list
		# print rst_filter_list
		return (self.data.countProb(cond_filter_list, rst_filter_list), \
			self.data.countProb(cond_all_filter_list, rst_filter_list))


class Node:
	def __init__(self, startTime=(), title='nil'):
		# (): inf in Python
		self.pi = []
		self.children = []
		self.title = title
		self.startTime = startTime

class Data:
	def __init__(self):
		f = open('history.data')
		lines = f.readlines()
		self.history_matrix = []
		for line in lines:
		    line = line.strip('\n')
		    feature_list = [int(feature) for feature in line.split(' ')]
		    self.history_matrix.append(feature_list)
	
	def countFeature(self, filter_list):
		counter = 0
		for feature_list in self.history_matrix:
		    match = True
		    for t in filter_list:
		        index = t[0]
		        value = t[1]
		        if feature_list[index-1] != value:
		            match = False
		            break
		    if match:
		        counter += 1
		return counter

	def countProb(self, cond_filter_list, rst_filter_list):
		rst_filter_list += cond_filter_list
		# Attention: these 2 list might overlap!!
		stricterCondCnt = self.countFeature(rst_filter_list)
		condCnt = self.countFeature(cond_filter_list)
		if condCnt==0:
			print "Cannot find any instance of this condition in history"
			return 0
		return 1.0*stricterCondCnt/condCnt

if __name__ == '__main__':
	data = Data()
	# print data.countFeature([(1,1),(2,1),(3,1)])
	# print data.countFeature([(1,1),(2,1),(3,1),(6,1)])
	net = Network('NetworkData', data)

	#time.sleep(5)
	print net.getProb(6)
	# print time.time()
	# time.sleep(1)
	# print time.time()

	# for key in net.nodes.keys():
	# 	print key, net.nodes[key].pi

	# for i in range(1,6):
	# 	net.addNode(i)
	# net.addArrow(1,2)
	# net.addArrow(1,3)
	# net.addArrow(2,4)
	# net.addArrow(2,6)
	# net.addArrow(3,5)
	# net.addArrow(5,6)


