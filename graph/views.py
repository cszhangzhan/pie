from django.http import HttpResponse 
import json
from BayesNetwork import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.views import serve


# This is really bad, I don't want to do it this way!
module_dir = os.path.dirname(__file__)  # get current directory
file_path = os.path.join(module_dir, 'NetworkData')
data = Data()
net = Network(file_path, data)

def index(request):
    return serve(request, 'index.html')

def get_topnews_id(request):
    top_news_list = net.getStartNodes()
    return HttpResponse(json.dumps(top_news_list), content_type="application/json")

def get_graph(request):
    graph_info = {}
    graph_info['top_news_id'] = net.getCareNodes()
    graph_info['nodes'] = {}
    node_dict = net.nodes
    initial_time = net.getStartTime()
    for node_id in node_dict:
        node = node_dict[node_id]
        graph_info['nodes'][node_id] = {'child': node.children, 'title': node.title, 'timestamp': 1000 * (initial_time + node.startTime)}
    return HttpResponse(json.dumps(graph_info), content_type="application/json")

@csrf_exempt
def get_prob(request):
    id_json = request.body
    id_list = json.loads(id_json)
    prob_dict = {}
    for id in id_list:
        prob_dict[id] = net.getProb(id)
    return HttpResponse(json.dumps(prob_dict), content_type="application/json")
    #return HttpResponse(id_json)

@csrf_exempt
def set_topnews_time(request):
    time_offset_json = request.body
    time_offset_strdict = json.loads(time_offset_json)
    time_offset_dict = {}
    for key in time_offset_strdict:
        time_offset_dict[int(key)] = int(time_offset_strdict[key])
    net.setStartTime(time_offset_dict)
    result_dict = {"result": "success"}
    return HttpResponse(json.dumps(result_dict), content_type="application/json")
    
