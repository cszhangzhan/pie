#!/usr/bin/env python

import csv
import sys

class Network:
	def __init__(self, networkfilename):
		self.nodes = {}

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
			(nodeFromIndex,nodeToIndex) = line.split(',')
			self.addArrow(int(nodeFromIndex), int(nodeToIndex))

		netfile.close()
	def addNode(self, nodeIndex):
		if not self.nodes.has_key(nodeIndex):
			self.nodes[nodeIndex] = Node()
		else:
			print "NodeIndex '%i' already exists!" % nodeIndex
	def addArrow(self, nodeFromIndex, nodeToIndex):
		if not self.nodes.has_key(nodeFromIndex):
			print "NodeIndex '%s' doesn't exist in the graph!" %nodeFromIndex
			return
		elif not self.nodes.has_key(nodeToIndex):
			print "NodeIndex '%s' doesn't exist in the graph!" %nodeToIndex
			return
		else:
			self.nodes[nodeToIndex].pi.append(nodeFromIndex)

class Node:
	def __init__(self):
		self.pi = []

class Data:
	def __init__(self):
		f = open('history.data')
	    lines = f.readlines()
	    self.history_matrix = []
	    for line in lines:
	        line = line.strip('\n')
	        feature_list = [int(feature) for feature in line.split(' ')]
	        self.history_matrix.append(feature_list)
	
	def count_feature(self, filter_list):
	    counter = 0
	    for feature_list in self.history_matrix:
	        match = True
	        for t in filter_list:
	            index = t[0]
	            value = t[1]
	            if feature_list[index] != value:
	                match = False
	                break
	        if match:
	            counter += 1
	    return counter

if __name__ == '__main__':
	net = Network('NetworkData')


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


