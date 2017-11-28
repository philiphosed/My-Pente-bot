# DO NOT EDIT THIS FILE

from commands import *

def drawTree(problem, nodes, start, goal, highlight=None):
	"""Draw the search tree and render it to the file tree.pdf"""
	
	f = file('tree.dot', 'w')
	f.write('digraph {\n')
		
	for n in nodes:
		label = 'H'+str(hash(n.getState())).replace('-','0')
		text = problem.text(n.getState()).replace('\n','\\n')
		if n.getState() == highlight:
			f.write('%s [label="%s",shape=circle,color="blue"];\n' % (label,text))
		elif n.getState() == start:
			f.write('%s [label="%s",shape=circle,color="red"];\n' % (label,text))
		elif n.getState() == goal:
			f.write('%s [label="%s",shape=circle,color="green"];\n' % (label,text))			
		else:
			f.write('%s [label="%s",shape=circle];\n' % (label,text))
		
		if n._parent:
			label2 = 'H' + str(hash(n._parent.getState())).replace('-','0')
			label3 = str(n._action) + ': ' + str(n._cost)
			f.write('%s -> %s [label="%s"];\n' % (label2,label,label3))
				
	f.write('}\n')
	f.close()
		
	print getoutput('dot -Tpdf tree.dot > tree.pdf')

def drawGraph(problem, nodes, start, goal, highlight=None):
	"""Draw the graph that has been explored with the search tree highlighted and render it to graph.pdf"""
	
	f = file('graph.dot', 'w')
	f.write('digraph {\n')
	f.write('edge [len=2];\n')
		
	treeEdges = set()
	parents = set()
	for n in nodes:
		if n._parent:
			parents.add(n._parent)
			treeEdges.add( (n._parent.getState(), n._action) )
		
	for n in nodes:
		label = 'H'+str(hash(n.getState())).replace('-','0')
		text = problem.text(n.getState()).replace('\n','\\n')
		if n.getState() == highlight:
			f.write('%s [label="%s",shape=circle,color="blue"];\n' % (label,text))
		elif n.getState() == start:
			f.write('%s [label="%s",shape=circle,color="red"];\n' % (label,text))
		elif n.getState() == goal:
			f.write('%s [label="%s",shape=circle,color="green"];\n' % (label,text))			
		else:
			f.write('%s [label="%s",shape=circle];\n' % (label,text))
				
		if n in parents:
			actions = problem.actions(n.getState())
			for a in actions:
				result = problem.result(n.getState(), a)
				cost = problem.cost(n.getState(), a)
				label2 = 'H' + str(hash(result)).replace('-','0')
				label3 = str(a) + ': ' + str(cost)
				
				if (n.getState(), a) in treeEdges:
					f.write('%s -> %s [label="%s"];\n' % (label,label2,label3))
				else:
					f.write('%s -> %s [label="%s",style=dashed];\n' % (label,label2,label3))
			
	f.write('}\n')
	f.close()
		
	print getoutput('neato -Tpdf graph.dot > graph.pdf')